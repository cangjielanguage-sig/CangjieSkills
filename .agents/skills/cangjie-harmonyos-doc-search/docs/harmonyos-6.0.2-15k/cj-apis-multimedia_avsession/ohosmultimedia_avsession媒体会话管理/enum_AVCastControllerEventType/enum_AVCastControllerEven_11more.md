## enum AVCastControllerEventType

```cangjie
public enum AVCastControllerEventType <: ToString & Equatable<AVCastControllerEventType> {
    | CAST_CONTROLLER_PLAYBACK_STATE_CHANGE
    | CAST_CONTROLLER_MEDIA_ITEM_CHANGE
    | CAST_CONTROLLER_PLAY_NEXT
    | CAST_CONTROLLER_PLAY_PREVIOUS
    | CAST_CONTROLLER_REQUEST_PLAY
    | CAST_CONTROLLER_END_OF_STREAM
    | CAST_CONTROLLER_SEEK_DONE
    | CAST_CONTROLLER_VALID_COMMAND_CHANGE
    | CAST_CONTROLLER_ERROR
    | CAST_CONTROLLER_KEY_REQUEST
    | ...
}
```

**功能：** 投播控制器支持订阅的监听事件。

**系统能力：** 详见各枚举值

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<[AVCastControllerEventType](#enum-avcastcontrollereventtype)>

### CAST_CONTROLLER_END_OF_STREAM

```cangjie
CAST_CONTROLLER_END_OF_STREAM
```

**功能：** 播放结束的监听事件。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

### CAST_CONTROLLER_ERROR

```cangjie
CAST_CONTROLLER_ERROR
```

**功能：** 远端播放器的错误事件，该事件仅用于错误提示，不需要用户停止播控动作，远端播放过程中发生的错误，会提供错误码ID和错误信息[BusinessException](../BasicServicesKit/cj-apis-base.md#class-businessexception)。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

### CAST_CONTROLLER_KEY_REQUEST

```cangjie
CAST_CONTROLLER_KEY_REQUEST
```

**功能：** 在线DRM资源投播时，许可证请求的事件监听，触发时提供String和Array\<UInt8>，表示媒体资源及许可证请求数据。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

### CAST_CONTROLLER_MEDIA_ITEM_CHANGE

```cangjie
CAST_CONTROLLER_MEDIA_ITEM_CHANGE
```

**功能：** 投播当前播放媒体内容的监听事件，触发时提供[AVQueueItem](#class-avqueueitem)，表示当前正在播放的媒体内容。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

### CAST_CONTROLLER_PLAYBACK_STATE_CHANGE

```cangjie
CAST_CONTROLLER_PLAYBACK_STATE_CHANGE
```

**功能：** 播放状态变化的监听事件，触发时提供[AVPlaybackState](#class-avplaybackstate)，表示变化后的播放状态。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

### CAST_CONTROLLER_PLAY_NEXT

```cangjie
CAST_CONTROLLER_PLAY_NEXT
```

**功能：** 播放下一首资源的监听事件。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

### CAST_CONTROLLER_PLAY_PREVIOUS

```cangjie
CAST_CONTROLLER_PLAY_PREVIOUS
```

**功能：** 播放上一首资源的监听事件。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

### CAST_CONTROLLER_REQUEST_PLAY

```cangjie
CAST_CONTROLLER_REQUEST_PLAY
```

**功能：** 请求播放的监听事件，触发时提供[AVQueueItem](#class-avqueueitem)，表示当前正在播放的媒体内容。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

### CAST_CONTROLLER_SEEK_DONE

```cangjie
CAST_CONTROLLER_SEEK_DONE
```

**功能：** seek结束的监听事件，触发时提供Int32，表示seek后的播放位置。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

### CAST_CONTROLLER_VALID_COMMAND_CHANGE

```cangjie
CAST_CONTROLLER_VALID_COMMAND_CHANGE
```

**功能：** 有效命令变化监听事件，触发时提供Array\<[AVCastControlCommandType](#enum-avcastcontrolcommandtype)>，表示变化命令的有效集合。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19