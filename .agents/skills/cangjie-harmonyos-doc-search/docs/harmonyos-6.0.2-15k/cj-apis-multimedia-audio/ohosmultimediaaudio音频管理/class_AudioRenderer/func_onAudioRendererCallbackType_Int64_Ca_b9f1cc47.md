### func on(AudioRendererCallbackType, Int64, Callback1Argument\<Int64>)

```cangjie
public func on(`type`: AudioRendererCallbackType, frame: Int64, callback: Callback1Argument<Int64>): Unit
```

**功能：** 'AR_MARK_PEACH': 监听标记到达事件（当采集的帧数达到frame参数的值时触发，仅调用一次）。

举例说明，如果frame设置为100，当采集帧数到达第100帧时，将上报信息。

'AR_PERIOD_REACH': 监听到达标记事件（当采集的帧数达到frame参数的值时触发，即按周期上报信息）。

举例说明，如果frame设置为10，每当采集10帧数据时将上报信息，例如在第10帧、20帧、30帧，均会上报信息。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioRendererCallbackType](#enum-audiorenderercallbacktype)|是|-|监听事件，固定为：'AR_MARK_PEACH'或'AR_PERIOD_REACH'。|
|frame|Int64|是|-|触发事件的帧数。该值必须大于0。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Int64>|是|-|回调函数，返回frame参数的值。|

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
class MarkPeachCallback <: Callback1Argument<Int64> {
    public func invoke(arg: Int64) {
        Hilog.info(0, "callback", "callback: ${arg}")
    }
}

class PeriodPeachCallback <: Callback1Argument<Int64> {
    public func invoke(arg: Int64) {
        Hilog.info(0, "callback", "callback: ${arg}")
    }
}

try {
    let rendererInfo = AudioRendererInfo(
        StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION,
        0)
    let streamInfo = AudioStreamInfo(
        AudioChannel.CHANNEL_1,
        AudioEncodingType.ENCODING_TYPE_RAW,
        AudioSampleFormat.SAMPLE_FORMAT_S16LE,
        AudioSamplingRate.SAMPLE_RATE_44100)
    let options = AudioRendererOptions(rendererInfo, streamInfo)
    let audioRenderer = createAudioRenderer(options)
    try {
        let mark_peach_cb = MarkPeachCallback()
        let frame: Int64 = 1000
        audioRenderer.on(AudioRendererCallbackType.AR_MARK_PEACH, frame, mark_peach_cb)
        Hilog.info(0, "on", "AudioRendererCallbackType.AR_MARK_PEACH on")
        let period_peach_cb = PeriodPeachCallback()
        audioRenderer.on(AudioRendererCallbackType.AR_PERIOD_REACH, frame, period_peach_cb)
        Hilog.info(0, "on", "AudioRendererCallbackType.AR_PERIOD_REACH on")
        audioRenderer.off(AudioRendererCallbackType.AR_MARK_PEACH, callback: mark_peach_cb)
        Hilog.info(0, "off", "AudioRendererCallbackType.AR_MARK_PEACH off")
    } catch (e: BusinessException) {
        Hilog.error(0, "AudioRendererCallbackType.AR_MARK_PEACH", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioRenderer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```