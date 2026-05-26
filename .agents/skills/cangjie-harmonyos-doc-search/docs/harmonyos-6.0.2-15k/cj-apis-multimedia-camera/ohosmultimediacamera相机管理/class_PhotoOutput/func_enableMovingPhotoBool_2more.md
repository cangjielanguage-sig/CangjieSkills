### func enableMovingPhoto(Bool)

```cangjie
public func enableMovingPhoto(enabled: Bool): Unit
```

**功能：** 使能动态照片拍照。

**需要权限：** ohos.permission.MICROPHONE

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enabled|Bool|是|-|true为开启动态照片，false为关闭动态照片。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID    | 错误信息                                           |
  | :------- |:-----------------------------------------------|
  | 201      | permission denied.                             |
  | 7400101  | Parameter missing or parameter type incorrect. |
  | 7400201  | Camera service fatal error.                    |

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
let enabled = true
output.enableMovingPhoto(enabled)
```

### func getActiveProfile()

```cangjie
public func getActiveProfile(): Profile
```

**功能：** 获取当前生效的配置信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[Profile](#class-profile)|当前生效的配置信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID   | 错误信息                         |
  |:--------|:-----------------------------|
  | 7400201 | Camera service fatal error.  |

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
let profile = output.getActiveProfile()
```