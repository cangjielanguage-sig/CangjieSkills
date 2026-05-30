### func cancel()

```cangjie
public func cancel(): Unit
```

**功能：** 取消视频转码。需要在[prepare()](#func-prepare)、[start()](#func-start)或[pause()](#func-pause)事件成功触发后，才能调用cancel()方法。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400101|No memory.|
  |5400102|Operation not allowed.|
  |5400103|IO error.|
  |5400105|Service died.|

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
    avTranscoder.start()
    avTranscoder.cancel()
} catch (e: BusinessException) {
    AppLog.error("ErrorCode: ${e.code}, ErrorMessage: ${e.message}")
}
```