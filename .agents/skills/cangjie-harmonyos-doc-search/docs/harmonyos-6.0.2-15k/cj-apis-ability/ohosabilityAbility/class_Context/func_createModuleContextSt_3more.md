### func createModuleContext(String)

```cangjie
public func createModuleContext(moduleName: String): Context
```

**功能：** 根据模块名创建上下文。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|moduleName|String|是|-|模块名。|

**返回值：**

|类型|说明|
|:----|:----|
|[Context](#class-context)|模块的上下文。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :------- | :-------------------------------- |
  | 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.AbilityKit.*
import ohos.base.AppLog

class MainAbility <: UIAbility {
    public init() {
        super()
        registerSelf()
    }

    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("MainAbility OnCreated.${want.abilityName}")
        let moduleContext = this.context.createModuleContext("entry")
        match (launchParam.launchReason) {
            case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
            case _ => ()
        }
    }
}
```

> 说明：仅支持获取本应用中其他Module的Context，不支持获取其他应用的Context。

### func getApplicationContext()

```cangjie
public func getApplicationContext(): ApplicationContext
```

**功能：** 获取本应用的应用上下文。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[ApplicationContext](#class-applicationcontext)|应用上下文Context。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :------- | :-------------------------------- |
  | 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.AbilityKit.*
import ohos.base.AppLog

class MainAbility <: UIAbility {
    public init() {
        super()
        registerSelf()
    }

    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("MainAbility OnCreated.${want.abilityName}")
        let applicationContext = this.context.getApplicationContext()
        match (launchParam.launchReason) {
            case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
            case _ => ()
        }
    }
}
```

### func getGroupDir(String)

```cangjie
public func getGroupDir(dataGroupID: String): String
```

**功能：** 通过使用应用中的Group ID获取对应的共享目录。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dataGroupID|String|是|-|原子化服务应用项目创建时，系统会指定分配唯一Group ID。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回对应的共享目录。如果不存在则返回为空，仅支持应用el2加密级别。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :------- | :-------------------------------- |
  | 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
  | 16000011 | The context does not exist. |