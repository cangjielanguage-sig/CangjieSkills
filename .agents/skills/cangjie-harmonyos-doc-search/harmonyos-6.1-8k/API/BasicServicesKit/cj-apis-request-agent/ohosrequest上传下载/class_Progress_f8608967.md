## class Progress

```cangjie
public class Progress {
    public let state: State
    public let index: UInt32
    public let processed: Int64
    public let sizes: Array<Int64>
    public let extras: HashMap<String, String>
}
```

**功能：** 任务进度的数据结构。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let extras

```cangjie
public let extras: HashMap<String, String>
```

**功能：** 交互的额外内容，例如：来自服务器的响应的header和body。

**类型：** HashMap\<String,String>

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let index

```cangjie
public let index: UInt32
```

**功能：** 任务中当前正在处理的文件索引。

**类型：** UInt32

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let processed

```cangjie
public let processed: Int64
```

**功能：** 任务中当前文件的已处理数据大小，单位为字节（B）。

**类型：** Int64

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let sizes

```cangjie
public let sizes: Array<Int64>
```

**功能：** 任务中文件的大小，单位为字节（B）。在下载过程中，若服务器使用chunk方式传输导致无法从请求头中获取文件总大小时，sizes为 -1。

**类型：** Array\<Int64>

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let state

```cangjie
public let state: State
```

**功能：** 任务当前的状态。

**类型：** [State](#enum-state)

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22