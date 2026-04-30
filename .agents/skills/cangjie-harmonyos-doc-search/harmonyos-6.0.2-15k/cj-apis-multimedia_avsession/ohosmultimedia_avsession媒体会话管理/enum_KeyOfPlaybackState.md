## enum KeyOfPlaybackState

```cangjie
public enum KeyOfPlaybackState <: Equatable<KeyOfPlaybackState> {
    | PLAYBACK_KEY_STATE
    | PLAYBACK_KEY_SPEED
    | PLAYBACK_KEY_POSITION
    | PLAYBACK_KEY_BUFFERED_TIME
    | PLAYBACK_KEY_LOOP_MODE
    | PLAYBACK_KEY_IS_FAVORITE
    | PLAYBACK_KEY_ACTIVE_ITEM_ID
    | PLAYBACK_KEY_VOLUME
    | PLAYBACK_KEY_MAX_VOLUME
    | PLAYBACK_KEY_MUTED
    | PLAYBACK_KEY_DURATION
    | PLAYBACK_KEY_VIDEO_WIDTH
    | PLAYBACK_KEY_VIDEO_HEIGHT
    | PLAYBACK_KEY_EXTRAS
    | ...
}
```

**功能：** 媒体播放状态的相关属性。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**父类型：**

- Equatable\<[KeyOfPlaybackState](#enum-keyofplaybackstate)>

### PLAYBACK_KEY_ACTIVE_ITEM_ID

```cangjie
PLAYBACK_KEY_ACTIVE_ITEM_ID
```

**功能：** 正在播放的媒体Id。

**起始版本：** 19

### PLAYBACK_KEY_BUFFERED_TIME

```cangjie
PLAYBACK_KEY_BUFFERED_TIME
```

**功能：** 缓冲时间。

**起始版本：** 19

### PLAYBACK_KEY_DURATION

```cangjie
PLAYBACK_KEY_DURATION
```

**功能：** 当前媒体资源的时长。

**起始版本：** 19

### PLAYBACK_KEY_EXTRAS

```cangjie
PLAYBACK_KEY_EXTRAS
```

**功能：** 自定义媒体数据。

**起始版本：** 19

### PLAYBACK_KEY_IS_FAVORITE

```cangjie
PLAYBACK_KEY_IS_FAVORITE
```

**功能：** 是否收藏。

**起始版本：** 19

### PLAYBACK_KEY_LOOP_MODE

```cangjie
PLAYBACK_KEY_LOOP_MODE
```

**功能：** 循环模式。

**起始版本：** 19

### PLAYBACK_KEY_MAX_VOLUME

```cangjie
PLAYBACK_KEY_MAX_VOLUME
```

**功能：** 最大音量。

**起始版本：** 19

### PLAYBACK_KEY_MUTED

```cangjie
PLAYBACK_KEY_MUTED
```

**功能：** 当前静音状态。

**起始版本：** 19

### PLAYBACK_KEY_POSITION

```cangjie
PLAYBACK_KEY_POSITION
```

**功能：** 播放位置。

**起始版本：** 19

### PLAYBACK_KEY_SPEED

```cangjie
PLAYBACK_KEY_SPEED
```

**功能：** 播放倍速。

**起始版本：** 19

### PLAYBACK_KEY_STATE

```cangjie
PLAYBACK_KEY_STATE
```

**功能：** 播放状态。

**起始版本：** 19

### PLAYBACK_KEY_VIDEO_HEIGHT

```cangjie
PLAYBACK_KEY_VIDEO_HEIGHT
```

**功能：** 媒体资源的视频高度。

**起始版本：** 19

### PLAYBACK_KEY_VIDEO_WIDTH

```cangjie
PLAYBACK_KEY_VIDEO_WIDTH
```

**功能：** 媒体资源的视频宽度。

**起始版本：** 19

### PLAYBACK_KEY_VOLUME

```cangjie
PLAYBACK_KEY_VOLUME
```

**功能：** 正在播放的媒体音量。

**起始版本：** 19

### func !=(KeyOfPlaybackState)

```cangjie
public operator func !=(other: KeyOfPlaybackState): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[KeyOfPlaybackState](#enum-keyofplaybackstate)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(KeyOfPlaybackState)

```cangjie
public operator func ==(other: KeyOfPlaybackState): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[KeyOfPlaybackState](#enum-keyofplaybackstate)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的字符串表示。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的字符串表示。|