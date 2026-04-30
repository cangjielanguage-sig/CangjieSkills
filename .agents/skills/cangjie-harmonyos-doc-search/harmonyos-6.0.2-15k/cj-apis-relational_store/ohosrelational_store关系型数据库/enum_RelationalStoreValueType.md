## enum RelationalStoreValueType

```cangjie
public enum RelationalStoreValueType {
    | null
    | integer(Int64)
    | double(Float64)
    | string(String)
    | boolean(Bool)
    | Uint8Array(Array<UInt8>)
    | AssetEnum(Asset)
    | AssetsEnum(Array<Asset>)
    | ...
}
```

**功能：** 用于表示允许的数据字段类型，接口参数具体类型根据其功能而定。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

### AssetEnum(Asset)

```cangjie
AssetEnum(Asset)
```

**功能：** 表示值类型为附件[Asset](#struct-asset)。

**起始版本：** 12

### AssetsEnum(Array\<Asset>)

```cangjie
AssetsEnum(Array<Asset>)
```

**功能：** 表示值类型为附件数组Array\<[Asset](#struct-asset)>。

**起始版本：** 12

### Uint8Array(Array\<UInt8>)

```cangjie
Uint8Array(Array<UInt8>)
```

**功能：** 表示值类型为UInt8类型的数组。

**起始版本：** 12

### boolean(Bool)

```cangjie
boolean(Bool)
```

**功能：** 表示值类型为布尔值。

**起始版本：** 12

### double(Float64)

```cangjie
double(Float64)
```

**功能：** 表示值类型为浮点型数字。

**起始版本：** 12

### integer(Int64)

```cangjie
integer(Int64)
```

**功能：** 表示值类型为整型数字。

**起始版本：** 12

### null

```cangjie
null
```

**功能：** 表示值类型为空。

**起始版本：** 12

### string(String)

```cangjie
string(String)
```

**功能：** 表示值类型为字符。

**起始版本：** 12