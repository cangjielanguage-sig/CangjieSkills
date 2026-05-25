### func on(AudioRendererCallbackType, Callback1Argument\<AudioDeviceDescriptors>)

```cangjie
public func on(`type`: AudioRendererCallbackType, callback: Callback1Argument<AudioDeviceDescriptors>): Unit
```

**功能：** 监听音频数据写入回调事件（当需要写入音频数据时触发）。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioRendererCallbackType](#enum-audiorenderercallbacktype)|是|-|监听事件，固定为：'AR_OUTPUT_DEVICE_CHANGE'。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[AudioDeviceDescriptors](#type-audiodevicedescriptors)>|是|-|回调函数，返回当前音频流的输出设备描述信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6800101|Invalid parameter.|
  |6800301|System error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*
import kit.BasicServicesKit.*
import ohos.hilog.*

// 此处代码可添加在依赖项定义中
class OutputDeviceInfoCallback <: Callback1Argument<AudioDeviceDescriptors> {
    public func invoke(arg: AudioDeviceDescriptors) {
        AppLog.info("OutputDeviceInfoCallback: ${arg[0].displayName}")
    }
}

try {
    let streamInfo = AudioStreamInfo(AudioChannel.CHANNEL_2, AudioEncodingType.ENCODING_TYPE_RAW,
    AudioSampleFormat.SAMPLE_FORMAT_S16LE, AudioSamplingRate.SAMPLE_RATE_44100)
    let capturerInfo = AudioCapturerInfo(SourceType.SOURCE_TYPE_VOICE_RECOGNITION, 0)
    let options = AudioCapturerOptions(capturerInfo, streamInfo)
    let audioCapturer = createAudioCapturer(options)
    try {
        let rendererInfo = AudioRendererInfo(
            StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, 0)
        let streamInfo = AudioStreamInfo(
            AudioChannel.CHANNEL_1,
            AudioEncodingType.ENCODING_TYPE_RAW,
            AudioSampleFormat.SAMPLE_FORMAT_S16LE,
            AudioSamplingRate.SAMPLE_RATE_48000)
        let options = AudioRendererOptions(rendererInfo, streamInfo)
        let render = createAudioRenderer(options)
        let cb = OutputDeviceInfoCallback()
        render.on(AudioRendererCallbackType.AR_OUTPUT_DEVICE_CHANGE, cb)
        Hilog.error(0, "test_AR_OutputDeviceInfoCallback", "test_AR_OutputDeviceInfoCallback")
    } catch (e: BusinessException) {
        Hilog.error(0, "AudioRendererCallbackType.AR_OUTPUT_DEVICE_CHANGE", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioCapturer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```