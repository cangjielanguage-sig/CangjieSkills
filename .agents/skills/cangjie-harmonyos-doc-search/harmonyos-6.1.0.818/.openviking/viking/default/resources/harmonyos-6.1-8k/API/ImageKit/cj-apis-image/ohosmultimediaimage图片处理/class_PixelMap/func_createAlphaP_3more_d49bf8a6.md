### func createAlphaPixelMap()

```cangjie
public func createAlphaPixelMap(): PixelMap
```

**功能：** 根据Alpha通道的信息，来生成一个仅包含Alpha通道信息的pixelmap，可用于阴影效果，yuv格式不支持此接口。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](#class-pixelmap)|返回pixelmap实例。|

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
    let alphaPixelmap = pixelMap.createAlphaPixelMap()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func crop(Region)

```cangjie
public func crop(region: Region): Unit
```

**功能：** 根据输入的尺寸对图片进行裁剪。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|region|[Region](#class-region)|是|-|裁剪的尺寸。取值范围不能超过图片的宽高。|

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
    let region: Region = Region(Size(100, 100), 0, 0)
    pixelMap.crop(region)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func flip(Bool, Bool)

```cangjie
public func flip(horizontal: Bool, vertical: Bool): Unit
```

**功能：** 根据输入的条件对图片进行翻转。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|horizontal|Bool|是|-|true表示进行水平翻转，false表示不进行水平翻转。|
|vertical|Bool|是|-|true表示进行垂直翻转，false表示不进行垂直翻转。|

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
    let horizontal: Bool = true
    let vertical: Bool = false
    pixelMap.flip(horizontal, vertical)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```