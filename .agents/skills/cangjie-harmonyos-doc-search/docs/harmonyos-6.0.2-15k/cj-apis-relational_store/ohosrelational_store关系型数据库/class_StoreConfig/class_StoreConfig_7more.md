## class StoreConfig

```cangjie
public class StoreConfig {
    public let name: String
    public let securityLevel: RelationalStoreSecurityLevel
    public let encrypt: Bool
    public let dataGroupId: String
    public let customDir: String
    public let autoCleanDirtyData: Bool
    public init(name: String, securityLevel: RelationalStoreSecurityLevel, encrypt!: Bool = false, dataGroupId!: String = "",
    customDir!: String = "", autoCleanDirtyData!: Bool = true)
}
```

**功能：** 管理关系数据库配置。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

### let autoCleanDirtyData

```cangjie
public let autoCleanDirtyData: Bool
```

**功能：** 指定是否自动清理云端删除后同步到本地的数据，true表示自动清理，false表示手动清理，默认自动清理。对于端云协同的数据库，当云端删除的数据同步到设备端时，可通过该参数设置设备端是否自动清理。手动清理可以通过cleanDirtyData接口清理。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let customDir

```cangjie
public let customDir: String
```

**功能：** 数据库自定义路径。

**使用约束：** 数据库路径大小限制为128字节，如果超过该大小会开库失败，返回错误。

数据库将在如下的目录结构中被创建：context.databaseDir + "/rdb/" + customDir，其中context.databaseDir是应用沙箱对应的路径，"/rdb/"表示创建的是关系型数据库，customDir表示自定义的路径。当此参数不填时，默认在本应用沙箱目录下创建RdbStore实例。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let dataGroupId

```cangjie
public let dataGroupId: String
```

**功能：** 应用组ID，需要向应用市场获取。

**模型约束：** 此属性仅在Stage模型下可用。指定在此dataGroupId对应的沙箱路径下创建RdbStore实例，当此参数不填时，默认在本应用沙箱目录下创建RdbStore实例。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let encrypt

```cangjie
public let encrypt: Bool
```

**功能：** 指定数据库是否加密，默认不加密。true: 加密。false: 非加密。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let name

```cangjie
public let name: String
```

**功能：** 数据库文件名。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let securityLevel

```cangjie
public let securityLevel: RelationalStoreSecurityLevel
```

**功能：** 设置数据库安全级别。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**类型：** [RelationalStoreSecurityLevel](#enum-relationalstoresecuritylevel)

**读写能力：** 只读

**起始版本：** 12