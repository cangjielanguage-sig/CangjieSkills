### func off(AudioCapturerCallbackType, ?CallbackObject)

```cangjie
public func off(`type`: AudioCapturerCallbackType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消监听事件。

**系统能力：** 与\`type\`取值有关，详见[AudioCapturerCallbackType](#enum-audiocapturercallbacktype)

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioCapturerCallbackType](#enum-audiocapturercallbacktype)|是|-|监听事件类型。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None| **命名参数。** 需要注销的回调函数，默认为空，表示取消该类型事件所有的回调。|

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
        Hilog.info(0, "callback", "callback: ${arg.eventType}")
        Hilog.info(0, "callback", "callback: ${arg.forceType}")
        Hilog.info(0, "callback", "callback: ${arg.hintType}")
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
        Hilog.error(0, "getStreamInfo", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioCapturer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```