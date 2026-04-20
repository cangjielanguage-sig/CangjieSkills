## class Filter

```cangjie
public class Filter {
    public var before:?Int64
    public var after:?Int64
    public var state:?State
    public var action:?Action
    public var mode:?Mode

    public init(before!: ?Int64 = None, after!: ?Int64 = None, state!: ?State = None,
        action!: ?Action = None, mode!: ?Mode = None
    )
}
```

**功能：** 过滤条件。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var action

```cangjie
public var action:?Action
```

**功能：** 任务操作选项。

Upload表示上传任务。

Download表示下载任务。

**类型：** ?[Action](#enum-action)

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var after

```cangjie
public var after:?Int64
```

**功能：** 开始的Unix时间戳（毫秒）。

**类型：** ?Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var before

```cangjie
public var before:?Int64
```

**功能：** 结束的Unix时间戳（毫秒）。

**类型：** ?Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var mode

```cangjie
public var mode:?Mode
```

**功能：** 任务模式。

Foreground表示前台任务。

Background表示后台任务。

**类型：** ?[Mode](#enum-mode)

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var state

```cangjie
public var state:?State
```

**功能：** 指定任务的状态。

**类型：** ?[State](#enum-state)

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### init(?Int64, ?Int64, ?State, ?Action, ?Mode)

```cangjie
public init(before!: ?Int64 = None, after!: ?Int64 = None, state!: ?State = None,
    action!: ?Action = None, mode!: ?Mode = None
)
```

**功能：** 创建Filter对象。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :----- | :-------- | :--- | :----- | :--------- |
| before | ?Int64 | 否   | None   | **命名参数。** 结束的Unix时间戳（毫秒），默认为调用时刻。|
| after  | ?Int64 | 否   | None   | **命名参数。** 开始的Unix时间戳（毫秒），默认值为调用时刻减24小时。|
| state  | ?[State](#enum-state)   | 否   | None   | **命名参数。** 指定任务的状态。如果未填写，则查询所有任务。|
| action | ?[Action](#enum-action) | 否   | None   | **命名参数。** 任务操作选项。如果未填写，则查询所有任务。|
| mode   | ?[Mode](#enum-mode)     | 否   | None   | **命名参数。** 任务模式。如果未填写，则查询所有任务。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

try {
    let filter = Filter(
        state: State.Running,
        action: Action.Download,
        mode: Mode.Background
    )
    Hilog.info(0, "test", "成功创建过滤器对象")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```