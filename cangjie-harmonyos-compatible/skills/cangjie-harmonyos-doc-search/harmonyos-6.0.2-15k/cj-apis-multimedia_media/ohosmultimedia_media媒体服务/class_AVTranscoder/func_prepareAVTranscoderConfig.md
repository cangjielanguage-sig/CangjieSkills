### func prepare(AVTranscoderConfig)

```cangjie
public func prepare(config: AVTranscoderConfig): Unit
```

**功能：** 设置视频转码参数。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|config|[AVTranscoderConfig](#class-avtranscoderconfig)|是|-|配置视频转码的相关参数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400101|No memory.|
  |5400102|Operation not allowed.|
  |5400105|Service died.|
  |5400106|Unsupported format.|

- IllegalArgumentException：

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |The parameter check failed.|参数校验错误。|请检查传入的参数是否正确。|

**示例：**

- 本示例代码需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。
- 本示例代码需在仓颉模板工程中rawfile目录下添加input.mp4作为转码源文件。

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import kit.CoreFileKit.*
import ohos.base.BusinessException

try {
    let avConfig = AVTranscoderConfig(
        audioBitrate: 100000, // 音频比特率
        audioCodec: CodecMimeType.AUDIO_AAC, // 音频编码格式
        fileFormat: ContainerFormatType.CFT_MPEG_4, // 封装格式
        videoBitrate: 200000, // 视频比特率
        videoCodec: CodecMimeType.VIDEO_AVC, // 视频编码格式
        videoFrameWidth: 640, // 视频分辨率的宽
        videoFrameHeight: 480 // 视频分辨率的高
    )
    let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
    let fileDesc = abilityContext.resourceManager.getRawFd("input.mp4") // rawfile目录下添加mp4文件
    let dstFile = FileFs.open("/data/storage/el2/base/haps/entry/files/output.mp4", mode: (READ_WRITE.mode | CREATE.mode))
    let avTranscoder = createAVTranscoder()
    avTranscoder.fdSrc = AVFileDescriptor(fileDesc.fd, fileDesc.offset, fileDesc.length)
    avTranscoder.fdDst = dstFile.fd
    avTranscoder.prepare(avConfig)
} catch (e: BusinessException) {
    AppLog.error("ErrorCode: ${e.code}, ErrorMessage: ${e.message}")
}
```