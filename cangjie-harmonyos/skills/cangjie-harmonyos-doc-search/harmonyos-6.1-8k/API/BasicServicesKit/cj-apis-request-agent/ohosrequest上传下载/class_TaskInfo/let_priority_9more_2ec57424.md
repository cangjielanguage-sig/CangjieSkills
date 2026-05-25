### let priority

```cangjie
public let priority: UInt32
```

**功能：** 任务配置中的优先级。前端任务的优先级比后台任务高。相同模式的任务，数字越小优先级越高。

**类型：** UInt32

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let progress

```cangjie
public let progress: Progress
```

**功能：** 任务的过程进度。

**类型：** [Progress](#class-progress)

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let reason

```cangjie
public let reason: String
```

**功能：** 等待/失败/停止/暂停任务的原因。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let retry

```cangjie
public let retry: Bool
```

**功能：** 任务的重试开关，仅应用于后台任务。

true：是

false：否

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let saveas

```cangjie
public let saveas: String
```

**功能：** 保存下载文件的路径。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let tid

```cangjie
public let tid: String
```

**功能：** 任务id。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let title

```cangjie
public let title: String
```

**功能：** 任务标题。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let tries

```cangjie
public let tries: UInt32
```

**功能：** 任务的尝试次数。

**类型：** UInt32

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let url

```cangjie
public let url: String
```

**功能：** 任务的url。

通过[request.agent.show](#func-showstring)、[request.agent.touch](#func-touchstring-string)进行查询。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22