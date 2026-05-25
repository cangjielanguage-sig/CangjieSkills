### func on(AudioCapturerCallbackType, Callback1Argument\<InterruptEvent>)

```cangjie
public func on(`type`: AudioCapturerCallbackType, callback: Callback1Argument<InterruptEvent>): Unit
```

**功能：** 监听音频中断事件（当音频焦点发生变化时触发），使用callback方式返回结果。

[AudioCapturer](#class-audiocapturer)对象在start事件发生时会主动获取焦点，在pause、stop等事件发生时会主动释放焦点，不需要开发者主动发起获取焦点或释放焦点的申请。

调用此方法，在[AudioCapturer](#class-audiocapturer)对象获取焦点失败或发生中断事件（如被其他音频打断等）时，会收到[InterruptEvent](#class-interruptevent)。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioCapturerCallbackType](#enum-audiocapturercallbacktype)|是|-|监听事件，固定为：'AUDIO_INTERRUPT'。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[InterruptEvent](#class-interruptevent)>|是|-|回调函数，返回录制中断时，应用接收的中断事件信息。|

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
class InterruptEventCallback <: Callback1Argument<InterruptEvent> {
    public func invoke(arg: InterruptEvent) {
        Hilog.info(0, "", "callback: ${arg.eventType}")
        Hilog.info(0, "", "callback: ${arg.forceType}")
        Hilog.info(0, "", "callback: ${arg.hintType}")
    }
}

try {
    let streamInfo = AudioStreamInfo(AudioChannel.CHANNEL_2, AudioEncodingType.ENCODING_TYPE_RAW,
        AudioSampleFormat.SAMPLE_FORMAT_S16LE, AudioSamplingRate.SAMPLE_RATE_44100)
    let capturerInfo = AudioCapturerInfo(SourceType.SOURCE_TYPE_VOICE_RECOGNITION, 0)
    let options = AudioCapturerOptions(capturerInfo, streamInfo)
    let audioCapturer = createAudioCapturer(options)
    try {
        let cb = InterruptEventCallback()
        audioCapturer.on(AudioCapturerCallbackType.AUDIO_INTERRUPT, cb)
        Hilog.info(0, "on", "AudioCapturerCallbackType.AUDIO_INTERRUPT on")
        audioCapturer.off(AudioCapturerCallbackType.AUDIO_INTERRUPT, callback: cb)
        Hilog.info(0, "off", "AudioCapturerCallbackType.AUDIO_INTERRUPT off")
    } catch (e: BusinessException) {
        Hilog.error(0, "AudioCapturerCallbackType.AUDIO_INTERRUPT", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioCapturer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```