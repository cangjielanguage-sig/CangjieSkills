### func on(AudioCapturerCallbackType, Callback1Argument\<AudioCapturerChangeInfo>)

```cangjie
public func on(`type`: AudioCapturerCallbackType, callback: Callback1Argument<AudioCapturerChangeInfo>): Unit
```

**功能：** 监听录音流配置变化事件（当音频录制流状态变化、设备变化时触发），使用callback方式返回结果。订阅内部是异步实现，是非精确回调，在录音流配置变化的同时注册回调，收到的返回结果存在变化可能性。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioCapturerCallbackType](#enum-audiocapturercallbacktype)|是|-|监听事件，固定为：'AUDIO_CAPTURER_CHANGE'。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[AudioCapturerChangeInfo](#class-audiocapturerchangeinfo)>|是|-|回调函数，录音流配置或状态变化时返回监听的录音流当前配置和状态信息。|

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
class AudioCapturerChangeInfoCallback <: Callback1Argument<AudioCapturerChangeInfo> {
    public func invoke(arg: AudioCapturerChangeInfo) {
        Hilog.info(0, "callback", "callback: ${arg.streamId}")
        Hilog.info(0, "callback", "callback: ${arg.muted}")
        Hilog.info(0, "callback", "callback: ${arg.capturerInfo.source}")
        Hilog.info(0, "callback", "callback: ${arg.capturerInfo.capturerFlags}")
        Hilog.info(0, "callback", "callback: ${arg.deviceDescriptors.size}")
    }
}

try {
    let streamInfo = AudioStreamInfo(AudioChannel.CHANNEL_2, AudioEncodingType.ENCODING_TYPE_RAW,
        AudioSampleFormat.SAMPLE_FORMAT_S16LE, AudioSamplingRate.SAMPLE_RATE_44100)
    let capturerInfo = AudioCapturerInfo(SourceType.SOURCE_TYPE_VOICE_RECOGNITION, 0)
    let options = AudioCapturerOptions(capturerInfo, streamInfo)
    let audioCapturer = createAudioCapturer(options)
    try {
        let change_info_cb = AudioCapturerChangeInfoCallback()
        audioCapturer.on(AudioCapturerCallbackType.AUDIO_CAPTURER_CHANGE, change_info_cb)
        Hilog.info(0, "on", "AudioCapturerCallbackType.AUDIO_CAPTURER_CHANGE on")
        audioCapturer.off(AudioCapturerCallbackType.AUDIO_CAPTURER_CHANGE, callback: change_info_cb)
        Hilog.info(0, "off", "AudioCapturerCallbackType.AUDIO_CAPTURER_CHANGE off")
    } catch (e: BusinessException) {
        Hilog.error(0, "AudioCapturerCallbackType.AUDIO_CAPTURER_CHANGE", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioCapturer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```