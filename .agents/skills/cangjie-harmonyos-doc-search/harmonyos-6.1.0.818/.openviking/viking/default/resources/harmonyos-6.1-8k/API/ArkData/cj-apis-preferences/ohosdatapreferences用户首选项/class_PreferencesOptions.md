## class PreferencesOptions

```cangjie
public class PreferencesOptions {
    public var name: String
    public var dataGroupId: String
    public var storageType: StorageType
    public init(name: String, dataGroupId!: String = String.empty,
        storageType!: StorageType = StorageType.Xml)
}
```

**功能：** Preferences实例配置选项。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

### var dataGroupId

```cangjie
public var dataGroupId: String
```

**功能：** 应用组ID，<!--RP1-->暂不支持指定dataGroupId在对应共享沙箱路径下创建Preferences实例。<!--RP1End-->

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

### var name

```cangjie
public var name: String
```

**功能：** Preferences实例的名称。名称长度需大于零且小于等于255字节，名称中不能包含'/'且不能以'/'结尾。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

### var storageType

```cangjie
public var storageType: StorageType
```

**功能：** 存储模式。表示当前Preferences实例需要使用的存储模式。当选择某种存储模式创建Preferences后，不支持中途切换存储模式。

**类型：** [StorageType](#enum-storagetype)

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

### init(String, String, StorageType)

```cangjie
public init(name: String, dataGroupId!: String = String.empty,
    storageType!: StorageType = StorageType.Xml)
```

**功能：** 用于创建PreferencesOptions实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|Preferences实例的名称。名称长度需大于零且小于等于255字节，名称中不能包含'/'且不能以'/'结尾。|
|dataGroupId|String|否|String.empty|**命名参数。** 应用组ID，为可选参数。|
|storageType|[StorageType](#enum-storagetype)|否|StorageType.Xml|**命名参数。** 存储模式。表示当前Preferences实例需要使用的存储模式。当选择某种存储模式创建Preferences后，不支持中途切换存储模式。|