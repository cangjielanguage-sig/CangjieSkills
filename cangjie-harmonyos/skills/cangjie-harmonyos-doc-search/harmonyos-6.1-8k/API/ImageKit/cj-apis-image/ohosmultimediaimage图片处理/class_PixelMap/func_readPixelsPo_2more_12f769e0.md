### func readPixels(PositionArea)

```cangjie
public func readPixels(area: PositionArea): Unit
```

**功能：** 按照PixelMap的像素格式，读取PixelMap的图像像素数据，并写入缓冲区中。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|area|[PositionArea](#class-positionarea)|是|-|缓冲区，函数执行结束后获取的图像像素数据写入到该内存区域内。缓冲区大小由[getPixelBytesNumber](#func-getpixelbytesnumber)接口获取。|

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
    let area: PositionArea = PositionArea(
        Array<UInt8>(8, repeat: 0),
        0,
        8,
        Region(Size(1, 2), 0, 0)
    )
    pixelMap.readPixels(area)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func readPixelsToBuffer(Array\<UInt8>)

```cangjie
public func readPixelsToBuffer(dst: Array<UInt8>): Unit
```

**功能：** 按照PixelMap的像素格式，读取PixelMap的图像像素数据，并写入缓冲区中。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dst|Array\<UInt8>|是|-|缓冲区，函数执行结束后获取的图像像素数据写入到该内存区域内。缓冲区大小由[getPixelBytesNumber](#func-getpixelbytesnumber)接口获取。|

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
    let readBuffer: Array<UInt8> = Array<UInt8>(96, repeat: 0) //96为需要创建的像素buffer大小，取值为：height * width *4
    pixelMap.readPixelsToBuffer(readBuffer)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```