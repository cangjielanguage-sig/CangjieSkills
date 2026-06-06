### func on(AudioCapturerCallbackType, Callback1Argument\<AudioDeviceDescriptors>)

```cangjie
public func on(`type`: AudioCapturerCallbackType, callback: Callback1Argument<AudioDeviceDescriptors>): Unit
```

**功能：** 监听音频输入设备变化事件（当音频输入设备发生变化时触发），使用callback方式返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioCapturerCallbackType](#enum-audiocapturercallbacktype)|是|-|监听事件，固定为：'INPUT_DEVICE_CHANGE'。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[AudioDeviceDescriptors](#type-audiodevicedescriptors)>|是|-|回调函数，返回监听的音频输入设备变化(返回数据为切换后的设备信息)。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |6800101|Invalid parameter.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*
import kit.BasicServicesKit.*
import ohos.hilog.*

// 此处代码可添加在依赖项定义中
class InputDeviceChangeCallback <: Callback1Argument<AudioDeviceDescriptors> {
    public func invoke(arg: AudioDeviceDescriptors) {
        Hilog.info(0, "callback", "callback: ${arg.size}")
    }
}

try {
    let streamInfo = AudioStreamInfo(AudioChannel.CHANNEL_2, AudioEncodingType.ENCODING_TYPE_RAW,
    AudioSampleFormat.SAMPLE_FORMAT_S16LE, AudioSamplingRate.SAMPLE_RATE_44100)
    let capturerInfo = AudioCapturerInfo(SourceType.SOURCE_TYPE_VOICE_RECOGNITION, 0)
    let options = AudioCapturerOptions(capturerInfo, streamInfo)
    let audioCapturer = createAudioCapturer(options)
    try {
        let devices_cb = InputDeviceChangeCallback()
        audioCapturer.on(AudioCapturerCallbackType.INPUT_DEVICE_CHANGE, devices_cb)
        Hilog.info(0, "on", "AudioCapturerCallbackType.INPUT_DEVICE_CHANGE on")
        audioCapturer.off(AudioCapturerCallbackType.INPUT_DEVICE_CHANGE, callback: devices_cb)
        Hilog.info(0, "off", "AudioCapturerCallbackType.INPUT_DEVICE_CHANGE off")
    } catch (e: BusinessException) {
        Hilog.error(0, "AudioCapturerCallbackType.INPUT_DEVICE_CHANGE", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioCapturer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```