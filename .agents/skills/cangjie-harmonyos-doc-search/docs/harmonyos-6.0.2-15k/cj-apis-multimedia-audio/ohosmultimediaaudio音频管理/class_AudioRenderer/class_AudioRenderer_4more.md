## class AudioRenderer

```cangjie
public class AudioRenderer {}
```

**功能：** 提供音频渲染的相关接口。在调用[AudioRenderer](#class-audiorenderer)的接口前，需要先通过[createAudioRenderer](#func-createaudiorendereraudiorendereroptions)创建实例。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

### prop state

```cangjie
public prop state: AudioState
```

**功能：** 音频渲染器的状态。

**类型：** [AudioState](#enum-audiostate)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

### func drain()

```cangjie
public func drain()
```

**功能：** 检查缓冲区是否已被耗尽。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6800301|System error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*
import kit.BasicServicesKit.*
import ohos.hilog.*

try {
    let rendererInfo = AudioRendererInfo(
    StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, 0)
    let streamInfo = AudioStreamInfo(
        AudioChannel.CHANNEL_1,
        AudioEncodingType.ENCODING_TYPE_RAW,
        AudioSampleFormat.SAMPLE_FORMAT_S16LE,
        AudioSamplingRate.SAMPLE_RATE_44100)
    let options = AudioRendererOptions(rendererInfo, streamInfo)
    let audioRenderer = createAudioRenderer(options)
    try {
        audioRenderer.start()
        audioRenderer.drain()
    } catch (e: BusinessException) {
        Hilog.error(0, "drain", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioRenderer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func flush()

```cangjie
public func flush()
```

**功能：** 清空缓冲区（[AudioState](#enum-audiostate)为STATE_RUNNING、STATE_PAUSED、STATE_STOPPED状态下可用）。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6800103|Unsupported state.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*
import kit.BasicServicesKit.*
import ohos.hilog.*

try {
    let rendererInfo = AudioRendererInfo(
    StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, 0)
    let streamInfo = AudioStreamInfo(
        AudioChannel.CHANNEL_1,
        AudioEncodingType.ENCODING_TYPE_RAW,
        AudioSampleFormat.SAMPLE_FORMAT_S16LE,
        AudioSamplingRate.SAMPLE_RATE_44100)
    let options = AudioRendererOptions(rendererInfo, streamInfo)
    let audioRenderer = createAudioRenderer(options)
    try {
        audioRenderer.stop()
        audioRenderer.flush()
    } catch (e: BusinessException) {
        Hilog.error(0, "flush", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioRenderer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```