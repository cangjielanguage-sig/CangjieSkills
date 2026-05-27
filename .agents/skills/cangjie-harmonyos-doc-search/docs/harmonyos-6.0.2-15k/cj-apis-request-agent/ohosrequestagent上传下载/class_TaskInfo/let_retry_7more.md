### let retry

```cangjie
public let retry: Bool
```

**功能：** 任务的重试开关，仅应用于后台任务。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 15

### let saveas

```cangjie
public let saveas: ?String = None
```

**功能：** 保存下载文件的路径。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 15

### let tid

```cangjie
public let tid: String
```

**功能：** 任务id。

**类型：** String

**读写能力：** 只读

**起始版本：** 15

### let title

```cangjie
public let title: String
```

**功能：** 任务标题。

**类型：** String

**读写能力：** 只读

**起始版本：** 15

### let tries

```cangjie
public let tries: UInt32
```

**功能：** 任务的尝试次数。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 15

### let url

```cangjie
public let url: ?String = None
```

**功能：** 任务的url。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 15

### init(?String, ?String, ?String, ?String, ?ConfigDataType, String, String, String, Action, Mode, UInt32, String, Progress, Bool, UInt64, UInt64, Bool, UInt32, String, ?Faults, ?HashMap\<String, String>)

```cangjie
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
```

**功能：** 创建TaskInfo对象。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|uid|?String|否|None| **命名参数。** 任务uid。|
|bundle|?String|否|None| **命名参数。** 应用程序的包名。|
|saveas|?String|否|None| **命名参数。** 保存下载文件的路径。|
|url|?String|否|None| **命名参数。** 任务的url。|
|data|?[ConfigDataType](#enum-configdatatype)|否|None| **命名参数。** 任务值。|
|tid|String|是|-| **命名参数。** 任务id。|
|title|String|是|-| **命名参数。** 任务标题。|
|description|String|是|-| **命名参数。** 任务描述。|
|action|[Action](#enum-action)|是|-| **命名参数。** 任务操作选项。<br>-UPLOAD表示上传任务。<br>-DOWNLOAD表示下载任务。|
|mode|[Mode](#enum-mode)|是|-| **命名参数。** 指定任务模式。<br>-FOREGROUND表示前端任务。<br>-BACKGROUND表示后台任务。|
|priority|UInt32|是|-| **命名参数。** 任务配置中的优先级。前端任务的优先级比后台任务高。相同模式的任务，数字越小优先级越高。|
|mimeType|String|是|-| **命名参数。** 任务配置中的mimetype。|
|progress|[Progress](#class-progress)|是|-| **命名参数。** 任务的过程进度。|
|gauge|Bool|是|-| **命名参数。** 后台任务的进度通知策略。|
|ctime|UInt64|是|-| **命名参数。** 创建任务的Unix时间戳（毫秒），由当前设备的系统生成。|
|mtime|UInt64|是|-| **命名参数。** 任务状态改变时的Unix时间戳（毫秒），由当前设备的系统生成。|
|retry|Bool|是|-| **命名参数。** 任务的重试开关，仅应用于后台任务。|
|tries|UInt32|是|-| **命名参数。** 任务的尝试次数。|
|reason|String|是|-| **命名参数。** 等待/失败/停止/暂停任务的原因。|
|faults|?[Faults](#enum-faults)|是|-| **命名参数。** 任务的失败原因。<br>-OTHERS表示其他故障。<br>-DISCONNECT表示网络断开连接。<br>-TIMEOUT表示任务超时。<br>-PROTOCOL表示协议错误。<br>-FSIO表示文件系统io错误。|
|extras|?HashMap\<String, String>|是|-| **命名参数。** 任务的额外部分。|