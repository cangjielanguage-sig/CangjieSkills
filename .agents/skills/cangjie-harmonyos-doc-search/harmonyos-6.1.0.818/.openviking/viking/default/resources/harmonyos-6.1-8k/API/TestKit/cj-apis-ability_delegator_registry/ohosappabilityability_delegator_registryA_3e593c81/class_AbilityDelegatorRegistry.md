## class AbilityDelegatorRegistry

```cangjie
public class AbilityDelegatorRegistry {}
```

**功能：** [AbilityDelegatorRegistry](#class-abilitydelegatorregistry)提供用于存储已注册的[AbilityDelegator](#class-abilitydelegator)和[AbilityDelegatorArgs](#class-abilitydelegatorargs)对象的全局寄存器的能力。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### static func getAbilityDelegator()

```cangjie
public static func getAbilityDelegator(): AbilityDelegator
```

**功能：** 获取应用程序的[AbilityDelegator](#class-abilitydelegator)对象，该对象能够使用调度测试框架的相关功能。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[AbilityDelegator](#class-abilitydelegator)|[AbilityDelegator](#class-abilitydelegator)对象。可以用来调度测试框架相关功能。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let delegator = AbilityDelegatorRegistry.getAbilityDelegator()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func getArguments()

```cangjie
public static func getArguments(): AbilityDelegatorArgs
```

**功能：** 获取单元测试参数[AbilityDelegatorArgs](#class-abilitydelegatorargs)对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[AbilityDelegatorArgs](#class-abilitydelegatorargs)|[AbilityDelegatorArgs](#class-abilitydelegatorargs)对象。可以用来获取测试参数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let args = AbilityDelegatorRegistry.getArguments()
    Hilog.info(0, "test", "args is ${args.bundleName}")
    Hilog.info(0, "test", "args is ${args.testCaseNames}")
    Hilog.info(0, "test", "args is ${args.testRunnerClassName}")
    Hilog.info(0, "test", "args is ${args.parameters}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```