## interface Flash

```cangjie
sealed interface Flash <: FlashQuery {
    func setFlashMode(flashMode: FlashMode): Unit
    func getFlashMode(): FlashMode
}
```

**功能：** 设备闪光灯操作。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- [FlashQuery](#interface-flashquery)

### func getFlashMode()

```cangjie
func getFlashMode(): FlashMode
```

**功能：** 获取当前设备的闪光灯模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[FlashMode](#enum-flashmode)|当前设备的闪光灯模式。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID|错误信息|
  |:----|:----|
  |7400103|Session not config.|

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
let flashMode = photoSession.getFlashMode()
```

### func setFlashMode(FlashMode)

```cangjie
func setFlashMode(flashMode: FlashMode): Unit
```

**功能：** 设置闪光灯模式。

进行设置之前，需要先检查：

1. 设备是否支持闪光灯，可使用方法[hasFlash](#func-hasflash)判断。
2. 设备是否支持指定的闪光灯模式，可使用方法[isFlashModeSupported](#func-isflashmodesupportedflashmode)判断。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|flashMode|[FlashMode](#enum-flashmode)|是|-|指定闪光灯模式。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID|错误信息|
  |:----|:----|
  |7400103|Session not config.|

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
let flashMode = FlashMode.FLASH_MODE_ALWAYS_OPEN
photoSession.setFlashMode(flashMode)
```