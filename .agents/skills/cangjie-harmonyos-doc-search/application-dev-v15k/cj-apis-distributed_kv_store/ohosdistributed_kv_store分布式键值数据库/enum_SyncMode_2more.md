## enum SyncMode

```cangjie
public enum SyncMode {
    | PULL_ONLY
    | PUSH_ONLY
    | PUSH_PULL
    | ...
}
```

**功能：** 同步模式枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

### PULL_ONLY

```cangjie
PULL_ONLY
```

**功能：** 表示只能从远端拉取数据到本端。

**起始版本：** 19

### PUSH_ONLY

```cangjie
PUSH_ONLY
```

**功能：** 表示只能从本端推送数据到远端。

**起始版本：** 19

### PUSH_PULL

```cangjie
PUSH_PULL
```

**功能：** 表示从本端推送数据到远端，然后从远端拉取数据到本端。

**起始版本：** 19

## enum KVValueType

```cangjie
public enum KVValueType <: ToString {
    | STRING(String)
    | INTEGER(Int32)
    | FLOAT(Float32)
    | BYTE_ARRAY(Array<Byte>)
    | BOOLEAN(Bool)
    | DOUBLE(Float64)
    | ...
}
```

**功能：** 数据类型枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**父类型：**

- ToString

### BOOLEAN(Bool)

```cangjie
BOOLEAN(Bool)
```

**功能：** 表示值类型为布尔值。

**起始版本：** 12

### BYTE_ARRAY(Array\<Byte>)

```cangjie
BYTE_ARRAY(Array<Byte>)
```

**功能：** 表示值类型为字节数组。

**起始版本：** 12

### DOUBLE(Float64)

```cangjie
DOUBLE(Float64)
```

**功能：** 表示值类型为Float64浮点数。

**起始版本：** 12

### FLOAT(Float32)

```cangjie
FLOAT(Float32)
```

**功能：** 表示值类型为Float32浮点数。

**起始版本：** 12

### INTEGER(Int32)

```cangjie
INTEGER(Int32)
```

**功能：** 表示值类型为Int32整数。

**起始版本：** 12

### STRING(String)

```cangjie
STRING(String)
```

**功能：** 表示值类型为字符串。

**起始版本：** 12

### func toString()

```cangjie
public func toString(): String
```

**功能：** 转成字符串格式。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|返回转换后的字符串。|