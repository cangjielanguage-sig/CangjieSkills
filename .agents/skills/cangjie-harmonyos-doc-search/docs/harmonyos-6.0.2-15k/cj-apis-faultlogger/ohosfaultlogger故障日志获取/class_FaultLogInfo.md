## class FaultLogInfo

```cangjie
public class FaultLogInfo {
    public FaultLogInfo(
        public let pid: Int32,
        public let uid: Int32,
        public let faultType: FaultType,
        public let timestamp: Int64,
        public let reason: String,
        public let module: String,
        public let summary: String,
        public let fullLog: String
    )
}
```

**功能：** 故障信息数据结构。

**系统能力：** SystemCapability.HiviewDFX.Hiview.FaultLogger

**起始版本：** 19

### let faultType

```cangjie
public let faultType: FaultType
```

**功能：** 故障类型。

**类型：** [FaultType](#enum-faulttype)

**读写能力：** 只读

**起始版本：** 19

### let fullLog

```cangjie
public let fullLog: String
```

**功能：** 故障日志全文。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let module

```cangjie
public let module: String
```

**功能：** 发生故障的模块。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let pid

```cangjie
public let pid: Int32
```

**功能：** 故障进程的进程id。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let reason

```cangjie
public let reason: String
```

**功能：** 发生故障的原因。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let summary

```cangjie
public let summary: String
```

**功能：** 故障的概要。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let timestamp

```cangjie
public let timestamp: Int64
```

**功能：** 日志生成时的毫秒级时间戳。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 19

### let uid

```cangjie
public let uid: Int32
```

**功能：** 故障进程的用户id。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### FaultLogInfo(Int32, Int32, FaultType, Int64, String, String, String, String)

```cangjie
public FaultLogInfo(
    public let pid: Int32,
    public let uid: Int32,
    public let faultType: FaultType,
    public let timestamp: Int64,
    public let reason: String,
    public let module: String,
    public let summary: String,
    public let fullLog: String
)
```

**功能：** 创建[FaultLogInfo](#class-faultloginfo)实例。

**系统能力：** SystemCapability.HiviewDFX.Hiview.FaultLogger

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pid|Int32|是|-|故障进程的进程id。|
|uid|Int32|是|-|故障进程的用户id。|
|faultType|[FaultType](#enum-faulttype)|是|-|故障类型。|
|timestamp|Int64|是|-|日志生成时的毫秒级时间戳。|
|reason|String|是|-|发生故障的原因。|
|module|String|是|-|发生故障的模块。|
|summary|String|是|-|故障的概要。|
|fullLog|String|是|-|故障日志全文。|