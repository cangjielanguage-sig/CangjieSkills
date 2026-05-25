## enum AVPlayerCallbackType

```cangjie
public enum AVPlayerCallbackType <: ToString {
    | StateChange
    | AVError
    | SeekDone
    | SpeedDone
    | BitrateDone
    | AvailableBitrates
    | VolumeChange
    | EndOfStream
    | TimeUpdate
    | DurationUpdate
    | BufferingUpdate
    | StartRenderFrame
    | VideoSizeChange
    | AudioInterrupt
    | AudioOutputDeviceChangeWithInfo
    | SubtitleUpdate
    | TrackChange
    | TrackInfoUpdate
    | AmplitudeUpdate
    | ...
}
```

**功能：** 回调事件。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**父类型：**

- ToString

### AVError

```cangjie
AVError
```

**功能：** 错误事件。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### AmplitudeUpdate

```cangjie
AmplitudeUpdate
```

**功能：** 订阅音频最大电平值。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### AudioInterrupt

```cangjie
AudioInterrupt
```

**功能：** 音频焦点变化事件。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### AudioOutputDeviceChangeWithInfo

```cangjie
AudioOutputDeviceChangeWithInfo
```

**功能：** 音频流输出设备变化事件。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### AvailableBitrates

```cangjie
AvailableBitrates
```

**功能：** HLS/DASH协议网络流可用的比特率列表。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### BitrateDone

```cangjie
BitrateDone
```

**功能：** setBitrate生效的事件。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### BufferingUpdate

```cangjie
BufferingUpdate
```

**功能：** 音视频缓存更新事件。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### DurationUpdate

```cangjie
DurationUpdate
```

**功能：** 资源播放资源的时长。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### EndOfStream

```cangjie
EndOfStream
```

**功能：** 资源播放至结尾的事件。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### SeekDone

```cangjie
SeekDone
```

**功能：** seek生效的事件。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### SpeedDone

```cangjie
SpeedDone
```

**功能：** setSpeed生效的事件。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### StartRenderFrame

```cangjie
StartRenderFrame
```

**功能：** 视频播放开始首帧渲染的更新事件。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### StateChange

```cangjie
StateChange
```

**功能：** 播放状态机AVPlayerState切换的事件。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### SubtitleUpdate

```cangjie
SubtitleUpdate
```

**功能：** 获取外挂字幕的事件。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### TimeUpdate

```cangjie
TimeUpdate
```

**功能：** 资源播放当前时间。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### TrackChange

```cangjie
TrackChange
```

**功能：** 获取轨道变更的事件。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### TrackInfoUpdate

```cangjie
TrackInfoUpdate
```

**功能：** 轨道信息更新的事件。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### VideoSizeChange

```cangjie
VideoSizeChange
```

**功能：** 视频播放宽高变化事件。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### VolumeChange

```cangjie
VolumeChange
```

**功能：** setVolume生效的事件。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19