## enum TypeCode

```cangjie
public enum TypeCode <: Equatable<TypeCode> & ToString {
    | INT8_ARRAY
    | UINT8_ARRAY
    | INT16_ARRAY
    | UINT16_ARRAY
    | INT32_ARRAY
    | UINT32_ARRAY
    | FLOAT32_ARRAY
    | FLOAT64_ARRAY
    | BIGINT64_ARRAY
    | BIGUINT64_ARRAY
    | ...
}
```

**功能：** 传递数据时通过具体类型值来分辨业务是以哪一种TypedArray去进行数据的读写。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**父类型：**

- Equatable\<TypeCode>
- ToString

### BIGINT64_ARRAY

```cangjie
BIGINT64_ARRAY
```

**功能：** TypedArray类型为BIGINT64_ARRAY。

**起始版本：** 19

### BIGUINT64_ARRAY

```cangjie
BIGUINT64_ARRAY
```

**功能：** TypedArray类型为BIGUINT64_ARRAY。

**起始版本：** 19

### FLOAT32_ARRAY

```cangjie
FLOAT32_ARRAY
```

**功能：** TypedArray类型为FLOAT32_ARRAY。

**起始版本：** 19

### FLOAT64_ARRAY

```cangjie
FLOAT64_ARRAY
```

**功能：** TypedArray类型为FLOAT64_ARRAY。

**起始版本：** 19

### INT16_ARRAY

```cangjie
INT16_ARRAY
```

**功能：** TypedArray类型为INT16_ARRAY。

**起始版本：** 19

### INT32_ARRAY

```cangjie
INT32_ARRAY
```

**功能：** TypedArray类型为INT32_ARRAY。

**起始版本：** 19

### INT8_ARRAY

```cangjie
INT8_ARRAY
```

**功能：** TypedArray类型为INT8_ARRAY。

**起始版本：** 19

### UINT16_ARRAY

```cangjie
UINT16_ARRAY
```

**功能：** TypedArray类型为UINT16_ARRAY。

**起始版本：** 19

### UINT32_ARRAY

```cangjie
UINT32_ARRAY
```

**功能：** TypedArray类型为UINT32_ARRAY。

**起始版本：** 19

### UINT8_ARRAY

```cangjie
UINT8_ARRAY
```

**功能：** TypedArray类型为UINT8_ARRAY。

**起始版本：** 19

### func !=(TypeCode)

```cangjie
public operator func !=(other: TypeCode): Bool
```

**功能：** 比较两个枚举值是否不相等。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TypeCode](#enum-typecode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值是否不相等。|

### func ==(TypeCode)

```cangjie
public operator func ==(other: TypeCode): Bool
```

**功能：** 比较两个枚举值是否相等。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TypeCode](#enum-typecode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值是否相等。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 枚举值的字符串表达。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表达。|