## enum AudioSamplingRate

```cangjie
public enum AudioSamplingRate <: Equatable<AudioSamplingRate> & ToString {
    | SAMPLE_RATE_8000
    | SAMPLE_RATE_11025
    | SAMPLE_RATE_12000
    | SAMPLE_RATE_16000
    | SAMPLE_RATE_22050
    | SAMPLE_RATE_24000
    | SAMPLE_RATE_32000
    | SAMPLE_RATE_44100
    | SAMPLE_RATE_48000
    | SAMPLE_RATE_64000
    | SAMPLE_RATE_88200
    | SAMPLE_RATE_96000
    | SAMPLE_RATE_176400
    | SAMPLE_RATE_192000
    | ...
}
```

**功能：** 音频采样率，具体设备支持的采样率规格会存在差异。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**父类型：**

- Equatable\<[AudioSamplingRate](#enum-audiosamplingrate)>
- ToString

### SAMPLE_RATE_11025

```cangjie
SAMPLE_RATE_11025
```

**功能：** 采样率为11025。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SAMPLE_RATE_12000

```cangjie
SAMPLE_RATE_12000
```

**功能：** 采样率为12000。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SAMPLE_RATE_16000

```cangjie
SAMPLE_RATE_16000
```

**功能：** 采样率为16000。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SAMPLE_RATE_176400

```cangjie
SAMPLE_RATE_176400
```

**功能：** 采样率为176400。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SAMPLE_RATE_192000

```cangjie
SAMPLE_RATE_192000
```

**功能：** 采样率为192000。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SAMPLE_RATE_22050

```cangjie
SAMPLE_RATE_22050
```

**功能：** 采样率为22050。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SAMPLE_RATE_24000

```cangjie
SAMPLE_RATE_24000
```

**功能：** 采样率为24000。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SAMPLE_RATE_32000

```cangjie
SAMPLE_RATE_32000
```

**功能：** 采样率为32000。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SAMPLE_RATE_44100

```cangjie
SAMPLE_RATE_44100
```

**功能：** 采样率为44100。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SAMPLE_RATE_48000

```cangjie
SAMPLE_RATE_48000
```

**功能：** 采样率为48000。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SAMPLE_RATE_64000

```cangjie
SAMPLE_RATE_64000
```

**功能：** 采样率为64000。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SAMPLE_RATE_8000

```cangjie
SAMPLE_RATE_8000
```

**功能：** 采样率为8000。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SAMPLE_RATE_88200

```cangjie
SAMPLE_RATE_88200
```

**功能：** 采样率为88200。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SAMPLE_RATE_96000

```cangjie
SAMPLE_RATE_96000
```

**功能：** 采样率为96000。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioSamplingRate)

```cangjie
public operator func !=(other: AudioSamplingRate): Bool
```

**功能：** 对音频采样率枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioSamplingRate](#enum-audiosamplingrate)|是|-|音频采样率。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频采样率不同，返回true，否则返回false。|