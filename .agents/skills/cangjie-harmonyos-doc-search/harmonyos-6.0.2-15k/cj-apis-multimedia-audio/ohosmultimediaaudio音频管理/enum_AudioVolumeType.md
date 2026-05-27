## enum AudioVolumeType

```cangjie
public enum AudioVolumeType <: Equatable<AudioVolumeType> & ToString {
    | VOICE_CALL
    | RINGTONE
    | MEDIA
    | ALARM
    | ACCESSIBILITY
    | VOICE_ASSISTANT
    | UNKNOWN
    | ...
}
```

**功能：** 音频流类型。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**父类型：**

- Equatable\<[AudioVolumeType](#enum-audiovolumetype)>
- ToString

### ACCESSIBILITY

```cangjie
ACCESSIBILITY
```

**功能：** 无障碍。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### ALARM

```cangjie
ALARM
```

**功能：** 闹钟。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### MEDIA

```cangjie
MEDIA
```

**功能：** 媒体。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### RINGTONE

```cangjie
RINGTONE
```

**功能：** 铃声。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** 未知的音频音量类型。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### VOICE_ASSISTANT

```cangjie
VOICE_ASSISTANT
```

**功能：** 语音助手。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### VOICE_CALL

```cangjie
VOICE_CALL
```

**功能：** 语音电话。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioVolumeType)

```cangjie
public operator func !=(other: AudioVolumeType): Bool
```

**功能：** 对音频流类型枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioVolumeType](#enum-audiovolumetype)|是|-|音频流类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频流类型不同，返回true，否则返回false。|

### func ==(AudioVolumeType)

```cangjie
public operator func ==(other: AudioVolumeType): Bool
```

**功能：** 对音频流类型枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioVolumeType](#enum-audiovolumetype)|是|-|音频流类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频流类型相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取音频流类型枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|音频流类型枚举值的字符串表示。|