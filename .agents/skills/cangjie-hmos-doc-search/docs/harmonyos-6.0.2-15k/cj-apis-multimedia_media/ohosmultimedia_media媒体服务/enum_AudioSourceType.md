## enum AudioSourceType

```cangjie
public enum AudioSourceType <: ToString & Equatable<AudioSourceType> {
    | AUDIO_SOURCE_TYPE_DEFAULT
    | AUDIO_SOURCE_TYPE_MIC
    | AUDIO_SOURCE_TYPE_VOICE_RECOGNITION
    | AUDIO_SOURCE_TYPE_VOICE_COMMUNICATION
    | AUDIO_SOURCE_TYPE_VOICE_MESSAGE
    | AUDIO_SOURCE_TYPE_CAMCORDER
    | ...
}
```

**功能：** 表示视频录制中音频源类型。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<AudioSourceType>

### AUDIO_SOURCE_TYPE_CAMCORDER

```cangjie
AUDIO_SOURCE_TYPE_CAMCORDER
```

**功能：** 表示相机录像的音频源。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### AUDIO_SOURCE_TYPE_DEFAULT

```cangjie
AUDIO_SOURCE_TYPE_DEFAULT
```

**功能：** 默认的音频输入源类型。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### AUDIO_SOURCE_TYPE_MIC

```cangjie
AUDIO_SOURCE_TYPE_MIC
```

**功能：** 表示MIC的音频输入源。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### AUDIO_SOURCE_TYPE_VOICE_COMMUNICATION

```cangjie
AUDIO_SOURCE_TYPE_VOICE_COMMUNICATION
```

**功能：** 表示语音通话场景的音频源。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### AUDIO_SOURCE_TYPE_VOICE_MESSAGE

```cangjie
AUDIO_SOURCE_TYPE_VOICE_MESSAGE
```

**功能：** 表示短语音消息的音频源。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### AUDIO_SOURCE_TYPE_VOICE_RECOGNITION

```cangjie
AUDIO_SOURCE_TYPE_VOICE_RECOGNITION
```

**功能：** 表示语音识别场景的音频源。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取音频源类型枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|音频源类型枚举值的字符串表示。|

### func !=(AudioSourceType)

```cangjie
public operator override func !=(that: AudioSourceType): Bool
```

**功能：** 对音频源类型枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|that|[AudioSourceType](#enum-audiosourcetype)|是|-|音频源类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频源类型不等，返回true，否则返回false。|

### func ==(AudioSourceType)

```cangjie
public operator override func ==(that: AudioSourceType): Bool
```

**功能：** 对音频源类型枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|that|[AudioSourceType](#enum-audiosourcetype)|是|-|音频源类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频源类型相等，返回true，否则返回false。|