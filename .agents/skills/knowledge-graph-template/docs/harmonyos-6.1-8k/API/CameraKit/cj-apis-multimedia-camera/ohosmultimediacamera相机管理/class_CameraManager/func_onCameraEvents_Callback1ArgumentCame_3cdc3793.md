### func on(CameraEvents, Callback1Argument\<CameraStatusInfo>)

```cangjie
public func on(eventType: CameraEvents, callback: Callback1Argument<CameraStatusInfo>): Unit
```

**功能：** 相机设备状态回调，通过注册回调函数获取相机的状态变化。

> **说明：**
>
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[CameraEvents](#enum-cameraevents)|是|-|监听事件，必须为CameraStatus。CameraManager对象获取成功后可监听。目前只支持对设备打开或者关闭会触发该事件并返回对应信息。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<[CameraStatusInfo](#class-camerastatusinfo)>|是|-|回调函数，用于获取镜头状态变化信息。|

**异常：**

- BusinessException：对应错误码如下表，详见[Camera错误码](./cj-errorcode-multimedia-camera.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 7400201 | Camera service fatal error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.business_exception.BusinessException
import ohos.callback_invoke.Callback1Argument
import kit.PerformanceAnalysisKit.Hilog

// 此处代码可添加在依赖项定义中
class TestCallbackTorchStatusChange <: Callback1Argument<TorchStatusInfo> {
    public init() {}
    public func invoke(err: ?BusinessException, res: TorchStatusInfo): Unit {
        Hilog.info(0, "Camera", "Call invoke TorchStatusChange. isTorchAvailable: ${res.isTorchAvailable}, isTorchActive: ${res.isTorchActive}, torchLevel:${res.torchLevel}")
    }
}

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let cameraManager = getCameraManager(ctx)
    let testCallbackTorchStatusChange = TestCallbackTorchStatusChange()
    cameraManager.on(CameraEvents.TorchStatusChange, testCallbackTorchStatusChange)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```