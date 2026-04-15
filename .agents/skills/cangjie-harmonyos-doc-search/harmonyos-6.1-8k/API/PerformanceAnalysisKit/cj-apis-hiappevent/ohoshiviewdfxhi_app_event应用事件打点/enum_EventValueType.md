## enum EventValueType

```cangjie
public enum EventValueType <: ToString {
    | IntValue(Int32)
    | FloatValue(Float64)
    | StringValue(String)
    | BoolValue(Bool)
    | ArrString(Array<String>)
    | ArrInt32(Array<Int32>)
    | ArrBool(Array<Bool>)
    | ArrFloat64(Array<Float64>)
    | Int64Value(Int64)
    | ArrInt64(Array<Int64>)
    | ...
}
```

**功能：** 事件参数值数据。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**父类型：**

- ToString

### ArrBool(Array\<Bool>)

```cangjie
ArrBool(Array<Bool>)
```

**功能：** Bool类型数组数据。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### ArrFloat64(Array\<Float64>)

```cangjie
ArrFloat64(Array<Float64>)
```

**功能：** Float64类型数组数据。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### ArrInt32(Array\<Int32>)

```cangjie
ArrInt32(Array<Int32>)
```

**功能：** Int32类型数组数据。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### ArrInt64(Array\<Int64>)

```cangjie
ArrInt64(Array<Int64>)
```

**功能：** Int64类型数组数据。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### ArrString(Array\<String>)

```cangjie
ArrString(Array<String>)
```

**功能：** 字符串数组数据。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### BoolValue(Bool)

```cangjie
BoolValue(Bool)
```

**功能：** 布尔类型数据。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### FloatValue(Float64)

```cangjie
FloatValue(Float64)
```

**功能：** Float64类型数据。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### Int64Value(Int64)

```cangjie
Int64Value(Int64)
```

**功能：** Int64类型数据。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### IntValue(Int32)

```cangjie
IntValue(Int32)
```

**功能：** Int32类型数据。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### StringValue(String)

```cangjie
StringValue(String)
```

**功能：** 字符串类型数据。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回数据的字符串表示。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|数据的字符串表示。|

**异常：**

- BusinessException：对应错误码如下表，详见[应用事件打点错误码](./cj-errorcode-hiappevent.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 11105001 | Parameter error. |