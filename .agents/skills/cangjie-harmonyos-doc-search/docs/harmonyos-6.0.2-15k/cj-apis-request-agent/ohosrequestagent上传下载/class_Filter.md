## class Filter

```cangjie
public class Filter {
    public Filter (
        var bundle!: ?String = None,
        public var before!: ?Int64 = None,
        public var after!: ?Int64 = None,
        public var state!: ?State = None,
        public var action!: ?Action = None,
        public var mode!: ?Mode = None
    )
}
```

**功能：** 过滤条件。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

### var action

```cangjie
public var action: ?Action = None
```

**功能：** 任务操作选项。UPLOAD表示上传任务。DOWNLOAD表示下载任务。

**类型：** ?[Action](#enum-action)

**读写能力：** 可读写

**起始版本：** 12

### var after

```cangjie
public var after: ?Int64 = None
```

**功能：** 开始的Unix时间戳（毫秒），默认值为调用时刻减24小时。

**类型：** ?Int64

**读写能力：** 可读写

**起始版本：** 12

### var before

```cangjie
public var before: ?Int64 = None
```

**功能：** 结束的Unix时间戳（毫秒），默认为调用时刻。

**类型：** ?Int64

**读写能力：** 可读写

**起始版本：** 12

### var mode

```cangjie
public var mode: ?Mode = None
```

**功能：** 任务模式。FOREGROUND表示前端任务。BACKGROUND表示后台任务。如果未填写，则查询所有任务。

**类型：** ?[Mode](#enum-mode)

**读写能力：** 可读写

**起始版本：** 12

### var state

```cangjie
public var state: ?State = None
```

**功能：** 指定任务的状态。

**类型：** ?[State](#enum-state)

**读写能力：** 可读写

**起始版本：** 12

### Filter(?String, ?Int64, ?Int64, ?State, ?Action, ?Mode)

```cangjie
public Filter (
    var bundle!: ?String = None,
    public var before!: ?Int64 = None,
    public var after!: ?Int64 = None,
    public var state!: ?State = None,
    public var action!: ?Action = None,
    public var mode!: ?Mode = None
)
```

**功能：** 创建Filter对象。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bundle|?String|否|None| **命名参数。** 应用程序的包名。|
|before|?Int64|否|None| **命名参数。** 结束的Unix时间戳（毫秒），默认为调用时刻。|
|after|?Int64|否|None| **命名参数。** 开始的Unix时间戳（毫秒），默认值为调用时刻减24小时。 |
|state|?[State](#enum-state)|否|None| **命名参数。** 指定任务的状态。|
|action|?[Action](#enum-action)|否|None| **命名参数。** 任务操作选项。<br>-UPLOAD表示上传任务。<br>-DOWNLOAD表示下载任务。|
|mode|?[Mode](#enum-mode)|否|None| **命名参数。** 任务模式。<br>-FOREGROUND表示前端任务。<br>-BACKGROUND表示后台任务。<br>-如果未填写，则查询所有任务。|