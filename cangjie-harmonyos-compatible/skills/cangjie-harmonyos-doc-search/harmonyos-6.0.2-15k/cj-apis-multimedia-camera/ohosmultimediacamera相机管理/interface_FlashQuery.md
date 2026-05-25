## interface FlashQuery

```cangjie
sealed interface FlashQuery {
    func hasFlash(): Bool
    func isFlashModeSupported(flashMode: FlashMode): Bool
}
```

**功能：** 提供了查询设备的闪光灯状态和模式的能力。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### func hasFlash()

```cangjie
func hasFlash(): Bool
```

**功能：** 检测是否有闪光灯。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示设备支持闪光灯，false表示不支持。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID|错误信息|
  |:----|:----|
  |7400103|Session not config, only throw in session usage.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.base.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let session = cameraManager.createSession(SceneMode.NORMAL_PHOTO)
var photoSessionOption = session as PhotoSession
let photoSession = photoSessionOption.getOrThrow()
AppLog.info(photoSession.hasFlash())
```

### func isFlashModeSupported(FlashMode)

```cangjie
func isFlashModeSupported(flashMode: FlashMode): Bool
```

**功能：** 检测是否支持指定的闪光灯模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|flashMode|[FlashMode](#enum-flashmode)|是|-|指定闪光灯模式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示支持该闪光灯模式，false表示不支持。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID|错误信息|
  |:----|:----|
  |7400103|Session not config, only throw in session usage.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let session = cameraManager.createSession(SceneMode.NORMAL_PHOTO)
var photoSessionOption = session as PhotoSession
let photoSession = photoSessionOption.getOrThrow()
photoSession.isFlashModeSupported(FlashMode.FLASH_MODE_ALWAYS_OPEN)
```