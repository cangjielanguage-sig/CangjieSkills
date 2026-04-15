### func packToData(PixelMap, PackingOption)

```cangjie
public func packToData(source: PixelMap, options: PackingOption): Array<UInt8>
```

**功能：** 图片压缩或重新编码。

> **注意：**
> 接口如果返回62980115错误码，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|source|[PixelMap](#class-pixelmap)|是|-|编码的PixelMap源。|
|options|[PackingOption](#class-packingoption)|是|-|设置编码参数。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt8>|返回压缩或编码后的数据。|

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980096 | The operation failed. Possible cause: 1.Image upload exception.2. Decoding process exception. 3. Insufficient memory. |
  | 62980101 | The image data is abnormal. |
  | 62980104 | Failed to initialize the internal object. |
  | 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
  | 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be occorrupted. |
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
    var colors: Array<UInt8> = [80, 2, 4, 8, 40, 2, 4, 8]
    var pm = createPixelMap(colors,
        InitializationOptions(Size(2, 1), scaleMode: ScaleMode.CenterCrop))
    var imagePacker = createImagePacker()
    let supportedFormats = imagePacker.supportedFormats
    let packingOption = PackingOption("image/jpeg", 98)
    let packRes = imagePacker.packToData(pm, packingOption)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```