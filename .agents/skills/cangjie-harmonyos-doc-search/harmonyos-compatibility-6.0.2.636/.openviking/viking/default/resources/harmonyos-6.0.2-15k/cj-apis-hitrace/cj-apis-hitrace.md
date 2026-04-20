# ohos.hitrace（ArkTS Trace功能函数）

提供了跟踪进程轨迹，度量程序执行性能的打点能力。

## 导入模块

```cangjie
import ohos.hitrace.*
```

## class Hitrace <sub>(deprecated)</sub>

```cangjie
public class HiTrace {}
```

**功能：** 该类提供了跟踪进程轨迹，度量程序执行性能的打点能力。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

### static func finishTrace(String, Int32) <sub>(deprecated)</sub>

```cangjie
public static func finishTrace(name: String, taskId: Int32): Unit
```

**功能：** 标记一个预跟踪耗时任务的结束。

[finishTrace](#static-func-finishtracestring-int32-deprecated)的name和taskId必须与流程开始的[startTrace](#static-func-starttracestring-int32-deprecated)对应参数值一致。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|要跟踪的任务名称。|
|taskId|Int32|是|-|任务id。|

### static func startTrace(String, Int32) <sub>(deprecated)</sub>

```cangjie
public static func startTrace(name: String, taskId: Int32): Unit
```

**功能：** 标记一个预跟踪耗时任务的开始。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|要跟踪的任务名称。|
|taskId|Int32|是|-|任务id。|

### static func traceByValue(String, Int64) <sub>(deprecated)</sub>

```cangjie
public static func traceByValue(name: String, count: Int64): Unit
```

**功能：** 用来标记一个预跟踪的数值变量，该变量的数值会不断变化。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|要跟踪的数值变量名称。|
|count|Int64|是|-|变量的值。|
