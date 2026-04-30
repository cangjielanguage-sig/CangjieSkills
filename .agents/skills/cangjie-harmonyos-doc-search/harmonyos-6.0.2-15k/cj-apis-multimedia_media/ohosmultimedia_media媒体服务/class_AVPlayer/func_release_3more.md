### func release()

```cangjie
public func release(): Unit
```

**功能：** 销毁播放资源，除released状态外，均可以调用。

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

import ohos.base.*
import kit.MediaKit.*

let player = createAVPlayer()
try {
    player.release()
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```

### func reset()

```cangjie
public func reset(): Unit
```

**功能：** 重置播放，只能在initialized/prepared/playing/paused/completed/stopped/error状态调用。

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

import ohos.base.*
import kit.MediaKit.*

let player = createAVPlayer()
try {
    player.reset()
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```

### func seek(Int32, SeekMode)

```cangjie
public func seek(timeMs: Int32, mode!: SeekMode = SeekMode.SEEK_PREV_SYNC): Unit
```

**功能：** 跳转到指定播放位置，只能在prepared/playing/paused/completed状态调用，可以通过[seekDone事件](#func-onavplayercallbacktype-callback1argumentint32)确认是否生效。 注：直播场景不支持seek。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|timeMs|Int32|是|-|指定的跳转时间节点，单位毫秒（ms），取值范围为[0, [duration](#prop-duration)]。|
|mode|[SeekMode](#enum-seekmode)|否|SeekMode.SEEK_PREV_SYNC| **命名参数。** 基于视频I帧的跳转模式，默认为SEEK_PREV_SYNC模式，**仅在视频资源播放时设置**。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.MediaKit.*

let player = createAVPlayer()
try {
    player.seek(2000)
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```