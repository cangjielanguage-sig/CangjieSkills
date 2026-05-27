## struct DistributedConfig

```cangjie
public struct DistributedConfig {
    public let autoSync: Bool
    public init(autoSync: Bool)
}
```

**功能：** 记录表的分布式配置信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

### let autoSync

```cangjie
public let autoSync: Bool
```

**功能：** 是否支持自动同步。

- 该值为true时，表示该表支持自动同步和手动同步。
- 该值为false时，表示该表只支持手动同步，不支持自动同步。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### init(Bool)

```cangjie
public init(autoSync: Bool)
```

**功能：** 构建DistributedConfig。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|autoSync|Bool|是|-|是否支持自动同步。该值为true时，表示该表支持自动同步和手动同步；该值为false时，表示该表只支持手动同步，不支持自动同步。|

## struct ProgressDetails

```cangjie
public struct ProgressDetails {
    public let schedule: Progress
    public let code: ProgressCode
    public let details: Map<String, TableDetails>
    public init(schedule: Progress, code: ProgressCode, details: Map<String, TableDetails>)
}
```

**功能：** 描述数据库整体执行端云同步任务上传和下载的统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

### let code

```cangjie
public let code: ProgressCode
```

**功能：** 表示端云同步过程的状态。

**类型：** [ProgressCode](#enum-progresscode)

**读写能力：** 只读

**起始版本：** 19

### let details

```cangjie
public let details: Map<String, TableDetails>
```

**功能：** 表示端云同步各表的统计信息。键表示表名，值表示该表的端云同步过程统计信息。

**类型：** Map\<String, [TableDetails](#struct-tabledetails)>

**读写能力：** 只读

**起始版本：** 19

### let schedule

```cangjie
public let schedule: Progress
```

**功能：** 表示端云同步过程。

**类型：** [Progress](#enum-progress)

**读写能力：** 只读

**起始版本：** 19

### init(Progress, ProgressCode, Map\<String, TableDetails>)

```cangjie
public init(schedule: Progress, code: ProgressCode, details: Map<String, TableDetails>)
```

**功能：** 构建ProgressDetails。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|schedule|[Progress](#enum-progress)|是|-|表示端云同步过程。|
|code|[ProgressCode](#enum-progresscode)|是|-|表示端云同步过程的状态。|
|details|Map\<String, [TableDetails](#struct-tabledetails)>|是|-|表示端云同步各表的统计信息。键表示表名，值表示该表的端云同步过程统计信息。|