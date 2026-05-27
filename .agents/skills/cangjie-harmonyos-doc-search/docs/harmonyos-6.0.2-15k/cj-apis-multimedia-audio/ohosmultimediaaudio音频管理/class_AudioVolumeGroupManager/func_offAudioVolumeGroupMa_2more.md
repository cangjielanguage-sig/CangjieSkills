### func off(AudioVolumeGroupManagerCallbackType, ?CallbackObject)

```cangjie
public func off(`type`: AudioVolumeGroupManagerCallbackType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消监听事件。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioVolumeGroupManagerCallbackType](#enum-audiovolumegroupmanagercallbacktype)|是|-|监听事件。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None| **命名参数。** 回调函数。|

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

class MicChangeCallback <: Callback1Argument<MicStateChangeEvent> {
    public func invoke(arg: MicStateChangeEvent) {
        AppLog.info("MicChangeCallback: ${arg.mute}")
    }
}

try {
    let LOCAL_VOLUME_GROUP_ID: Int32 = 1
    let audioMgr: AudioManager = getAudioManager()
    let audioVolMgr: AudioVolumeManager = audioMgr.getVolumeManager()
    let audioVolGrpMgr: AudioVolumeGroupManager = audioVolMgr.getVolumeGroupManager(LOCAL_VOLUME_GROUP_ID)
    var cb = MicChangeCallback()
    audioVolGrpMgr.on(AudioVolumeGroupManagerCallbackType.MICSTATE_CHANGE, cb)
    audioVolGrpMgr.off(AudioVolumeGroupManagerCallbackType.MICSTATE_CHANGE)
} catch (e: BusinessException) {
    Hilog.error(0, "AudioVolumeGroupManager:on/off", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func on(AudioVolumeGroupManagerCallbackType, Callback1Argument\<MicStateChangeEvent>)

```cangjie
public func on(`type`: AudioVolumeGroupManagerCallbackType, callback: Callback1Argument<MicStateChangeEvent>): Unit
```

**功能：** 监听系统麦克风状态更改事件（当检测到系统麦克风状态发生改变时触发），使用callback方式返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioVolumeGroupManagerCallbackType](#enum-audiovolumegroupmanagercallbacktype)|是|-|监听事件，固定为：'MICSTATE_CHANGE'。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[MicStateChangeEvent](#class-micstatechangeevent)>|是|-|回调函数，返回当前音频渲染器信息。|

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
class MicChangeCallback <: Callback1Argument<MicStateChangeEvent> {
    public func invoke(arg: MicStateChangeEvent) {
        AppLog.info("MicChangeCallback: ${arg.mute}")
    }
}

try {
    let LOCAL_VOLUME_GROUP_ID: Int32 = 1
    let audioMgr: AudioManager = getAudioManager()
    let audioVolMgr: AudioVolumeManager = audioMgr.getVolumeManager()
    let audioVolGrpMgr: AudioVolumeGroupManager = audioVolMgr.getVolumeGroupManager(LOCAL_VOLUME_GROUP_ID)
    var cb = MicChangeCallback()
    audioVolGrpMgr.on(AudioVolumeGroupManagerCallbackType.MICSTATE_CHANGE, cb)
    audioVolGrpMgr.off(AudioVolumeGroupManagerCallbackType.MICSTATE_CHANGE)
} catch (e: BusinessException) {
    Hilog.error(0, "AudioVolumeGroupManager:on/off", "errCode: ${e.code}, errMessage: ${e.message}")
}
```