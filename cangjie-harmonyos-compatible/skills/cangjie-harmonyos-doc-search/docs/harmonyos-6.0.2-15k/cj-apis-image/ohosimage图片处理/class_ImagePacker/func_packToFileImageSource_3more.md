### func packToFile(ImageSource, IntNative, PackingOption)

```cangjie
public func packToFile(source: ImageSource, fd: IntNative, option: PackingOption): Unit
```

**功能：** 图片压缩或重新打包到文件中。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|source|[ImageSource](#class-imagesource)|是|-|打包的图片源。|
|fd|IntNative|是|-|打包的目的文件的文件描述符。|
|option|[PackingOption](#class-packingoption)|是|-|设置打包参数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*
import ohos.file_fs.*

let imagePacker = createImagePacker()
var colors: Array<UInt8> = [80, 2, 4, 8, 40, 2, 4, 8]
var imageSource = createImageSource("xxx/test.jpg")
var fd: Int32 = 0
let filePath = "data/storage/el1/base/temp.txt"
let file = FileFs.open(
    filePath,
    mode: (OpenMode
        .CREATE
        .mode | OpenMode
        .READ_WRITE
        .mode)
)
let packingOption = PackingOption("image/jpeg", 98)
imagePacker.packToFile(imageSource, IntNative(fd), packingOption)
```

### func packToFile(Picture, IntNative, PackingOption)

```cangjie
public func packToFile(source: Picture, fd: IntNative, option: PackingOption): Unit
```

**功能：** 指定编码参数，将Picture直接编码进文件。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|source|[Picture](#class-picture)|是|-|编码的Picture资源。|
|fd|IntNative|是|-|文件描述符。|
|option|[PackingOption](#class-packingoption)|是|-|设置编码参数。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |62980115|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.|
  |7800301|Encode failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let color: Array<UInt8> = Array<UInt8>(96, repeat: 0) //96为需要创建的像素buffer大小，取值为：height * width *4
let opts: InitializationOptions = InitializationOptions(editable: true, pixelFormat: RGBA_8888,
    size: Size(height: 4, width: 6))
let pixelMap = createPixelMap(color, opts)
let picture = createPicture(pixelMap)
var fd: Int32 = 0
let filePath = "data/storage/el1/base/xxx.txt"
let file = FileFs.open(filePath,mode: (OpenMode.CREATE.mode | OpenMode.READ_WRITE.mode))
let packingOption = PackingOption("image/jpeg", 98)
imagePacker.packToFile(picture, IntNative(fd), packingOption)
```

### func packing(ImageSource, PackingOption)

```cangjie
public func packing(source: ImageSource, option: PackingOption): Array<UInt8>
```

**功能：** 图片压缩或重新打包，返回Array\<UInt8>结果。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|source|[ImageSource](#class-imagesource)|是|-|打包的图片源。|
|option|[PackingOption](#class-packingoption)|是|-|设置打包参数。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt8>|用于获取压缩或打包后的数据。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

var imageSource = createImageSource("xxx/test.jpg")
var imagePacker = createImagePacker()
let packingOption = PackingOption("image/jpeg", 98)
let packRes = imagePacker.packing(imageSource, packingOption)
```