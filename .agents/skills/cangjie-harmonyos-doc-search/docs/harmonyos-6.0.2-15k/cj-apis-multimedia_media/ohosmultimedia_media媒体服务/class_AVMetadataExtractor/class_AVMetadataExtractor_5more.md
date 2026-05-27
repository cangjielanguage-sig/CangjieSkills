## class AVMetadataExtractor

```cangjie
public class AVMetadataExtractor {}
```

**功能：** 元数据获取类，用于从媒体资源中获取元数据。在调用AVMetadataExtractor的方法前，需要先通过[createAVMetadataExtractor()](#func-createavmetadataextractor)构建一个AVMetadataExtractor实例。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 19

### prop dataSrc

```cangjie
public mut prop dataSrc: AVDataSrcDescriptor
```

**功能：** 流式媒体资源描述，通过该属性设置数据源。在获取元数据之前，必须设置数据源属性，只能设置fdSrc和dataSrc的其中一个。<br/>当应用从远端获取音视频媒体文件，在应用未下载完整音视频资源时，可以设置dataSrc提前获取该资源的元数据。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**类型：** [AVDataSrcDescriptor](#class-avdatasrcdescriptor)

**读写能力：** 可读写

**起始版本：** 19

### prop fdSrc

```cangjie
public mut prop fdSrc: AVFileDescriptor
```

**功能：** 媒体文件描述，通过该属性设置数据源。在获取元数据之前，必须设置数据源属性，只能设置fdSrc和dataSrc的其中一个。

**使用示例**：假设一个连续存储的媒体文件，地址偏移:0，字节长度:100。其文件描述为AVFileDescriptor(资源句柄, offset: 0, length: 100)。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**类型：** [AVFileDescriptor](#class-avfiledescriptor)

**读写能力：** 可读写

**起始版本：** 19

### func fetchAlbumCover()

```cangjie
public func fetchAlbumCover(): PixelMap
```

**功能：** 获取音频专辑封面。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|音频专辑封面。|

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
import ohos.base.*

try {
    let extractor = createAVMetadataExtractor()
    let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
    let rawFd = abilityContext.resourceManager.getRawFd("demo.mp4")
    extractor.fdSrc = AVFileDescriptor(rawFd.fd, rawFd.offset, rawFd.length)
    let pic = extractor.fetchAlbumCover()
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```

### func fetchMetadata()

```cangjie
public func fetchMetadata(): AVMetadata
```

**功能：** 获取媒体元数据。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AVMetadata](#class-avmetadata)|媒体元数据。|

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
import ohos.base.*

try {
    let extractor = createAVMetadataExtractor()
    let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
    let rawFd = abilityContext.resourceManager.getRawFd("demo.mp4")
    extractor.fdSrc = AVFileDescriptor(rawFd.fd, rawFd.offset, rawFd.length)
    let data = extractor.fetchMetadata()
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```