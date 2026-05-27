## class ErrorManager

```cangjie
public class ErrorManager {}
```

**功能：** 提供注册和注销错误观察器方法的类。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### static func off(String, Int32)

```cangjie
public static func off(offType: String, observerId: Int32): Unit
```

**功能：** 注销主线程消息处理监听器。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offType|String|是|-|填写"error"，表示错误观察器。|
|observerId|Int32|是|-|由on方法返回的观察器的index值。|

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

try {
    let observerId: Int32 = 1
    ErrorManager.off("error", observerId)
} catch (e: BusinessException) {
    AppLog.info(e)
}
```

### static func off(String, ?LoopObserver)

```cangjie
public static func off(`type`: String, observer!: ?LoopObserver = None): Unit
```

**功能：** 注销主线程消息处理监听器。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|String|是|-|填写'loopObserver'，表示应用主线程观察器。|
|observer|?[LoopObserver](#class-loopobserver)|否|None| **命名参数。** 应用主线程观察器标志。|

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

try {
    ErrorManager.off("loopObserver")
    AppLog.error("error_manager test ok")
} catch (e: BusinessException) {
    AppLog.error("error_manager  error: ${e}")
}
```