## class Schema

```cangjie
public class Schema {
    public var root: FieldNode
    public var indexes: Array<String>
    public var mode: Int32
    public var skip: Int32

    public init(root: FieldNode, indexes: Array<String>, mode: Int32, skip: Int32)
}
```

**功能：** 表示数据库模式，可以在创建或打开数据库时创建Schema对象并将它们放入[KVOptions](#class-kvoptions)中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 22

### var indexes

```cangjie
public var indexes: Array<String>
```

**功能：** 索引字段定义，只有通过此字段指定的FieldNode才会创建索引，格式为：`'$.field1'`, `'$.field2'`。

**类型：** Array\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 22

### var mode

```cangjie
public var mode: Int32
```

**功能：** Schema的模式，可以取值0或1，0表示COMPATIBLE模式，1表示STRICT模式。

STRICT：STRICT模式要求用户插入的值必须与Schema定义严格匹配，字段数量和格式都不能有差异。如果不匹配，数据库将在插入数据时返回错误。

COMPATIBLE：选择为COMPATIBLE模式时，数据库在检查Value格式时较为宽松，只要Value具有Schema描述的特征即可，允许存在额外字段。例如，定义了id、name字段时，可以插入id、name、age等多个字段。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 22

### var root

```cangjie
public var root: FieldNode
```

**功能：** 存放了Value中所有字段的定义。

**类型：** [FieldNode](#class-fieldnode)

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 22

### var skip

```cangjie
public var skip: Int32
```

**功能：** 支持在检查Value时跳过skip指定的字节数，取值范围为[0, 4 * 1024 * 1024 - 2]字节。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 22

### init(FieldNode, Array\<String>, Int32, Int32)

```cangjie
public init(root: FieldNode, indexes: Array<String>, mode: Int32, skip: Int32)
```

**功能：** 表示数据库模式，可以在创建或打开数据库时创建Schema对象并将它们放入[KVOptions](#class-kvoptions)中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|root|[FieldNode](#class-fieldnode)|是|-|存放了Value中所有字段的定义。|
|indexes|Array\<String>|是|-|索引字段定义，只有通过此字段指定的FieldNode才会创建索引，格式为：`'$.field1'`, `'$.field2'`。|
|mode|Int32|是|-|Schema的模式，可以取值0或1，0表示COMPATIBLE模式，1表示STRICT模式。|
|skip|Int32|是|-|支持在检查Value时，跳过skip指定的字节数，且取值范围为[0, 4 * 1024 * 1024 - 2]字节。|