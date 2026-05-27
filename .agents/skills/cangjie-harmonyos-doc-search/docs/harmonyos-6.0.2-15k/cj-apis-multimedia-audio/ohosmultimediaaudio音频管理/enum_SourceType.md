## enum SourceType

```cangjie
public enum SourceType <: Equatable<SourceType> & ToString {
    | SOURCE_TYPE_INVALID
    | SOURCE_TYPE_MIC
    | SOURCE_TYPE_VOICE_RECOGNITION
    | SOURCE_TYPE_VOICE_COMMUNICATION
    | SOURCE_TYPE_VOICE_MESSAGE
    | SOURCE_TYPE_CAMCORDER
    | SOURCE_TYPE_UNKNOWN
    | ...
}
```

**功能：** 音源类型。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**父类型：**

- Equatable\<[SourceType](#enum-sourcetype)>
- ToString

### SOURCE_TYPE_CAMCORDER

```cangjie
SOURCE_TYPE_CAMCORDER
```

**功能：** 短语音消息的音频源。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SOURCE_TYPE_INVALID

```cangjie
SOURCE_TYPE_INVALID
```

**功能：** 无效的音频源。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SOURCE_TYPE_MIC

```cangjie
SOURCE_TYPE_MIC
```

**功能：** Mic音频源。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SOURCE_TYPE_VOICE_COMMUNICATION

```cangjie
SOURCE_TYPE_VOICE_COMMUNICATION
```

**功能：** 播放音频流（内录）录制音频源。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SOURCE_TYPE_VOICE_MESSAGE

```cangjie
SOURCE_TYPE_VOICE_MESSAGE
```

**功能：** 语音通话场景的音频源。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SOURCE_TYPE_VOICE_RECOGNITION

```cangjie
SOURCE_TYPE_VOICE_RECOGNITION
```

**功能：** 语音识别源。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SOURCE_TYPE_UNKNOWN

```cangjie
SOURCE_TYPE_UNKNOWN
```

**功能：** 未知音频源。

**起始版本：** 19

### func !=(SourceType)

```cangjie
public operator func !=(other: SourceType): Bool
```

**功能：** 对音源类型枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SourceType](#enum-sourcetype)|是|-|音源类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音源类型不同，返回true，否则返回false。|

### func ==(SourceType)

```cangjie
public operator func ==(other: SourceType): Bool
```

**功能：** 对音源类型枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SourceType](#enum-sourcetype)|是|-|音源类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音源类型相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取音源类型枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|音源类型枚举值的字符串表示。|