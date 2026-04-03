### func onWindowStageDestroy()

```cangjie
public open func onWindowStageDestroy(): Unit
```

**功能：** 当WindowStage销毁后调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.AppLog
import kit.AbilityKit.*

class MainAbility <: UIAbility {
    public override func onWindowStageDestroy(): Unit {
        AppLog.info("MainAbility onWindowStageDestroy.")
    }
}
```

### func onWindowStageRestore(WindowStage)

```cangjie
protected open func onWindowStageRestore(windowStage: WindowStage): Unit
```

**功能：** 当UIAbility跨端迁移时，目标端UIAbility恢复页面栈时回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|windowStage|[WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage)|是|-|[WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage)相关信息。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.AppLog
import kit.AbilityKit.*

class MainAbility <: UIAbility {
    public override onWindowStageRestore(windowStage: WindowStage): Unit {
        AppLog.info("MainAbility onWindowStageRestore.")
    }
}
```

### func onWindowStageWillDestroy(WindowStage)

```cangjie
public open func onWindowStageWillDestroy(windowStage: WindowStage): Unit
```

**功能：** 当WindowStage即将销毁时调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|windowStage|[WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage)|是|-|[WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage)相关信息。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.AppLog
import kit.AbilityKit.*

class MainAbility <: UIAbility {
    public override func onWindowStageWillDestroy(windowStage: WindowStage): Unit {
        AppLog.info("onWindowStageWillDestroy called")
    }
}
```