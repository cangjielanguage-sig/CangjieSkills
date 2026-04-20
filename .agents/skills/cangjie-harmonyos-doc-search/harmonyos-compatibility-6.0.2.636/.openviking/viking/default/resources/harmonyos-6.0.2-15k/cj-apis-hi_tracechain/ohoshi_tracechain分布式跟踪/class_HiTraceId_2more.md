## class HiTraceId

```cangjie
public class HiTraceId {
    public var chainId: UInt64
    public var spanId: UInt64
    public var parentSpanId: UInt64
    public var flags: Int32
    public init(chainId: UInt64, spanId: UInt64, parentSpanId: UInt64, flags: Int32)
}
```

**功能：** 此接口为[HiTraceId](#class-hitraceid)对象接口。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

### var chainId

```cangjie
public var chainId: UInt64
```

**功能：** 跟踪链标识。

**类型：** UInt64

**读写能力：** 可读写

**起始版本：** 12

### var flags

```cangjie
public var flags: Int32
```

**功能：** 跟踪标志组合。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

### var parentSpanId

```cangjie
public var parentSpanId: UInt64
```

**功能：** 父分支标识。

**类型：** UInt64

**读写能力：** 可读写

**起始版本：** 12

### var spanId

```cangjie
public var spanId: UInt64
```

**功能：** 分支标识。

**类型：** UInt64

**读写能力：** 可读写

**起始版本：** 12

### init(UInt64, UInt64, UInt64, Int32)

```cangjie
public init(chainId: UInt64, spanId: UInt64, parentSpanId: UInt64, flags: Int32)
```

**功能：** 创建[HiTraceId](#class-hitraceid)实例。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|chainId|UInt64|是|-|跟踪链标识。|
|spanId|UInt64|是|-|分支标识。|
|parentSpanId|UInt64|是|-|父分支标识。|
|flags|Int32|是|-|跟踪标志组合。|

## enum HiTraceCommunicationMode

```cangjie
public enum HiTraceCommunicationMode {
    | DEFAULT
    | THREAD
    | PROCESS
    | DEVICE
    | ...
}
```

**功能：** 跟踪通信类型枚举。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

### DEFAULT

```cangjie
DEFAULT
```

**功能：** 缺省通信类型。

**起始版本：** 12

### DEVICE

```cangjie
DEVICE
```

**功能：** 设备间通信类型。

**起始版本：** 12

### PROCESS

```cangjie
PROCESS
```

**功能：** 进程间通信类型。

**起始版本：** 12

### THREAD

```cangjie
THREAD
```

**功能：** 线程间通信类型。

**起始版本：** 12

### prop value

```cangjie
public prop value: UInt64
```

**功能：** 获取枚举值的值。

**类型：** UInt64

**读写能力：** 只读

**起始版本：** 12