## enum CodecType

```cangjie
public enum CodecType <: Equatable<CodecType> & ToString {
    | CodecTypeInvalid
    | CodecTypeSbc
    | CodecTypeAac
    | CodecTypeL2hc
    | ...
}
```

**功能：** 蓝牙编码器类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**父类型：**

- Equatable\<CodecType>
- ToString

### CodecTypeAac

```cangjie
CodecTypeAac
```

**功能：** AAC。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### CodecTypeInvalid

```cangjie
CodecTypeInvalid
```

**功能：** 未知编码类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### CodecTypeL2hc

```cangjie
CodecTypeL2hc
```

**功能：** L2HC。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### CodecTypeSbc

```cangjie
CodecTypeSbc
```

**功能：** SBC。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### func !=(CodecType)

```cangjie
public operator func !=(other: CodecType): Bool
```

**功能：** 对蓝牙编码器类型进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CodecType](#enum-codectype)|是|-|另一个枚举值。|

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

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CodecType](#enum-codectype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果蓝牙编码器类型相同，返回true，否则返回false。|

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