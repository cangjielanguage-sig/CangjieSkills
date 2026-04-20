## enum CodecBitsPerSample

```cangjie
public enum CodecBitsPerSample <: Equatable<CodecBitsPerSample> & ToString {
    | CodecBitsPerSampleNone
    | CodecBitsPerSample16
    | CodecBitsPerSample24
    | CodecBitsPerSample32
    | ...
}
```

**功能：** 蓝牙编码器每个采样点的位数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**父类型：**

- Equatable\<CodecBitsPerSample>
- ToString

### CodecBitsPerSample16

```cangjie
CodecBitsPerSample16
```

**功能：** 16位采样点的位数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### CodecBitsPerSample24

```cangjie
CodecBitsPerSample24
```

**功能：** 24位采样点的位数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### CodecBitsPerSample32

```cangjie
CodecBitsPerSample32
```

**功能：** 32位采样点的位数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### CodecBitsPerSampleNone

```cangjie
CodecBitsPerSampleNone
```

**功能：** 未知采样点的位数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### func !=(CodecBitsPerSample)

```cangjie
public operator func !=(other: CodecBitsPerSample): Bool
```

**功能：** 对蓝牙编码器每个采样点的位数进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CodecBitsPerSample](#enum-codecbitspersample)|是|-|另一个枚举值。|

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

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CodecBitsPerSample](#enum-codecbitspersample)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果蓝牙编码器每个采样点的位数相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回枚举值的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表示。|