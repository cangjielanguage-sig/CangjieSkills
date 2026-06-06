### func on(AudioRoutingManagerCallbackType, AudioRendererInfo, Callback1Argument\<AudioDeviceDescriptors>)

```cangjie
public func on(`type`: AudioRoutingManagerCallbackType, rendererInfo: AudioRendererInfo,
    callback: Callback1Argument<AudioDeviceDescriptors>)
```

**功能：** 监听最高优先级输入或输出设备变化事件（当最高优先级输出设备发生变化时触发），使用callback方式返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioRoutingManagerCallbackType](#enum-audioroutingmanagercallbacktype)|是|-|监听事件，固定为：'PREFERR_OUTPUT_DEVICE_CHANGE_FOR_RENDERER_INFO'。|
|rendererInfo|[AudioRendererInfo](#class-audiorendererinfo)|是|-|表示渲染器信息。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[AudioDeviceDescriptors](#type-audiodevicedescriptors)>|是|-|回调函数，返回优先级最高的输出设备信息。|

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

// 此处代码可添加在依赖项定义中
class OutputDeviceChangeCallback <: Callback1Argument<AudioDeviceDescriptors> {
    public func invoke(arg: AudioDeviceDescriptors) {
        AppLog.info("callback: ${arg.size}")
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
        let instance = getAudioManager()
        let routingmgr = instance.getRoutingManager()
        var cb2 = OutputDeviceChangeCallback()
        let rendererInfo = AudioRendererInfo(StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, 0)
        routingmgr.on(AudioRoutingManagerCallbackType.PREFERR_OUTPUT_DEVICE_CHANGE_FOR_RENDERER_INFO, rendererInfo, cb2)
        routingmgr.off(AudioRoutingManagerCallbackType.PREFERR_OUTPUT_DEVICE_CHANGE_FOR_RENDERER_INFO)
    } catch (e: BusinessException) {
        Hilog.error(0, "RoutingManager:on/off", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioRenderer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```