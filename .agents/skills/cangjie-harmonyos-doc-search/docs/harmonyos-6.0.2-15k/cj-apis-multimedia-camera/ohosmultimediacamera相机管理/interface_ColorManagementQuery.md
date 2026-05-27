## interface ColorManagementQuery

```cangjie
sealed interface ColorManagementQuery {
    func getSupportedColorSpaces(): Array<ColorSpace>
}
```

**功能：** 用于查询色彩空间参数。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### func getSupportedColorSpaces()

```cangjie
func getSupportedColorSpaces(): Array<ColorSpace>
```

**功能：** 获取支持的色彩空间列表。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[ColorSpace](../ArkGraphics2D/cj-apis-color_manager.md#enum-colorspace)>|支持的色彩空间列表。|

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
let colorSpaces = photoSession.getSupportedColorSpaces()
```