### func flip(Bool, Bool)

```cangjie
public func flip(horizontal: Bool, vertical: Bool): Unit
```

**功能：** 根据输入的条件对图片进行翻转。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|horizontal|Bool|是|-|水平翻转。|
|vertical|Bool|是|-|垂直翻转。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
let sourceOptions: SourceOptions = SourceOptions(sourceDensity: 120)
let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)
let pixelMap = imageSourceApi.createPixelMap()
let horizontal: Bool = true
let vertical: Bool = false
pixelMap.flip(horizontal, vertical)
```

### func getBytesNumberPerRow()

```cangjie
public func getBytesNumberPerRow(): UInt32
```

**功能：** 获取图像像素每行字节数。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|图像像素的行字节数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
let sourceOptions: SourceOptions = SourceOptions(sourceDensity: 120)
let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)
let pixelMap = imageSourceApi.createPixelMap()
let rowCount: UInt32 = pixelMap.getBytesNumberPerRow()
```

### func getColorSpace()

```cangjie
public func getColorSpace(): ColorSpaceManager
```

**功能：** 获取图像广色域信息。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[ColorSpaceManager](../ArkGraphics2D/cj-apis-color_manager.md#class-colorspacemanager)|图像广色域信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |62980101|If the image data abnormal.|
  |62980103|If the image data unsupport.|
  |62980115|If the image parameter invalid.|

### func getDensity()

```cangjie
public func getDensity(): Int32
```

**功能：** 获取当前图像像素的密度。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|图像像素的密度。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
let sourceOptions: SourceOptions = SourceOptions(sourceDensity: 120)
let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)
let pixelMap = imageSourceApi.createPixelMap()
let getDensity: Int32 = pixelMap.getDensity()
```

### func getImageInfo()

```cangjie
public func getImageInfo(): ImageInfo
```

**功能：** 获取图像像素信息。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[ImageInfo](#class-imageinfo)|用于获取图像像素信息，失败时返回错误信息。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
let sourceOptions: SourceOptions = SourceOptions(sourceDensity: 120)
let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)
let pixelMap = imageSourceApi.createPixelMap()
pixelMap.getImageInfo()
```