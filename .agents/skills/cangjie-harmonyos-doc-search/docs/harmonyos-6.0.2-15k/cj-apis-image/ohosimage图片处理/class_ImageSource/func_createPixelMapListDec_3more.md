### func createPixelMapList(DecodingOptions)

```cangjie
public func createPixelMapList(options!: DecodingOptions = DecodingOptions()): Array<PixelMap>
```

**功能：** 通过图片解码参数创建PixelMap数组。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[DecodingOptions](#class-decodingoptions)|否|DecodingOptions()| **命名参数。** 解码参数。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[PixelMap](#class-pixelmap)>|返回PixeMap数组。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |62980096|The operation failed.|
  |62980099|The shared memory data is abnormal.|
  |62980101|The image data is abnormal.|
  |62980103|The image data is not supported.|
  |62980106|The image is too large.|
  |62980109|Failed to crop the image.|
  |62980110|The image source data is incorrect.|
  |62980111|The image source data is incomplete.|
  |62980112|The image format does not match.|
  |62980113|Unknown image format.|
  |62980115|Invalid image parameter.|
  |62980116|Failed to decode the image.|
  |62980118|Failed to create the image plugin.|
  |62980122|The image decoding header is abnormal.|
  |62980137|Invalid media operation.|
  |62980173|The DMA memory does not exist.|
  |62980174|The DMA memory data is abnormal.|

### func getDelayTimeList()

```cangjie
public func getDelayTimeList(): Array<Int32>
```

**功能：** 获取图像延迟时间数组。此接口仅用于gif图片。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Int32>|返回延迟时间数组。|

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
  |62980149|Invalid MIME type for the image source.|

### func getDisposalTypeList()

```cangjie
public func getDisposalTypeList(): Array<Int32>
```

**功能：** 获取图像帧过渡模式数组。此接口仅用于gif图片。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Int32>|返回帧过渡模式数组。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |62980096|The operation failed.|
  |62980101|The image data is abnormal.|
  |62980137|Invalid media operation.|
  |62980149|Invalid MIME type for the image source.|