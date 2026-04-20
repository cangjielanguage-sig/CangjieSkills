### func off(CameraCallbackType)

```cangjie
public func off(`type`: CameraCallbackType): Unit
```

**功能：** 取消对应监听事件的所有回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let device = cameraManager.getSupportedCameras()[0]
let mode = cameraManager.getSupportedSceneModes(device)[0]
let ability = cameraManager.getSupportedOutputCapability(device, mode)
let output = cameraManager.createPhotoOutput(ability.photoProfiles[0])
output.off(CameraCallbackType.CaptureStartWithInfo)
```

### func on(CameraCallbackType, Callback1Argument\<CaptureStartInfo>)

```cangjie
public func on(`type`: CameraCallbackType, callback: Callback1Argument<CaptureStartInfo>): Unit
```

**功能：** 监听拍照开始，通过注册回调函数获取[CaptureStartInfo](#struct-capturestartinfo)。

> **说明：**
>
> 不支持在on监听的回调方法里调用off注销回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件，必须为captureStartWithInfo，photoOutput创建成功后可监听。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[CaptureStartInfo](#struct-capturestartinfo)>|是|-|回调函数，用于获取相关信息。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.hilog.Hilog
import ohos.base.*

// 此处代码可添加在依赖项定义中
class TestCallbackCaptureStartWithInfo <: Callback1Argument<CaptureStartInfo> {
    public init() {}
    public open func invoke(res: CaptureStartInfo): Unit {
        Hilog.info(0, "Camera", "Call invoke CaptureStartWithInfo. captureId: ${res.captureId}, time： ${res.time}")
    }
}

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let device = cameraManager.getSupportedCameras()[0]
let mode = cameraManager.getSupportedSceneModes(device)[0]
let ability = cameraManager.getSupportedOutputCapability(device, mode)
let output = cameraManager.createPhotoOutput(ability.photoProfiles[0])
let testCallbackCaptureStartWithInfo = TestCallbackCaptureStartWithInfo()
output.on(CameraCallbackType.CaptureStartWithInfo, testCallbackCaptureStartWithInfo)
```