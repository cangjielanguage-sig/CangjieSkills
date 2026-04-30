### func on(AudioVolumeGroupManagerCallbackType, Callback1Argument\<AudioRingMode>)

```cangjie
public func on(`type`: AudioVolumeGroupManagerCallbackType, callback: Callback1Argument<AudioRingMode>): Unit
```

**功能：** 监听铃声模式变化事件（当铃声模式发生变化时触发），使用callback方式返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioVolumeGroupManagerCallbackType](#enum-audiovolumegroupmanagercallbacktype)|是|-|监听事件，固定为：'RING_MODE_CHANGE'。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[AudioRingMode](#enum-audioringmode)>|是|-|回调函数，返回变化后的铃声模式。|

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
class RingModeCallback <: Callback1Argument<AudioRingMode> {
    public func invoke(arg: AudioRingMode) {
        AppLog.info("RingModeCallback ${arg}")
    }
}

try {
    let LOCAL_VOLUME_GROUP_ID: Int32 = 1
    let audioMgr: AudioManager = getAudioManager()
    let audioVolMgr: AudioVolumeManager = audioMgr.getVolumeManager()
    let audioVolGrpMgr: AudioVolumeGroupManager = audioVolMgr.getVolumeGroupManager(LOCAL_VOLUME_GROUP_ID)
    var cb = RingModeCallback()
    audioVolGrpMgr.on(AudioVolumeGroupManagerCallbackType.RING_MODE_CHANGE, cb)
    audioVolGrpMgr.off(AudioVolumeGroupManagerCallbackType.RING_MODE_CHANGE)
} catch (e: BusinessException) {
    Hilog.error(0, "AudioVolumeGroupManager:on/off", "errCode: ${e.code}, errMessage: ${e.message}")
}
```