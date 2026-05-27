### func selectTrack(Int32, SwitchMode)

```cangjie
public func selectTrack(index: Int32, mode!: SwitchMode = SwitchMode.SMOOTH): Unit
```

**功能：** 使用AVPlayer播放多音视频轨资源时，选择指定轨道播放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|多音视频资源的轨道索引，可通过[getTrackDescription](#func-gettrackdescription)接口获取当前资源的所有轨道信息[MediaDescription](#type-mediadescription)。|
|mode|[SwitchMode](#enum-switchmode)|否|SwitchMode.SMOOTH| **命名参数。** 切换视频轨道模式，**仅在DASH协议网络流视频轨切换时生效**，其他场景当前暂不支持。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |5400102|Operation not allowed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import ohos.base.*

try {
    var audioTrackIndex: Int32 = 0
    let player = createAVPlayer()
    let mediaDescriptions = player.getTrackDescription()
    for (i in 0..mediaDescriptions.size) {
        let value = mediaDescriptions[i].get(MediaDescriptionKey.MD_KEY_TRACK_INDEX)
        if (let Some(v) <- value) {
            match (v) {
                case ValueType.INT(index) => audioTrackIndex = index
                case _ => ()
            }
        }
    }
    player.selectTrack(audioTrackIndex)
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```

### func setBitrate(Int32)

```cangjie
public func setBitrate(bitrate: Int32): Unit
```

**功能：** 设置比特率，以播放所指定比特率的流媒体资源，当前仅对**HLS/DASH协议网络流**有效。默认情况下，AVPlayer会根据网络连接速度选择合适的比特率。只能在prepared/playing/paused/completed状态调用，可以通过[bitrateDone事件回调](#func-onavplayercallbacktype-callback1argumentint32)确认是否生效。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bitrate|Int32|是|-|指定比特率，须通过[availableBitrates事件回调](#func-onavplayercallbacktype-callback1argumentarrayint32)获得当前HLS/DASH协议网络流可用的比特率列表，如果用户指定的比特率不在此列表中，则播放器将从可用比特率列表中选择最接近的比特率。如果通过availableBitrates事件获得的比特率列表长度为0，则不支持指定比特率，也不会产生bitrateDone回调。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*

let player = createAVPlayer()
let bitrate: Int32 = 96000
player.setBitrate(bitrate)
```