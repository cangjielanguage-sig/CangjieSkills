### func on(CameraEvents, Callback1Argument\<FocusState>)

```cangjie
public func on(eventType: CameraEvents, callback: Callback1Argument<FocusState>): Unit
```

**功能：** 监听相机聚焦的状态变化，通过注册回调函数获取结果。

> **说明：**
>
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[CameraEvents](#enum-cameraevents)|是|-|监听事件，必须为FocusStateChange，session创建成功可监听。仅当自动对焦模式时，且相机对焦状态发生改变时可触发该事件。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<[FocusState](#enum-focusstate)>|是|-|回调函数，用于获取当前对焦状态。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.callback_invoke.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

// 此处代码可添加在依赖项定义中
class FocusStateChangeCallback <: Callback1Argument<FocusState> {
    public static var invoked = false

    public func invoke(err: ?BusinessException, state: FocusState) {
        Hilog.info(0, "AppLogCj", "[multimedia_camera | FocusStateChange Callback]: state: ${state.toString()}")
        invoked = true
    }
}

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let cameraManager = getCameraManager(ctx)
    let photoSession = cameraManager.createSession(SceneMode.NormalPhoto) as PhotoSession
    let session = photoSession.getOrThrow()
    let callback = FocusStateChangeCallback()
    session.on(CameraEvents.FocusStateChange, callback)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func on(CameraEvents, Callback1Argument\<SmoothZoomInfo>)

```cangjie
public func on(eventType: CameraEvents, callback: Callback1Argument<SmoothZoomInfo>): Unit
```

**功能：** 监听相机平滑变焦的状态变化，通过注册回调函数获取结果。

> **说明：**
>
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[CameraEvents](#enum-cameraevents)|是|-|监听事件，必须为SmoothZoomInfoAvailable，session创建成功可监听。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<[SmoothZoomInfo](#class-smoothzoominfo)>|是|-|回调函数，用于获取当前平滑变焦状态。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.callback_invoke.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

// 此处代码可添加在依赖项定义中
class SmoothZoomInfoAvailableCallback2 <: Callback1Argument<SmoothZoomInfo> {
    public static var invoked = false

    public func invoke(err: ?BusinessException, info: SmoothZoomInfo) {
        Hilog.info(0, "AppLogCj", "[multimedia_camera | SmoothZoomInfoAvailable Callback]: info: ${info.duration}")
        invoked = true
    }
}

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let cameraManager = getCameraManager(ctx)
    let photoSession = cameraManager.createSession(SceneMode.NormalPhoto) as PhotoSession
    let session = photoSession.getOrThrow()
    let callback = SmoothZoomInfoAvailableCallback2()
    session.on(CameraEvents.SmoothZoomInfoAvailable, callback)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```