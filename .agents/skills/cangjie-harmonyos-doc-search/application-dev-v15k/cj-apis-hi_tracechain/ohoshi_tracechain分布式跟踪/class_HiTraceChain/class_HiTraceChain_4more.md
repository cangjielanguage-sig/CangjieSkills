## class HiTraceChain

```cangjie
public class HiTraceChain {}
```

**功能：** 该类提供了端侧业务流程调用链跟踪的打点能力。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

### static func begin(String, Int32)

```cangjie
public static func begin(name: String, flag!: Int32 = HiTraceFlag.DEFAULT.value): HiTraceId
```

**功能：** 开始跟踪。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|跟踪业务名。|
|flag|Int32|否|[HiTraceFlag](#enum-hitraceflag).DEFAULT.value| **命名参数。** 跟踪标志组合，具体可参考[HiTraceFlag](#enum-hitraceflag)。|

**返回值：**

|类型|说明|
|:----|:----|
|[HiTraceId](#class-hitraceid)|[HiTraceId](#class-hitraceid)实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

// 开启跟踪，跟踪标志是INCLUDE_ASYNC与DONOT_CREATE_SPAN的并集。
let traceId = HiTraceChain.begin("business", flag: HiTraceFlag.INCLUDE_ASYNC.value | HiTraceFlag.DONOT_CREATE_SPAN.value)
// 若干业务逻辑完成后，结束跟踪。
HiTraceChain.end(traceId)
```

### static func clearId()

```cangjie
public static func clearId(): Unit
```

**功能：** 清除跟踪标识。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

// 业务开始前，尝试清除跟踪标识。
HiTraceChain.clearId()
// 开启跟踪，跟踪标志是DEFAULT。
let traceId = HiTraceChain.begin("business", flag: HiTraceFlag.DEFAULT.value)
// 若干业务逻辑完成后，结束跟踪。
HiTraceChain.end(traceId)
```

### static func createSpan()

```cangjie
public static func createSpan(): HiTraceId
```

**功能：** 创建跟踪分支。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[HiTraceId](#class-hitraceid)|[HiTraceId](#class-hitraceid)实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let traceId = HiTraceChain.begin("business", flag: HiTraceFlag.DEFAULT.value)
// 若干业务逻辑完成后，创建跟踪分支。
let spanTraceId = HiTraceChain.createSpan()
// 同一跟踪链的跟踪标识的chainId一定相同。
if (spanTraceId.chainId != traceId.chainId) {
    // 基于异常场景的处理逻辑。
}
// 业务结束，关闭跟踪。
HiTraceChain.end(traceId)
```