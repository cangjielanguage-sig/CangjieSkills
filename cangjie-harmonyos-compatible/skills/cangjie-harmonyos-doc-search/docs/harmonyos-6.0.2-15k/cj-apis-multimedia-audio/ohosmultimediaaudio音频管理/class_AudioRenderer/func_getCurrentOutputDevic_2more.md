### func getCurrentOutputDevices()

```cangjie
public func getCurrentOutputDevices(): AudioDeviceDescriptors
```

**功能：** 获取音频流输出设备描述符。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AudioDeviceDescriptors](#type-audiodevicedescriptors)|返回音频流的输出设备描述信息。|

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
        let devices = audioRenderer.getCurrentOutputDevices()
        Hilog.info(0, "devices", "${devices.size}")
        Hilog.info(0, "devices", "${devices[0].id}" )
        Hilog.info(0, "devices", "${devices[0].displayName}")
        Hilog.info(0, "devices", "${devices[0].deviceType}")
        Hilog.info(0, "devices", "${devices[0].deviceRole}")
        Hilog.info(0, "devices", "${devices[0].channelCounts[0]}")
        Hilog.info(0, "devices", "${devices[0].sampleRates[0]}")
    } catch (e: BusinessException) {
        Hilog.error(0, "getCurrentOutputDevices", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioRenderer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func getMaxStreamVolume()

```cangjie
public func getMaxStreamVolume(): Float64
```

**功能：** 获取音频流最大音量（音量范围0-1）。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Float64|返回音频流最大音量（音量范围0-1）。|

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
        let audioRenderer = createAudioRenderer(options)
        let maxStreamVol: Float64 = audioRenderer.getMaxStreamVolume()
        Hilog.info(0, "maxStreamVol", "maxStreamVol: ${maxStreamVol}")
    } catch (e: BusinessException) {
        Hilog.error(0, "getMaxStreamVolume", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioRenderer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```