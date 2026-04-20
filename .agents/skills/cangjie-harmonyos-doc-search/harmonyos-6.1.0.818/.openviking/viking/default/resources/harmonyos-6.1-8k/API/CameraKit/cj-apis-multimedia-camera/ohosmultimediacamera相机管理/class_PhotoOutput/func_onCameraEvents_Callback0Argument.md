### func on(CameraEvents, Callback0Argument)

```cangjie
public func on(eventType: CameraEvents, callback: Callback0Argument): Unit
```

**功能：** 监听可拍下一张或拍照错误，通过注册回调函数获取结果。

> **说明：**
>
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[CameraEvents](#enum-cameraevents)|是|-|监听事件，必须为[CaptureReady, CameraError]其中之一，photoOutput创建成功后可监听。当下一张可拍时或拍照接口调用时出现错误可触发该事件发生并返回相应信息。|
|callback|[Callback0Argument](../arkinterop/cj-api-callback_invoke.md#class-callback0argument)|是|-|回调函数。|

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
import ohos.callback_invoke.Callback0Argument
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

// 此处代码可添加在依赖项定义中
class TestCallbackError7 <: Callback0Argument {
    public init() {}
    public func invoke(res: ?BusinessException): Unit {
        Hilog.info(0, "Camera", "Call invoke error. code: ${res?.code}, msg: ${res?.message}")
    }
}

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let cameraManager = getCameraManager(ctx)
    let device = cameraManager.getSupportedCameras()[0]
    let mode = cameraManager.getSupportedSceneModes(device)[0]
    let ability = cameraManager.getSupportedOutputCapability(device, mode)
    let output = cameraManager.createPhotoOutput(profile:ability.photoProfiles[0])
    let testCallbackError = TestCallbackError7()
    output.on(CameraEvents.CameraError, testCallbackError)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```