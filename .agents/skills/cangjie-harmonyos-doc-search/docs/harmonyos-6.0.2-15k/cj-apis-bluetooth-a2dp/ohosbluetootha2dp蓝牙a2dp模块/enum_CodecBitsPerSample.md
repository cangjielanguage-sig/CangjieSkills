## enum CodecBitsPerSample

```cangjie
public enum CodecBitsPerSample <: Equatable<CodecBitsPerSample> & ToString {
    | CODEC_BITS_PER_SAMPLE_NONE
    | CODEC_BITS_PER_SAMPLE_16
    | CODEC_BITS_PER_SAMPLE_24
    | CODEC_BITS_PER_SAMPLE_32
    | ...
}
```

**功能：** 蓝牙编码器每个采样点的位数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<CodecBitsPerSample>
- ToString

### CODEC_BITS_PER_SAMPLE_16

```cangjie
CODEC_BITS_PER_SAMPLE_16
```

**功能：** 16位采样点的位数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CODEC_BITS_PER_SAMPLE_24

```cangjie
CODEC_BITS_PER_SAMPLE_24
```

**功能：** 24位采样点的位数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CODEC_BITS_PER_SAMPLE_32

```cangjie
CODEC_BITS_PER_SAMPLE_32
```

**功能：** 32位采样点的位数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CODEC_BITS_PER_SAMPLE_NONE

```cangjie
CODEC_BITS_PER_SAMPLE_NONE
```

**功能：** 未知采样点的位数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(CodecBitsPerSample)

```cangjie
public operator func !=(other: CodecBitsPerSample): Bool
```

**功能：** 对蓝牙编码器每个采样点的位数进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[CodecBitsPerSample](#enum-codecbitspersample)|是|蓝牙编码器每个采样点的位数。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果蓝牙编码器每个采样点的位数不同，返回true，否则返回false。|

### func ==(CodecBitsPerSample)

```cangjie
public operator func ==(other: CodecBitsPerSample): Bool
```

**功能：** 对蓝牙编码器每个采样点的位数进行判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[CodecBitsPerSample](#enum-codecbitspersample)|是|蓝牙编码器每个采样点的位数。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果蓝牙编码器每个采样点的位数相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回蓝牙编码器每个采样点的位数的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|蓝牙编码器每个采样点的位数的字符串表示。|