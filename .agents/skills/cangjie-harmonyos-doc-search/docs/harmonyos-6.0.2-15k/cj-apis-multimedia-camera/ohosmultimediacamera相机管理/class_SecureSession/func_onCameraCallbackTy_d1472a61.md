### func on(CameraCallbackType, Callback1Argument\<FocusState>)

```cangjie
public func on(`type`: CameraCallbackType, callback: Callback1Argument<FocusState>): Unit
```

**功能：** 监听相机聚焦的状态变化，通过注册回调函数获取结果。

> **说明：**
>
> 不支持在on监听的回调方法里调用off注销回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件，必须为CameraCallbackType.focusStateChange，session创建成功可监听。仅当自动对焦模式时，且相机对焦状态发生改变时可触发该事件。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[FocusState](#enum-focusstate)>|是|-|回调函数，用于获取当前对焦状态。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.base.*

// 此处代码可添加在依赖项定义中
class FocusStateChangeCallback <: Callback1Argument<FocusState> {
    public static var invoked = false

    public func invoke(state: FocusState) {
        AppLog.info("[multimedia_camera | FocusStateChange Callback]: focus state: ${state}")

        invoked = true
    }
}

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let secureSession = cameraManager.createSession(SceneMode.SECURE_PHOTO) as SecureSession
let session = secureSession.getOrThrow()
let callback = FocusStateChangeCallback()
session.on(CameraCallbackType.FocusStateChange, callback)
```