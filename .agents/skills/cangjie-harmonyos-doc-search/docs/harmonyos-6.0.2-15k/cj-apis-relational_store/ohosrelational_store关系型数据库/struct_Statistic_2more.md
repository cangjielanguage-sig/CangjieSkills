## struct Statistic

```cangjie
public struct Statistic {
    public let total: UInt32
    public let successful: UInt32
    public let failed: UInt32
    public let remained: UInt32
    public init(total: UInt32, successful: UInt32, failed: UInt32, remained: UInt32)
}
```

**功能：** 描述数据库表的端云同步过程的统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

### let failed

```cangjie
public let failed: UInt32
```

**功能：** 表示数据库表中端云同步失败的行数。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let remained

```cangjie
public let remained: UInt32
```

**功能：** 表示数据库表中端云同步剩余未执行的行数。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let successful

```cangjie
public let successful: UInt32
```

**功能：** 表示数据库表中端云同步成功的行数。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let total

```cangjie
public let total: UInt32
```

**功能：** 表示数据库表中需要端云同步的总行数。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### init(UInt32, UInt32, UInt32, UInt32)

```cangjie
public init(total: UInt32, successful: UInt32, failed: UInt32, remained: UInt32)
```

**功能：** 描述数据库表的端云同步过程的统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|total|UInt32|是|-|表示数据库表中需要端云同步的总行数。|
|successful|UInt32|是|-|表示数据库表中端云同步成功的行数。|
|failed|UInt32|是|-|表示数据库表中端云同步失败的行数。|
|remained|UInt32|是|-|表示数据库表中端云同步剩余未执行的行数。|

## struct TableDetails

```cangjie
public struct TableDetails {
    public let upload: Statistic
    public let download: Statistic
    public init(upload: Statistic, download: Statistic)
}
```

**功能：** 描述数据库表执行端云同步任务上传和下载的统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

### let download

```cangjie
public let download: Statistic
```

**功能：** 表示数据库表中端云同步下载过程的统计信息。

**类型：** [Statistic](#struct-statistic)

**读写能力：** 只读

**起始版本：** 19

### let upload

```cangjie
public let upload: Statistic
```

**功能：** 表示数据库表中端云同步上传过程的统计信息。

**类型：** [Statistic](#struct-statistic)

**读写能力：** 只读

**起始版本：** 19

### init(Statistic, Statistic)

```cangjie
public init(upload: Statistic, download: Statistic)
```

**功能：** 构建TableDetails。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|upload|[Statistic](#struct-statistic)|是|-|表示数据库表中端云同步上传过程的统计信息。|
|download|[Statistic](#struct-statistic)|是|-|表示数据库表中端云同步下载过程的统计信息。|