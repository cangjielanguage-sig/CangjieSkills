### func on(AudioCapturerCallbackType, Int64, Callback1Argument\<Int64>)

```cangjie
public func on(`type`: AudioCapturerCallbackType, frame: Int64, callback: Callback1Argument<Int64>): Unit
```

**功能：** 监听标记到达事件，使用callback方式返回结果。

- 'MARK_REACH': 当采集的帧数达到frame参数的值时触发，仅调用一次。

    举例说明，如果frame设置为100，当采集帧数到达第100帧时，将上报信息。

- 'PERIOD_REACH': 当采集的帧数达到frame参数的值时触发，即按周期上报信息。

    举例说明，如果frame设置为10，每当采集10帧数据时将上报信息，例如在第10帧、20帧、30帧，均会上报信息。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioCapturerCallbackType](#enum-audiocapturercallbacktype)|是|-|监听事件，固定为：'MARK_REACH'或'PERIOD_REACH'。|
|frame|Int64|是|-|触发事件的帧数。该值必须大于0。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Int64>|是|-|回调函数，返回frame参数的值。|

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
    let streamInfo = AudioStreamInfo(AudioChannel.CHANNEL_2, AudioEncodingType.ENCODING_TYPE_RAW,
    AudioSampleFormat.SAMPLE_FORMAT_S16LE, AudioSamplingRate.SAMPLE_RATE_44100)
    let capturerInfo = AudioCapturerInfo(SourceType.SOURCE_TYPE_VOICE_RECOGNITION, 0)
    let options = AudioCapturerOptions(capturerInfo, streamInfo)
    let audioCapturer = createAudioCapturer(options)
    try {
        let mark_peach_cb = MarkPeachCallback()
        let frame: Int64 = 1000
        audioCapturer.on(AudioCapturerCallbackType.MARK_REACH, frame, mark_peach_cb)
        Hilog.info(0, "on", "AudioCapturerCallbackType.MARK_REACH on")
        let period_peach_cb = PeriodPeachCallback()
        audioCapturer.on(AudioCapturerCallbackType.PERIOD_REACH, frame, period_peach_cb)
        Hilog.info(0, "on", "AudioCapturerCallbackType.PERIOD_REACH on")
        audioCapturer.off(AudioCapturerCallbackType.MARK_REACH, callback: mark_peach_cb)
        Hilog.info(0, "off", "AudioCapturerCallbackType.MARK_REACH off")
    } catch (e: BusinessException) {
        Hilog.error(0, "AudioCapturerCallbackType.MARK_REACH", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioCapturer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```