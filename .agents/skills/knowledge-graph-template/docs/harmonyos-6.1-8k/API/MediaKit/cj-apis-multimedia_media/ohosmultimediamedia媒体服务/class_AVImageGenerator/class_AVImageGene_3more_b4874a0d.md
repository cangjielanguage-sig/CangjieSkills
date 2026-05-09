## class AVImageGenerator

```cangjie
public class AVImageGenerator {}
```

**功能：** 视频缩略图获取类，用于从视频资源中获取缩略图。在调用AVImageGenerator的方法前，需要先通过[createAVImageGenerator()](#func-createavimagegenerator)构建一个AVImageGenerator实例。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 22

### prop fdSrc

```cangjie
public mut prop fdSrc: AVFileDescriptor
```

**功能：** 媒体文件描述，通过该属性设置数据源。

使用示例：

假设一个连续存储的媒体文件，地址偏移：0，字节长度：100。其文件描述为AVFileDescriptor { fd = 资源句柄; offset = 0; length = 100; }。

> **说明：**
>
> 将资源句柄（fd）传递给AVImageGenerator实例之后，不允许通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer/AVImageGenerator/AVTranscoder。同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致视频缩略图数据获取异常。

**类型：** [AVFileDescriptor](#class-avfiledescriptor)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[Media错误码](./cj-errorcode-multimedia-media.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 5400101 | No memory. |
  | 5400102 | Operation not allowed. |

### func fetchFrameByTime(Int64, AVImageQueryOptions, PixelMapParams)

```cangjie
public func fetchFrameByTime(timeUs: Int64, options: AVImageQueryOptions, param: PixelMapParams): PixelMap
```

**功能：** 获取视频缩略图。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|timeUs|Int64|是|-|需要获取的缩略图在视频中的时间点，单位为微秒（μs）。|
|options|[AVImageQueryOptions](#enum-avimagequeryoptions)|是|-| 需要获取的缩略图时间点与视频帧的对应关系。|
|param|[PixelMapParams](#class-pixelmapparams)|是|-|需要获取的缩略图的格式参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|视频缩略图。|

**异常：**

- BusinessException：对应错误码如下表，详见[Media错误码](./cj-errorcode-multimedia-media.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 5400101 | No memory. |
  | 5400102 | Operation not allowed. |
  | 5400106 | Unsupported format. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import kit.LocalizationKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let timeUs = 0
    let queryOption = AVImageQueryOptions.AvImageQueryNextSync
    let param = PixelMapParams(width: 300, height: 300)
    let generator = createAVImageGenerator()
    let abilityContext = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let rawFd = abilityContext.resourceManager.getRawFd("trailer.mp4")    // 请替换您的资源路径，获取文件路径参考本文使用说明
    generator.fdSrc = AVFileDescriptor(rawFd.fd, offset: rawFd.offset, length: rawFd.length)
    let pic = generator.fetchFrameByTime(timeUs, queryOption, param)
    generator.release()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```