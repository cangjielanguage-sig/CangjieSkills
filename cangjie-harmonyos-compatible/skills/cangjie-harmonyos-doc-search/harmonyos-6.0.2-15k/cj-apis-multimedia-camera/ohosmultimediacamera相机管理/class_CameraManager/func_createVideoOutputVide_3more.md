### func createVideoOutput(VideoProfile, String)

```cangjie
public func createVideoOutput(profile: VideoProfile, surfaceId: String): VideoOutput
```

**功能：** 创建录像输出对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|profile|[VideoProfile](#class-videoprofile)|是|-|支持的录像配置信息，通过[getSupportedOutputCapability](#func-getsupportedoutputcapabilitycameradevice-scenemode)接口获取。|
|surfaceId|String|是|-|从AVRecorder获取的surfaceId。|

**返回值：**

|类型|说明|
|:----|:----|
|[VideoOutput](#class-videooutput)|VideoOutput实例。|

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
let mode = cameraManager.getSupportedSceneModes(cameraDevice)[1]
let cameraOutputCapability = cameraManager.getSupportedOutputCapability(cameraDevice, mode)
let receiver = createImageReceiver(8192, 8, ImageFormat.JPEG, 8)
let surfaceId: String = receiver.getReceivingSurfaceId()
let videoOutput = cameraManager.createVideoOutput(cameraOutputCapability.videoProfiles[0], surfaceId)
```

### func createVideoOutput(String)

```cangjie
public func createVideoOutput(surfaceId: String): VideoOutput
```

**功能：** 创建无配置信息的录像输出对象。该接口需配合[preconfig](#func-preconfigpreconfigtype-preconfigratio)功能一起使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|surfaceId|String|是|-|从AVRecorder获取的surfaceId。|

**返回值：**

|类型|说明|
|:----|:----|
|[VideoOutput](#class-videooutput)|VideoOutput实例。|

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
import ohos.image.createImageReceiver
import ohos.image.ImageFormat

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let receiver = createImageReceiver(8192, 8, ImageFormat.JPEG, 8)
let surfaceId: String = receiver.getReceivingSurfaceId()
let videoOutput = cameraManager.createVideoOutput(surfaceId)
```

### func getSupportedCameras()

```cangjie
public func getSupportedCameras(): Array<CameraDevice>
```

**功能：** 获取支持指定的相机设备对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[CameraDevice](#class-cameradevice)>|相机设备列表。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let cameraDevices = cameraManager.getSupportedCameras()
```