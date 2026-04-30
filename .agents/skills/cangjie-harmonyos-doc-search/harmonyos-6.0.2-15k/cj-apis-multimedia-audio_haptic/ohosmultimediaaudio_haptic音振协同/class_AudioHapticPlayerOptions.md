## class AudioHapticPlayerOptions

```cangjie
public class AudioHapticPlayerOptions <: ToString {
    public AudioHapticPlayerOptions(
        public var muteAudio!: Bool = false,
        public var muteHaptics!: Bool = false
    )
}
```

**功能：** 音振播放器选项。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**父类型：**

- ToString

### var muteAudio

```cangjie
public var muteAudio: Bool = false
```

**功能：** 是否将音频静音，true表示将音频静音，false表示正常播放声音。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var muteHaptics

```cangjie
public var muteHaptics: Bool = false
```

**功能：** 是否禁止振动，true表示将禁止振动，false表示正常振动。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### AudioHapticPlayerOptions(Bool, Bool)

```cangjie
public AudioHapticPlayerOptions(
    public var muteAudio!: Bool = false,
    public var muteHaptics!: Bool = false
)
```

**功能：** 创建[AudioHapticPlayerOptions](#class-audiohapticplayeroptions)实例。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|muteAudio|Bool|否|false| **命名参数。** 是否将音频静音，true表示将音频静音，false表示正常播放声音。|
|muteHaptics|Bool|否|false| **命名参数。** 是否禁止振动，true表示将禁止振动，false表示正常振动。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回类对象的字符串表示，包含具体成员信息。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|类对象的字符串表示。|