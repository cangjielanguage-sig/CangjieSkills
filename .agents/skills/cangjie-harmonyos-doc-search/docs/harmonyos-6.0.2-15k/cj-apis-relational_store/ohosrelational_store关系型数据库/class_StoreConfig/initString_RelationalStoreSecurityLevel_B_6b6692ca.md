### init(String, RelationalStoreSecurityLevel, Bool, String, String, Bool)

```cangjie
public init(name: String, securityLevel: RelationalStoreSecurityLevel, encrypt!: Bool = false, dataGroupId!: String = "",
customDir!: String = "", autoCleanDirtyData!: Bool = true)
```

**功能：** 构建StoreConfig。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|数据库文件名。<br/>**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core|
|securityLevel|[RelationalStoreSecurityLevel](#enum-relationalstoresecuritylevel)|是|-|设置数据库安全级别。<br/>**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core|
|encrypt|Bool|否|false| **命名参数。** 指定数据库是否加密，默认不加密。<br/> true: 加密。<br/> false: 非加密。<br/>**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core|
|dataGroupId|String|否|""| **命名参数。** 应用组ID，需要向应用市场获取。<br/>**模型约束：** 此属性仅在Stage模型下可用。<br/>指定在此dataGroupId对应的沙箱路径下创建RdbStore实例，当此参数不填时，默认在本应用沙箱目录下创建RdbStore实例。<br/>**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core|
|customDir|String|否|""|数据库自定义路径。<br/>**使用约束：** 数据库路径大小限制为128字节，如果超过该大小会开库失败，返回错误。<br/>数据库将在如下的目录结构中被创建：context.databaseDir + "/rdb/" + customDir，其中context.databaseDir是应用沙箱对应的路径，"/rdb/"表示创建的是关系型数据库，customDir表示自定义的路径。当此参数不填时，默认在本应用沙箱目录下创建RdbStore实例。<br/>**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core|
|autoCleanDirtyData|Bool|否|true| **命名参数。** 指定是否自动清理云端删除后同步到本地的数据，true表示自动清理，false表示手动清理，默认自动清理。<br/>对于端云协同的数据库，当云端删除的数据同步到设备端时，可通过该参数设置设备端是否自动清理。手动清理可以通过cleanDirtyData接口清理。<br/>**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client|