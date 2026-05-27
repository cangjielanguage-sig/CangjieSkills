# ohos.values_bucket（数据集）

数据集(ValuesBucket) 是开发者向数据库插入的数据集合，数据集以键值对的形式进行传输。

## 导入模块

```cangjie
import kit.ArkData.*
```

## enum VBValueType

```cangjie
public enum VBValueType {
    | Null
    | Integer(Int64)
    | Double(Float64)
    | Str(String)
    | Boolean(Bool)
    | ...
}
```

**功能：** 该类型用于表示数据库允许的数据字段类型。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**起始版本：** 19

### Boolean(Bool)

```cangjie
Boolean(Bool)
```

**功能：** 表示字段类型为布尔值。

**起始版本：** 19

### Double(Float64)

```cangjie
Double(Float64)
```

**功能：** 表示字段类型为浮点数。

**起始版本：** 19

### Integer(Int64)

```cangjie
Integer(Int64)
```

**功能：** 表示字段类型为整型数。

**起始版本：** 19

### Null

```cangjie
Null
```

**功能：** 表示字段类型为空类型。

**起始版本：** 19

### Str(String)

```cangjie
Str(String)
```

**功能：** 表示字段类型为字符串。

**起始版本：** 19
