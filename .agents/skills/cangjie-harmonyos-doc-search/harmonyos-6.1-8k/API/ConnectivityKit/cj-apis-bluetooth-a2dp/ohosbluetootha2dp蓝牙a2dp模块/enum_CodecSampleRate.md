## enum CodecSampleRate

```cangjie
public enum CodecSampleRate <: Equatable<CodecSampleRate> & ToString {
    | CodecSampleRateNone
    | CodecSampleRate44100
    | CodecSampleRate48000
    | CodecSampleRate88200
    | CodecSampleRate96000
    | CodecSampleRate176400
    | CodecSampleRate192000
    | ...
}
```

**功能：** 蓝牙编码器的采样率。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**父类型：**

- Equatable\<CodecSampleRate>
- ToString

### CodecSampleRate176400

```cangjie
CodecSampleRate176400
```

**功能：** 176.4k位采样率

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### CodecSampleRate192000

```cangjie
CodecSampleRate192000
```

**功能：** 192k位采样率。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### CodecSampleRate44100

```cangjie
CodecSampleRate44100
```

**功能：** 44.1k采样率。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### CodecSampleRate48000

```cangjie
CodecSampleRate48000
```

**功能：** 48k采样率。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### CodecSampleRate88200

```cangjie
CodecSampleRate88200
```

**功能：** 88.2k采样率。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### CodecSampleRate96000

```cangjie
CodecSampleRate96000
```

**功能：** 96k位采样率。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### CodecSampleRateNone

```cangjie
CodecSampleRateNone
```

**功能：** 未知采样率。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### func !=(CodecSampleRate)

```cangjie
public operator func !=(other: CodecSampleRate): Bool
```

**功能：** 对蓝牙编码器的采样率进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CodecSampleRate](#enum-codecsamplerate)|是|-|另一个枚举值。|

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

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CodecSampleRate](#enum-codecsamplerate)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果蓝牙编码器的采样率相同，返回true，否则返回false。|

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