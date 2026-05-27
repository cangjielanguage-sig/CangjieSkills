### func on(AudioRendererCallbackType, Callback1Argument\<InterruptEvent>)

```cangjie
public func on(`type`: AudioRendererCallbackType, callback: Callback1Argument<InterruptEvent>): Unit
```

**功能：** 监听音频中断事件（当音频焦点发生变化时触发）。

[AudioRenderer](#class-audiorenderer)对象在start事件发生时会主动获取焦点，在pause、stop等事件发生时会主动释放焦点，不需要开发者主动发起获取焦点或释放焦点的申请。

调用此方法，在[AudioRenderer](#class-audiorenderer)对象获取焦点失败或发生中断事件（如被其他音频打断等）时，会收到[InterruptEvent](#class-interruptevent)。建议应用可根据[InterruptEvent](#class-interruptevent)的信息完成进一步处理，更多信息可参考文档处理音频焦点事件。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioRendererCallbackType](#enum-audiorenderercallbacktype)|是|-|监听事件，固定为：'AR_AUDIO_INTERRUPT'。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[InterruptEvent](#class-interruptevent)>|是|-|回调函数，返回录制中断时，应用接收的中断事件信息。|

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
class AR_AudioInterruptCallback <: Callback1Argument<InterruptEvent> {
    public func invoke(interruptEvent: InterruptEvent): Unit {
        AppLog.info("AR_AudioInterruptCallback on")
    }
}

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
        let rendererInfo = AudioRendererInfo(StreamUsage.STREAM_USAGE_MUSIC, 0)
        let rendererInfo2 = AudioRendererInfo(StreamUsage.STREAM_USAGE_MUSIC, 0)
        let streamInfo = AudioStreamInfo(AudioChannel.CHANNEL_2, AudioEncodingType.ENCODING_TYPE_RAW,
            AudioSampleFormat.SAMPLE_FORMAT_S16LE, AudioSamplingRate.SAMPLE_RATE_16000,
            channelLayout: AudioChannelLayout.CH_LAYOUT_UNKNOWN)
        let audiorenderOptions = AudioRendererOptions(rendererInfo, streamInfo)
        let audiorenderOptions1 = AudioRendererOptions(rendererInfo2, streamInfo)
        let audioRendererr = createAudioRenderer(audiorenderOptions)
        let res = AR_AudioInterruptCallback()
        audioRendererr.on(AudioRendererCallbackType.AR_AUDIO_INTERRUPT, res)
        audioRendererr.start()
        let audioRendererr1 = createAudioRenderer(audiorenderOptions1)
        audioRendererr1.start()
        sleep(Duration.second * 1)
    } catch (e: BusinessException) {
        Hilog.error(0, "AudioRendererCallbackType.AUDIO_INTERRUPT", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioRenderer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```