## enum AVPlaybackStateFilter

```cangjie
public enum AVPlaybackStateFilter <: ToString & Equatable<AVPlaybackStateFilter> {
    | FILTER_KEY_STATE
    | FILTER_KEY_SPEED
    | FILTER_KEY_POSITION
    | FILTER_KEY_BUFFERED_TIME
    | FILTER_KEY_LOOP_MODE
    | FILTER_KEY_IS_FAVORITE
    | FILTER_KEY_ACTIVE_ITEM_ID
    | FILTER_KEY_VOLUME
    | FILTER_KEY_MAX_VOLUME
    | FILTER_KEY_MUTED
    | FILTER_KEY_DURATION
    | FILTER_KEY_VIDEO_WIDTH
    | FILTER_KEY_VIDEO_HEIGHT
    | FILTER_KEY_EXTRAS
    | FILTER_ALL
    | ...
}
```

**功能：** 表示关注媒体播放状态变化的字段。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<[AVPlaybackStateFilter](#enum-avplaybackstatefilter)>

### FILTER_ALL

```cangjie
FILTER_ALL
```

**功能：** 关注播放状态的所有字段变化。

**起始版本：** 19

### FILTER_KEY_ACTIVE_ITEM_ID

```cangjie
FILTER_KEY_ACTIVE_ITEM_ID
```

**功能：** 关注正在播放的媒体Id字段的变化。

**起始版本：** 19

### FILTER_KEY_BUFFERED_TIME

```cangjie
FILTER_KEY_BUFFERED_TIME
```

**功能：** 关注缓冲时间的变化。

**起始版本：** 19

### FILTER_KEY_DURATION

```cangjie
FILTER_KEY_DURATION
```

**功能：** 关注当前媒体资源时长的变化。

**起始版本：** 19

### FILTER_KEY_EXTRAS

```cangjie
FILTER_KEY_EXTRAS
```

**功能：** 关注自定义媒体数据的变化。

**起始版本：** 19

### FILTER_KEY_IS_FAVORITE

```cangjie
FILTER_KEY_IS_FAVORITE
```

**功能：** 关注是否收藏状态的变化。

**起始版本：** 19

### FILTER_KEY_LOOP_MODE

```cangjie
FILTER_KEY_LOOP_MODE
```

**功能：** 关注循环模式的变化。

**起始版本：** 19

### FILTER_KEY_MAX_VOLUME

```cangjie
FILTER_KEY_MAX_VOLUME
```

**功能：** 关注最大音量的变化。

**起始版本：** 19

### FILTER_KEY_MUTED

```cangjie
FILTER_KEY_MUTED
```

**功能：** 关注当前静音状态的变化。

**起始版本：** 19

### FILTER_KEY_POSITION

```cangjie
FILTER_KEY_POSITION
```

**功能：** 关注播放位置的变化。

**起始版本：** 19

### FILTER_KEY_SPEED

```cangjie
FILTER_KEY_SPEED
```

**功能：** 关注播放倍速的变化。

**起始版本：** 19

### FILTER_KEY_STATE

```cangjie
FILTER_KEY_STATE
```

**功能：** 关注播放状态的变化。

**起始版本：** 19

### FILTER_KEY_VIDEO_HEIGHT

```cangjie
FILTER_KEY_VIDEO_HEIGHT
```

**功能：** 关注媒体资源的视频高度的变化。

**起始版本：** 19

### FILTER_KEY_VIDEO_WIDTH

```cangjie
FILTER_KEY_VIDEO_WIDTH
```

**功能：** 关注媒体资源的视频宽度的变化。

**起始版本：** 19

### FILTER_KEY_VOLUME

```cangjie
FILTER_KEY_VOLUME
```

**功能：** 关注正在播放的媒体音量的变化。

**起始版本：** 19

### func !=(AVPlaybackStateFilter)

```cangjie
public operator func !=(other: AVPlaybackStateFilter): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVPlaybackStateFilter](#enum-avplaybackstatefilter)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(AVPlaybackStateFilter)

```cangjie
public operator func ==(other: AVPlaybackStateFilter): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVPlaybackStateFilter](#enum-avplaybackstatefilter)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|