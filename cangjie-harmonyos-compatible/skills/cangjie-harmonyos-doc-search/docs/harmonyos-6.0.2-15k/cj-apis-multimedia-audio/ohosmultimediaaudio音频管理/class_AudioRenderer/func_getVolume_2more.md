### func getVolume()

```cangjie
public func getVolume(): Float64
```

**功能：** 获取音频渲染器的当前音量值。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Float64|返回音量大小，音量范围[0.0-1.0]。|

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
        audioRenderer.setVolume(0.5)
        let vol = audioRenderer.getVolume()
        Hilog.info(0, "setVolume", "volume: ${vol}")
    } catch (e: BusinessException) {
        Hilog.error(0, "setVolume", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioRenderer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func off(AudioRendererCallbackType, ?CallbackObject)

```cangjie
public func off(`type`: AudioRendererCallbackType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消监听事件。

**系统能力：** 与\`type\`取值有关，详见[AudioRendererCallbackType](#enum-audiorenderercallbacktype)

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioRendererCallbackType](#enum-audiorenderercallbacktype)|是|-|监听事件类型。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None| **命名参数。** 需要注销的回调函数，默认为空，表示取消该类型事件所有的回调。|

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
        AppLog.info("AR_State_Change_Callback: ${arg}")
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