### func packToData(PixelMap, PackingOption)

```cangjie
public func packToData(source: PixelMap, option: PackingOption): Array<UInt8>
```

**功能：** 图片压缩或重新编码。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|source|[PixelMap](#class-pixelmap)|是|-|打包的图片源。|
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

var colors: Array<UInt8> = [80, 2, 4, 8, 40, 2, 4, 8]
var pm = createPixelMap(colors, InitializationOptions(scaleMode: ScaleMode.CENTER_CROP, size: Size(height: 2, width: 1))
)
var imagePacker = createImagePacker()
let supportedFormats = imagePacker.supportedFormats
let packingOption = PackingOption("image/jpeg", 98)
let packRes = imagePacker.packToData(pm, packingOption)
```

### func packToFile(PixelMap, IntNative, PackingOption)

```cangjie
public func packToFile(source: PixelMap, fd: IntNative, option: PackingOption): Unit
```

**功能：** 图片压缩或重新打包到文件中。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|source|[PixelMap](#class-pixelmap)|是|-|打包的图片源。|
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
var pm = createPixelMap(colors,
    InitializationOptions(scaleMode: ScaleMode.CENTER_CROP, size: Size(height: 4, width: 3)))
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
imagePacker.packToFile(pm, IntNative(fd), packingOption)
```