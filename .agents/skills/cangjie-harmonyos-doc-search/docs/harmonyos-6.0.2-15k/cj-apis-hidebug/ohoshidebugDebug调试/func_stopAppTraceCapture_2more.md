## func stopAppTraceCapture()

```cangjie
public func stopAppTraceCapture(): Unit
```

**功能：** 停止应用trace采集，在停止采集前，需要通过[startAppTraceCapture](#func-startapptracecapturearrayuint64-traceflag-uint32)方法开始采集。

先开启后关闭，严禁使用'start->start->stop'，'start->stop->stop'，'start->start->stop->stop'等类似的顺序调用。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Hidebug错误码](../../errorcodes/cj-errorcode-hidebug.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |11400104|The status of the trace is abnormal.|
  |11400105|No capture trace running.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let fileName: String = startAppTraceCapture([Tags.ABILITY_MANAGER, Tags.ARKUI], MAIN_THREAD, 1024*1204)
// code block
// ...
// code block
stopAppTraceCapture()
```

## class MemoryLimit

```cangjie
public class MemoryLimit {
    public let rssLimit: UInt64
    public let vssLimit: UInt64
}
```

**功能：** 应用程序进程内存限制。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

### let rssLimit

```cangjie
public let rssLimit: UInt64
```

**功能：** 应用程序进程的驻留集的限制，以KB为单位。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**类型：** UInt64

**读写能力：** 只读

**起始版本：** 19

### let vssLimit

```cangjie
public let vssLimit: UInt64
```

**功能：** 进程的虚拟内存限制，以KB为单位。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**类型：** UInt64

**读写能力：** 只读

**起始版本：** 19