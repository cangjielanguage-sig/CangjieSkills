## enum AVSessionEventType

```cangjie
public enum AVSessionEventType <: ToString & Equatable<AVSessionEventType> {
    | Play
    | Pause
    | Stop
    | PlayNext
    | PlayPrevious
    | FastForward
    | Rewind
    | PlayFromAssetId
    | Seek
    | SetSpeed
    | SetLoopMode
    | ToggleFavorite
    | SkipToQueueItem
    | HandleKeyEvent
    | OutputDeviceChange
    | CommonCommand
    | Answer
    | HangUp
    | ToggleCallMute
    | CastDisplayChange
    | ...
}
```

**功能：** 会话支持订阅的监听事件，并在触发时提供相应数据给注册的回调函数使用。（[注册方法](#func-onavsessioncontrollereventtype-callback0argument)）。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<[AVSessionEventType](#enum-avsessioneventtype)>

### Answer

```cangjie
Answer
```

**功能：** 通话接听监听事件。

**起始版本：** 19

### CastDisplayChange

```cangjie
CastDisplayChange
```

**功能：** 扩展屏投播显示设备变化监听事件，提供[CastDisplayInfo](#class-castdisplayinfo)，表示扩展屏投播显示设备信息。

**起始版本：** 19

### CommonCommand

```cangjie
CommonCommand
```

**功能：** 自定义控制命令变化监听事件，提供HashMap，内容与[sendCommonCommand](#func-sendcommoncommandstring-hashmapstring-valuetype)方法设置的参数内容完全一致。

**起始版本：** 19

### FastForward

```cangjie
FastForward
```

**功能：** 快进命令监听事件，事件触发时提供Int64，表示时间节点。

**起始版本：** 19

### HandleKeyEvent

```cangjie
HandleKeyEvent
```

**功能：** 蓝牙/有线等外设接入的按键输入事件的监听，监听多媒体按键事件中播放、暂停、上下一首、快进、快退的指令。当按键事件被发送到会话时触发，提供[KeyEvent](../InputKit/cj-apis-multimodalInput-keyEvent.md#class-keyevent)，表示按键事件。

**起始版本：** 19

### HangUp

```cangjie
HangUp
```

**功能：** 通话挂断监听事件。

**起始版本：** 19

### OutputDeviceChange

```cangjie
OutputDeviceChange
```

**功能：** 播放设备变化监听事件，提供[ConnectionState](#enum-connectionstate)和[OutputDeviceInfo](#class-outputdeviceinfo)，表示连接状态和播放设备。

**起始版本：** 19

### Pause

```cangjie
Pause
```

**功能：** 暂停命令监听事件。

**起始版本：** 19

### Play

```cangjie
Play
```

**功能：** 播放命令监听事件。

**起始版本：** 19

### PlayFromAssetId

```cangjie
PlayFromAssetId
```

**功能：** 媒体id播放命令监听事件，事件触发时提供Int64，表示媒体id。

**起始版本：** 19

### PlayNext

```cangjie
PlayNext
```

**功能：** 播放下一首命令监听事件。

**起始版本：** 19

### PlayPrevious

```cangjie
PlayPrevious
```

**功能：** 播放上一首命令监听事件。

**起始版本：** 19

### Rewind

```cangjie
Rewind
```

**功能：** 快退命令监听事件，事件触发时提供Int64，表示时间节点。

**起始版本：** 19

### Seek

```cangjie
Seek
```

**功能：** 跳转节点监听事件，当跳转节点命令被发送到会话时触发，提供Int64，表示时间节点。

**起始版本：** 19

### SetLoopMode

```cangjie
SetLoopMode
```

**功能：** 循环模式监听事件，当设置循环模式的命令被发送到会话时触发，提供[LoopMode](#enum-loopmode)，表示循环模式。

**起始版本：** 19

### SetSpeed

```cangjie
SetSpeed
```

**功能：** 播放速率监听事件，当设置播放速率的命令被发送到会话时触发，提供Float64，表示播放倍速。

**起始版本：** 19

### SkipToQueueItem

```cangjie
SkipToQueueItem
```

**功能：** 播放列表中某项被选中的监听事件，session端可以选择对这个单项歌曲进行播放，当播放列表选中单项的命令被发送到会话时触发，提供Int32，表示选中的播放列表项的ID。

**起始版本：** 19

### Stop

```cangjie
Stop
```

**功能：** 停止命令监听事件。

**起始版本：** 19

### ToggleCallMute

```cangjie
ToggleCallMute
```

**功能：** 通话静音监听事件。

**起始版本：** 19