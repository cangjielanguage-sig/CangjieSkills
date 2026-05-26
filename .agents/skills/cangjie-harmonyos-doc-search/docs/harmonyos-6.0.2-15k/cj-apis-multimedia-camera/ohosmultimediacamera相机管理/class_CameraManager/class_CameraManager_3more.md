## class CameraManager

```cangjie
public class CameraManager {}
```

**功能：** 相机管理器类，使用前需要通过[getCameraManager](#func-getcameramanageruiabilitycontext)获取相机管理实例。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### func createCameraInput(CameraDevice)

```cangjie
public func createCameraInput(camera: CameraDevice): CameraInput
```

**功能：** 使用CameraDevice对象创建CameraInput实例。

**需要权限：** ohos.permission.CAMERA

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|camera|[CameraDevice](#class-cameradevice)|是|-|CameraDevice对象，通过[getSupportedCameras](#func-getsupportedcameras)接口获取。|

**返回值：**

|类型|说明|
|:----|:----|
|[CameraInput](#class-camerainput)|CameraInput实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID         | 错误信息        |
  | :-------------- | :-------------- |
  | 7400101                |  Parameter missing or parameter type incorrect.               |
  | 7400102                |  Operation not allowed.               |
  | 7400201                |  Camera service fatal error.               |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let cameraDevices = cameraManager.getSupportedCameras()
let cameraInput = cameraManager.createCameraInput(cameraDevices[0])
```

### func createCameraInput(CameraPosition, CameraType)

```cangjie
public func createCameraInput(position: CameraPosition, `type`: CameraType): CameraInput
```

**功能：** 根据相机位置和类型创建CameraInput实例。

**需要权限：** ohos.permission.CAMERA

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|position|[CameraPosition](#enum-cameraposition)|是|-|相机位置，通过[getSupportedCameras](#func-getsupportedcameras)接口获取设备，然后获取设备位置信息。|
|\`type\`|[CameraType](#enum-cameratype)|是|-|相机类型，通过[getSupportedCameras](#func-getsupportedcameras)接口获取设备，然后获取设备类型信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[CameraInput](#class-camerainput)|CameraInput实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID         | 错误信息        |
  | :-------------- | :-------------- |
  | 7400101                |  Parameter missing or parameter type incorrect.               |
  | 7400102                |  Operation not allowed.               |
  | 7400201                |  Camera service fatal error.               |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let cameraDevices = cameraManager.getSupportedCameras()
let cameraDevice0 = cameraDevices[0]
let position = cameraDevice0.cameraPosition
let `type` = cameraDevice0.cameraType
let cameraInput = cameraManager.createCameraInput(position, `type`)
```