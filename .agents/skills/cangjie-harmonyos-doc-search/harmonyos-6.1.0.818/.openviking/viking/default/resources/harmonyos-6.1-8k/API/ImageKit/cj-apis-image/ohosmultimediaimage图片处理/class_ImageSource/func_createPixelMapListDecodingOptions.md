### func createPixelMapList(DecodingOptions)

```cangjie
public func createPixelMapList(options!: DecodingOptions = DecodingOptions()): Array<PixelMap>
```

**功能：** 通过图片解码参数创建PixelMap数组。

> **说明：**
>
> - 针对动图如Gif、Webp，此接口返回每帧图片数据；针对静态图，此接口返回唯一的一帧图片数据。
>
> - 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](#func-release-4)方法，及时释放内存。释放时应确保后续不再使用该对象。

> **注意：**
>
> - 此接口会一次性解码全部帧，当帧数过多或单帧图像过大时，会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接口少。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[DecodingOptions](#class-decodingoptions)|否|DecodingOptions()|**命名参数。** 解码参数。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[PixelMap](#class-pixelmap)>|返回PixeMap数组。|

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
  | 62980099 | The shared memory data is abnormal. |
  | 62980101 | The image data is abnormal. |
  | 62980102 | Failed to malloc memory. |
  | 62980103 | The image data is not supported. |
  | 62980104 | Failed to initialize the internal object. |
  | 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
  | 62980109 | Failed to crop the image. |
  | 62980111 | The image source data is incomplete. |
  | 62980115 | Invalid image parameter. |
  | 62980116 | Failed to decode the image. |
  | 62980118 | Failed to create the image plugin. |
  | 62980137 | Invalid media operation. |
  | 62980173 | The DMA memory does not exist. |
  | 62980174 | The DMA memory data is abnormal. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
    let sourceOptions: SourceOptions = SourceOptions(120)
    let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)  // 请替换为正确的图片源，参考本文使用说明。
    let option = DecodingOptions(
        sampleSize: 1,
        rotate: 10,
        editable: true,
        desiredSize: Size(3, 4),
        desiredRegion: Region(Size(3, 4), 0, 0),
        desiredPixelFormat: PixelMapFormat.Rgba8888,
        index: 0,
        fitDensity: 20
    )
    let pixelMap = imageSourceApi.createPixelMapList(options: option)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```