## class ImageSource

```cangjie
public class ImageSource {}
```

**功能：** 图片源类，用于获取图片相关信息。在调用ImageSource的方法前，需要先通过createImageSource构建一个ImageSource实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

### prop supportedFormats

```cangjie
public prop supportedFormats: Array<String>
```

**功能：** 支持的图片格式，包括：png，jpeg，bmp，gif，webp，RAW。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 12

### func Release()<sup>(deprecated)</sup>

```cangjie
public func Release(): Unit
```

**功能：** 释放图片源实例。

> **注意：**
>
> 从API version 19版本开始废弃不再维护，可使用[release](#func-release-4)替代。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
let sourceOptions: SourceOptions = SourceOptions(sourceDensity: 120)
let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)
imageSourceApi.Release()
```

### func release()

```cangjie
public func release(): Unit
```

**功能：** 释放图片源实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
let sourceOptions: SourceOptions = SourceOptions(sourceDensity: 120)
let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)
imageSourceApi.release()
```

### func createPixelMap(DecodingOptions)

```cangjie
public func createPixelMap(options!: DecodingOptions = DecodingOptions()): PixelMap
```

**功能：** 通过图片解码参数创建PixelMap对象。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[DecodingOptions](#class-decodingoptions)|否|DecodingOptions()| **命名参数。** 解码参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](#class-pixelmap)|返回pixelMap实例|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
let sourceOptions: SourceOptions = SourceOptions(sourceDensity: 120)
let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)
let option = DecodingOptions(
    sampleSize: 1,
    rotate: 10,
    editable: true,
    desiredSize: Size(height: 3, width: 4),
    desiredRegion: Region(Size(height: 3, width: 4), 0, 0),
    desiredPixelFormat: PixelMapFormat.RGBA_8888,
    index: 0,
    fitDensity: 20
)
let pixelMap = imageSourceApi.createPixelMap(options: option)
```