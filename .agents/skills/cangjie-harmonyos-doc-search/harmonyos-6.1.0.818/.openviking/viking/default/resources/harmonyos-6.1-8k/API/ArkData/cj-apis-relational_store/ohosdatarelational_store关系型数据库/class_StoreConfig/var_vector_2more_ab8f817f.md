### var vector

```cangjie
public var vector: Bool
```

**功能：** 指定数据库是否是向量数据库，true表示向量数据库，false表示关系型数据库。

向量数据库适用于存储和处理高维向量数据，关系型数据库适用于存储和处理结构化数据。

当使用向量数据库时，在调用deleteRdbStore接口前，应当确保向量数据库已打开的RdbStore和ResultSet均已成功关闭。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### init(RelationalStoreSecurityLevel, String, Bool, String, String, String, Bool, Bool, Bool, Array\<String>, CryptoParam, Bool, Tokenizer, Bool, Bool)

```cangjie
public init(securityLevel: RelationalStoreSecurityLevel, name!: String = "",
    encrypt!: Bool = false, dataGroupId!: String = "",
    customDir!: String = "", rootDir!: String = "",
    autoCleanDirtyData!: Bool = true, allowRebuild!: Bool = false,
    isReadOnly!: Bool = false, pluginLibs!: Array<String> = Array<String>(),
    cryptoParam!: CryptoParam = CryptoParam([]), vector!: Bool = false,
    tokenizer!: Tokenizer = Tokenizer.NoneTokenizer, persist!: Bool = true,
    enableSemanticIndex!: Bool = false)
```

**功能：** StoreConfig类的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|securityLevel|[RelationalStoreSecurityLevel](#enum-relationalstoresecuritylevel)|是|-|设置数据库安全级别。|
|name|String|否|""|数据库文件名，也是数据库唯一标识符。|
|encrypt|Bool|否|false|指定数据库是否加密，默认不加密。|
|dataGroupId|String|否|""|应用组ID，<!--RP1-->暂不支持指定dataGroupId在对应的沙箱路径下创建RdbStore实例。<!--RP1End-->|
|customDir|String|否|""|数据库自定义路径。|
|rootDir|String|否|""|指定数据库根路径。|
|autoCleanDirtyData|Bool|否|true|指定是否自动清理云端删除后同步到本地的数据，true表示自动清理，false表示手动清理，默认自动清理。|
|allowRebuild|Bool|否|false|指定数据库是否支持异常时自动删除，并重建一个空库空表，默认不删除。|
|isReadOnly|Bool|否|false|指定数据库是否只读，默认为数据库可读写。|
|pluginLibs|Array\<String>|否|Array\<String>()|表示包含有fts（Full-Text Search，即全文搜索引擎）等能力的动态库名的数组。|
|cryptoParam|[CryptoParam](#class-cryptoparam)|否|CryptoParam([])|指定用户自定义的加密参数。|
|vector|Bool|否|false|指定数据库是否是向量数据库，true表示向量数据库，false表示关系型数据库，默认为false。|
|tokenizer|[Tokenizer](#enum-tokenizer)|否|Tokenizer.NoneTokenizer|指定用户在fts场景下使用哪种分词器。|
|persist|Bool|否|true|指定数据库是否需要持久化。true表示持久化，false表示不持久化，即内存数据库。默认为true。|
|enableSemanticIndex|Bool|否|false|指定数据库是否启用语义索引处理功能。true表示启用语义索引处理功能，false表示不启用。默认为false。|