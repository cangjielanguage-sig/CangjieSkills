### func onCreate(Want, LaunchParam)

```cangjie
public open func onCreate(want: Want, launchParam: LaunchParam): Unit
```

**功能：** UIAbility创建时回调，执行初始化业务逻辑操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 12

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|want|[Want](#class-want)|是|当前UIAbility的Want类型信息，包括UIAbility名称、Bundle名称等。|
|launchParam|[LaunchParam](#class-launchparam)|是|创建 ability、上次异常退出的原因信息。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.AppLog
import kit.AbilityKit.*

class MainAbility <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("MainAbility OnCreated.${want.abilityName}")
        match (launchParam.launchReason) {
            case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
            case _ => ()
        }
    }
}
```

### func onDestroy()

```cangjie
public open func onDestroy(): Unit
```

**功能：** UIAbility销毁时回调，执行资源清理等操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.AppLog
import kit.AbilityKit.*

class MainAbility <: UIAbility {
    public override func onDestroy(): Unit {
        AppLog.info("onDestroy")
    }
}
```

### func onDump(Array\<String>)

```cangjie
public open func onDump(params: Array<String>): Array<String>
```

**功能：** 转储客户端信息时调用，可用于转储非敏感信息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|params|Array\<String>|是|表示命令形式的参数。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>| 转储信息数组。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.AppLog
import kit.AbilityKit.*

class MainAbility <: UIAbility {
    public override func onDump(params: Array<String>): Array<String> {
        AppLog.info("MainAbility onDump.")
        return Array<String>()
    }
}
```

### func onForeground()

```cangjie
public open func onForeground(): Unit
```

**功能：** UIAbility生命周期回调，当应用从后台转到前台时触发。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.AppLog
import kit.AbilityKit.*

class MainAbility <: UIAbility {
    public override func onForeground(): Unit {
        AppLog.info("onForeground")
    }
}
```

### func onNewWant(Want, LaunchParam)

```cangjie
public open func onNewWant(want: Want, launchParams: LaunchParam): Unit
```

**功能：** UIAbility实例已经启动并在前台运行过，由于某些原因切换到后台，再次启动该UIAbility实例时会回调执行该方法。即UIAbility实例热启动时进入该生命周期回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 12

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|want|[Want](#class-want)|是|当前UIAbility的Want类型信息，包括ability名称、bundle名称等。|
|launchParams|[LaunchParam](#class-launchparam)|是|Ability启动的原因、上次异常退出的原因信息。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.AppLog
import kit.AbilityKit.*

class MainAbility <: UIAbility {
    public override func onNewWant(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("MainAbility onNewWant.${want.abilityName}")
        match (launchParam.launchReason) {
            case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
            case _ => ()
        }
    }
}
```