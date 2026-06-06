## interface ColorManagement

```cangjie
sealed interface ColorManagement <: ColorManagementQuery {
    func setColorSpace(colorSpace: ColorSpace): Unit
    func getActiveColorSpace(): ColorSpace
}
```

**功能：** 用于管理色彩空间参数。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- [ColorManagementQuery](#interface-colormanagementquery)

### func getActiveColorSpace()

```cangjie
func getActiveColorSpace(): ColorSpace
```

**功能：** 获取当前设置的色彩空间。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[ColorSpace](../ArkGraphics2D/cj-apis-color_manager.md#enum-colorspace)|当前设置的色彩空间。|

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
let colorSpace = photoSession.getActiveColorSpace()
```

### func setColorSpace(ColorSpace)

```cangjie
func setColorSpace(colorSpace: ColorSpace): Unit
```

**功能：** 设置色彩空间。可以先通过[getSupportedColorSpaces](#func-getsupportedcolorspaces)获取当前设备所支持的ColorSpaces。

应用可以下发不同的色彩空间（[ColorSpace](../ArkGraphics2D/cj-apis-color_manager.md#enum-colorspace)）参数来支持P3广色域以及HDR高动态范围成像的功能。

当应用不主动设置色彩空间时，拍照以及录像模式默认为HDR拍摄效果。

在拍照模式下设置HDR高显效果可直接支持P3色域。

应用针对不同模式使能HDR效果以及设置的色彩空间可参考下表。

表1：录像模式

|SDR/HRD拍摄|CameraFormat|ColorSpace|
|:---|:---|:---|
|SDR|CAMERA_FORMAT_YUV_420_SP|BT709_LIMIT|
|HDR_VIVID(Default)|CAMERA_FORMAT_YCRCB_P010|BT2020_HLG_LIMIT|

表2：拍照模式

|SDR/HRD拍摄|ColorSpace|
|:---|:---|
|SDR|SRGB|
|HDR_VIVID(Default)|DISPLAY_P3|

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|colorSpace|[ColorSpace](../ArkGraphics2D/cj-apis-color_manager.md#enum-colorspace)|是|-|色彩空间，通过[getSupportedColorSpaces](#func-getsupportedcolorspaces)接口获取。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID|错误信息|
  |:----|:----|
  |7400101|Parameter missing or parameter type incorrect.|
  |7400102|The colorSpace does not match the format.|
  |7400103|Session not config.|
  |7400201|Camera service fatal error.|

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
let colorSpace = photoSession.getSupportedColorSpaces()[0]
photoSession.setColorSpace(colorSpace)
```