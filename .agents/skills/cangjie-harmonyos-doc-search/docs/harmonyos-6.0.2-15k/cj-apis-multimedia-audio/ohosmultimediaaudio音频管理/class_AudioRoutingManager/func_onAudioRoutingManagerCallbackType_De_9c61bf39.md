### func on(AudioRoutingManagerCallbackType, DeviceFlag, Callback1Argument\<DeviceChangeAction>)

```cangjie
public func on(`type`: AudioRoutingManagerCallbackType, deviceFlag: DeviceFlag,
    callback: Callback1Argument<DeviceChangeAction>): Unit
```

**功能：** 监听音频设备连接变化事件（当音频设备连接状态发生变化时触发），使用callback方式返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioRoutingManagerCallbackType](#enum-audioroutingmanagercallbacktype)|是|-|监听事件，固定为：'DEVICE_CHANGE'。|
|deviceFlag|[DeviceFlag](#enum-deviceflag)|是|-|设备类型的flag。|
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
class DeviceChangeActionCallback <: Callback1Argument<DeviceChangeAction> {
    public func invoke(arg: DeviceChangeAction) {
        AppLog.info("callback: ${arg.`type`}")
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
        var cb2 = DeviceChangeActionCallback()
        routingmgr.on(AudioRoutingManagerCallbackType.DEVICE_CHANGE, DeviceFlag.OUTPUT_DEVICES_FLAG, cb2)
        routingmgr.off(AudioRoutingManagerCallbackType.DEVICE_CHANGE)
    } catch (e: BusinessException) {
        Hilog.error(0, "RoutingManager:on/off", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioRenderer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```