## enum ParamType

```cangjie
public enum ParamType {
    | FLOAT(Float64)
    | STRING(String)
    | BOOL(Bool)
    | ARRSTRING(Array<String>)
    | ...
}
```

**功能：** 提供了setEventParam允许的数据字段类型。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 20

### ARRSTRING(Array\<String>)

```cangjie
ARRSTRING(Array<String>)
```

**功能：** 表示值类型为字符串数组。

**起始版本：** 20

### BOOL(Bool)

```cangjie
BOOL(Bool)
```

**功能：** 表示值类型为布尔类型。

**起始版本：** 20

### FLOAT(Float64)

```cangjie
FLOAT(Float64)
```

**功能：** 表示值类型为浮点型数字。

**起始版本：** 20

### STRING(String)

```cangjie
STRING(String)
```

**功能：** 表示值类型为字符。

**起始版本：** 20

## enum ValueType

```cangjie
public enum ValueType {
    | INT(Int32)
    | FLOAT(Float64)
    | STRING(String)
    | BOOL(Bool)
    | ARRSTRING(Array<String>)
    | ARRAYI32(Array<Int32>)
    | ARRAYBOOL(Array<Bool>)
    | ARRAYF64(Array<Float64>)
    | INT64(Int64)
    | ARRAYINT64(Array<Int64>)
    | ...
}
```

**功能：** 用于表示允许的数据字段类型。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

### ARRAYBOOL(Array\<Bool>)

```cangjie
ARRAYBOOL(Array<Bool>)
```

**功能：** 表示值类型为Bool类型的数组。

**起始版本：** 12

### ARRAYF64(Array\<Float64>)

```cangjie
ARRAYF64(Array<Float64>)
```

**功能：** 表示值类型为Float64类型的数组。

**起始版本：** 12

### ARRAYI32(Array\<Int32>)

```cangjie
ARRAYI32(Array<Int32>)
```

**功能：** 表示值类型为Int32类型的数组。

**起始版本：** 12

### ARRAYI64(Array\<Int64>)

```cangjie
ARRAYI64(Array<Int64>)
```

**功能：** 表示值类型为Int64类型的数组。

**起始版本：** 20

### ARRSTRING(Array\<String>)

```cangjie
ARRSTRING(Array<String>)
```

**功能：** 表示值类型为字符串数组。

**起始版本：** 12

### BOOL(Bool)

```cangjie
BOOL(Bool)
```

**功能：** 表示值类型为布尔类型。

**起始版本：** 12

### FLOAT(Float64)

```cangjie
FLOAT(Float64)
```

**功能：** 表示值类型为浮点型数字。

**起始版本：** 12

### INT(Int32)

```cangjie
INT(Int32)
```

**功能：** 表示值类型为整型数字。

**起始版本：** 12

### INT(Int64)

```cangjie
INT(Int64)
```

**功能：** 表示值类型为Int64整型数字。

**起始版本：** 20

### STRING(String)

```cangjie
STRING(String)
```

**功能：** 表示值类型为字符。

**起始版本：** 12

### prop value

```cangjie
public prop value: String
```

**功能：** 以字符串形式返回该枚举的值。

**类型：** String

**读写能力：** 只读

**起始版本：** 12