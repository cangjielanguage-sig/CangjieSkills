### func convertPixelFormat(PixelMapFormat)

```cangjie
public func convertPixelFormat(targetPixelFormat: PixelMapFormat): Unit
```

**功能：** YUV和RGB类型互转，目前仅支持NV12/NV21与RGB888/RGBA8888/RGB565/BGRA8888/RGBAF16互转，YCRCB_P010/YCBCR_P010与RGBA1010102互转。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|targetPixelFormat|[PixelMapFormat](#enum-pixelmapformat)|是|-|目标像素格式，用于YUV和RGB类型互转。目前仅支持NV12/NV21与RGB888/RGBA8888/RGB565/BGRA8888/RGBAF16互转，YCRCB_P010/YCBCR_P010与RGBA1010102互转。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |62980111|The image source data is incomplete.|
  |62980115|Invalid input parameter.|
  |62980178|Failed to create the pixelmap.|
  |62980274|The conversion failed.|
  |62980276|The type to be converted is an unsupported target pixel format.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let color: Array<UInt8> = Array<UInt8>(96, repeat: 0) //96为需要创建的像素buffer大小，取值为：height * width *4
let opts: InitializationOptions = InitializationOptions(editable: true, pixelFormat: RGBA_8888,
    size: Size(height: 4, width: 6))
let pixelMap = createPixelMap(color, opts)
let targetPixelFormat = PixelMapFormat.NV12
pixelMap.convertPixelFormat(targetPixelFormat)
```

### func createAlphaPixelmap()

```cangjie
public func createAlphaPixelmap(): PixelMap
```

**功能：** 根据Alpha通道的信息，来生成一个仅包含Alpha通道信息的pixelmap，可用于阴影效果。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](#class-pixelmap)|返回pixelmap实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
let sourceOptions: SourceOptions = SourceOptions(sourceDensity: 120)
let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)
let pixelMap = imageSourceApi.createPixelMap()
let alphaPixelmap = pixelMap.createAlphaPixelmap()
```

### func crop(Region)

```cangjie
public func crop(region: Region): Unit
```

**功能：** 根据输入的尺寸对图片进行裁剪。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|region|[Region](#struct-region)|是|-|裁剪的尺寸。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
let sourceOptions: SourceOptions = SourceOptions(sourceDensity: 120)
let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)
let pixelMap = imageSourceApi.createPixelMap()
let region: Region = Region(Size(height: 100, width: 100), 0, 0)
pixelMap.crop(region)
```