## enum State

```cangjie
public enum State <: ToString {
    | Initialized
    | Waiting
    | Running
    | Retrying
    | Paused
    | Stopped
    | Completed
    | Failed
    | Removed
    | ...
}
```

**功能：** 定义任务当前的状态。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**父类型：**

- ToString

### Completed

```cangjie
Completed
```

**功能：** 表示任务完成。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Failed

```cangjie
Failed
```

**功能：** 表示任务失败。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Initialized

```cangjie
Initialized
```

**功能：** 表示通过配置信息（[Config](#class-config)）创建的任务已初始化。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Paused

```cangjie
Paused
```

**功能：** 表示任务暂停，通常后续会恢复任务。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Removed

```cangjie
Removed
```

**功能：** 表示任务移除。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Retrying

```cangjie
Retrying
```

**功能：** 表示任务至少失败一次，现在正在再次处理中。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Running

```cangjie
Running
```

**功能：** 表示任务正在运行中。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Stopped

```cangjie
Stopped
```

**功能：** 表示任务停止。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Waiting

```cangjie
Waiting
```

**功能：** 表示任务缺少运行或重试的资源，又或是网络状态不匹配。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**返回值：**

| 类型   | 说明                       |
| :----- | :------------------------- |
| String | 获取当前枚举的字符串表示。 |