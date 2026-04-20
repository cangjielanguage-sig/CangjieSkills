## struct ChangeInfo

```cangjie
public struct ChangeInfo {
    public let table: String
    public let `type`: ChangeType
    public let inserted: Array<PRIKeyType>
    public let updated: Array<PRIKeyType>
    public let deleted: Array<PRIKeyType>
    public init(table: String, `type`: ChangeType, inserted: Array<PRIKeyType>, updated: Array<PRIKeyType>,
        deleted: Array<PRIKeyType>)
}
```

**功能：** 记录端云同步过程详情。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

### let \`type\`

```cangjie
public let `type`: ChangeType
```

**功能：** 表示发生变化的数据的类型，数据或者资产附件发生变化。

**类型：** [ChangeType](#enum-changetype)

**读写能力：** 只读

**起始版本：** 19

### let deleted

```cangjie
public let deleted: Array<PRIKeyType>
```

**功能：** 记录删除数据的位置，如果该表的主键是String类型，该值是主键的值，否则该值表示删除数据的行号。

**类型：** Array\<[PRIKeyType](#enum-prikeytype)>

**读写能力：** 只读

**起始版本：** 19

### let inserted

```cangjie
public let inserted: Array<PRIKeyType>
```

**功能：** 记录插入数据的位置，如果该表的主键是String类型，该值是主键的值，否则该值表示插入数据的行号。

**类型：** Array\<[PRIKeyType](#enum-prikeytype)>

**读写能力：** 只读

**起始版本：** 19

### let table

```cangjie
public let table: String
```

**功能：** 表示发生变化的表的名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let updated

```cangjie
public let updated: Array<PRIKeyType>
```

**功能：** 记录更新数据的位置，如果该表的主键是String类型，该值是主键的值，否则该值表示更新数据的行号。

**类型：** Array\<[PRIKeyType](#enum-prikeytype)>

**读写能力：** 只读

**起始版本：** 19

### init(String, ChangeType, Array\<PRIKeyType>, Array\<PRIKeyType>, Array\<PRIKeyType>)

```cangjie
public init(table: String, `type`: ChangeType, inserted: Array<PRIKeyType>, updated: Array<PRIKeyType>,
    deleted: Array<PRIKeyType>)
```

**功能：** 构建ChangeInfo。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|table|String|是|-|表示发生变化的表的名称。|
|'type'|[ChangeType](#enum-changetype)|是|-|表示发生变化的数据的类型，数据或者资产附件发生变化。|
|inserted|Array\<[PRIKeyType](#enum-prikeytype)>|是|-|记录插入数据的位置，如果该表的主键是String类型，该值是主键的值，否则该值表示插入数据的行号。|
|updated|Array\<[PRIKeyType](#enum-prikeytype)>|是|-|记录更新数据的位置，如果该表的主键是String类型，该值是主键的值，否则该值表示更新数据的行号。|
|deleted|Array\<[PRIKeyType](#enum-prikeytype)>|是|-|记录删除数据的位置，如果该表的主键是String类型，该值是主键的值，否则该值表示删除数据的行号。|