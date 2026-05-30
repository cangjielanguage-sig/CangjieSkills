## class HiTraceMeter

```cangjie
public class HiTraceMeter {}
```

**功能：** 该类提供了跟踪进程轨迹，度量程序执行性能的打点能力。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

### static func finishTrace(String, Int32)

```cangjie
public static func finishTrace(name: String, taskId: Int32): Unit
```

**功能：** 标记一个预跟踪耗时任务的结束。

[finishTrace](#static-func-finishtracestring-int32)的name和taskId必须与流程开始的[startTrace](#static-func-starttracestring-int32)对应参数值一致。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|要跟踪的任务名称。|
|taskId|Int32|是|-|任务id。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

func f1(){
    HiTraceMeter.finishTrace("myTestFunc", 1)
}

func f2(){
    // 跟踪并行执行的同名任务
    HiTraceMeter.startTrace("myTestFunc", 1)
    // 业务流程代码
    HiTraceMeter.startTrace("myTestFunc", 2)  // 第二个跟踪的任务开始，同时第一个跟踪的同名任务还没结束，出现了并行执行，对应接口的taskId需要不同。
    // 业务流程代码
    HiTraceMeter.finishTrace("myTestFunc", 1)
    // 业务流程代码
    HiTraceMeter.finishTrace("myTestFunc", 2)
}

func f3(){
    // 跟踪串行执行的同名任务
    HiTraceMeter.startTrace("myTestFunc", 1)
    // 业务流程代码
    HiTraceMeter.finishTrace("myTestFunc", 1)  // 第一个跟踪的任务结束
    // 业务流程代码
    HiTraceMeter.startTrace("myTestFunc", 1)   // 第二个跟踪的同名任务开始，同名的待跟踪任务串行执行。
    // 业务流程代码
    HiTraceMeter.finishTrace("myTestFunc", 1)
}

f1()
f2()
f3()
```

### static func startTrace(String, Int32)

```cangjie
public static func startTrace(name: String, taskId: Int32): Unit
```

**功能：** 标记一个预跟踪耗时任务的开始。

如果有多个相同name的任务需要跟踪或者对同一个任务要跟踪多次，并且任务同时被执行，则每次调用[startTrace](#static-func-starttracestring-int32)的taskId不相同。

如果具有相同name的任务是串行执行的，则taskId可以相同。具体示例可参考[HiTraceMeter.finishTrace](#static-func-finishtracestring-int32)中的示例。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|要跟踪的任务名称。|
|taskId|Int32|是|-|任务id。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

HiTraceMeter.startTrace("myTestFunc", 1)
```

### static func traceByValue(String, Int32)

```cangjie
public static func traceByValue(name: String, count: Int32): Unit
```

**功能：** 用来标记一个预跟踪的数值变量，该变量的数值会不断变化。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|要跟踪的数值变量名称。|
|count|Int32|是|-|变量的值。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

var traceCount = Int32(3)
HiTraceMeter.traceByValue("myTestCount", traceCount)
traceCount = 4
HiTraceMeter.traceByValue("myTestCount", traceCount)
// 业务流程代码
```