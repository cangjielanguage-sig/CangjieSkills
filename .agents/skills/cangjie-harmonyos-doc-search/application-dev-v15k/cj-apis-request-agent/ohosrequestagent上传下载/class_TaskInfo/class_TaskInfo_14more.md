## class TaskInfo

```cangjie
public class TaskInfo {
    public let uid: ?String
    public let bundle: ?String
    public let saveas: ?String
    public let url: ?String
    public let data: ?ConfigDataType
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
    public let faults: ?Faults
    public let reason: String
    public let extras: ?HashMap<String, String>

    public init(
        uid!: ?String = None,
        bundle!: ?String = None,
        saveas!: ?String = None,
        url!: ?String = None,
        data!: ?ConfigDataType = None,
        tid!: String,
        title!: String,
        description!: String,
        action!: Action,
        mode!: Mode,
        priority!: UInt32,
        mimeType!: String,
        progress!: Progress,
        gauge!: Bool,
        ctime!: UInt64,
        mtime!: UInt64,
        retry!: Bool,
        tries!: UInt32,
        reason!: String,
        faults!: ?Faults,
        extras!: ?HashMap<String, String>
    )
}
```

**功能：** 查询结果的任务信息数据结构，提供普通查询和系统查询，两种字段的可见范围不同。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 15

### let action

```cangjie
public let action: Action
```

**功能：** 任务操作选项。UPLOAD表示上传任务。DOWNLOAD表示下载任务。

**类型：** [Action](#enum-action)

**读写能力：** 只读

**起始版本：** 15

### let ctime

```cangjie
public let ctime: UInt64
```

**功能：** 创建任务的Unix时间戳（毫秒），由当前设备的系统生成。

**类型：** UInt64

**读写能力：** 只读

**起始版本：** 15

### let data

```cangjie
public let data: ?ConfigDataType = None
```

**功能：** 任务值。

**类型：** ?[ConfigDataType](#enum-configdatatype)

**读写能力：** 只读

**起始版本：** 15

### let description

```cangjie
public let description: String
```

**功能：** 任务描述。

**类型：** String

**读写能力：** 只读

**起始版本：** 15

### let extras

```cangjie
public let extras: ?HashMap<String, String>
```

**功能：** 任务的额外部分。

**类型：** ?HashMap\<String, String>

**读写能力：** 只读

**起始版本：** 15

### let faults

```cangjie
public let faults: ?Faults
```

**功能：** 任务的失败原因。OTHERS表示其他故障。DISCONNECT表示网络断开连接。TIMEOUT表示任务超时。PROTOCOL表示协议错误。FSIO表示文件系统io错误。

**类型：** ?[Faults](#enum-faults)

**读写能力：** 只读

**起始版本：** 15

### let gauge

```cangjie
public let gauge: Bool
```

**功能：** 后台任务的进度通知策略。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 15

### let mimeType

```cangjie
public let mimeType: String
```

**功能：** 任务配置中的mimetype。

**类型：** String

**读写能力：** 只读

**起始版本：** 15

### let mode

```cangjie
public let mode: Mode
```

**功能：** 指定任务模式。FOREGROUND表示前端任务。BACKGROUND表示后台任务。

**类型：** [Mode](#enum-mode)

**读写能力：** 只读

**起始版本：** 15

### let mtime

```cangjie
public let mtime: UInt64
```

**功能：** 任务状态改变时的Unix时间戳（毫秒），由当前设备的系统生成。

**类型：** UInt64

**读写能力：** 只读

**起始版本：** 15

### let priority

```cangjie
public let priority: UInt32
```

**功能：** 任务配置中的优先级。前端任务的优先级比后台任务高。相同模式的任务，数字越小优先级越高。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 15

### let progress

```cangjie
public let progress: Progress
```

**功能：** 任务的过程进度。

**类型：** [Progress](#class-progress)

**读写能力：** 只读

**起始版本：** 15

### let reason

```cangjie
public let reason: String
```

**功能：** 等待/失败/停止/暂停任务的原因。

**类型：** String

**读写能力：** 只读

**起始版本：** 15