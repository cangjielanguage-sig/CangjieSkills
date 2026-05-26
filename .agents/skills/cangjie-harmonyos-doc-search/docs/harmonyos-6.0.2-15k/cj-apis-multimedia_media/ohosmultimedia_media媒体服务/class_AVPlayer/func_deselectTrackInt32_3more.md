### func deselectTrack(Int32)

```cangjie
public func deselectTrack(index: Int32): Unit
```

**功能：** 使用AVPlayer播放多音轨视频时取消指定音视频轨道播放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|多音视频资源的轨道索引，来自[getTrackDescription](#func-gettrackdescription)接口所获取的轨道信息[MediaDescription](#type-mediadescription)。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|The parameter check failed.|
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
    player.deselectTrack(audioTrackIndex)
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```

### func getPlaybackInfo()

```cangjie
public func getPlaybackInfo(): PlaybackInfo
```

**功能：** 获取播放过程信息，可以在prepared/playing/paused状态调用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[PlaybackInfo](#type-playbackinfo)|播放信息。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import ohos.base.*

try {
    let player = createAVPlayer()
    let playbackInfo = player.getPlaybackInfo()
    AppLog.info("playbackInfo.size = ${playbackInfo.size}")
    for ((key, value) in playbackInfo) {
        AppLog.info("key = ${key}")
        match (value) {
            case INT(v) => AppLog.info("value = Int32(${v})")
            case INT64(v) => AppLog.info("value = Int64(${v})")
            case DOUBLE(v) => AppLog.info("value = Float64(${v})")
            case STRING(v) => AppLog.info("value = String(${v})")
            case _ => throw IllegalArgumentException("The type is not supported.")
        }
    }
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```

### func getSelectedTracks()

```cangjie
public func getSelectedTracks(): Array<Int32>
```

**功能：** 获取已选择的音视频轨道索引，可以在prepared/playing/paused状态调用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Int32>|已选择的音视频轨道索引。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400102|Operation not allowed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import ohos.base.*

try {
    let player = createAVPlayer()
    let selected = player.getSelectedTracks()
    AppLog.info("selectedTracks = ${selected}")
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```