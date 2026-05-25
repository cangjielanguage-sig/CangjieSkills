### func off(CameraEvents, Callback1Argument\<SmoothZoomInfo>)

```cangjie
public func off(eventType: CameraEvents, callback: Callback1Argument<SmoothZoomInfo>): Unit
```

**功能：** 注销监听相机平滑变焦的状态变化。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[CameraEvents](#enum-cameraevents)|是|-|监听事件，必须为SmoothZoomInfoAvailable，session创建成功之后可监听该接口。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<[SmoothZoomInfo](#class-smoothzoominfo)>|是|-|回调函数，取消对应callback。|

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
import kit.PerformanceAnalysisKit.Hilog

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let cameraManager = getCameraManager(ctx)
    let videoSession = cameraManager.createSession(SceneMode.NormalVideo) as VideoSession
    let session = videoSession.getOrThrow()
    session.off(CameraEvents.SmoothZoomInfoAvailable)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func off(CameraEvents)

```cangjie
public func off(eventType: CameraEvents): Unit
```

**功能：** 注销监听普通录像会话的错误事件。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[CameraEvents](#enum-cameraevents)|是|-|监听事件。|

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
import kit.PerformanceAnalysisKit.Hilog

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let cameraManager = getCameraManager(ctx)
    let videoSession = cameraManager.createSession(SceneMode.NormalVideo) as VideoSession
    let session = videoSession.getOrThrow()
    session.off(CameraEvents.SmoothZoomInfoAvailable)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```