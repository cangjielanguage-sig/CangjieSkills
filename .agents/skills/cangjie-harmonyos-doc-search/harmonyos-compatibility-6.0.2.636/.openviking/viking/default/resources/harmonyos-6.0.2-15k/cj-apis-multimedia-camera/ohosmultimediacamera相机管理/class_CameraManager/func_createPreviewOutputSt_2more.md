### func createPreviewOutput(String)

```cangjie
public func createPreviewOutput(surfaceId: String): PreviewOutput
```

**功能：** 创建无配置信息的预览输出对象。该接口需配合[preconfig](#func-preconfigpreconfigtype-preconfigratio)一起使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|surfaceId|String|是|-|从XComponent或者[ImageReceiver](../ImageKit/cj-apis-image.md#class-imagereceiver)组件获取的surfaceId。|

**返回值：**

|类型|说明|
|:----|:----|
|[PreviewOutput](#class-previewoutput)|PreviewOutput实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID   | 错误信息                                           |
  |:--------|:-----------------------------------------------|
  | 7400101 | Parameter missing or parameter type incorrect. |
  | 7400201 | Camera service fatal error.                    |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.image.createImageReceiver
import ohos.image.ImageFormat

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let receiver = createImageReceiver(8192, 8, ImageFormat.JPEG, 8)
let surfaceId: String = receiver.getReceivingSurfaceId()
let previewOutput = cameraManager.createPreviewOutput(surfaceId)
```

### func createSession(SceneMode)

```cangjie
public func createSession(mode: SceneMode): Session
```

**功能：** 创建指定SceneMode的Session实例。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[SceneMode](#enum-scenemode)|是|-|相机支持的模式。|

**返回值：**

|类型|说明|
|:----|:----|
|[Session](#interface-session)|Session实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID         | 错误信息                                                                                 |
  | :-------------- |:----------------------------------------------------------------------------------------|
  | 401     | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3.Parameter verification failed. |
  | 7400201                | Camera service fatal error.                                                                                                                    |

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
let session = cameraManager.createSession(mode)
```