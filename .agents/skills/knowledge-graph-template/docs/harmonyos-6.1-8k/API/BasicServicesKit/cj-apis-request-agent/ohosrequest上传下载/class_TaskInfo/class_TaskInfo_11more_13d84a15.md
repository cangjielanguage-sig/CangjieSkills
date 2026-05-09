## class TaskInfo

```cangjie
public class TaskInfo {
    public let saveas: String
    public let url: String
    public let data: ConfigData
    public let tid: String
    public let title: String
    public let description: String
    public let action: Action
    public let mode: Mode
    public let priority: UInt32
    public let mimeType: String
    public let progress: Progress
    public let gauge: Bool
    public let ctime: UInt64
    public let mtime: UInt64
    public let retry: Bool
    public let tries: UInt32
    public let faults: Faults
    public let reason: String
    public let extras: HashMap<String, String>
}
```

**功能：** 查询结果的任务信息数据结构，提供普通查询和系统查询，两种字段的可见范围不同。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let action

```cangjie
public let action: Action
```

**功能：** 任务操作选项。

Upload表示上传任务。

Download表示下载任务。

**类型：** [Action](#enum-action)

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let ctime

```cangjie
public let ctime: UInt64
```

**功能：** 创建任务的Unix时间戳（毫秒），由当前设备的系统生成。

> **说明：**
>
> 使用[request.agent.search](#func-searchfilter)进行查询时，该值需处于[after,before]区间内才可正常查询到任务id，before和after信息详见[Filter](#class-filter)。

**类型：** UInt64

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let data

```cangjie
public let data: ConfigData
```

**功能：** 任务值。

通过[request.agent.show](#func-showstring)、[request.agent.touch](#func-touchstring-string)进行查询。

**类型：** [ConfigData](#enum-configdata)

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let description

```cangjie
public let description: String
```

**功能：** 任务描述。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let extras

```cangjie
public let extras: HashMap<String, String>
```

**功能：** 任务的额外部分。

**类型：** HashMap\<String,String>

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let faults

```cangjie
public let faults: Faults
```

**功能：** 任务的失败原因。Others表示其他故障。Disconnected表示网络断开连接。Timeout表示任务超时。Protocol表示协议错误。Fsio表示文件系统io错误。

**类型：** [Faults](#enum-faults)

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let gauge

```cangjie
public let gauge: Bool
```

**功能：** 后台任务的进度通知策略。

false：代表仅完成或失败的通知。

true，发出每个进度已完成或失败的通知。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let mimeType

```cangjie
public let mimeType: String
```

**功能：** 任务配置中的mimetype。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let mode

```cangjie
public let mode: Mode
```

**功能：** 任务模式。

Foreground表示前台任务。

Background表示后台任务。

**类型：** [Mode](#enum-mode)

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let mtime

```cangjie
public let mtime: UInt64
```

**功能：** 任务状态改变时的Unix时间戳（毫秒），由当前设备的系统生成。

**类型：** UInt64

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22