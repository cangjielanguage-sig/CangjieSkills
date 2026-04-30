## enum AVCastControlCommandType

```cangjie
public enum AVCastControlCommandType <: Equatable<AVCastControlCommandType> & Hashable & ToString {
    | CAST_CONTROL_CMD_INVALID
    | CAST_CONTROL_CMD_PLAY
    | CAST_CONTROL_CMD_PAUSE
    | CAST_CONTROL_CMD_STOP
    | CAST_CONTROL_CMD_PLAY_NEXT
    | CAST_CONTROL_CMD_PLAY_PREVIOUS
    | CAST_CONTROL_CMD_FAST_FORWARD
    | CAST_CONTROL_CMD_REWIND
    | CAST_CONTROL_CMD_SEEK
    | CAST_CONTROL_CMD_SET_VOLUME
    | CAST_CONTROL_CMD_SET_SPEED
    | CAST_CONTROL_CMD_SET_LOOP_MODE
    | CAST_CONTROL_CMD_TOGGLE_FAVORITE
    | CAST_CONTROL_CMD_TOGGLE_MUTE
    | ...
}
```

**功能：** 投播控制器可传递的命令。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

**父类型：**

- Equatable\<[AVCastControlCommandType](#enum-avcastcontrolcommandtype)>
- Hashable
- ToString

### CAST_CONTROL_CMD_FAST_FORWARD

```cangjie
CAST_CONTROL_CMD_FAST_FORWARD
```

**功能：** 快进。

**起始版本：** 19

### CAST_CONTROL_CMD_INVALID

```cangjie
CAST_CONTROL_CMD_INVALID
```

**功能：** 无效命令。

**起始版本：** 19

### CAST_CONTROL_CMD_PAUSE

```cangjie
CAST_CONTROL_CMD_PAUSE
```

**功能：** 暂停。

**起始版本：** 19

### CAST_CONTROL_CMD_PLAY

```cangjie
CAST_CONTROL_CMD_PLAY
```

**功能：** 播放。

**起始版本：** 19

### CAST_CONTROL_CMD_PLAY_NEXT

```cangjie
CAST_CONTROL_CMD_PLAY_NEXT
```

**功能：** 下一首。

**起始版本：** 19

### CAST_CONTROL_CMD_PLAY_PREVIOUS

```cangjie
CAST_CONTROL_CMD_PLAY_PREVIOUS
```

**功能：** 上一首。

**起始版本：** 19

### CAST_CONTROL_CMD_REWIND

```cangjie
CAST_CONTROL_CMD_REWIND
```

**功能：** 快退。

**起始版本：** 19

### CAST_CONTROL_CMD_SEEK

```cangjie
CAST_CONTROL_CMD_SEEK
```

**功能：** 跳转某一节点。

**起始版本：** 19

### CAST_CONTROL_CMD_SET_LOOP_MODE

```cangjie
CAST_CONTROL_CMD_SET_LOOP_MODE
```

**功能：** 设置循环模式。

**起始版本：** 19

### CAST_CONTROL_CMD_SET_SPEED

```cangjie
CAST_CONTROL_CMD_SET_SPEED
```

**功能：** 设置播放速度。

**起始版本：** 19

### CAST_CONTROL_CMD_SET_VOLUME

```cangjie
CAST_CONTROL_CMD_SET_VOLUME
```

**功能：** 设置音量。

**起始版本：** 19

### CAST_CONTROL_CMD_STOP

```cangjie
CAST_CONTROL_CMD_STOP
```

**功能：** 停止。

**起始版本：** 19

### CAST_CONTROL_CMD_TOGGLE_FAVORITE

```cangjie
CAST_CONTROL_CMD_TOGGLE_FAVORITE
```

**功能：** 是否收藏。

**起始版本：** 19

### CAST_CONTROL_CMD_TOGGLE_MUTE

```cangjie
CAST_CONTROL_CMD_TOGGLE_MUTE
```

**功能：** 设置静音状态。

**起始版本：** 19

### func !=(AVCastControlCommandType)

```cangjie
public operator func !=(other: AVCastControlCommandType): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVCastControlCommandType](#enum-avcastcontrolcommandtype)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(AVCastControlCommandType)

```cangjie
public operator func ==(other: AVCastControlCommandType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVCastControlCommandType](#enum-avcastcontrolcommandtype)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|