## class Config

```cangjie
public class Config {
    public var action: Action
    public var url: String
    public var title:?String
    public var description: String
    public var mode: Mode
    public var overwrite: Bool
    public var method:?String
    public var headers: HashMap<String, String>
    public var data:?ConfigData
    public var saveas:String
    public var network: Network
    public var metered: Bool
    public var roaming: Bool
    public var retry: Bool
    public var redirect: Bool
    public var index: UInt32
    public var begins: Int64
    public var ends: Int64
    public var gauge: Bool
    public var precise: Bool
    public var token: ?String
    public var priority: UInt32
    public var extras: HashMap<String, String>

    public init(action: Action, url: String, title!: ?String = None, description!: String = "",
        mode!: Mode = Mode.Background, overwrite!: Bool = false, method!: ?String = None,
        headers!: HashMap<String, String> = HashMap<String, String>(), data!: ?ConfigData = None,  saveas!: String = "./",
        network!: Network = Network.AnyType, metered!: Bool = false, roaming!: Bool = true, retry!: Bool = true,
        redirect!: Bool = true, index!: UInt32 = 0, begins!: Int64 = 0, ends!: Int64 = -1, gauge!: Bool = false,
        precise!: Bool = false,  token!: ?String = None, priority!: UInt32 = 0,extras!: HashMap<String, String> = HashMap<String, String>()
    )
}
```

**功能：** 上传/下载任务的配置信息。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var action

```cangjie
public var action: Action
```

**功能：** 任务操作选项。

UPLOAD表示上传任务。

DOWNLOAD表示下载任务。

**类型：** [Action](#enum-action)

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var begins

```cangjie
public var begins: Int64
```

**功能：** 文件起点，通常情况下用于断点续传。

下载时，请求读取服务器开始下载文件时的起点位置（HTTP协议中设置"Range"选项）。

上传时，读取需上传的文件的起点位置。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var data

```cangjie
public var data:?ConfigData
```

**功能：** 下载时，data为字符串类型，通常情况下使用json格式（object将被转换为json文本）。

上传时，data是表单项数组Array&lt;[FormItem](#class-formitem)&gt;。创建单个任务可以上传最多100个文件。

**类型：** ?[ConfigData](#enum-configdata)

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var description

```cangjie
public var description: String
```

**功能：** 任务的详细信息，其最大长度为1024个字符。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var ends

```cangjie
public var ends: Int64
```

**功能：** 文件终点，通常情况下用于断点续传。默认值为-1，取值为闭区间，表示传输到整个文件末尾结束。

下载时，请求读取服务器开始下载文件时的结束位置（HTTP协议中设置"Range"选项）。

上传时，读取需上传的文件的结束位置。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var extras

```cangjie
public var extras: HashMap<String, String>
```

**功能：** 配置的附加功能。

**类型：** HashMap\<String,String>

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var gauge

```cangjie
public var gauge: Bool
```

**功能：** 后台任务的过程进度通知策略，仅应用于后台任务。

false：代表仅完成或失败的通知。

true：发出每个进度已完成或失败的通知。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22