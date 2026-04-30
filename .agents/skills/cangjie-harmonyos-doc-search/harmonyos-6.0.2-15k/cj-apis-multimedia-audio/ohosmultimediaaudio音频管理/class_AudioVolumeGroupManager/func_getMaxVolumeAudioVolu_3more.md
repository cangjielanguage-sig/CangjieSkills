### func getMaxVolume(AudioVolumeType)

```cangjie
public func getMaxVolume(volumeType: AudioVolumeType): Int32
```

**功能：** 获取指定流的最大音量，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|volumeType|[AudioVolumeType](#enum-audiovolumetype)|是|-|音量流类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回最大音量大小。|

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

try {
    let LOCAL_VOLUME_GROUP_ID: Int32 = 1
    let audioVolGrpMgr: AudioVolumeGroupManager = getAudioManager().getVolumeManager().getVolumeGroupManager(LOCAL_VOLUME_GROUP_ID)
    let maxVoiceCall: Int32 = audioVolGrpMgr.getMaxVolume(AudioVolumeType.VOICE_CALL)  // VOICE_CALL
} catch (e: BusinessException) {
    Hilog.error(0, "getMaxVolume", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func getMinVolume(AudioVolumeType)

```cangjie
public func getMinVolume(volumeType: AudioVolumeType): Int32
```

**功能：** 获取指定流的最小音量，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|volumeType|[AudioVolumeType](#enum-audiovolumetype)|是|-|音量流类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回最小音量。|

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

try {
    let LOCAL_VOLUME_GROUP_ID: Int32 = 1
    let audioVolGrpMgr: AudioVolumeGroupManager = getAudioManager().getVolumeManager().getVolumeGroupManager(LOCAL_VOLUME_GROUP_ID)
    let minVoiceCall: Int32 = audioVolGrpMgr.getMinVolume(AudioVolumeType.VOICE_CALL)  // VOICE_CALL
} catch (e: BusinessException) {
    Hilog.error(0, "getMinVolume", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func getRingerMode()

```cangjie
public func getRingerMode(): AudioRingMode
```

**功能：** 获取铃声模式，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AudioRingMode](#enum-audioringmode)|铃声模式。|

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
    let LOCAL_VOLUME_GROUP_ID: Int32 = 1
    let audioVolGrpMgr: AudioVolumeGroupManager = getAudioManager().getVolumeManager().getVolumeGroupManager(LOCAL_VOLUME_GROUP_ID)
    let ringerMode: AudioRingMode = audioVolGrpMgr.getRingerMode()
} catch (e: BusinessException) {
    Hilog.error(0, "getMinVolume", "errCode: ${e.code}, errMessage: ${e.message}")
}
```