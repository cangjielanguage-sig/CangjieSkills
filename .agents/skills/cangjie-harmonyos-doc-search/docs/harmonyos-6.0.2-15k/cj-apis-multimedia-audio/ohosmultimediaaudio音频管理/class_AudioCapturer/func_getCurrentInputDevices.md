### func getCurrentInputDevices()

```cangjie
public func getCurrentInputDevices(): AudioDeviceDescriptors
```

**功能：** 获取录音流输入设备描述符，使用同步方式返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AudioDeviceDescriptors](#type-audiodevicedescriptors)|同步接口，返回设备属性数组类型数据。|

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
        let devices = audioCapturer.getCurrentInputDevices()
        Hilog.info(0, "changinfo", "devices.size: ${devices.size}")
        Hilog.info(0, "changinfo", "devices[0].displayName: ${devices[0].displayName}")
        Hilog.info(0, "changinfo", "devices[0].address: ${devices[0].address}")
        Hilog.info(0, "changinfo", "devices[0].channelCounts[0]: ${devices[0].channelCounts[0]}")
        Hilog.info(0, "changinfo", "devices[0].channelMasks[0]: ${devices[0].channelMasks[0]}")
        Hilog.info(0, "changinfo", "devices[0].deviceRole: ${devices[0].deviceRole}")
        Hilog.info(0, "changinfo", "devices[0].deviceType: ${devices[0].deviceType}")
        Hilog.info(0, "changinfo", "devices[0].id: ${devices[0].id}")
        Hilog.info(0, "changinfo", "devices[0].name: ${devices[0].name}")
        Hilog.info(0, "changinfo", "devices[0].sampleRates[0]: ${devices[0].sampleRates[0]}")
        Hilog.info(0, "changinfo", "devices[0].encodingTypes.isSome(): ${devices[0].encodingTypes.isSome()}")
        Hilog.info(0, "changinfo", "devices[0].encodingTypes: ${Some(devices[0].encodingTypes)}")
    } catch (e: BusinessException) {
        Hilog.error(0, "getCurrentInputDevices", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioCapturer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```