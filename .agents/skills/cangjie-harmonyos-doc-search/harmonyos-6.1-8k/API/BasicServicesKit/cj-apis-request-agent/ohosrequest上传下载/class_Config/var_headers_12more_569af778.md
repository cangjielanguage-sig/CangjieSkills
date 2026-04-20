### var headers

```cangjie
public var headers: HashMap<String, String>
```

**功能：** 添加要包含在任务中的HTTP协议标志头。

上传请求，默认的Content-Type为"multipart/form-data"。

下载请求，默认的Content-Type为"application/json"。

**类型：** HashMap

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var index

```cangjie
public var index: UInt32
```

**功能：** 任务的路径索引，通常情况下用于任务断点续传。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var metered

```cangjie
public var metered: Bool
```

**功能：** 是否允许在按流量计费的网络中工作。

true：是

false：否

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var method

```cangjie
public var method:?String
```

**功能：** 上传或下载HTTP的标准方法，包括GET、POST和PUT，不区分大小写。

上传时，使用PUT或POST，默认值为PUT。

下载时，使用GET或POST，默认值为GET。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var mode

```cangjie
public var mode: Mode
```

**功能：** 任务模式，默认为后台任务。下载到用户文件场景必须为Mode.Foreground。

**类型：** [Mode](#enum-mode)

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var network

```cangjie
public var network: Network
```

**功能：** 网络选项，当前支持无线网络Wifi和蜂窝数据网络Cellular。

**类型：** [Network](#enum-network)

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var overwrite

```cangjie
public var overwrite: Bool
```

**功能：** 下载过程中路径已存在时的解决方案选择。

true，覆盖已存在的文件。

false，下载失败。

下载到用户文件场景必须为true。

设置为 `true` 时，不建议创建多个任务同时往同一个文件下载内容，会导致文件内容混乱。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var precise

```cangjie
public var precise: Bool
```

**功能：** 如果设置为true，在上传/下载无法获取文件大小时任务失败。

如果设置为false，将文件大小设置为-1时任务继续。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var priority

```cangjie
public var priority: UInt32
```

**功能：** 任务的优先级。前台任务的优先级比后台任务高。任务模式相同的情况下，该配置项的数字越小优先级越高。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var redirect

```cangjie
public var redirect: Bool
```

**功能：** 是否允许重定向。

true：是

false：否

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var retry

```cangjie
public var retry: Bool
```

**功能：** 是否为后台任务启用自动重试，仅应用于后台任务。

true：是

false：否

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var roaming

```cangjie
public var roaming: Bool
```

**功能：** 是否允许在漫游网络中工作。

true：是

false：否

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22