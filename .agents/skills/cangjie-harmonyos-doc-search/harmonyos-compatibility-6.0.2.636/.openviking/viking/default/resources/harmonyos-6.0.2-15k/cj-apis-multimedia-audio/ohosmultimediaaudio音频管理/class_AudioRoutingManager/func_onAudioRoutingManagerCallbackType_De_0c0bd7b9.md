### func on(AudioRoutingManagerCallbackType, DeviceUsage, Callback1Argument\<DeviceChangeAction>)

```cangjie
public func on(`type`: AudioRoutingManagerCallbackType, deviceUsage: DeviceUsage, callback: Callback1Argument<DeviceChangeAction>): Unit
```

**功能：** 监听音频可选设备连接变化事件（当音频可选设备连接状态发生变化时触发），使用callback方式返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioRoutingManagerCallbackType](#enum-audioroutingmanagercallbacktype)|是|-|监听事件，固定为：'AVAILABLE_DEVICE_CHANGE'。|
|deviceUsage|[DeviceUsage](#enum-deviceusage)|是|-|设备的usage。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[DeviceChangeAction](#class-devicechangeaction)>|是|-|回调函数，返回设备更新详情。|

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
class deviceChangeCallback <: Callback1Argument<DeviceChangeAction> {
    public func invoke(arg: DeviceChangeAction) {
        AppLog.info("deviceChangeCallback called")
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
        let capturerchange = deviceChangeCallback()
        let instance = getAudioManager()
        let arm = instance.getRoutingManager()
        arm.on(AudioRoutingManagerCallbackType.AVAILABLE_DEVICE_CHANGE, DeviceUsage.MEDIA_OUTPUT_DEVICES, capturerchange)
        Hilog.error(0, "test_ARM_DEVICE_CHANGE", "test_ARM_DEVICE_CHANGE")
    } catch (e: BusinessException) {
        Hilog.error(0, "RoutingManager:on/off", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioRenderer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```