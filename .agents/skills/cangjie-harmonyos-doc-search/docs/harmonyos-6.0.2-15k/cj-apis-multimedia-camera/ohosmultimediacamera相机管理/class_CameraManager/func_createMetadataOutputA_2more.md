### func createMetadataOutput(Array\<MetadataObjectType>)

```cangjie
public func createMetadataOutput(metadataObjectTypes: Array<MetadataObjectType>): MetadataOutput
```

**功能：** 创建metadata流输出对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|metadataObjectTypes|Array\<[MetadataObjectType](#enum-metadataobjecttype)>|是|-|metadata流类型信息，通过[getSupportedOutputCapability](#func-getsupportedoutputcapabilitycameradevice-scenemode)接口获取。|

**返回值：**

|类型|说明|
|:----|:----|
|[MetadataOutput](#class-metadataoutput)|MetadataOutput实例。|

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

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let metadataObjectTypes = [MetadataObjectType.FACE_DETECTION]
let metadataOutput = cameraManager.createMetadataOutput(metadataObjectTypes)
```

### func createPhotoOutput()

```cangjie
public func createPhotoOutput(): PhotoOutput
```

**功能：** 创建拍照输出对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

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
let cameraInput = cameraManager.createCameraInput(cameraDevices[0])
let photoOutput = cameraManager.createPhotoOutput()
```