## enum PlaybackState

```cangjie
public enum PlaybackState <: Equatable<PlaybackState> & ToString {
    | PLAYBACK_STATE_INITIAL
    | PLAYBACK_STATE_PREPARE
    | PLAYBACK_STATE_PLAY
    | PLAYBACK_STATE_PAUSE
    | PLAYBACK_STATE_FAST_FORWARD
    | PLAYBACK_STATE_REWIND
    | PLAYBACK_STATE_STOP
    | PLAYBACK_STATE_COMPLETED
    | PLAYBACK_STATE_RELEASED
    | PLAYBACK_STATE_ERROR
    | PLAYBACK_STATE_IDLE
    | PLAYBACK_STATE_BUFFERING
    | ...
}
```

**功能：** 表示媒体播放状态的枚举。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**父类型：**

- Equatable\<[PlaybackState](#enum-playbackstate)>
- ToString

### PLAYBACK_STATE_BUFFERING

```cangjie
PLAYBACK_STATE_BUFFERING
```

**功能：** 缓冲。

**起始版本：** 19

### PLAYBACK_STATE_COMPLETED

```cangjie
PLAYBACK_STATE_COMPLETED
```

**功能：** 播放完成。

**起始版本：** 19

### PLAYBACK_STATE_ERROR

```cangjie
PLAYBACK_STATE_ERROR
```

**功能：** 错误。

**起始版本：** 19

### PLAYBACK_STATE_FAST_FORWARD

```cangjie
PLAYBACK_STATE_FAST_FORWARD
```

**功能：** 快进。

**起始版本：** 19

### PLAYBACK_STATE_IDLE

```cangjie
PLAYBACK_STATE_IDLE
```

**功能：** 空闲。

**起始版本：** 19

### PLAYBACK_STATE_INITIAL

```cangjie
PLAYBACK_STATE_INITIAL
```

**功能：** 初始状态。

**起始版本：** 19

### PLAYBACK_STATE_PAUSE

```cangjie
PLAYBACK_STATE_PAUSE
```

**功能：** 暂停。

**起始版本：** 19

### PLAYBACK_STATE_PLAY

```cangjie
PLAYBACK_STATE_PLAY
```

**功能：** 正在播放。

**起始版本：** 19

### PLAYBACK_STATE_PREPARE

```cangjie
PLAYBACK_STATE_PREPARE
```

**功能：** 播放准备状态。

**起始版本：** 19

### PLAYBACK_STATE_RELEASED

```cangjie
PLAYBACK_STATE_RELEASED
```

**功能：** 释放。

**起始版本：** 19

### PLAYBACK_STATE_REWIND

```cangjie
PLAYBACK_STATE_REWIND
```

**功能：** 快退。

**起始版本：** 19

### PLAYBACK_STATE_STOP

```cangjie
PLAYBACK_STATE_STOP
```

**功能：** 停止。

**起始版本：** 19

### func !=(PlaybackState)

```cangjie
public operator func !=(other: PlaybackState): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PlaybackState](#enum-playbackstate)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(PlaybackState)

```cangjie
public operator func ==(other: PlaybackState): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PlaybackState](#enum-playbackstate)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表示。|