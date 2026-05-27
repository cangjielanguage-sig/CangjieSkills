### static func tracepoint(HiTraceCommunicationMode, HiTraceTracepointType, HiTraceId, String)

```cangjie
public static func tracepoint(mode: HiTraceCommunicationMode, traceType: HiTraceTracepointType, id: HiTraceId, msg!: String = ""): Unit
```

**功能：** 信息埋点。

**注意：** 此接口的信息埋点功能在开启TP_INFO和D2D_TP_INFO追踪模式时才生效。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[HiTraceCommunicationMode](#enum-hitracecommunicationmode)|是|-|信息埋点需要指定的跟踪通信模式。|
|traceType|[HiTraceTracepointType](#enum-hitracetracepointtype)|是|-|信息埋点需要指定的跟踪埋点类型。|
|id|[HiTraceId](#class-hitraceid)|是|-|实施信息埋点操作的[HiTraceId](#class-hitraceid)实例。|
|msg|String|否|""| **命名参数。** 信息埋点操作传入的trace说明信息。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

// 开启跟踪，跟踪标志是DEFAULT。
// 开启跟踪，跟踪标志是INCLUDE_ASYNC与DONOT_CREATE_SPAN的并集。
let traceId = HiTraceChain.begin("business", flag: HiTraceFlag.INCLUDE_ASYNC.value)
// 若干业务逻辑完成后，触发信息埋点操作。
HiTraceChain.tracepoint(HiTraceCommunicationMode.THREAD, HiTraceTracepointType.SS, traceId, msg: "Just a example")
//业务结束，关闭跟踪。
HiTraceChain.end(traceId)
```