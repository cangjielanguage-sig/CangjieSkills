### func getImageProperty(PropertyKey, ImagePropertyOptions)

```cangjie
public func getImageProperty(key: PropertyKey, options!: ImagePropertyOptions = ImagePropertyOptions()): String
```

**功能：** 获取图片中给定索引处图像的指定属性键的值，仅支持JPEG文件，且需要包含exif信息。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[PropertyKey](#enum-propertykey)|是|-|图片属性名。|
|options|[ImagePropertyOptions](#struct-imagepropertyoptions)|否|ImagePropertyOptions()| **命名参数。** 图片属性，包括图片序号与默认属性值。|

**返回值：**

|类型|说明|
|:----|:----|
|String|获取图片属性值，如获取失败则返回属性默认值。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
let sourceOptions: SourceOptions = SourceOptions(sourceDensity: 120)
let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)
imageSourceApi.getImageProperty(IMAGE_LENGTH)
```

### func modifyImageProperties(Array\<(PropertyKey, String)>)

```cangjie
public func modifyImageProperties(records: Array<(PropertyKey, String)>): Unit
```

**功能：** 批量通过指定的键修改图片属性的值。仅支持JPEG、PNG和HEIF（不同硬件设备支持情况不同）文件，且需要包含exif信息。其中可以通过supportedFormats属性查询是否支持HEIF格式的exif读写。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|records|Array\<([PropertyKey](#enum-propertykey), String)>|是|-|包含图片属性名和属性值的数组。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed;|
  |62980123|The image does not support EXIF decoding.|
  |62980133|The EXIF data is out of range.|
  |62980135|The EXIF value is invalid.|
  |62980146|The EXIF data failed to be written to the file.|

### func modifyImageProperty(PropertyKey, String)

```cangjie
public func modifyImageProperty(key: PropertyKey, value: String): Unit
```

**功能：** 通过指定的键修改图片属性的值，仅支持JPEG文件，且需要包含exif信息。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[PropertyKey](#enum-propertykey)|是|-|图片属性名。|
|value|String|是|-|属性值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|The parameter check failed.|
  |62980123|The parameter check failed.|
  |62980133|The image source data is incomplete.|
  |62980135|The image source data is incomplete.|
  |62980146|The EXIF data failed to be written to the file.|