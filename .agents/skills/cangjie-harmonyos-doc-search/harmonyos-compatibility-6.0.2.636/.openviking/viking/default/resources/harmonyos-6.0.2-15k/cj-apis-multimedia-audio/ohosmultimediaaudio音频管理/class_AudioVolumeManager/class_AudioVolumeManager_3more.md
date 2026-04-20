## class AudioVolumeManager

```cangjie
public class AudioVolumeManager {}
```

**功能：** 获取音频组管理器，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

### func getVolumeGroupManager(Int32)

```cangjie
public func getVolumeGroupManager(groupId: Int32): AudioVolumeGroupManager
```

**功能：** 获取音频组管理器，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|groupId|Int32|是|-|音量组id，默认使用LOCAL_VOLUME_GROUP_ID。|

**返回值：**

|类型|说明|
|:----|:----|
|[AudioVolumeGroupManager](#class-audiovolumegroupmanager)|音量组实例。|

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

try {
    let LOCAL_VOLUME_GROUP_ID: Int32 = 1
    let audioMgr: AudioManager = getAudioManager()
    let audioVolMgr: AudioVolumeManager = audioMgr.getVolumeManager()
    let audioVolGrpMgr: AudioVolumeGroupManager = audioVolMgr.getVolumeGroupManager(LOCAL_VOLUME_GROUP_ID)
} catch (e: BusinessException) {
    Hilog.error(0, "getVolumeGroupManager", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func off(AudioVolumeManagerCallbackType, ?CallbackObject)

```cangjie
public func off(`type`: AudioVolumeManagerCallbackType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消监听事件。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioVolumeManagerCallbackType](#enum-audiovolumemanagercallbacktype)|是|-|监听事件。|
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