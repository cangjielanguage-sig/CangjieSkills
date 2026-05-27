## enum HuksParamValue

```cangjie
public enum HuksParamValue {
    | boolean(Bool)
    | int32(Int32)
    | uint32(UInt32)
    | uint64(UInt64)
    | bytes(Array<UInt8>)
    | ...
}
```

**功能：** 用于表示HuksParam中value的值，支持Bool、Int32、UInt32、UInt64、Array\<UInt8>格式。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

### boolean(Bool)

```cangjie
boolean(Bool)
```

**功能：** 该字段用于传入Bool类型的value值。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

### int32(Int32)

```cangjie
int32(Int32)
```

**功能：** 该字段用于传入Int32类型的value值。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

### uint32(UInt32)

```cangjie
uint32(UInt32)
```

**功能：** 该字段用于传入UInt32类型的value值。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

### uint64(UInt64)

```cangjie
uint64(UInt64)
```

**功能：** 该字段用于传入UInt64类型的value值。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

### bytes(Array\<UInt8>)

```cangjie
bytes(Array<UInt8>)
```

**功能：** 该字段用于传入Array\<UInt8>类型的value值。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

### func toBool()

```cangjie
public func toBool(): Option<Bool>
```

**功能：** 获取HuksParamValue的Bool值。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|Option\<Bool>|返回HuksParamValue的Bool值。|

### func toBytes()

```cangjie
public func toBytes(): Option<Array<UInt8>>
```

**功能：** 获取HuksParamValue的Array\<UInt8>值。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|Option\<Array\<UInt8>>|返回HuksParamValue的UInt32值。|

### func toInt32()

```cangjie
public func toInt32(): Option<Int32>
```

**功能：** 获取HuksParamValue的Int32值。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|Option\<Int32>|返回HuksParamValue的Int32值。|

### func toUInt32()

```cangjie
public func toUInt32(): Option<UInt32>
```

**功能：** 获取HuksParamValue的UInt32值。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|Option\<UInt32>|返回HuksParamValue的UInt32值。|

### func toUInt64()

```cangjie
public func toUInt64(): Option<UInt64>
```

**功能：** 获取HuksParamValue的UInt64值。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|Option\<UInt64>|返回HuksParamValue的UInt64值。|

### func |(HuksParamValue)

```cangjie
public operator func |(other: HuksParamValue): HuksParamValue
```

**功能：** 将当前HuksParamValue的UInt32值与另一HuksParamValue的UInt32值进行或运算。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[HuksParamValue](#enum-huksparamvalue)|是|需要进行或运算的HuksParamValue。|

**返回值：**

|类型|说明|
|:----|:----|
|[HuksParamValue](#enum-huksparamvalue)|返回或运算后的HuksParamValue。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|