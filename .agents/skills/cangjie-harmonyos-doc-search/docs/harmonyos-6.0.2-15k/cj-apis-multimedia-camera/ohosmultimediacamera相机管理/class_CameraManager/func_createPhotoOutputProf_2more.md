### func createPhotoOutput(Profile)

```cangjie
public func createPhotoOutput(profile: Profile): PhotoOutput
```

**功能：** 创建拍照输出对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|profile|[Profile](#class-profile)|是|-|支持的拍照配置信息，通过[getSupportedOutputCapability](#func-getsupportedoutputcapabilitycameradevice-scenemode)接口获取。|

**返回值：**

|类型|说明|
|:----|:----|
|[PhotoOutput](#class-photooutput)|PhotoOutput实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID    | 错误信息                                           |
  |:---------|:-----------------------------------------------|
  | 7400101  | Parameter missing or parameter type incorrect. |
  | 7400201  | Camera service fatal error.                    |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let cameraDevices = cameraManager.getSupportedCameras()
let camera = cameraDevices[0]
let mode = cameraManager.getSupportedSceneModes(camera)[0]
let cameraOutputCapability = cameraManager.getSupportedOutputCapability(camera, mode)
let profile = cameraOutputCapability.photoProfiles[0]
let photoOutput = cameraManager.createPhotoOutput(profile)
```

### func createPreviewOutput(Profile, String)

```cangjie
public func createPreviewOutput(profile: Profile, surfaceId: String): PreviewOutput
```

**功能：** 创建预览输出对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|profile|[Profile](#class-profile)|是|-|支持的预览配置信息，通过[getSupportedOutputCapability](#func-getsupportedoutputcapabilitycameradevice-scenemode)接口获取。|
|surfaceId|String|是|-|从XComponent或者[ImageReceiver](../ImageKit/cj-apis-image.md#class-imagereceiver)组件获取的surfaceId。|

**返回值：**

|类型|说明|
|:----|:----|
|[PreviewOutput](#class-previewoutput)|PreviewOutput实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID         | 错误信息        |
  | :-------------- | :-------------- |
  | 7400101                |  Parameter missing or parameter type incorrect.               |
  | 7400201                |  Camera service fatal error.               |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.image.createImageReceiver
import ohos.image.ImageFormat

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let cameraDevice = cameraManager.getSupportedCameras()[0]
let mode = cameraManager.getSupportedSceneModes(cameraDevice)[0]
let cameraOutputCapability = cameraManager.getSupportedOutputCapability(cameraDevice, mode)
let profile = cameraOutputCapability.previewProfiles[0]
let receiver = createImageReceiver(8192, 8, ImageFormat.JPEG, 8)
let surfaceId: String = receiver.getReceivingSurfaceId()
let previewOutput = cameraManager.createPreviewOutput(profile, surfaceId)
```