### func getImageInfo()

```cangjie
public func getImageInfo(): ImageInfo
```

**功能：** 获取图像像素信息。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[ImageInfo](#class-imageinfo)|返回图像像素信息。|

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
    let pixelMap = imageSourceApi.createPixelMap()
    pixelMap.getImageInfo()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getPixelBytesNumber()

```cangjie
public func getPixelBytesNumber(): UInt32
```

**功能：** 获取图像像素的总字节数。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|图像像素的总字节数。|

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
    let pixelMap = imageSourceApi.createPixelMap()
    let pixelBytesNumber : UInt32 = pixelMap.getPixelBytesNumber()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func opacity(Float32)

```cangjie
public func opacity(rate: Float32): Unit
```

**功能：** 通过设置透明比率来让PixelMap达到对应的透明效果，yuv图片不支持设置透明度。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rate|Float32|是|-|透明比率的值，取值范围是(0.0,1.0]。|

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
    let pixelMap = imageSourceApi.createPixelMap()
    let rate: Float32 = 0.5
    pixelMap.opacity(rate)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```