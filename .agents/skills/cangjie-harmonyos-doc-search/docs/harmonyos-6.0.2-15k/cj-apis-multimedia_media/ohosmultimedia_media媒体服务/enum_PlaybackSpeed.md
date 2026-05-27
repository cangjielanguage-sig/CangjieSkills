## enum PlaybackSpeed

```cangjie
public enum PlaybackSpeed <: Equatable<PlaybackSpeed> & ToString {
    | SPEED_FORWARD_0_75_X
    | SPEED_FORWARD_1_00_X
    | SPEED_FORWARD_1_25_X
    | SPEED_FORWARD_1_75_X
    | SPEED_FORWARD_2_00_X
    | SPEED_FORWARD_0_50_X
    | SPEED_FORWARD_1_50_X
    | SPEED_FORWARD_0_25_X
    | SPEED_FORWARD_0_125_X
    | ...
}
```

**功能：** 视频播放的倍速枚举，可通过setSpeed方法作为参数传递下去。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

**父类型：**

- Equatable\<PlaybackSpeed>
- ToString

### SPEED_FORWARD_0_125_X

```cangjie
SPEED_FORWARD_0_125_X
```

**功能：** 表示视频播放正常播速的0.125倍。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

### SPEED_FORWARD_0_25_X

```cangjie
SPEED_FORWARD_0_25_X
```

**功能：** 表示视频播放正常播速的0.25倍。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

### SPEED_FORWARD_0_50_X

```cangjie
SPEED_FORWARD_0_50_X
```

**功能：** 表示视频播放正常播速的0.50倍。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

### SPEED_FORWARD_0_75_X

```cangjie
SPEED_FORWARD_0_75_X
```

**功能：** 表示视频播放正常播速的0.75倍。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

### SPEED_FORWARD_1_00_X

```cangjie
SPEED_FORWARD_1_00_X
```

**功能：** 表示视频播放正常播速。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

### SPEED_FORWARD_1_25_X

```cangjie
SPEED_FORWARD_1_25_X
```

**功能：** 表示视频播放正常播速的1.25倍。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

### SPEED_FORWARD_1_50_X

```cangjie
SPEED_FORWARD_1_50_X
```

**功能：** 表示视频播放正常播速的1.50倍。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

### SPEED_FORWARD_1_75_X

```cangjie
SPEED_FORWARD_1_75_X
```

**功能：** 表示视频播放正常播速的1.75倍。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

### SPEED_FORWARD_2_00_X

```cangjie
SPEED_FORWARD_2_00_X
```

**功能：** 表示视频播放正常播速的2.00倍。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

### func !=(PlaybackSpeed)

```cangjie
public operator func !=(other: PlaybackSpeed): Bool
```

**功能：** 判断两个PlaybackSpeed是否不等。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PlaybackSpeed](#enum-playbackspeed)|是|-|另一PlaybackSpeed。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个PlaybackSpeed不等返回true，否则返回false。|

### func ==(PlaybackSpeed)

```cangjie
public operator func ==(other: PlaybackSpeed): Bool
```

**功能：** 判断两个PlaybackSpeed是否相等。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PlaybackSpeed](#enum-playbackspeed)|是|-|另一PlaybackSpeed。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个PlaybackSpeed相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回PlaybackSpeed的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回PlaybackSpeed的字符串表示。|