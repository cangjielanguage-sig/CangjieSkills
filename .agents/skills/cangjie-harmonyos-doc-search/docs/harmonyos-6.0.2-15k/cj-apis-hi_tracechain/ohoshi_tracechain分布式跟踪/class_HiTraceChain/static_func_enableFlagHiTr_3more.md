### static func enableFlag(HiTraceId, Int32)

```cangjie
public static func enableFlag(id: HiTraceId, flag: Int32): Unit
```

**功能：** 置位[HiTraceId](#class-hitraceid)对象中指定的跟踪标志。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|[HiTraceId](#class-hitraceid)|是|-|需要置位指定跟踪标志的[HiTraceId](#class-hitraceid)实例。|
|flag|Int32|是|-|指定的跟踪标志。具体可参考[HiTraceFlag](#enum-hitraceflag)。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

// 开启跟踪，跟踪标志是INCLUDE_ASYNC。
var traceId = HiTraceChain.begin("business", flag: HiTraceFlag.INCLUDE_ASYNC.value)
// enabledDoNotCreateSpanFlag为false。
var enabledDoNotCreateSpanFlag = HiTraceChain.isFlagEnabled(traceId, HiTraceFlag.DONOT_CREATE_SPAN.value)
// 设置DONOT_CREATE_SPAN跟踪标志。
HiTraceChain.enableFlag(traceId, HiTraceFlag.DONOT_CREATE_SPAN.value)
// enabledDoNotCreateSpanFlag为true。
enabledDoNotCreateSpanFlag = HiTraceChain.isFlagEnabled(traceId, HiTraceFlag.DONOT_CREATE_SPAN.value)
if (enabledDoNotCreateSpanFlag) {
    // 基于DONOT_CREATE_SPAN跟踪标志已设置场景的处理逻辑。
}
//业务结束，关闭跟踪。
HiTraceChain.end(traceId)
```

### static func end(HiTraceId)

```cangjie
public static func end(id: HiTraceId): Unit
```

**功能：** 结束跟踪。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|[HiTraceId](#class-hitraceid)|是|-|[HiTraceId](#class-hitraceid)实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let traceId = HiTraceChain.begin("business", flag: HiTraceFlag.INCLUDE_ASYNC.value)
// 若干业务逻辑完成后，结束跟踪。
HiTraceChain.end(traceId)
```

### static func getId()

```cangjie
public static func getId(): HiTraceId
```

**功能：** 获取跟踪标识。

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

// 开启跟踪，跟踪标志是DEFAULT。
let traceId = HiTraceChain.begin("business", flag: HiTraceFlag.DEFAULT.value)
// 若干业务逻辑完成后，获取当前跟踪标识。
let curTraceId = HiTraceChain.getId()
// 同一跟踪链获取的跟踪标识的chainId一定相同。
if (curTraceId.chainId != traceId.chainId) {
    // 基于异常场景的处理逻辑。
}
// 若干业务逻辑完成后，结束跟踪。
HiTraceChain.end(traceId)
```