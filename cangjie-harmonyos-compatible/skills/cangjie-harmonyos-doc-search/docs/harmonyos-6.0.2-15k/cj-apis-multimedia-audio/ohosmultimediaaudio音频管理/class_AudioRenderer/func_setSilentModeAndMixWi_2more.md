### func setSilentModeAndMixWithOthers(Bool)

```cangjie
public func setSilentModeAndMixWithOthers(on: Bool): Unit
```

**功能：** 设置静音并发播放模式。当设置为true，打开静音并发播放模式，系统将让此音频流静音播放，并且不会打断其它音频流。设置为false，将关闭静音并发播放，音频流可根据系统焦点策略抢占焦点。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|on|Bool|是|-|打开/关闭静音并发播放模式，true打开，false关闭。|

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
        audioRenderer.setSilentModeAndMixWithOthers(true)
        let on = audioRenderer.getSilentModeAndMixWithOthers()
        Hilog.info(0, "setSilentModeAndMixWithOthers", "on: ${on}")
    } catch (e: BusinessException) {
        Hilog.error(0, "setSilentModeAndMixWithOthers", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioRenderer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func setSpeed(Float64)

```cangjie
public func setSpeed(speed: Float64): Unit
```

**功能：** 设置播放倍速。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|speed|Float64|是|-|设置播放的倍速值（倍速范围：0.125-4.0）。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6800103|Unsupported state.|
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
        audioRenderer.setSpeed(1.5)
        let speed = audioRenderer.getSpeed()
        Hilog.info(0, "setSpeed", "speed: ${speed}")
    } catch (e: BusinessException) {
        Hilog.error(0, "setSpeed", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioRenderer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```