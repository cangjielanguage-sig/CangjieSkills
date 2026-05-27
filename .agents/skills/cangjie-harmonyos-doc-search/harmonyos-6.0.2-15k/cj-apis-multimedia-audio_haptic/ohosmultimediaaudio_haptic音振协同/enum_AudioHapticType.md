## enum AudioHapticType

```cangjie
public enum AudioHapticType <: ToString & Equatable<AudioHapticType> {
    | AUDIO_HAPTIC_TYPE_AUDIO
    | AUDIO_HAPTIC_TYPE_HAPTIC
    | ...
}
```

**功能：** 音振类型。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<[AudioHapticType](#enum-audiohaptictype)>

### AUDIO_HAPTIC_TYPE_AUDIO

```cangjie
AUDIO_HAPTIC_TYPE_AUDIO
```

**功能：** 音频。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

### AUDIO_HAPTIC_TYPE_HAPTIC

```cangjie
AUDIO_HAPTIC_TYPE_HAPTIC
```

**功能：** 振动。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

### func !=(AudioHapticType)

```cangjie
public operator func !=(other: AudioHapticType): Bool
```

**功能：** 对枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioHapticType](#enum-audiohaptictype)|是|-|音振类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音振类型相同，返回false，否则返回true。|

### func ==(AudioHapticType)

```cangjie
public operator func ==(other: AudioHapticType): Bool
```

**功能：** 对枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioHapticType](#enum-audiohaptictype)|是|-|音振类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音振类型相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|