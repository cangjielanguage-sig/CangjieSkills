## class StoreConfig

```cangjie
public class StoreConfig {
    public var name: String
    public var securityLevel: RelationalStoreSecurityLevel
    public var encrypt: Bool
    public var dataGroupId: String
    public var customDir: String
    public var rootDir: String
    public var autoCleanDirtyData: Bool
    public var allowRebuild: Bool
    public var vector: Bool
    public var isReadOnly: Bool
    public var pluginLibs: Array<String>
    public var cryptoParam: CryptoParam
    public var tokenizer: Tokenizer
    public var persist: Bool
    public var enableSemanticIndex: Bool

    public init(securityLevel: RelationalStoreSecurityLevel, name!: String = "",
        encrypt!: Bool = false, dataGroupId!: String = "",
        customDir!: String = "", rootDir!: String = "",
        autoCleanDirtyData!: Bool = true, allowRebuild!: Bool = false,
        isReadOnly!: Bool = false, pluginLibs!: Array<String> = Array<String>(),
        cryptoParam!: CryptoParam = CryptoParam([]), vector!: Bool = false,
        tokenizer!: Tokenizer = Tokenizer.NoneTokenizer, persist!: Bool = true,
        enableSemanticIndex!: Bool = false)
}
```

**功能：** 管理关系数据库配置。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### var allowRebuild

```cangjie
public var allowRebuild: Bool
```

**功能：** 指定数据库是否支持异常时自动删除，并重建一个空库空表，true表示自动删除，false表示不自动删除。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### var autoCleanDirtyData

```cangjie
public var autoCleanDirtyData: Bool
```

**功能：** 指定是否自动清理云端删除后同步到本地的数据，true表示自动清理，false表示手动清理。

对于端云协同的数据库，当云端删除的数据同步到设备端时，可通过该参数设置设备端是否自动清理。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**起始版本：** 22

### var cryptoParam

```cangjie
public var cryptoParam: CryptoParam
```

**功能：** 指定用户自定义的加密参数。

**类型：** [CryptoParam](#class-cryptoparam)

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### var customDir

```cangjie
public var customDir: String
```

**功能：** 数据库自定义路径。

使用约束：数据库路径大小限制为128字节，如果超过该大小会开库失败，返回错误。

数据库将在如下的目录结构中被创建：context.databaseDir + "/rdb/" + customDir，其中context.databaseDir是应用沙箱对应的路径，"/rdb/"表示创建的是关系型数据库，customDir表示自定义的路径。当此参数不填时，默认在本应用沙箱目录下创建RdbStore实例。如果同时配置了rootDir参数，将打开或删除如下路径数据库：rootDir + "/" + customDir + "/" + name。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### var dataGroupId

```cangjie
public var dataGroupId: String
```

**功能：** 应用组ID，<!--RP1-->暂不支持指定dataGroupId在对应的沙箱路径下创建RdbStore实例。<!--RP1End-->

dataGroupId共享沙箱的方式不支持多进程访问加密数据库。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### var enableSemanticIndex

```cangjie
public var enableSemanticIndex: Bool
```

**功能：** 指定数据库是否启用语义索引处理功能。true表示启用语义索引处理功能，false表示不启用。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22