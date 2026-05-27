### func getFrameCount()

```cangjie
public func getFrameCount(): UInt32
```

**功能：** 获取图像帧数。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回图像帧数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |62980096|The operation failed.|
  |62980110|The image source data is incorrect.|
  |62980111|The image source data is incomplete.|
  |62980112|The image format does not match.|
  |62980113|Unknown image format.|
  |62980115|Invalid image parameter.|
  |62980116|Failed to decode the image.|
  |62980118|Failed to create the image plugin.|
  |62980122|The image decoding header is abnormal.|
  |62980137|Invalid media operation.|

### func getImageInfo(UInt32)

```cangjie
public func getImageInfo(index!: UInt32 = 0): ImageInfo
```

**功能：** 获取图片信息。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|UInt32|否|0| **命名参数。** 创建图片源时的序号，不选择时默认为0。|

**返回值：**

|类型|说明|
|:----|:----|
|[ImageInfo](#class-imageinfo)|返回获取到的图片信息。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
let sourceOptions: SourceOptions = SourceOptions(sourceDensity: 120)
let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)
imageSourceApi.getImageInfo(index : 0)
```

### func getImageProperties(Array\<PropertyKey>)

```cangjie
public func getImageProperties(key: Array<PropertyKey>): Array<(PropertyKey, String)>
```

**功能：** 批量获取图片中的指定属性键的值。仅支持JPEG、PNG和HEIF（不同硬件设备支持情况不同）文件，且需要包含exif信息。其中可以通过supportedFormats属性查询是否支持HEIF格式的exif读写。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|Array\<[PropertyKey](#enum-propertykey)>|是|-|图片属性名的数组。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<([PropertyKey](#enum-propertykey), String)>|返回图片属性值，如获取失败则返回空字符串。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed;|
  |62980096|The operation failed.|
  |62980110|The image source data is incorrect.|
  |62980113|Unknown image format.|
  |62980116|Failed to decode the image.|