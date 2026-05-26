### func on(AudioVolumeManagerCallbackType, Callback1Argument\<VolumeEvent>)

```cangjie
public func on(`type`: AudioVolumeManagerCallbackType, callback: Callback1Argument<VolumeEvent>): Unit
```

**功能：** 监听系统音量变化事件（当系统音量发生变化时触发），使用callback方式返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioVolumeManagerCallbackType](#enum-audiovolumemanagercallbacktype)|是|-|监听事件，固定为：'VOLUME_CHANGE'。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[VolumeEvent](#class-volumeevent)>|是|-|回调函数，返回变化后的音量信息。|

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
class VolumeEventCallback <: Callback1Argument<VolumeEvent> {
    public func invoke(arg: VolumeEvent) {
        AppLog.info("VolumeEventCallback")
    }
}

try {
    let audioVolMgr: AudioVolumeManager = getAudioManager().getVolumeManager()
    var cb = VolumeEventCallback()
    audioVolMgr.on(AudioVolumeManagerCallbackType.VOLUME_CHANGE, cb)
    audioVolMgr.off(AudioVolumeManagerCallbackType.VOLUME_CHANGE)
} catch (e: BusinessException) {
    Hilog.error(0, "AudioVolumeManager on/off", "errCode: ${e.code}, errMessage: ${e.message}")
}
```