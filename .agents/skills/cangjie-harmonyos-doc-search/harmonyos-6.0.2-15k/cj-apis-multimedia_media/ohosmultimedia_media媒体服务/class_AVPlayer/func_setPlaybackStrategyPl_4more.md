### func setPlaybackStrategy(PlaybackStrategy)

```cangjie
public func setPlaybackStrategy(strategy: PlaybackStrategy): Unit
```

**功能：** 设置播放策略，只能在initialized状态下调用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|strategy|[PlaybackStrategy](#class-playbackstrategy)|是|-|播放策略。|

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

let player = createAVPlayer()
let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
let resMgr = abilityContext.resourceManager
let fileDescriptor = resMgr.getRawFd('xxx.mp4')
let rawFd = abilityContext.resourceManager.getRawFd("trailer.mp4")
player.fdSrc = AVFileDescriptor(rawFd.fd, Some(rawFd.offset), Some(rawFd.length))
let playbackStrategy = PlaybackStrategy(preferredWidth: 1, preferredHeight: 2,
    preferredBufferDuration: 3, preferredHdr: false)
player.setPlaybackStrategy(playbackStrategy)
```

### func setSpeed(PlaybackSpeed)

```cangjie
public func setSpeed(speed: PlaybackSpeed): Unit
```

**功能：** 设置倍速模式，只能在prepared/playing/paused/completed状态调用，可以通过[SpeedDone](#func-onavplayercallbacktype-callback1argumentint32)事件确认是否生效。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|speed|[PlaybackSpeed](#enum-playbackspeed)|是|-|指定播放倍速模式。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*

let player = createAVPlayer()
player.setSpeed(PlaybackSpeed.SPEED_FORWARD_2_00_X)
```

### func setVolume(Float32)

```cangjie
public func setVolume(volume: Float32): Unit
```

**功能：** 设置媒体播放音量，只能在prepared/playing/paused/completed状态调用，可以通过[VolumeChange](#func-onavplayercallbacktype-callback1argumentfloat32)事件确认是否生效。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|volume|Float32|是|-|指定的相对音量大小，取值范围为[0.00, 1.00]，1表示最大音量，即100%。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*

let player = createAVPlayer()
let volume: Float32 = 1.0
player.setVolume(volume)
```

### func stop()

```cangjie
public func stop(): Unit
```

**功能：** 停止播放音视频资源，只能在prepared/playing/paused/completed状态调用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

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

let player = createAVPlayer()
try {
    player.stop()
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```