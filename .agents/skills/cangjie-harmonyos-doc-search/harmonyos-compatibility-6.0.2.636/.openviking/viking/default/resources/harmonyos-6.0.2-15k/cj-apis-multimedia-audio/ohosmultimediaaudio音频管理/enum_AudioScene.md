## enum AudioScene

```cangjie
public enum AudioScene <: Equatable<AudioScene> & ToString {
    | AUDIO_SCENE_DEFAULT
    | AUDIO_SCENE_RINGING
    | AUDIO_SCENE_PHONE_CALL
    | AUDIO_SCENE_VOICE_CHAT
    | ...
}
```

**功能：** 音频场景。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**起始版本：** 19

**父类型：**

- Equatable\<[AudioScene](#enum-audioscene)>
- ToString

### AUDIO_SCENE_DEFAULT

```cangjie
AUDIO_SCENE_DEFAULT
```

**功能：** 默认音频场景。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### AUDIO_SCENE_PHONE_CALL

```cangjie
AUDIO_SCENE_PHONE_CALL
```

**功能：** 电话模式。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### AUDIO_SCENE_RINGING

```cangjie
AUDIO_SCENE_RINGING
```

**功能：** 响铃模式。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### AUDIO_SCENE_VOICE_CHAT

```cangjie
AUDIO_SCENE_VOICE_CHAT
```

**功能：** 语音聊天模式。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioScene)

```cangjie
public operator func !=(other: AudioScene): Bool
```

**功能：** 对音频场景枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioScene](#enum-audioscene)|是|-|音频场景。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频场景不同，返回true，否则返回false。|

### func ==(AudioScene)

```cangjie
public operator func ==(other: AudioScene): Bool
```

**功能：** 对音频场景枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioScene](#enum-audioscene)|是|-|音频场景。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频场景相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取音频场景枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|音频场景枚举值的字符串表示。|