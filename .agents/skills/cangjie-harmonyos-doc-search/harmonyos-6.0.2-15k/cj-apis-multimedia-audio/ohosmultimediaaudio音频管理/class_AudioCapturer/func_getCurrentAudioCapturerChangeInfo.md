### func getCurrentAudioCapturerChangeInfo()

```cangjie
public func getCurrentAudioCapturerChangeInfo(): AudioCapturerChangeInfo
```

**功能：** 获取录音流配置，使用同步方式返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AudioCapturerChangeInfo](#class-audiocapturerchangeinfo)|同步接口，返回描述音频采集器更改信息。|

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
        let changinfo = audioCapturer.getCurrentAudioCapturerChangeInfo()
        Hilog.info(0, "changinfo", "changinfo.streamId: ${changinfo.streamId}")
        Hilog.info(0, "changinfo", "changinfo.muted: ${changinfo.muted}")
        Hilog.info(0, "changinfo", "changinfo.capturerInfo.source: ${changinfo.capturerInfo.source}")
        Hilog.info(0, "changinfo", "changinfo.capturerInfo.capturerFlags: ${changinfo.capturerInfo.capturerFlags}")
        Hilog.info(0, "changinfo", "changinfo.deviceDescriptors.size: ${changinfo.deviceDescriptors.size}")
        Hilog.info(0, "changinfo", "changinfo.deviceDescriptors[0].displayName: ${changinfo.deviceDescriptors[0].displayName}")
        Hilog.info(0, "changinfo", "changinfo.deviceDescriptors[0].address: ${changinfo.deviceDescriptors[0].address}")
        Hilog.info(0, "changinfo", "changinfo.deviceDescriptors[0].channelCounts[0]: ${changinfo.deviceDescriptors[0].channelCounts[0]}")
        Hilog.info(0, "changinfo", "changinfo.deviceDescriptors[0].channelMasks[0]: ${changinfo.deviceDescriptors[0].channelMasks[0]}")
        Hilog.info(0, "changinfo", "changinfo.deviceDescriptors[0].deviceRole: ${changinfo.deviceDescriptors[0].deviceRole}")
        Hilog.info(0, "changinfo", "changinfo.deviceDescriptors[0].deviceType: ${changinfo.deviceDescriptors[0].deviceType}")
        Hilog.info(0, "changinfo", "changinfo.deviceDescriptors[0].id: ${changinfo.deviceDescriptors[0].id}")
        Hilog.info(0, "changinfo", "changinfo.deviceDescriptors[0].name: ${changinfo.deviceDescriptors[0].name}")
        Hilog.info(0, "changinfo", "changinfo.deviceDescriptors[0].sampleRates[0]: ${changinfo.deviceDescriptors[0].sampleRates[0]}")
        Hilog.info(0, "changinfo", "changinfo.deviceDescriptors[0].encodingTypes.isSome(): ${changinfo.deviceDescriptors[0].encodingTypes.isSome()}")
        Hilog.info(0, "changinfo", "changinfo.deviceDescriptors[0].encodingTypes: ${Some(changinfo.deviceDescriptors[0].encodingTypes)}")
    } catch (e: BusinessException) {
        Hilog.error(0, "getCurrentAudioCapturerChangeInfo", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioCapturer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```