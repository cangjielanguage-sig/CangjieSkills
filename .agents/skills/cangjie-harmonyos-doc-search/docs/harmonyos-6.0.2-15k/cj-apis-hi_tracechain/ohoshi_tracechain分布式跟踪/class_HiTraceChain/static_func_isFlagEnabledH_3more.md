### static func isFlagEnabled(HiTraceId, Int32)

```cangjie
public static func isFlagEnabled(id: HiTraceId, flag: Int32): Bool
```

**功能：** 判断[HiTraceId](#class-hitraceid)对象中指定的跟踪标志是否已置位。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|[HiTraceId](#class-hitraceid)|是|-|需要判断指定跟踪标志是否置位的[HiTraceId](#class-hitraceid)实例。|
|flag|Int32|是|-|指定的跟踪标志。具体可参考[HiTraceFlag](#enum-hitraceflag)。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true标识[HiTraceId](#class-hitraceid)已置位指定的flag，否则没有置位。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

// 开启跟踪，跟踪标志是INCLUDE_ASYNC。
let traceId = HiTraceChain.begin("business", flag: HiTraceFlag.INCLUDE_ASYNC.value)
// enabledIncludeAsyncFlag为true。
let enabledIncludeAsyncFlag = HiTraceChain.isFlagEnabled(traceId, HiTraceFlag.INCLUDE_ASYNC.value)
if (enabledIncludeAsyncFlag) {
    // 基于INCLUDE_ASYNC跟踪标志已设置场景的处理逻辑。
}
//业务结束，关闭跟踪。
HiTraceChain.end(traceId)
```

### static func isValid(HiTraceId)

```cangjie
public static func isValid(id: HiTraceId): Bool
```

**功能：** 判断[HiTraceId](#class-hitraceid)对象是否有效。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|[HiTraceId](#class-hitraceid)|是|-|需要判断是否有效的[HiTraceId](#class-hitraceid)实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示[HiTraceId](#class-hitraceid)有效，否则无效。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

// 开启跟踪，跟踪标志是DEFAULT。
let traceId = HiTraceChain.begin("business", flag: HiTraceFlag.DEFAULT.value)
// traceIdIsvalid为true
let traceIdIsvalid = HiTraceChain.isValid(traceId)
if (traceIdIsvalid) {
    // 基于跟踪标识合法性校验成功的场景的处理逻辑。
}
//业务结束，关闭跟踪。
HiTraceChain.end(traceId)
```

### static func setId(HiTraceId)

```cangjie
public static func setId(id: HiTraceId): Unit
```

**功能：** 设置跟踪标识。

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

// 获取当前跟踪链中的跟踪标识。
let traceId = HiTraceChain.getId()
// 将获取的跟踪标识设置为当前traceId。
HiTraceChain.setId(traceId)
```