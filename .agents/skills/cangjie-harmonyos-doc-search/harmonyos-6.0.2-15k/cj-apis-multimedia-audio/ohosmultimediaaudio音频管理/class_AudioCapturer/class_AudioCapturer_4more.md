## class AudioCapturer

```cangjie
public class AudioCapturer {}
```

**功能：** 提供音频采集的相关接口。在调用[AudioCapturer](#class-audiocapturer)的接口前，需要先通过[createAudioCapturer](#func-createaudiocaptureraudiocaptureroptions)创建实例。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

### prop state

```cangjie
public prop state: AudioState
```

**功能：** 音频采集器状态。

**类型：** [AudioState](#enum-audiostate)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

### func getAudioStreamId()

```cangjie
public func getAudioStreamId(): UInt32
```

**功能：** 获取音频流id，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回音频流id。|

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
    let streamInfo = AudioStreamInfo(AudioChannel.CHANNEL_2, AudioEncodingType.ENCODING_TYPE_RAW,
    AudioSampleFormat.SAMPLE_FORMAT_S16LE, AudioSamplingRate.SAMPLE_RATE_44100)
    let capturerInfo = AudioCapturerInfo(SourceType.SOURCE_TYPE_VOICE_RECOGNITION, 0)
    let options = AudioCapturerOptions(capturerInfo, streamInfo)
    let audioCapturer = createAudioCapturer(options)
    try {
        let id = audioCapturer.getAudioStreamId()
        Hilog.info(0, "id", "id: ${id}")
    } catch (e: BusinessException) {
        Hilog.error(0, "getAudioStreamId", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioCapturer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func getAudioTime()

```cangjie
public func getAudioTime(): Int64
```

**功能：** 获取播放到当前位置时的时间戳（从1970年1月1日开始），单位为纳秒，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回时间戳。|

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
    let streamInfo = AudioStreamInfo(AudioChannel.CHANNEL_2, AudioEncodingType.ENCODING_TYPE_RAW,
    AudioSampleFormat.SAMPLE_FORMAT_S16LE, AudioSamplingRate.SAMPLE_RATE_44100)
    let capturerInfo = AudioCapturerInfo(SourceType.SOURCE_TYPE_VOICE_RECOGNITION, 0)
    let options = AudioCapturerOptions(capturerInfo, streamInfo)
    let audioCapturer = createAudioCapturer(options)
    try {
        let time = audioCapturer.getAudioTime()
        Hilog.info(0, "time", "time: ${time}")
    } catch (e: BusinessException) {
        Hilog.error(0, "getAudioTime", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioCapturer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```