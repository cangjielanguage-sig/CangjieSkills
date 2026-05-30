### func getBufferSize()

```cangjie
public func getBufferSize(): UInt32
```

**功能：** 获取音频渲染器的最小缓冲区大小，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回缓冲区大小。|

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
        let buff = audioCapturer.getBufferSize()
        Hilog.info(0, "buff", "buff: ${buff}")
    } catch (e: BusinessException) {
        Hilog.error(0, "getBufferSize", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioCapturer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func getCapturerInfo()

```cangjie
public func getCapturerInfo(): AudioCapturerInfo
```

**功能：** 获取采集器信息，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AudioCapturerInfo](#class-audiocapturerinfo)|返回采集器信息。|

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
        let info = audioCapturer.getCapturerInfo()
        Hilog.info(0, "info", "info.capturerFlags: ${info.capturerFlags}")
        Hilog.info(0, "info", "info.source: ${info.source}")
    } catch (e: BusinessException) {
        Hilog.error(0, "getCapturerInfo", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioCapturer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```