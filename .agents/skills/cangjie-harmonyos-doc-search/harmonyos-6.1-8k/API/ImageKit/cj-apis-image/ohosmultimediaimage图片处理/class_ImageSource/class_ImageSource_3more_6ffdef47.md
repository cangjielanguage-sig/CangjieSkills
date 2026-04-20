## class ImageSource

```cangjie
public class ImageSource {}
```

**功能：** ImageSource类，用于获取图片相关信息。

> **说明：**
>
> - 在调用ImageSource的方法前，需要先通过[createImageSource](#func-createimagesourcearrayuint8)构建一个ImageSource实例。
>
> - ImageSource的所有方法均不支持并发调用。
>
> - 由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](#func-release-3)方法及时释放内存。释放时应确保后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

### prop supportedFormats

```cangjie
public prop supportedFormats: Array<String>
```

**功能：** 支持的图片格式，包括：png，jpeg，bmp，gif，webp，dng，heic（不同硬件设备支持情况不同）。

**类型：** Array\<String>

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980102 | Failed to malloc memory. |
  | 62980104 | Failed to initialize the internal object. |

### func createPixelMap(DecodingOptions)

```cangjie
public func createPixelMap(options!: DecodingOptions = DecodingOptions()): PixelMap
```

**功能：** 通过图片解码参数创建PixelMap对象。

> **说明：**
>
> 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](#func-release-4)方法，及时释放内存。释放时应确保后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[DecodingOptions](#class-decodingoptions)|否|DecodingOptions()|**命名参数。** 解码参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](#class-pixelmap)|返回PixelMap。|

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980104 | Failed to initialize the internal object. |

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
    let pixelMap = imageSourceApi.createPixelMap(options: option)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```