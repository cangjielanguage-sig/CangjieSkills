### func open(Bool)

```cangjie
public func open(isSecureEnabled: Bool): UInt64
```

**功能：** 打开相机，获取安全相机的句柄。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isSecureEnabled|Bool|是|-|是否以安全的方式打开相机。|

**返回值：**

|类型|说明|
|:----|:----|
|UInt64|打开相机的句柄。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID         | 错误信息        |
  | :-------------- | :-------------- |
  | 7400107                |  Can not use camera cause of conflict.               |
  | 7400108                |  Camera disabled cause of security reason.                                  |
  | 7400201                |  Camera service fatal error.                                  |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let cameraDevice = cameraManager.getSupportedCameras()[0]
let cameraInput = cameraManager.createCameraInput(cameraDevice)
let isSecureEnabled = false
let handle = cameraInput.open(isSecureEnabled)
```