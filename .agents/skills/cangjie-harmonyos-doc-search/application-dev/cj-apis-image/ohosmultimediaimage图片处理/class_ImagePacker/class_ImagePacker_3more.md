## class ImagePacker

```cangjie
public class ImagePacker {}
```

**功能：** ImagePacker类，用于图片压缩和编码。

> **说明：**
>
> - 在调用ImagePacker的方法前，需要先通过[createImagePacker](#func-createimagepacker)构建一个ImagePacker实例。
>
> - 编码期间，请避免修改或释放作为输入的ImageSource/PixelMap对象，以免出现crash或其他未定义行为。
>
> - 由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用[release](#func-release-1)方法及时释放内存。释放时应确保后续不再使用该实例。
>
> - 当前支持的格式有：jpeg、webp、png、heif、gif（不同硬件设备支持情况不同，可通过ImagePacker的supportedFormats属性查看）。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 22

### prop supportedFormats

```cangjie
public prop supportedFormats: Array<String>
```

**功能：** 图片编码支持的格式，包括：jpeg、webp、png、heic、gif（不同硬件设备支持情况不同）

**类型：** Array\<String>

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980098 | Failed to malloc memory. |
  | 62980104 | Failed to initialize the internal object. |

### func packToData(ImageSource, PackingOption)

```cangjie
public func packToData(source: ImageSource, options: PackingOption): Array<UInt8>
```

**功能：** 图片压缩或重新编码。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|source|[ImageSource](#class-imagesource)|是|-|编码的ImageSource。|
|options|[PackingOption](#class-packingoption)|是|-|设置编码参数。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt8>|返回压缩或编码后的数据。|

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
  | 62980101 | The image data is abnormal. |
  | 62980104 | Failed to initialize the internal object. |
  | 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
  | 62980113 | Unknown image format. The image data provided is not in a recognized or supported format, or it may be occorrupted. |
  | 62980115 | If the parameter is invalid. |
  | 62980119 | Failed to encode the image. |
  | 62980120 | Add pixelmap out of range. |
  | 62980172 | Failed to encode icc. |
  | 62980252 | Failed to create surface. |

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
    let imageSource: ImageSource = createImageSource(data, sourceOptions)  // 请替换为正确的图片源，参考本文使用说明。
    var imagePacker = createImagePacker()
    let supportedFormats = imagePacker.supportedFormats
    let packingOption = PackingOption("image/jpeg", 98)
    let packRes = imagePacker.packToData(imageSource, packingOption)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```