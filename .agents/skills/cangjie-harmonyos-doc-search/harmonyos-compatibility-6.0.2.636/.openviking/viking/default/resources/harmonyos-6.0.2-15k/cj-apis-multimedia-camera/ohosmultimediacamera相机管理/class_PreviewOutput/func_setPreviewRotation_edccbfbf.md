### func setPreviewRotation(ImageRotation, Bool)

```cangjie
public func setPreviewRotation(previewRotation: ImageRotation, isDisplayLocked!: Bool = false): Unit
```

**功能：** 设置预览旋转角度。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|previewRotation|[ImageRotation](#enum-imagerotation)|是|-|预览旋转角度。|
|isDisplayLocked|Bool|否|false| **命名参数。** 是否旋转锁定。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID         | 错误信息        |
  | :-------------- | :-------------- |
  | 7400101 | Parameter missing or parameter type incorrect.  |
  | 7400201 | Camera service fatal error.  |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.image.createImageReceiver
import ohos.image.ImageFormat

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let device = cameraManager.getSupportedCameras()[0]
let mode = cameraManager.getSupportedSceneModes(device)[0]
let ability = cameraManager.getSupportedOutputCapability(device, mode)
let receiver = createImageReceiver(8192, 8, ImageFormat.JPEG, 8)
let surfaceId: String = receiver.getReceivingSurfaceId()
let output = cameraManager.createPreviewOutput(ability.previewProfiles[0], surfaceId)
output.setPreviewRotation(ROTATION_90)
```