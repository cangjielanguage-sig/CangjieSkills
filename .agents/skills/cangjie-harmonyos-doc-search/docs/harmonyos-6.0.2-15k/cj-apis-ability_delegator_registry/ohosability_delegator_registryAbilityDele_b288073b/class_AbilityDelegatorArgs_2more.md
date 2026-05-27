## class AbilityDelegatorArgs

```cangjie
public class AbilityDelegatorArgs {}
```

**功能：** 测试参数信息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### prop bundleName

```cangjie
public mut prop bundleName: String
```

**功能：** 当前被测试应用的包名。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### prop parameters

```cangjie
public mut prop parameters: HashMap<String, String>
```

**功能：** 当前启动单元测试的参数。

**类型：** HashMap\<String, String>

**读写能力：** 可读写

**起始版本：** 19

### prop testCaseNames

```cangjie
public mut prop testCaseNames: String
```

**功能：** 测试用例名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### prop testRunnerClassName

```cangjie
public mut prop testRunnerClassName: String
```

**功能：** 执行测试用例的测试执行器名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

## class AbilityDelegatorRegistry

```cangjie
public class AbilityDelegatorRegistry {}
```

**功能：** [AbilityDelegatorRegistry](#class-abilitydelegatorregistry)提供用于存储已注册的[AbilityDelegator](#class-abilitydelegator)和[AbilityDelegatorArgs](#class-abilitydelegatorargs)对象的全局寄存器的能力。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### static func getAbilityDelegator()

```cangjie
public static func getAbilityDelegator(): AbilityDelegator
```

**功能：** 获取应用程序的[AbilityDelegator](#class-abilitydelegator)对象，该对象能够使用调度测试框架的相关功能。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[AbilityDelegator](#class-abilitydelegator)|[AbilityDelegator](#class-abilitydelegator)对象。可以用来调度测试框架相关功能。|

### static func getArguments()

```cangjie
public static func getArguments(): AbilityDelegatorArgs
```

**功能：** 获取单元测试参数[AbilityDelegatorArgs](#class-abilitydelegatorargs)对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AbilityDelegatorArgs](#class-abilitydelegatorargs)|[AbilityDelegatorArgs](#class-abilitydelegatorargs)对象。可以用来获取测试参数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TestKit.*

let args = AbilityDelegatorRegistry.getArguments()
AppLog.info("args is ${args.bundleName}")
AppLog.info("args is ${args.testCaseNames}")
AppLog.info("args is ${args.testRunnerClassName}")
AppLog.info("args is ${args.parameters}")
```