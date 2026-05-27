## class KVOptions

```cangjie
public class KVOptions {
    public init (securityLevel: SecurityLevel, createIfMissing!: Bool = true, encrypt!: Bool = false,
        backup!: Bool = true, autoSync!: Bool = false, schema!: Schema = Schema())
}
```

**功能：** 用于提供创建数据库的配置信息。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

### init(SecurityLevel, Bool, Bool, Bool, Bool, Schema)

```cangjie
public init (securityLevel: SecurityLevel, createIfMissing!: Bool = true, encrypt!: Bool = false,
    backup!: Bool = true, autoSync!: Bool = false, schema!: Schema = Schema())
```

**功能：** 用于创建KVOptions实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|securityLevel|[SecurityLevel](cj-apis-relational_store.md#enum-relationalstoresecuritylevel)|是|-|设置数据库安全级别。<br>**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core|
|createIfMissing|Bool|否|true|当数据库文件不存在时是否创建数据库，默认为true，即创建。<br>**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core|
|encrypt|Bool|否|false|设置数据库文件是否加密，默认为false，即不加密。<br>**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core|
|backup|Bool|否|true|设置数据库文件是否备份，默认为true，即备份。 <br>**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core|
|autoSync|Bool|否|false|设置数据库文件是否自动同步。默认为false，即手动同步。<br>**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core<br>**需要权限**： ohos.permission.DISTRIBUTED_DATASYNC|
|schema|[Schema](#struct-schema)|否|Schema()|设置定义存储在数据库中的值，默认为undefined，即不使用Schema。<br>**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore|