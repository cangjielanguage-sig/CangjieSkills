## enum AudioSampleFormat

```cangjie
public enum AudioSampleFormat <: Equatable<AudioSampleFormat> & ToString {
    | SAMPLE_FORMAT_INVALID
    | SAMPLE_FORMAT_U8
    | SAMPLE_FORMAT_S16LE
    | SAMPLE_FORMAT_S24LE
    | SAMPLE_FORMAT_S32LE
    | SAMPLE_FORMAT_F32LE
    | ...
}
```

**功能：** 音频采样格式。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**父类型：**

- Equatable\<[AudioSampleFormat](#enum-audiosampleformat)>
- ToString

### SAMPLE_FORMAT_F32LE

```cangjie
SAMPLE_FORMAT_F32LE
```

**功能：** 带符号的32位浮点数，小尾数。

由于系统限制，该采样格式仅部分设备支持，请根据实际情况使用。

**起始版本：** 19

### SAMPLE_FORMAT_INVALID

```cangjie
SAMPLE_FORMAT_INVALID
```

**功能：** 无效格式。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SAMPLE_FORMAT_S16LE

```cangjie
SAMPLE_FORMAT_S16LE
```

**功能：** 带符号的16位整数，小尾数。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SAMPLE_FORMAT_S24LE

```cangjie
SAMPLE_FORMAT_S24LE
```

**功能：** 带符号的24位整数，小尾数。

由于系统限制，该采样格式仅部分设备支持，请根据实际情况使用。

**起始版本：** 19

### SAMPLE_FORMAT_S32LE

```cangjie
SAMPLE_FORMAT_S32LE
```

**功能：** 带符号的32位整数，小尾数。

由于系统限制，该采样格式仅部分设备支持，请根据实际情况使用。

**起始版本：** 19

### SAMPLE_FORMAT_U8

```cangjie
SAMPLE_FORMAT_U8
```

**功能：** 无符号8位整数。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioSampleFormat)

```cangjie
public operator func !=(other: AudioSampleFormat): Bool
```

**功能：** 对音频采样格式枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioSampleFormat](#enum-audiosampleformat)|是|-|音频采样格式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频采样格式不同，返回true，否则返回false。|

### func ==(AudioSampleFormat)

```cangjie
public operator func ==(other: AudioSampleFormat): Bool
```

**功能：** 对音频采样格式枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioSampleFormat](#enum-audiosampleformat)|是|-|音频采样格式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频采样格式相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取音频采样格式枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|音频采样格式枚举值的字符串表示。|