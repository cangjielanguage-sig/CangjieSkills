## enum RelationalStoreValueType

```cangjie
public enum RelationalStoreValueType {
    | Null
    | Integer(Int64)
    | Double(Float64)
    | StringValue(String)
    | Boolean(Bool)
    | Uint8Array(Array<UInt8>)
    | AssetEnum(Asset)
    | AssetsEnum(Array<Asset>)
    | ...
}
```

**功能：** 用于表示允许的数据字段类型，接口参数具体类型根据其功能而定。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### AssetEnum(Asset)

```cangjie
AssetEnum(Asset)
```

**功能：** 表示值类型为附件[Asset](#type-assets)。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### AssetsEnum(Array\<Asset>)

```cangjie
AssetsEnum(Array<Asset>)
```

**功能：** 表示值类型为附件数组Array\<[Asset](#class-asset)>。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### Boolean(Bool)

```cangjie
Boolean(Bool)
```

**功能：** 表示值类型为布尔值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### Double(Float64)

```cangjie
Double(Float64)
```

**功能：** 表示值类型为浮点型数字。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### Integer(Int64)

```cangjie
Integer(Int64)
```

**功能：** 表示值类型为整型数字。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### Null

```cangjie
Null
```

**功能：** 表示值类型为空。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### StringValue(String)

```cangjie
StringValue(String)
```

**功能：** 表示值类型为字符。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### Uint8Array(Array\<UInt8>)

```cangjie
Uint8Array(Array<UInt8>)
```

**功能：** 表示值类型为UInt8类型的数组。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22