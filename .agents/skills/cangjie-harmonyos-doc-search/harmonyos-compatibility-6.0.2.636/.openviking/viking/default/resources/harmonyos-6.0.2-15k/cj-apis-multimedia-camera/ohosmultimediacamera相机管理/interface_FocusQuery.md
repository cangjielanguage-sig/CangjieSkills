## interface FocusQuery

```cangjie
sealed interface FocusQuery {
    func isFocusModeSupported(afMode: FocusMode): Bool
}
```

**功能：** 提供了查询是否支持指定对焦模式的方法。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### func isFocusModeSupported(FocusMode)

```cangjie
func isFocusModeSupported(afMode: FocusMode): Bool
```

**功能：** 检测对焦模式是否支持。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|afMode|[FocusMode](#enum-focusmode)|是|-|指定的焦距模式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示支持该焦距模式，false表示不支持。|

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
let afMode = FocusMode.FOCOS_MODE_MANUAL
AppLog.info(photoSession.isFocusModeSupported(afMode))
```