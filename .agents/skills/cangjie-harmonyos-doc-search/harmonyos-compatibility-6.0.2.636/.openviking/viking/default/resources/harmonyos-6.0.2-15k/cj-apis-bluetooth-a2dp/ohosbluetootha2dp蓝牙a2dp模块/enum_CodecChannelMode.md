## enum CodecChannelMode

```cangjie
public enum CodecChannelMode <: Equatable<CodecChannelMode> & ToString {
    | CODEC_CHANNEL_MODE_NONE
    | CODEC_CHANNEL_MODE_MONO
    | CODEC_CHANNEL_MODE_STEREO
    | ...
}
```

**功能：** 蓝牙编码器的声道模式。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<CodecChannelMode>
- ToString

### CODEC_CHANNEL_MODE_MONO

```cangjie
CODEC_CHANNEL_MODE_MONO
```

**功能：** 单声道。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CODEC_CHANNEL_MODE_NONE

```cangjie
CODEC_CHANNEL_MODE_NONE
```

**功能：** 未知声道。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CODEC_CHANNEL_MODE_STEREO

```cangjie
CODEC_CHANNEL_MODE_STEREO
```

**功能：** 双声道。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(CodecChannelMode)

```cangjie
public operator func !=(other: CodecChannelMode): Bool
```

**功能：** 对蓝牙编码器的声道模式判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[CodecChannelMode](#enum-codecchannelmode)|是|蓝牙编码器的声道模式。|

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

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[CodecChannelMode](#enum-codecchannelmode)|是|蓝牙编码器的声道模式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果蓝牙编码器的声道模式相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回蓝牙编码器的声道模式的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|蓝牙编码器的声道模式的字符串表示。|