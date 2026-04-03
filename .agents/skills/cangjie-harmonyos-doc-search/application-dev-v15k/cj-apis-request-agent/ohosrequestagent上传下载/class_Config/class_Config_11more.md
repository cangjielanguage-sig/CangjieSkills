## class Config

```cangjie
public class Config {
    public Config(
        public var action!: Action,
        public var url!: String,
        public var title!: ?String = None,
        public var description!: ?String = None,
        public var mode!: ?Mode = None,
        public var overwrite!: Bool = false,
        public var method!: ?String= None,
        public var headers!: ?HashMap<String, String> = None,
        public var data!: ?ConfigDataType = None,
        public var saveas!: ?String = None,
        public var network!: Network = Network.ANY,
        public var metered!: Bool = false,
        public var roaming!: Bool = true,
        public var retry!: Bool = true,
        public var redirect!: Bool = true,
        public var index!: UInt32 = 0,
        public var begins!: Int64 = 0,
        public var ends!: Int64 = -1,
        public var gauge!: Bool = false,
        public var precise!: Bool = false,
        public var token!: ?String = None,
        public var priority!: UInt32 = 0,
        public var extras!: ?HashMap<String, String> = None
    )
}
```

**功能：** 上传/下载任务的配置信息。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

### var action

```cangjie
public var action: Action
```

**功能：** 任务操作选项，UPLOAD表示上传任务，DOWNLOAD表示下载任务。

**类型：** [Action](#enum-action)

**读写能力：** 可读写

**起始版本：** 12

### var begins

```cangjie
public var begins: Int64 = 0
```

**功能：** 文件起点，通常用于断点续传。默认值为0，取值为闭区间。下载时，请求读取服务器开始下载文件时的起点位置（http协议中设置"Range"选项）。上传时，在上传开始时读取。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 12

### var data

```cangjie
public var data: ?ConfigDataType = None
```

**功能：** 下载时，data为字符串类型，通常使用json(object将被转换为json文本)，默认为空。上传时，data是表单项数组Array\<FormItem>，默认为空。

**类型：** ?[ConfigDataType](#enum-configdatatype)

**读写能力：** 可读写

**起始版本：** 12

### var description

```cangjie
public var description: ?String = None
```

**功能：** 任务的详细信息，其最大长度为1024个字符，默认值为空字符串。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 12

### var ends

```cangjie
public var ends: Int64 = -1
```

**功能：** 文件终点，通常用于断点续传。默认值为-1，取值为闭区间。下载时，请求读取服务器开始下载文件时的结束位置（http协议中设置"Range"选项）。上传时，在上传时结束读取。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 12

### var extras

```cangjie
public var extras: ?HashMap<String, String> = None
```

**功能：** 配置的附加功能，默认为空。

**类型：** ?HashMap&lt;String, String&gt;

**读写能力：** 可读写

**起始版本：** 12

### var gauge

```cangjie
public var gauge: Bool = false
```

**功能：** 后台任务的过程进度通知策略，仅应用于后台任务，默认值为false。false：代表仅完成或失败的通知。true：发出每个进度已完成或失败的通知。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 12

### var headers

```cangjie
public var headers: ?HashMap<String, String> = None
```

**功能：** 添加要包含在任务中的HTTP协议标志头。对于上传请求，默认的Content-Type为"multipart/form-data"。对于下载请求，默认的Content-Type为"application/json"。

**类型：** ?HashMap&lt;String, String&gt;

**读写能力：** 可读写

**起始版本：** 12

### var index

```cangjie
public var index: UInt32 = 0
```

**功能：** 任务的路径索引，通常用于任务断点续传，默认为0。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 12

### var metered

```cangjie
public var metered: Bool = false
```

**功能：** 是否允许在按流量计费的网络中工作，默认为false。true：是。false：否。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 12