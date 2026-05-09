## class KVOptions

```cangjie
public class KVOptions {
    public var createIfMissing: Bool
    public var encrypt: Bool
    public var backup: Bool
    public var autoSync: Bool
    public var securityLevel: KVSecurityLevel
    public var schema:?Schema

    public init(securityLevel: KVSecurityLevel, createIfMissing!: Bool = true, encrypt!: Bool = false,
        backup!: Bool = true, autoSync!: Bool = false, schema!: ?Schema = None)
}
```

**功能：** 用于提供创建数据库的配置信息。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### var autoSync

```cangjie
public var autoSync: Bool
```

**功能：** 设置数据库文件是否自动同步。默认为false，即手动同步。配置为true，<!--RP1-->即只支持在跨设备Call调用实现的多端协同中生效，其他场景无法生效。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### var backup

```cangjie
public var backup: Bool
```

**功能：** 设置数据库文件是否备份，true为备份，false为不备份，默认为true。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### var createIfMissing

```cangjie
public var createIfMissing: Bool
```

**功能：** 当数据库文件不存在时是否创建数据库，true为创建，false为不创建，默认为true。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### var encrypt

```cangjie
public var encrypt: Bool
```

**功能：** 设置数据库文件是否加密，true为加密，false为不加密，默认为false。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### var schema

```cangjie
public var schema:?Schema
```

**功能：** 置定义存储在数据库中的值，默认为None，即不使用Schema。

**类型：** ?[Schema](#class-schema)

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 22

### var securityLevel

```cangjie
public var securityLevel: KVSecurityLevel
```

**功能：** 设置数据库安全级别。

**类型：** [KVSecurityLevel](#enum-kvsecuritylevel)

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### init(KVSecurityLevel, Bool, Bool, Bool, Bool, ?Schema)

```cangjie
public init(securityLevel: KVSecurityLevel, createIfMissing!: Bool = true, encrypt!: Bool = false,
    backup!: Bool = true, autoSync!: Bool = false, schema!: ?Schema = None)
```

**功能：** 用于创建KVOptions实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|securityLevel|[KVSecurityLevel](#enum-kvsecuritylevel)|是|-|设置数据库安全级别。|
|createIfMissing|Bool|否|true|**命名参数。** 当数据库文件不存在时是否创建数据库，true为创建，false为不创建，默认为true。|
|encrypt|Bool|否|false|**命名参数。** 设置数据库文件是否加密，true为加密，false为不加密，默认为false。|
|backup|Bool|否|true|**命名参数。** 设置数据库文件是否备份，true为备份，false为不备份，默认为true。|
|autoSync|Bool|否|false|**命名参数。** 设置数据库是否支持跨设备自动同步。默认为false，即只支持手动同步。|
|schema|?[Schema](#class-schema)|否|None|**命名参数。** 设置定义存储在数据库中的值，默认为None，即不使用Schema。|