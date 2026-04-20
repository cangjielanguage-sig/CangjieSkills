### func setPreviewRotation(ImageRotation, Bool)

```cangjie
public func setPreviewRotation(previewRotation: ImageRotation, isDisplayLocked!: Bool = false): Unit
```

**功能：** 设置预览旋转角度。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|previewRotation|[ImageRotation](#enum-imagerotation)|是|-|预览旋转角度。|
|isDisplayLocked|Bool|否|false|**命名参数。** Surface在屏幕旋转时是否锁定方向，未设置时默认取值为false，即不锁定方向。true表示锁定方向，false表示不锁定方向。|

**异常：**

- BusinessException：对应错误码如下表，详见[Camera错误码](./cj-errorcode-multimedia-camera.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 7400101 | Parameter missing or parameter type incorrect. |
  | 7400201 | Camera service fatal error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import kit.ImageKit.createImageReceiver
import kit.ImageKit.Size as ImageSize
import kit.ImageKit.ImageFormat
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let cameraManager = getCameraManager(ctx)
    let device = cameraManager.getSupportedCameras()[0]
    let mode = cameraManager.getSupportedSceneModes(device)[0]
    let ability = cameraManager.getSupportedOutputCapability(device, mode)
    let size = ImageSize(8, 8192)
    let receiver = createImageReceiver(size, ImageFormat.Jpeg, 8)
    let surfaceId: String = receiver.getReceivingSurfaceId()
    let output = cameraManager.createPreviewOutput(ability.previewProfiles[0], surfaceId)
    output.setPreviewRotation(ImageRotation.Rotation90)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```