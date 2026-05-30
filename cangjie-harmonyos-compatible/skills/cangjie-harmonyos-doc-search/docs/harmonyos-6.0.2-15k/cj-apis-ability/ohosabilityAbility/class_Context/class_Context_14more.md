## class Context

```cangjie
public open class Context {
    public let eventhub = EventHub()
}
```

**功能：** 提供ability或application的上下文的能力。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### prop applicationInfo

```cangjie
public prop applicationInfo: ApplicationInfo
```

**功能：** 当前应用程序的信息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [ApplicationInfo](./cj-apis-bundle_manager.md#struct-applicationinfo)

**读写能力：** 只读

**起始版本：** 19

### prop area

```cangjie
public prop area: AreaMode
```

**功能：** 文件分区信息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [AreaMode](#enum-areamode)

**读写能力：** 只读

**起始版本：** 19

### prop bundleCodeDir

```cangjie
public prop bundleCodeDir: String
```

**功能：** 安装包目录。不能拼接路径访问资源文件，请使用[资源管理接口](../LocalizationKit/cj-apis-resource_manager.md#ohosresource_manager资源管理)访问资源。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop cacheDir

```cangjie
public prop cacheDir: String
```

**功能：** 缓存目录。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop cloudFileDir

```cangjie
public prop cloudFileDir: String
```

**功能：** 云文件目录。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop databaseDir

```cangjie
public prop databaseDir: String
```

**功能：** 数据库目录。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop distributedFilesDir

```cangjie
public prop distributedFilesDir: String
```

**功能：** 分布式文件目录。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop filesDirectory

```cangjie
public prop filesDirectory: String
```

**功能：** 文件目录。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop preferencesDir

```cangjie
public prop preferencesDir: String
```

**功能：** preferences目录。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop resourceDir

```cangjie
public prop resourceDir: String
```

**功能：** 资源目录。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop resourceManager

```cangjie
public prop resourceManager: ResourceManager
```

**功能：** 资源管理对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [ResourceManager](../LocalizationKit/cj-apis-resource_manager.md#class-resourcemanager)

**读写能力：** 只读

**起始版本：** 19

### prop tempDir

```cangjie
public prop tempDir: String
```

**功能：** 临时目录。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let eventhub

```cangjie
public let eventhub = EventHub()
```

**功能：** 事件中心，提供订阅、取消订阅、触发事件对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [EventHub](./cj-apis-eventhub.md#ohoseventhub)

**读写能力：** 只读

**起始版本：** 12