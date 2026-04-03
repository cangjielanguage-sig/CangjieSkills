### func getOverflowCount()

```cangjie
public func getOverflowCount(): UInt32
```

**功能：** 获取当前录制音频流的过载音频帧数量，同步返回数据。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回音频流的过载音频帧数量。|

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
        let count = audioCapturer.getOverflowCount()
        Hilog.info(0, "count", "count: ${count}")
    } catch (e: BusinessException) {
        Hilog.error(0, "getOverflowCount", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioCapturer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func getStreamInfo()

```cangjie
public func getStreamInfo(): AudioStreamInfo
```

**功能：** 获取音频流信息，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AudioStreamInfo](#class-audiostreaminfo)|返回音频流信息。|

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
        let streaminfo = audioCapturer.getStreamInfo()
        Hilog.info(0, "streaminfo", "streaminfo.channels: ${streaminfo.channels}")
        Hilog.info(0, "streaminfo", "streaminfo.channelLayout: ${streaminfo.channelLayout}")
        Hilog.info(0, "streaminfo", "streaminfo.encodingType: ${streaminfo.encodingType}")
        Hilog.info(0, "streaminfo", "streaminfo.samplingRate: ${streaminfo.samplingRate}")
        Hilog.info(0, "streaminfo", "streaminfo.sampleFormat: ${streaminfo.sampleFormat}")
    } catch (e: BusinessException) {
        Hilog.error(0, "getStreamInfo", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioCapturer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```