## enum AudioConcurrencyMode

```cangjie
public enum AudioConcurrencyMode <: Equatable<AudioConcurrencyMode> & ToString {
    | CONCURRENCY_DEFAULT
    | CONCURRENCY_MIX_WITH_OTHERS
    | CONCURRENCY_DUCK_OTHERS
    | CONCURRENCY_PAUSE_OTHERS
    | ...
}
```

**功能：** 音频并发模式。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**父类型：**

- Equatable\<[AudioConcurrencyMode](#enum-audioconcurrencymode)>
- ToString

### CONCURRENCY_DEFAULT

```cangjie
CONCURRENCY_DEFAULT
```

**功能：** 默认使用系统策略。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CONCURRENCY_DUCK_OTHERS

```cangjie
CONCURRENCY_DUCK_OTHERS
```

**功能：** 后来播放应用压低正在播放应用的音量。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CONCURRENCY_MIX_WITH_OTHERS

```cangjie
CONCURRENCY_MIX_WITH_OTHERS
```

**功能：** 和其它正在播放应用进行混音。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CONCURRENCY_PAUSE_OTHERS

```cangjie
CONCURRENCY_PAUSE_OTHERS
```

**功能：** 后来播放应用暂停正在播放应用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioConcurrencyMode)

```cangjie
public operator func !=(other: AudioConcurrencyMode): Bool
```

**功能：** 对音频并发模式枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioConcurrencyMode](#enum-audioconcurrencymode)|是|-|音频并发模式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频声道不同，返回true，否则返回false。|

### func ==(AudioConcurrencyMode)

```cangjie
public operator func ==(other: AudioConcurrencyMode): Bool
```

**功能：** 对音频并发模式枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioConcurrencyMode](#enum-audioconcurrencymode)|是|-|音频并发模式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频并发模式相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取音频并发模式枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|音频并发模式枚举值的字符串表示。|