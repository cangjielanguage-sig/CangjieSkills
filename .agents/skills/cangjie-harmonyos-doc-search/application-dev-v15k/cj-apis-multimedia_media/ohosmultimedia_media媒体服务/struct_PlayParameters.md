## struct PlayParameters

```cangjie
public struct PlayParameters {
    public PlayParameters(
        public var loop!: Int32 = 0,
        public var rate!: AudioRendererRate = RENDER_RATE_NORMAL,
        public var leftVolume!: Float32 = 1.0,
        public var rightVolume!: Float32 = 1.0,
        public var priority!: Int32 = 0
    )
}
```

**功能：** 表示音频池播放参数设置。

通过设置播放相关参数，来控制播放的音量，循环次数，播放优先级等参数。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

### var leftVolume

```cangjie
public var leftVolume: Float32 = 1.0
```

**功能：** 设置左声道音量，设置范围（0.0~1.0）。默认值：1.0。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var loop

```cangjie
public var loop: Int32 = 0
```

**功能：** 设置循环参数，0为循环一次，-1表示一直循环。默认值：0。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var priority

```cangjie
public var priority: Int32 = 0
```

**功能：** 音频流播放的优先级，0为最低优先级，数值越大优先级越高，通过相互比较大小确定播放优先级。默认值：0。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var rate

```cangjie
public var rate: AudioRendererRate = RENDER_RATE_NORMAL
```

**功能：** 设置音频播放的倍速，具体倍速范围参照[AudioRendererRate](../AudioKit/cj-apis-multimedia-audio.md#enum-audiorendererrate)。默认值：0。

**类型：** [AudioRendererRate](../AudioKit/cj-apis-multimedia-audio.md#enum-audiorendererrate)

**读写能力：** 可读写

**起始版本：** 19

### var rightVolume

```cangjie
public var rightVolume: Float32 = 1.0
```

**功能：** 设置右声道音量。（当前不支持左右分别设置，将以左声道音量为准）。默认值：1.0。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### PlayParameters(Int32, AudioRendererRate, Float32, Float32, Int32)

```cangjie
public PlayParameters(
    public var loop!: Int32 = 0,
    public var rate!: AudioRendererRate = RENDER_RATE_NORMAL,
    public var leftVolume!: Float32 = 1.0,
    public var rightVolume!: Float32 = 1.0,
    public var priority!: Int32 = 0
)
```

**功能：** 构造PlayParameters类型。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|loop|Int32|否|0| **命名参数。** 设置循环参数，0为循环一次，-1表示一直循环。|
|rate|[AudioRendererRate](../AudioKit/cj-apis-multimedia-audio.md#enum-audiorendererrate)|否|RENDER_RATE_NORMAL| **命名参数。** 设置音频播放的倍速，具体倍速范围参照AudioRendererRate。|
|leftVolume|Float32|否|1.0| **命名参数。** 设置左声道音量，设置范围（0.0~1.0）。|
|rightVolume|Float32|否|1.0| **命名参数。** 设置右声道音量。（当前不支持左右分别设置，将以左声道音量为准）。|
|priority|Int32|否|0| **命名参数。** 音频流播放的优先级，0为最低优先级，数值越大优先级越高，通过相互比较大小确定播放优先级。|