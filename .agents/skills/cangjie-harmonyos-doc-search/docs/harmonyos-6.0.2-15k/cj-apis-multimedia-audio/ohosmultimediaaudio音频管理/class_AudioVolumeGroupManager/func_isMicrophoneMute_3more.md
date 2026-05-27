### func isMicrophoneMute()

```cangjie
public func isMicrophoneMute(): Bool
```

**功能：** 获取麦克风静音状态，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回系统麦克风静音状态，true为静音，false为非静音。|

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

try {
    let LOCAL_VOLUME_GROUP_ID: Int32 = 1
    let audioVolGrpMgr: AudioVolumeGroupManager = getAudioManager().getVolumeManager().getVolumeGroupManager(LOCAL_VOLUME_GROUP_ID)
    let isMute: Bool = audioVolGrpMgr.isMicrophoneMute()
} catch (e: BusinessException) {
    Hilog.error(0, "isMicrophoneMute", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func isMute(AudioVolumeType)

```cangjie
public func isMute(volumeType: AudioVolumeType): Bool
```

**功能：** 获取指定音量流是否被静音，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|volumeType|[AudioVolumeType](#enum-audiovolumetype)|是|-|音量流类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回流静音状态，true为静音，false为非静音。|

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

try {
    let LOCAL_VOLUME_GROUP_ID: Int32 = 1
    let audioVolGrpMgr: AudioVolumeGroupManager = getAudioManager().getVolumeManager().getVolumeGroupManager(LOCAL_VOLUME_GROUP_ID)
    let isMute1: Bool = audioVolGrpMgr.isMute(AudioVolumeType.VOICE_CALL)
} catch (e: BusinessException) {
    Hilog.error(0, "isMicrophoneMute", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func isVolumeUnadjustable()

```cangjie
public func isVolumeUnadjustable(): Bool
```

**功能：** 获取固定音量模式开关状态，打开时进入固定音量模式，此时音量固定无法被调节，使用同步方式返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|同步接口，返回固定音量模式开关状态，true为固定音量模式，false为非固定音量模式。|

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

try {
    let LOCAL_VOLUME_GROUP_ID: Int32 = 1
    let audioVolGrpMgr: AudioVolumeGroupManager = getAudioManager().getVolumeManager().getVolumeGroupManager(LOCAL_VOLUME_GROUP_ID)
    let isUnadjustable: Bool = audioVolGrpMgr.isVolumeUnadjustable()
} catch (e: BusinessException) {
    Hilog.error(0, "isVolumeUnadjustable", "errCode: ${e.code}, errMessage: ${e.message}")
}
```