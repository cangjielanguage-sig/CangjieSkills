## enum CodecType

```cangjie
public enum CodecType <: Equatable<CodecType> & ToString {
    | CODEC_TYPE_INVALID
    | CODEC_TYPE_SBC
    | CODEC_TYPE_AAC
    | CODEC_TYPE_L2HC
    | ...
}
```

**功能：** 蓝牙编码器类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<CodecType>
- ToString

### CODEC_TYPE_AAC

```cangjie
CODEC_TYPE_AAC
```

**功能：** AAC。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CODEC_TYPE_INVALID

```cangjie
CODEC_TYPE_INVALID
```

**功能：** 未知编码类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CODEC_TYPE_L2HC

```cangjie
CODEC_TYPE_L2HC
```

**功能：** L2HC。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CODEC_TYPE_SBC

```cangjie
CODEC_TYPE_SBC
```

**功能：** SBC。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(CodecType)

```cangjie
public operator func !=(other: CodecType): Bool
```

**功能：** 对蓝牙编码器类型进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[CodecType](#enum-codectype)|是|蓝牙编码器类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果蓝牙编码器类型不同，返回true，否则返回false。|

### func ==(CodecType)

```cangjie
public operator func ==(other: CodecType): Bool
```

**功能：** 对蓝牙编码器类型进行判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[CodecType](#enum-codectype)|是|蓝牙编码器类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果蓝牙编码器类型相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回蓝牙编码器类型的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|蓝牙编码器类型。|