### func off(CameraCallbackType)

```cangjie
public func off(`type`: CameraCallbackType): Unit
```

**功能：** 注销监听普通拍照会话的错误事件/相机聚焦的状态变化。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件，必须为CameraCallbackType.error或CameraCallbackType.focusStateChange。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let secureSession = cameraManager.createSession(SceneMode.SECURE_PHOTO) as SecureSession
let session = secureSession.getOrThrow()
session.off(CameraCallbackType.CameraError)
```

### func on(CameraCallbackType, Callback1Argument\<BusinessException>)

```cangjie
public func on(`type`: CameraCallbackType, callback: Callback1Argument<BusinessException>): Unit
```

**功能：** 监听普通拍照会话的错误事件，通过注册回调函数获取结果。

> **说明：**
>
> 不支持在on监听的回调方法里调用off注销回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件，必须为CameraCallbackType.error，session创建成功之后可监听该接口。session调用相关接口出现错误时会触发该事件，比如调用beginConfig，commitConfig，addInput等接口发生错误时返回错误信息。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[BusinessException](../BasicServicesKit/cj-apis-base.md#class-businessexception)>|是|-|回调函数，用于获取错误信息。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.base.*

// 此处代码可添加在依赖项定义中
class ErrorCallback <: Callback1Argument<BusinessException> {
    public static var invoked = false

    public func invoke(exception: BusinessException) {
        AppLog.info("[multimedia_camera | Error Callback]: exception: ${exception.message}")

        invoked = true
    }
}

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let secureSession = cameraManager.createSession(SceneMode.SECURE_PHOTO) as SecureSession
let session = secureSession.getOrThrow()
let callback = ErrorCallback()
session.on(CameraCallbackType.CameraError, callback)
```