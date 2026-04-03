### func on(AudioRendererCallbackType, Callback1Argument\<AudioState>)

```cangjie
public func on(`type`: AudioRendererCallbackType, callback: Callback1Argument<AudioState>): Unit
```

**功能：** 监听状态变化事件（当[AudioRenderer](#class-audiorenderer)状态发生变化时触发）。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioRendererCallbackType](#enum-audiorenderercallbacktype)|是|-|监听事件，固定为：'AR_STATE_CHANGE'。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[AudioState](#enum-audiostate)>|是|-|回调函数，返回当前音频流的输出设备描述信息。|

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
class AR_State_Change_Callback <: Callback1Argument<AudioState> {
    public func invoke(arg: AudioState) {
        AppLog.info("AR_State_Change_Callback:${arg}")
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
        let cb = AR_State_Change_Callback()
        audioRenderer.on(AudioRendererCallbackType.AR_STATE_CHANGE, cb)
        sleep(Duration.second * 3)
        audioRenderer.start()
        sleep(Duration.second * 3)
        audioRenderer.stop()
        sleep(Duration.second * 3)
        audioRenderer.off(AudioRendererCallbackType.AR_STATE_CHANGE)
    } catch (e: BusinessException) {
        Hilog.error(0, "off", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioRenderer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```