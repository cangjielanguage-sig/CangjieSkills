## class ThreadCpuUsage

```cangjie
public class ThreadCpuUsage {}
```

**功能：** 描述线程CPU使用情况。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

### let cpuUsage

```cangjie
public let cpuUsage: Float64
```

**功能：** 线程CPU使用率。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**类型：** Float64

**读写能力：** 只读

**起始版本：** 19

### let threadId

```cangjie
public let threadId: UInt32
```

**功能：** 线程号。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

## enum TraceFlag

```cangjie
public enum TraceFlag {
    | MAIN_THREAD
    | ALL_THREADS
    | ...
}
```

**功能：** 描述采集trace线程的类型。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

### ALL_THREADS

```cangjie
ALL_THREADS
```

**功能：** 采集当前应用下所有线程。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

### MAIN_THREAD

```cangjie
MAIN_THREAD
```

**功能：** 只采集当前应用主线程。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19