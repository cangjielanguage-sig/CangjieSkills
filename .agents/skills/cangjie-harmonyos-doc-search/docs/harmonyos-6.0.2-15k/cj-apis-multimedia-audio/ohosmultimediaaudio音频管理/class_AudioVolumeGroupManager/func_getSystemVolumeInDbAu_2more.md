### func getSystemVolumeInDb(AudioVolumeType, Int32, DeviceType)

```cangjie
public func getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: Int32, device: DeviceType): Float32
```

**功能：** 获取音量增益dB值，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|volumeType|[AudioVolumeType](#enum-audiovolumetype)|是|-|音量流类型。|
|volumeLevel|Int32|是|-|音量等级。|
|device|[DeviceType](#enum-devicetype)|是|-|设备类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Float32|返回对应的音量增益dB值。|

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
    let pVolType = AudioVolumeType.VOICE_CALL
    let pLevel: Int32 = 1
    let pDevType = DeviceType.BLUETOOTH_A2DP
    let db: Float32 = audioVolGrpMgr.getSystemVolumeInDb(pVolType, pLevel, pDevType)
} catch (e: BusinessException) {
    Hilog.error(0, "getSystemVolumeInDb", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func getVolume(AudioVolumeType)

```cangjie
public func getVolume(volumeType: AudioVolumeType): Int32
```

**功能：** 获取指定流的音量。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|volumeType|[AudioVolumeType](#enum-audiovolumetype)|是|-|音量流类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回指定流的音量。|

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
    let audioVolGrpMgr: AudioVolumeGroupManager = getAudioManager().getVolumeManager().getVolumeGroupManager(LOCAL_VOLUME_GROUP_ID)
    let pVolType: AudioVolumeType = AudioVolumeType.VOICE_CALL
    let volume: Int32 = audioVolGrpMgr.getVolume(pVolType)
} catch (e: BusinessException) {
    Hilog.error(0, "getVolume", "errCode: ${e.code}, errMessage: ${e.message}")
}
```