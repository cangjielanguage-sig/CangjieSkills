# ohos.faultlogger（故障日志获取）

提供获取故障日志的能力。

## 导入模块

```cangjie
import kit.PerformanceAnalysisKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## class FaultLogger

```cangjie
public class FaultLogger {}
```

**功能：** [FaultLogger](#class-faultlogger)类，提供获取故障日志的能力。

**系统能力：** SystemCapability.HiviewDFX.Hiview.FaultLogger

**起始版本：** 19

### static func query(FaultType)

```cangjie
public static func query(faultType: FaultType): Array<FaultLogInfo>
```

**功能：** 获取当前进程故障信息，返回故障信息数组，故障信息数组内最多上报10份故障信息。

**系统能力：** SystemCapability.HiviewDFX.Hiview.FaultLogger

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|faultType|[FaultType](#enum-faulttype)|是|-|输入要查询的故障类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[FaultLogInfo](#class-faultloginfo)>|故障信息数组。|

**异常：**

- BusinessException：对应错误码的详细介绍参见[Faultlogger错误码](../../errorcodes/cj-errorcode-faultlogger.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|The parameter check failed, Parameter type error. |
  |801|The specified SystemCapability name was not found.|
  |10600001|The service is not started or is faulty.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let value: Array<FaultLogInfo> = FaultLogger.query(NO_SPECIFIC)
Hilog.info(0, "test", "value size is ${value.size}")
for (i in 0..value.size){
    Hilog.info(0, "test", "Log pid is ${value[i].pid}")
    Hilog.info(0, "test", "Log uid is ${value[i].uid}")
    Hilog.info(0, "test", "Log timestamp is ${value[i].timestamp}")
    Hilog.info(0, "test", "Log reason is ${value[i].reason}")
    Hilog.info(0, "test", "Log module is ${value[i].module}")
    Hilog.info(0, "test", "Log summary is ${value[i].summary}")
    Hilog.info(0, "test", "Log text is ${value[i].fullLog}")
}
```