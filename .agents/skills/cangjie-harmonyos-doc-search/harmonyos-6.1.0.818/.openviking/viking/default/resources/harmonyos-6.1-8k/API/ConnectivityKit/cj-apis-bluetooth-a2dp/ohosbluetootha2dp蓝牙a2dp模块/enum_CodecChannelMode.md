## enum CodecChannelMode

```cangjie
public enum CodecChannelMode <: Equatable<CodecChannelMode> & ToString {
    | CodecChannelModeNone
    | CodecChannelModeMono
    | CodecChannelModeStereo
    | ...
}
```

**功能：** 蓝牙编码器的声道模式。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**父类型：**

- Equatable\<CodecChannelMode>
- ToString

### CodecChannelModeMono

```cangjie
CodecChannelModeMono
```

**功能：** 单声道。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### CodecChannelModeNone

```cangjie
CodecChannelModeNone
```

**功能：** 未知声道。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### CodecChannelModeStereo

```cangjie
CodecChannelModeStereo
```

**功能：** 双声道。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### func !=(CodecChannelMode)

```cangjie
public operator func !=(other: CodecChannelMode): Bool
```

**功能：** 对蓝牙编码器的声道模式判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CodecChannelMode](#enum-codecchannelmode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果蓝牙编码器的声道模式不同，返回true，否则返回false。|

### func ==(CodecChannelMode)

```cangjie
public operator func ==(other: CodecChannelMode): Bool
```

**功能：** 对蓝牙编码器的声道模式判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CodecChannelMode](#enum-codecchannelmode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果蓝牙编码器的声道模式相同，返回true，否则返回false。|

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