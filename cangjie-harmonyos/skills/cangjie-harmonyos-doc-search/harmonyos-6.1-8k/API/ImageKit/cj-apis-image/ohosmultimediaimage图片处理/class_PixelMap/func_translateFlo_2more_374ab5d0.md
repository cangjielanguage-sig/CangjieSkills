### func translate(Float32, Float32)

```cangjie
public func translate(x: Float32, y: Float32): Unit
```

**功能：** 根据输入的坐标对图片进行位置变换。

translate后的图片尺寸改变为：width+X ，height+Y，建议translate后的图片尺寸宽高不要超过屏幕的宽高。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|是|-|区域横坐标。单位：像素。|
|y|Float32|是|-|区域纵坐标。单位：像素。|

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
    let translateX: Float32 = 50.0
    let translateY: Float32 = 10.0
    pixelMap.translate(translateX, translateY)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func writeBufferToPixels(Array\<UInt8>)

```cangjie
public func writeBufferToPixels(src: Array<UInt8>): Unit
```

**功能：** 按照PixelMap的像素格式，读取缓冲区中的图像像素数据，并写入PixelMap。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|Array\<UInt8>|是|-|缓冲区，函数执行时会将该缓冲区中的图像像素数据写入到PixelMap。缓冲区大小由[getPixelBytesNumber](#func-getpixelbytesnumber)接口获取。|

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
    let color: Array<UInt8> = Array<UInt8>(96, {i => UInt8(i)}) //96为需要创建的像素buffer大小，取值为：height * width *4
    pixelMap.writeBufferToPixels(color)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```