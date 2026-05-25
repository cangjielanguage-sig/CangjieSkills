### static func on(String, ErrorObserver)

```cangjie
public static func on(onType: String, observer: ErrorObserver): Int32
```

**功能：** 注册错误观测器。注册后程序如果出现crash，会触发未捕获异常机制。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onType|String|是|-|填写"error"，表示错误观察器。|
|observer|[ErrorObserver](#struct-errorobserver)|是|-|错误观察器。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|观察器的index值，和观察器一一对应。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3. Parameter verification failed.|
  |16200001|The caller has been released.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*
import kit.PerformanceAnalysisKit.*

let observer = ErrorObserver(
    {
        errorMsg =>
            Hilog.info(0, "test_errorManager", "onUnhandledException, errorMsg:  =${errorMsg}")
    },
    onException: Some({ errorObj =>
        Hilog.info(0, "test_errorManager", "onException, name:   =${errorObj.name}")
        Hilog.info(0, "test_errorManager", "onException, message:   =${errorObj.message}")
        if (let Some(v) <-errorObj.stack) {
            Hilog.info(0, "test_errorManager", "onException, stack:    =${v}")
        }
    })
)
ErrorManager.on("error", observer)
```

### static func on(String, Int64, LoopObserver)

```cangjie
public static func on(`type`: String, timeout: Int64, observer: LoopObserver): Unit
```

**功能：** 注册主线程消息处理耗时监听器。注册后可以捕获到应用主线程处理消息的具体执行时间。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|String|是|-|填写'loopObserver'，表示注册主线程消息处理耗时监听器。|
|timeout|Int64|是|-|表示事件执行阈值（单位：毫秒）。 阈值必须大于0。|
|observer|[LoopObserver](#class-loopobserver)|是|-|注册主线程消息处理耗时监听器。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3. Parameter verification failed.|
  |16200001|The caller has been released.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

let loopObserver = LoopObserver(onLoopTimeOut: {
    timeout =>
        AppLog.info("onLoopTimeOut timeout:  ${timeout}")
    })
ErrorManager.on("loopObserver", 2, loopObserver)
```