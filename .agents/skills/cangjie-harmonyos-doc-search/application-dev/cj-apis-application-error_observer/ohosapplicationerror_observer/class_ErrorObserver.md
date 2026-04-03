## class ErrorObserver

```cangjie
public class ErrorObserver {
    public var onUnhandledException:(String) -> Unit
    public var onException: Option <(ErrorObject) -> Unit>
    public init(
        onUnhandledException: (String) -> Unit,
        onException!: Option<(ErrorObject) -> Unit> = None
    )
}
```

**功能：** 异常监听模块。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### var onException

```cangjie
public var onException: Option <(ErrorObject) -> Unit>
```

**功能：** 应用产生异常，上报cangjie层时的回调。

**类型：** Option\<([ErrorObject](#class-errorobject))->Unit>

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### var onUnhandledException

```cangjie
public var onUnhandledException:(String) -> Unit
```

**功能：** 应用产生未捕获的异常时的回调。

**类型：** (String)->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### init((String) -> Unit, Option\<(ErrorObject) -> Unit>)

```cangjie
public init(
    onUnhandledException: (String) -> Unit,
    onException!: Option<(ErrorObject) -> Unit> = None
)
```

**功能：** 构建异常监听类。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onUnhandledException|(String)->Unit|是|-|应用产生未捕获的异常时的回调。|
|onException|Option\<([ErrorObject](#class-errorobject))->Unit>|否|None|**命名参数。** 应用产生异常，上报仓颉层时的回调。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
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
    let id = ErrorManager.on(ErrorManagerEvent.Error, observer)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```