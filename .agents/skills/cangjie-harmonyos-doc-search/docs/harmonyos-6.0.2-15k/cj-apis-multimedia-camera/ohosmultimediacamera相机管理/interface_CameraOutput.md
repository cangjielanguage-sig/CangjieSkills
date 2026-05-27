## interface CameraOutput

```cangjie
sealed interface CameraOutput {
    func release(): Unit
}
```

**功能：** 会话中Session使用的输出信息，output的基类。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### func release()

```cangjie
func release(): Unit
```

**功能：** 释放输出资源。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID         | 错误信息        |
  | :-------------- | :-------------- |
  | 7400201                |  Camera service fatal error.                           |

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
let previewOutput = cameraManager.createPreviewOutput(ability.previewProfiles[0], surfaceId)
previewOutput.release()
```