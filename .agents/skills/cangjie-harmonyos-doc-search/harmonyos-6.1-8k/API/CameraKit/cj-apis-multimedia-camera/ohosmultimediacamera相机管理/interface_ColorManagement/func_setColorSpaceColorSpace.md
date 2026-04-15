### func setColorSpace(ColorSpace)

```cangjie
func setColorSpace(colorSpace: ColorSpace): Unit
```

**功能：** 设置色彩空间。

使用该接口前，必须先通过[getSupportedColorSpaces](#func-getsupportedcolorspaces)获取当前设备所支持的ColorSpaces。该接口建议在[addOutput](#func-addoutputcameraoutput)之后、[commitConfig](#func-commitconfig)之前调用，如果在[commitConfig](#func-commitconfig)之后调用该接口，会导致相机会话配置耗时增加。

**P3广色域与HDR高动态范围成像**

应用可以下发不同的色彩空间(ColorSpace)参数来支持P3广色域以及HDR的功能。
当应用不主动设置色彩空间时，拍照模式默认为SDR拍摄效果。
在拍照模式下若需要获取HDR高显效果的图片可通过设置色彩空间P3色域实现。
应用针对不同模式使能HDR效果、设置的色彩空间以及设置相机输出流[Profile](#class-profile)中的[CameraFormat](#enum-cameraformat)一一对应关系可参考下表。例如，在录像模式下若需要选择HDR拍摄，相机预览输出流和录像输出流[Profile](#class-profile)中的[CameraFormat](#enum-cameraformat)可选择CameraFormatYcrcbP010，色彩空间ColorSpace可选择设置Bt2020HlgLimit。

在录像模式下，使能SDR或HDR_VIVID拍摄效果时，CameraFormat与ColorSpace必须按照下列表格中的对应关系配置，若不满足表格中CameraFormat与ColorSpace配置，会导致预览异常等问题。

**录像模式：**

| SDR/HDR拍摄         | CameraFormat             | ColorSpace       |
|--------------------|--------------------------|------------------|
| SDR                | CameraFormatYuv420Sp | Bt709Limit      |
| HDR_VIVID          | CameraFormatYcrcbP010<br>CameraFormatYcbcrP010 | Bt2020HlgLimit |

**拍照模式：**

| SDR/HDR拍摄        | ColorSpace |
|--------------------|------------|
| SDR(Default)       | Srgb      |
| HDR                | DisplayP3 |

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|colorSpace|[ColorSpace](../ArkGraphics2D/cj-apis-color_manager.md#enum-colorspace)|是|-|色彩空间，通过[getSupportedColorSpaces](#func-getsupportedcolorspaces)接口获取。|

**异常：**

- BusinessException：对应错误码如下表，详见[Camera错误码](./cj-errorcode-multimedia-camera.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 7400101 | Parameter missing or parameter type incorrect. |
  | 7400102 | The colorSpace does not match the format. |
  | 7400103 | Session not config. |
  | 7400201 | Camera service fatal error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let cameraManager = getCameraManager(ctx)
    let session = cameraManager.createSession(SceneMode.NormalPhoto)
    var photoSessionOption = session as PhotoSession
    let photoSession = photoSessionOption.getOrThrow()
    let colorSpaces = photoSession.getSupportedColorSpaces()
    if (colorSpaces.size > 0) {
        let colorSpace = colorSpaces[0]
        photoSession.setColorSpace(colorSpace)
    }
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```