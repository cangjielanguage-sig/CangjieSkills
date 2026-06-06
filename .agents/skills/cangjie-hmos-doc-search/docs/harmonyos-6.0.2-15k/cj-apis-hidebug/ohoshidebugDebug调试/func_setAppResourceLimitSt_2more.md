## func setAppResourceLimit(String, Int32, Bool)

```cangjie
public func setAppResourceLimit(resType: String, value: Int32, enableDebugLog: Bool): Unit
```

**功能：** 设置应用的fd数量、线程数量或者native内存资源限制。

> **注意：**
>
> 当设置的开发者选项开关打开时，此功能有效。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resType|String|是|-|泄漏资源类型，共三种类型:pss_memory(native内存)、fd(文件描述符)或thread(线程)。 |
|value|Int32|是|-|对应泄漏资源类型的最大值。范围：pss_memory类型`[1024, 4 * 1024 * 1024](单位：KB)`， fd类型`[10, 10000]`， thread类型`[1, 1000]`。|
|enableDebugLog|Bool|是|-|是否启用外部调试日志，默认值为false，请仅在灰度版本中设置为true，因为收集调试日志会花费太多的cpu或内存。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Hidebug错误码](../../errorcodes/cj-errorcode-hidebug.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  | 401|Invalid argument, Possible causes:1.The limit parameter is too small 2.The parameter is not in the specified type 3.The parameter type error or parameter order error.|
  |11400104|Set limit failed due to remote exception.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

setAppResourceLimit("fd", 85, false)
```

## func startAppTraceCapture(Array\<UInt64>, TraceFlag, UInt32)

```cangjie
public func startAppTraceCapture(tags: Array<UInt64>, flag: TraceFlag, limitSize: UInt32): String
```

**功能：** 启动应用trace采集，[startAppTraceCapture](#func-startapptracecapturearrayuint64-traceflag-uint32)方法的调用需要与[stopAppTraceCapture](#func-stopapptracecapture)方法的调用一一对应。

先开启后关闭，严禁使用'start->start->stop'，'start->stop->stop'，'start->start->stop->stop'等类似的顺序调用。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|tags|Array\<UInt64>|是|-|详情请见[Tags](#class-tags)。|
|flag|[TraceFlag](#enum-traceflag)|是|-|详情请见[TraceFlag](#enum-traceflag)。|
|limitSize|UInt32|是|-|开启trace文件大小限制，单位为Byte，单个文件大小上限为500MB。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回trace文件名路径。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Hidebug错误码](../../errorcodes/cj-errorcode-hidebug.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Invalid argument, Possible causes:1.The limit parameter is too small 2.The parameter is not within the enumeration type 3.The parameter type error or parameter order error.|
  |11400102|Capture trace already enabled.|
  |11400103| No write permission on the file.|
  |11400104|Abnormal trace status.|

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