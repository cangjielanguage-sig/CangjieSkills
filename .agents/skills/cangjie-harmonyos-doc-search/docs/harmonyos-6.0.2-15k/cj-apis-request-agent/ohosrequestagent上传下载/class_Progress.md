## class Progress

```cangjie
public class Progress {
    public Progress(
        public let state!: State,
        public let index!: UInt32,
        public let processed!: Int64,
        public let sizes!: Array<Int64>,
        public let extras!: HashMap<String, String>
    )
}
```

**功能：** 任务进度的数据结构。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

### let extras

```cangjie
public let extras: HashMap<String, String>
```

**功能：** 交互的额外内容，例如来自服务器的响应的header和body。

**类型：** ?HashMap\<String, String>

**读写能力：** 只读

**起始版本：** 12

### let index

```cangjie
public let index: UInt32
```

**功能：** 任务中当前正在处理的文件索引。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### let processed

```cangjie
public let processed: Int64
```

**功能：** 任务中当前文件的已处理数据大小，单位为B。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

### let sizes

```cangjie
public let sizes: Array<Int64>
```

**功能：** 任务中文件的大小，单位为B。

**类型：** Array\<Int64>

**读写能力：** 只读

**起始版本：** 12

### let state

```cangjie
public let state: State
```

**功能：** 任务当前的状态。

**类型：** [State](#enum-state)

**读写能力：** 只读

**起始版本：** 12

### Progress(State, UInt32, Int64, Array\<Int64>, HashMap\<String, String>)

```cangjie
public Progress(
    public let state!: State,
    public let index!: UInt32,
    public let processed!: Int64,
    public let sizes!: Array<Int64>,
    public let extras!: HashMap<String, String>
)
```

**功能：** 创建Progress对象。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|state|[State](#enum-state)|是|-| **命名参数。** 任务当前的状态。|
|index|UInt32|是|-| **命名参数。** 任务中当前正在处理的文件索引。|
|processed|Int64|是|-| **命名参数。** 任务中当前文件的已处理数据大小，单位为B。|
|sizes|Array\<Int64>|是|-| **命名参数。** 任务中文件的大小，单位为B。|
|extras|?HashMap\<String, String>|是|-| **命名参数。** 交互的额外内容，例如来自服务器的响应的header和body。|