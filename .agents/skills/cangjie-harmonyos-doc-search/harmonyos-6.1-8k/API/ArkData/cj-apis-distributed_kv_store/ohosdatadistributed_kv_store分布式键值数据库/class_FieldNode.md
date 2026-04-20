## class FieldNode

```cangjie
public class FieldNode {
    public var default: String
    public var nullable: Bool
    public var nodeType: Int32

    public init(name: String, nullable: Bool, default: String, nodeType: Int32)
}
```

**功能：** 表示 Schema 实例的节点，提供定义存储在数据库中的值的方法。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 22

### var default

```cangjie
public var default: String
```

**功能：** 表示FieldNode的默认值。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 22

### var nodeType

```cangjie
public var nodeType: Int32
```

**功能：** 表示指定节点对应的数据类型，取值为[KVValueType](#enum-kvvaluetype)对应的枚举值。

> **说明：**
>
> 当前版本不支持BYTE_ARRAY，使用此类型会导致[getKVStore](#func-getkvstoretstring-kvoptions-where-t--singlekvstore)失败。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 22

### var nullable

```cangjie
public var nullable: Bool
```

**功能：** 表示数据库字段是否可以为空。true表示此节点数据可以为空，false表示此节点数据不能为空。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 22

### init(String, Bool, String, Int32)

```cangjie
public init(name: String, nullable: Bool, default: String, nodeType: Int32)
```

**功能：** 用于创建带有String字段FieldNode实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|FieldNode的值，不能为空，且不大于64个字符。|
|nullable|Bool|是|-|表示数据库字段是否可以为空。true表示此节点数据可以为空，false表示此节点数据不能为空。|
|default|String|是|-|表示FieldNode的默认值。|
|nodeType|Int32|是|-|表示指定节点对应的数据类型，取值为[KVValueType](#enum-kvvaluetype)对应的枚举值。暂不支持BYTE_ARRAY，使用此类型会导致[getKVStore](#func-getkvstoretstring-kvoptions-where-t--singlekvstore)失败。|