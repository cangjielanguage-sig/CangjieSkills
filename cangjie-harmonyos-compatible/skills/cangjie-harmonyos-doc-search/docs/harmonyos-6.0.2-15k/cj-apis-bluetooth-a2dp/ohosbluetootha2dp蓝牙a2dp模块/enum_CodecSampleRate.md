## enum CodecSampleRate

```cangjie
public enum CodecSampleRate <: Equatable<CodecSampleRate> & ToString {
    | CODEC_SAMPLE_RATE_NONE
    | CODEC_SAMPLE_RATE_44100
    | CODEC_SAMPLE_RATE_48000
    | CODEC_SAMPLE_RATE_88200
    | CODEC_SAMPLE_RATE_96000
    | CODEC_SAMPLE_RATE_176400
    | CODEC_SAMPLE_RATE_192000
    | ...
}
```

**功能：** 蓝牙编码器的采样率。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<CodecSampleRate>
- ToString

### CODEC_SAMPLE_RATE_176400

```cangjie
CODEC_SAMPLE_RATE_176400
```

**功能：** 176.4k位采样率。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CODEC_SAMPLE_RATE_192000

```cangjie
CODEC_SAMPLE_RATE_192000
```

**功能：** 192k位采样率。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CODEC_SAMPLE_RATE_44100

```cangjie
CODEC_SAMPLE_RATE_44100
```

**功能：** 44.1k采样率。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CODEC_SAMPLE_RATE_48000

```cangjie
CODEC_SAMPLE_RATE_48000
```

**功能：** 48k采样率。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CODEC_SAMPLE_RATE_88200

```cangjie
CODEC_SAMPLE_RATE_88200
```

**功能：** 88.2k采样率。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CODEC_SAMPLE_RATE_96000

```cangjie
CODEC_SAMPLE_RATE_96000
```

**功能：** 96k位采样率。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CODEC_SAMPLE_RATE_NONE

```cangjie
CODEC_SAMPLE_RATE_NONE
```

**功能：** 未知采样率。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(CodecSampleRate)

```cangjie
public operator func !=(other: CodecSampleRate): Bool
```

**功能：** 对蓝牙编码器的采样率进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[CodecSampleRate](#enum-codecsamplerate)|是|蓝牙编码器的采样率。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果蓝牙编码器的采样率不同，返回true，否则返回false。|

### func ==(CodecSampleRate)

```cangjie
public operator func ==(other: CodecSampleRate): Bool
```

**功能：** 对蓝牙编码器的采样率进行判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[CodecSampleRate](#enum-codecsamplerate)|是|蓝牙编码器的采样率。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果蓝牙编码器的采样率相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回蓝牙编码器的采样率的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|蓝牙编码器的采样率的字符串表示。|