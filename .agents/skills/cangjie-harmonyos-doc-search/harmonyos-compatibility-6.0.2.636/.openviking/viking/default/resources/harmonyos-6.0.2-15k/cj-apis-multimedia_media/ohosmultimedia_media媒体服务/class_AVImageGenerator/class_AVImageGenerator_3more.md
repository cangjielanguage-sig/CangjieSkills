## class AVImageGenerator

```cangjie
public class AVImageGenerator {}
```

**功能：** 视频缩略图获取类，用于从视频资源中获取缩略图。在调用AVImageGenerator的方法前，需要先通过[createAVImageGenerator()](#func-createavimagegenerator)构建一个AVImageGenerator实例。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 19

### prop fdSrc

```cangjie
public mut prop fdSrc: AVFileDescriptor
```

**功能：** 媒体文件描述，通过该属性设置数据源。

> **说明：**
>
> 将资源句柄（fd）传递给AVImageGenerator 实例之后，请不要通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer / AVMetadataExtractor / AVImageGenerator / AVTranscoder。同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致视频缩略图数据获取异常。

**使用示例**：假设一个连续存储的媒体文件，地址偏移:0，字节长度:100。其文件描述为AVFileDescriptor(资源句柄, offset: 0, length: 100)，示例代码如下：

```cangjie
func testfs() {
    let timeUs = 0
    let queryOption = AVImageQueryOptions.AV_IMAGE_QUERY_NEXT_SYNC
    let param = PixelMapParams(300, 300)
    let generator = createAVImageGenerator()
    let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
    let rawFd = abilityContext.resourceManager.getRawFd("trailer.mp4")
    generator.fdSrc = AVFileDescriptor(rawFd.fd, Some(rawFd.offset), Some(rawFd.length))
    let pic = generator.fetchFrameByTime(timeUs, queryOption, param)
    generator.release()
}
```

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**类型：** [AVFileDescriptor](#class-avfiledescriptor)

**读写能力：** 可读写

**起始版本：** 19

### func fetchFrameByTime(Int64, AVImageQueryOptions, PixelMapParams)

```cangjie
public func fetchFrameByTime(timeUs: Int64, option: AVImageQueryOptions, param: PixelMapParams): PixelMap
```

**功能：** 获取视频缩略图。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|timeUs|Int64|是|-|需要获取的缩略图在视频中的时间点，单位为微秒（μs）。|
|option|[AVImageQueryOptions](#enum-avimagequeryoptions)|是|-|需要获取的缩略图时间点与视频帧的对应关系。|
|param|[PixelMapParams](#struct-pixelmapparams)|是|-|需要获取的缩略图的格式参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|视频缩略图。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400102|Operation not allowed.|
  |5400106|Unsupported format.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*

let timeUs = 0
let queryOption = AVImageQueryOptions.AV_IMAGE_QUERY_NEXT_SYNC
let param = PixelMapParams(300, 300)
let generator = createAVImageGenerator()
let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
let rawFd = abilityContext.resourceManager.getRawFd("trailer.mp4")
generator.fdSrc = AVFileDescriptor(rawFd.fd, Some(rawFd.offset), Some(rawFd.length))
let pic = generator.fetchFrameByTime(timeUs, queryOption, param)
generator.release()
```