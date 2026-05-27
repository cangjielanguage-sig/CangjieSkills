## enum AVControlCommandType

```cangjie
public enum AVControlCommandType <: ToString & Equatable<AVControlCommandType> & Hashable {
    | SESSION_CMD_INVALID
    | SESSION_CMD_PLAY
    | SESSION_CMD_PAUSE
    | SESSION_CMD_STOP
    | SESSION_CMD_PLAY_NEXT
    | SESSION_CMD_PLAY_PREVIOUS
    | SESSION_CMD_FAST_FORWARD
    | SESSION_CMD_REWIND
    | SESSION_CMD_SEEK
    | SESSION_CMD_SET_SPEED
    | SESSION_CMD_SET_LOOP_MODE
    | SESSION_CMD_TOGGLE_FAVORITE
    | SESSION_CMD_PLAY_FROM_ASSETID
    | SESSION_CMD_AVCALL_ANSWER
    | SESSION_CMD_AVCALL_HANG_UP
    | SESSION_CMD_AVCALL_TOGGLE_CALL_MUTE
    | ...
}
```

**功能：** 会话可传递的命令。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<[AVControlCommandType](#enum-avcontrolcommandtype)>
- Hashable

### SESSION_CMD_AVCALL_ANSWER

```cangjie
SESSION_CMD_AVCALL_ANSWER
```

**功能：** 接听。

**起始版本：** 19

### SESSION_CMD_AVCALL_HANG_UP

```cangjie
SESSION_CMD_AVCALL_HANG_UP
```

**功能：** 挂断。

**起始版本：** 19

### SESSION_CMD_AVCALL_TOGGLE_CALL_MUTE

```cangjie
SESSION_CMD_AVCALL_TOGGLE_CALL_MUTE
```

**功能：** 设置通话静音状态。

**起始版本：** 19

### SESSION_CMD_FAST_FORWARD

```cangjie
SESSION_CMD_FAST_FORWARD
```

**功能：** 快进。

**起始版本：** 19

### SESSION_CMD_INVALID

```cangjie
SESSION_CMD_INVALID
```

**功能：** 非法命令。

**起始版本：** 19

### SESSION_CMD_PAUSE

```cangjie
SESSION_CMD_PAUSE
```

**功能：** 暂停。

**起始版本：** 19

### SESSION_CMD_PLAY

```cangjie
SESSION_CMD_PLAY
```

**功能：** 播放。

**起始版本：** 19

### SESSION_CMD_PLAY_FROM_ASSETID

```cangjie
SESSION_CMD_PLAY_FROM_ASSETID
```

**功能：** 播放指定的assetid。

**起始版本：** 19

### SESSION_CMD_PLAY_NEXT

```cangjie
SESSION_CMD_PLAY_NEXT
```

**功能：** 下一首。

**起始版本：** 19

### SESSION_CMD_PLAY_PREVIOUS

```cangjie
SESSION_CMD_PLAY_PREVIOUS
```

**功能：** 上一首。

**起始版本：** 19

### SESSION_CMD_REWIND

```cangjie
SESSION_CMD_REWIND
```

**功能：** 快退。

**起始版本：** 19

### SESSION_CMD_SEEK

```cangjie
SESSION_CMD_SEEK
```

**功能：** 跳转某一节点。

**起始版本：** 19

### SESSION_CMD_SET_LOOP_MODE

```cangjie
SESSION_CMD_SET_LOOP_MODE
```

**功能：** 设置循环模式。

**起始版本：** 19

### SESSION_CMD_SET_SPEED

```cangjie
SESSION_CMD_SET_SPEED
```

**功能：** 设置播放速度。

**起始版本：** 19

### SESSION_CMD_STOP

```cangjie
SESSION_CMD_STOP
```

**功能：** 停止。

**起始版本：** 19

### SESSION_CMD_TOGGLE_FAVORITE

```cangjie
SESSION_CMD_TOGGLE_FAVORITE
```

**功能：** 是否收藏。

**起始版本：** 19

### func !=(AVControlCommandType)

```cangjie
public operator func !=(other: AVControlCommandType): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVControlCommandType](#enum-avcontrolcommandtype)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(AVControlCommandType)

```cangjie
public operator func ==(other: AVControlCommandType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVControlCommandType](#enum-avcontrolcommandtype)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|