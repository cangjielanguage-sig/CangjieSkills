## enum SppType

```cangjie
public enum SppType <: Equatable<SppType> & ToString {
    SppRfcomm |
    ...
}
```

**功能：** 枚举，Spp链路类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core。

**起始版本：** 20

**父类型：**

- [Equatable\<SppType>](#enum-spptype)
- ToString

### SppRfcomm

```cangjie
SppRfcomm
```

**功能：** 表示rfcomm链路类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 20

### func !=(SppType)

```cangjie
public operator func !=(other: SppType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core。

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SppType](#enum-spptype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值是否不相等。|

### func ==(SppType)

```cangjie
public operator func ==(other: SppType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core。

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SppType](#enum-spptype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值是否相等。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 枚举值的字符串表达。

**系统能力：** SystemCapability.Communication.Bluetooth.Core。

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表达。|