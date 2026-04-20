## enum KVValueType

```cangjie
public enum KVValueType {
    | StringValue(String)
    | Integer(Int32)
    | Float(Float32)
    | ByteArray(Array<Byte>)
    | Boolean(Bool)
    | Double(Float64)
    | ...
}
```

**功能：** 数据类型枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### Boolean(Bool)

```cangjie
Boolean(Bool)
```

**功能：** 表示值类型为布尔值。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### ByteArray(Array\<Byte>)

```cangjie
ByteArray(Array<Byte>)
```

**功能：** 表示值类型为字节数组。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### Double(Float64)

```cangjie
Double(Float64)
```

**功能：** 表示值类型为双精度浮点数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### Float(Float32)

```cangjie
Float(Float32)
```

**功能：** 表示值类型为单精度浮点数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### Integer(Int32)

```cangjie
Integer(Int32)
```

**功能：** 表示值类型为Int32整数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### StringValue(String)

```cangjie
StringValue(String)
```

**功能：** 表示值类型为字符串。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22