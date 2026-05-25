### func packToFile(ImageSource, Int32, PackingOption)

```cangjie
public func packToFile(source: ImageSource, fd: Int32, options: PackingOption): Unit
```

**功能：** 指定编码参数，将ImageSource直接编码进文件。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|source|[ImageSource](#class-imagesource)|是|-|编码的ImageSource。|
|fd|Int32|是|-|文件描述符。|
|options|[PackingOption](#class-packingoption)|是|-|设置编码参数。|

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
  | 62980101 | The image data is abnormal. |
  | 62980104 | Failed to initialize the internal object. |
  | 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
  | 62980113 | Unknown image format. The image data provided is not in a recognized or supported format, or it may be occorrupted. |
  | 62980115 | Invalid input parameter. |
  | 62980119 | Failed to encode the image. |
  | 62980120 | Add pixelmap out of range. |
  | 62980172 | Failed to encode icc. |
  | 62980252 | Failed to create surface. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*
import kit.CoreFileKit.{FileIo, OpenMode}
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
    let sourceOptions: SourceOptions = SourceOptions(120)
    let imageSource: ImageSource = createImageSource(data, sourceOptions)  // 请替换为正确的图片源，参考本文使用说明。
    var fd: Int32 = 0
    let filePath = "data/storage/el1/base/xxx.txt"
    let file = FileIo.open(filePath,mode: (OpenMode.CREATE | OpenMode.READ_WRITE))
    let packingOption = PackingOption("image/jpeg", 98)
    let imagePacker = createImagePacker()
    imagePacker.packToFile(imageSource, fd, packingOption)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```