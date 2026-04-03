## class ImagePacker

```cangjie
public class ImagePacker {}
```

**功能：** 图片打包器类，用于图片压缩和打包。在调用ImagePacker的方法前，需要先通过[createImagePacker](#func-createimagepacker)构建一个ImagePacker实例，当前支持格式有：jpeg、webp、png。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 12

### prop supportedFormats

```cangjie
public prop supportedFormats: Array<String>
```

**功能：** 图片打包支持的格式jpeg、webp、png。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 12

### func Release()<sup>(deprecated)</sup>

```cangjie
public func Release(): Unit
```

**功能：** 释放图片打包实例。

> **注意：**
>
> 从API version 19版本开始废弃不再维护，可使用[release](#func-release-2)替代。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let imagePacker = createImagePacker()
imagePacker.Release()
```

### func release()

```cangjie
public func release(): Unit
```

**功能：** 释放图片打包实例。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let imagePacker = createImagePacker()
imagePacker.release()
```

### func packToData(ImageSource, PackingOption)

```cangjie
public func packToData(source: ImageSource, option: PackingOption): Array<UInt8>
```

**功能：** 图片压缩或重新编码。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|source|[ImageSource](#class-imagesource)|是|-|打包的图片源。|
|option|[PackingOption](#class-packingoption)|是|-|设置打包参数。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt8>|用于获取压缩或打包后的数据。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |62980115|The operation failed.|
  |62980096|If the parameter is invalid.|
  |62980101|The image data is abnormal.|
  |62980106|The image is too large.|
  |62980113|Unknown image format.|
  |62980119|If encoder occur error during encoding.|
  |62980120|Add pixelmap out of range.|
  |62980172|Failed to encode icc.|
  |62980252|Failed to create surface.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

var imageSource = createImageSource("xxx/test.jpg")
var imagePacker = createImagePacker()
let packingOption = PackingOption("image/jpeg", 98)
let packRes = imagePacker.packToData(imageSource, packingOption)
```