## enum StreamUsage

```cangjie
public enum StreamUsage <: Equatable<StreamUsage> & ToString {
    | STREAM_USAGE_UNKNOWN
    | STREAM_USAGE_MUSIC
    | STREAM_USAGE_VOICE_COMMUNICATION
    | STREAM_USAGE_VOICE_ASSISTANT
    | STREAM_USAGE_ALARM
    | STREAM_USAGE_VOICE_MESSAGE
    | STREAM_USAGE_RINGTONE
    | STREAM_USAGE_NOTIFICATION
    | STREAM_USAGE_ACCESSIBILITY
    | STREAM_USAGE_MOVIE
    | STREAM_USAGE_GAME
    | STREAM_USAGE_AUDIOBOOK
    | STREAM_USAGE_NAVIGATION
    | STREAM_USAGE_VIDEO_COMMUNICATION
    | ...
}
```

**功能：** 音频流使用类型。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**父类型：**

- Equatable\<[StreamUsage](#enum-streamusage)>
- ToString

### STREAM_USAGE_ACCESSIBILITY

```cangjie
STREAM_USAGE_ACCESSIBILITY
```

**功能：** 无障碍。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### STREAM_USAGE_ALARM

```cangjie
STREAM_USAGE_ALARM
```

**功能：** 闹钟。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### STREAM_USAGE_AUDIOBOOK

```cangjie
STREAM_USAGE_AUDIOBOOK
```

**功能：** 有声读物（包括听书、相声、评书）、听新闻、播客等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### STREAM_USAGE_GAME

```cangjie
STREAM_USAGE_GAME
```

**功能：** 游戏。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### STREAM_USAGE_MOVIE

```cangjie
STREAM_USAGE_MOVIE
```

**功能：** 电影或视频。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### STREAM_USAGE_MUSIC

```cangjie
STREAM_USAGE_MUSIC
```

**功能：** 音乐。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### STREAM_USAGE_NAVIGATION

```cangjie
STREAM_USAGE_NAVIGATION
```

**功能：** 导航。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### STREAM_USAGE_NOTIFICATION

```cangjie
STREAM_USAGE_NOTIFICATION
```

**功能：** 通知。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### STREAM_USAGE_RINGTONE

```cangjie
STREAM_USAGE_RINGTONE
```

**功能：** 铃声。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### STREAM_USAGE_UNKNOWN

```cangjie
STREAM_USAGE_UNKNOWN
```

**功能：** 未知类型。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### STREAM_USAGE_VIDEO_COMMUNICATION

```cangjie
STREAM_USAGE_VIDEO_COMMUNICATION
```

**功能：** VoIP视频通话。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### STREAM_USAGE_VOICE_ASSISTANT

```cangjie
STREAM_USAGE_VOICE_ASSISTANT
```

**功能：** 语音播报。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### STREAM_USAGE_VOICE_COMMUNICATION

```cangjie
STREAM_USAGE_VOICE_COMMUNICATION
```

**功能：** VoIP语音通话。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### STREAM_USAGE_VOICE_MESSAGE

```cangjie
STREAM_USAGE_VOICE_MESSAGE
```

**功能：** 语音消息。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(StreamUsage)

```cangjie
public operator func !=(other: StreamUsage): Bool
```

**功能：** 对音频流使用类型枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[StreamUsage](#enum-streamusage)|是|-|音频流使用类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频流使用类型不同，返回true，否则返回false。|