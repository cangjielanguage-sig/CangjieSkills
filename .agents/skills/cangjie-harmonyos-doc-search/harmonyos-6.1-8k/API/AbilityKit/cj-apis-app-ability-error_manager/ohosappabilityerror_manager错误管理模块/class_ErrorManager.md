## class ErrorManager

```cangjie
public class ErrorManager {}
```

**功能：** 提供Ability错误管理的能力，包括错误事件的监听和取消监听。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### static func off(ErrorManagerEvent, Int32)

```cangjie
public static func off(eventType: ErrorManagerEvent, observerId: Int32): Unit
```

**功能：** 取消监听Ability错误事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[ErrorManagerEvent](#enum-errormanagerevent)|是|-|错误事件类型。|
|observerId|Int32|是|-|观察者ID。|

**异常：**

- BusinessException：对应错误码如下表，详见[元能力子系统错误码](./cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 16000003 | The specified ID does not exist. |
  | 16000050 | Internal error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj
import kit.AbilityKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

try {
    let observerId: Int32 = 1
    ErrorManager.off(ErrorManagerEvent.Error, observerId)
} catch (e: BusinessException) {
    Hilog.info(0, "test_errorManager", "${e.message}")
}
```

### static func on(ErrorManagerEvent, ErrorObserver)

```cangjie
public static func on(eventType: ErrorManagerEvent, observer: ErrorObserver): Int32
```

**功能：** 监听Ability错误事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[ErrorManagerEvent](#enum-errormanagerevent)|是|-|错误事件类型。|
|observer|[ErrorObserver](./cj-apis-application-error_observer.md#class-errorobserver)|是|-|错误观察者。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|观察者ID。|

**异常：**

- BusinessException：对应错误码如下表，详见[元能力子系统错误码](./cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 16000003 | The specified ID does not exist. |
  | 16000050 | Internal error. |

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
            if (let Some(v) <- errorObj.stack) {
                Hilog.info(0, "test_errorManager", "onException, stack:    =${v}")
            }
        })
    )
    let id = ErrorManager.on(ErrorManagerEvent.Error, observer)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```