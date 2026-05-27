### func packing(Picture, PackingOption)

```cangjie
public func packing(source: Picture, option: PackingOption): Array<UInt8>
```

**功能：** 将图像压缩或重新编码。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|source|[Picture](#class-picture)|是|-|编码的Picture对象。|
|option|[PackingOption](#class-packingoption)|是|-|设置打包参数。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt8>|返回压缩或编码后的数据。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6298011562980115|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.|
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
let packingOption = PackingOption("image/jpeg", 98)
let arr = imagePacker.packing(picture, packingOption)
```

### func packing(PixelMap, PackingOption)

```cangjie
public func packing(source: PixelMap, option: PackingOption): Array<UInt8>
```

**功能：** 图片压缩或重新打包，返回Array\<UInt8>结果。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|source|[PixelMap](#class-pixelmap)|是|-|打包的图片源。|
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

var colors: Array<UInt8> = [80, 2, 4, 8, 40, 2, 4, 8]
var pm = createPixelMap(colors, InitializationOptions(scaleMode: ScaleMode.CENTER_CROP, size: Size(height: 4, width: 3))
)
var imagePacker = createImagePacker()
let supportedFormats = imagePacker.supportedFormats
let packingOption = PackingOption("image/jpeg", 98)
let packRes = imagePacker.packing(pm, packingOption)
```