## enum AudioLatencyMode

```cangjie
public enum AudioLatencyMode <: ToString & Equatable<AudioLatencyMode> {
    | AUDIO_LATENCY_MODE_NORMAL
    | AUDIO_LATENCY_MODE_FAST
    | ...
}
```

**功能：** 音频时延模式。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<[AudioLatencyMode](#enum-audiolatencymode)>

### AUDIO_LATENCY_MODE_FAST

```cangjie
AUDIO_LATENCY_MODE_FAST
```

**功能：** 低时延模式。该模式适用于比较短的音频文件，音频文件过长时可能被截断，该特性与[SoundPool](../MediaKit/cj-apis-multimedia_media.md#class-soundpool)一致。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

### AUDIO_LATENCY_MODE_NORMAL

```cangjie
AUDIO_LATENCY_MODE_NORMAL
```

**功能：** 普通时延模式。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

### func !=(AudioLatencyMode)

```cangjie
public operator func !=(other: AudioLatencyMode): Bool
```

**功能：** 对枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioLatencyMode](#enum-audiolatencymode)|是|-|音频时延模式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频时延模式相同，返回false，否则返回true。|

### func ==(AudioLatencyMode)

```cangjie
public operator func ==(other: AudioLatencyMode): Bool
```

**功能：** 对枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioLatencyMode](#enum-audiolatencymode)|是|-|音频时延模式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频时延模式相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取音频时延模式枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|音频时延模式枚举值的字符串表示。|