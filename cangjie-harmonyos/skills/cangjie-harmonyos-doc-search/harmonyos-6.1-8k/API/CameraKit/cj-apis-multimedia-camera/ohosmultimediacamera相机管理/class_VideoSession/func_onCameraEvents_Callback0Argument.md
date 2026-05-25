### func on(CameraEvents, Callback0Argument)

```cangjie
public func on(eventType: CameraEvents, callback: Callback0Argument): Unit
```

**功能：** 监听普通录像会话的错误事件，通过注册回调函数获取结果。

> **说明：**
>
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[CameraEvents](#enum-cameraevents)|是|-|监听事件，必须为CameraError，session创建成功之后可监听该接口。session调用相关接口出现错误时会触发该事件，比如调用[beginConfig](#func-beginconfig)，[commitConfig](#func-commitconfig)，[addInput](#func-addinputcamerainput)等接口发生错误时返回错误信息。|
|callback|[Callback0Argument](../arkinterop/cj-api-callback_invoke.md#class-callback0argument)|是|-|回调函数，用于获取错误信息。|

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
import ohos.callback_invoke.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

// 此处代码可添加在依赖项定义中
class SmoothZoomInfoAvailableCallback3 <: Callback1Argument<SmoothZoomInfo> {
    public static var invoked = false

    public func invoke(err: ?BusinessException, info: SmoothZoomInfo) {
        Hilog.info(0, "AppLogCj", "[multimedia_camera | SmoothZoomInfoAvailable Callback]: info: ${info.duration}")
        invoked = true
    }
}

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let cameraManager = getCameraManager(ctx)
    let videoSession = cameraManager.createSession(SceneMode.NormalVideo) as VideoSession
    let session = videoSession.getOrThrow()
    let callback = SmoothZoomInfoAvailableCallback3()
    session.on(CameraEvents.SmoothZoomInfoAvailable, callback)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```