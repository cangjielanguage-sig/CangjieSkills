## class ApplicationStateChangeCallback

```cangjie
public class ApplicationStateChangeCallback {
    public ApplicationStateChangeCallback(
        public let onApplicationForeground!: () -> Unit,
        public let onApplicationBackground!: () -> Unit
    )
}
```

**功能：** ApplicationStateChangeCallback类提供应用上下文提供应用上下文[ApplicationContext](#class-applicationcontext)对当前应用前后台变化监听回调的能力。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

### let onApplicationBackground

```cangjie
public let onApplicationBackground:() -> Unit
```

**功能：** 注册当前应用前后台变化的监听后，在当前应用从前台切换到后台时触发回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ()->Unit

**读写能力：** 只读

**起始版本：** 19

### let onApplicationForeground

```cangjie
public let onApplicationForeground:() -> Unit
```

**功能：** 注册当前应用前后台变化的监听后，在当前应用从后台切换到前台时触发回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ()->Unit

**读写能力：** 只读

**起始版本：** 19

### ApplicationStateChangeCallback(() -> Unit, () -> Unit)

```cangjie
public ApplicationStateChangeCallback(
    public let onApplicationForeground!: () -> Unit,
    public let onApplicationBackground!: () -> Unit
)
```

**功能：** ApplicationStateChangeCallback类的主构造器。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onApplicationForeground|()->Unit|是|-| **命名参数。** 注册当前应用前后台变化的监听后，在当前应用从后台切换到前台时触发回调。|
|onApplicationBackground|()->Unit|是|-| **命名参数。** 注册当前应用前后台变化的监听后，在当前应用从前台切换到后台时触发回调。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.AbilityKit.*

class MainAbility <: UIAbility {
    public init() {
        super()
        registerSelf()
    }

    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("MainAbility OnCreated.${want.abilityName}")
        match (launchParam.launchReason) {
            case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
            case _ => ()
        }
        let callback = ApplicationStateChangeCallback(
            onApplicationForeground: {
                => AppLog.info("ApplicationStateChangeCallback onApplicationForeground")
            },
            onApplicationBackground: {
                => AppLog.info("ApplicationStateChangeCallback onApplicationBackground")
            }
        )
        let appcontext = this.context.getApplicationContext()
        appcontext.on(ApplicationContextType.APPLICATION_STATE_CHANGE, callback)
    }

    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        AppLog.info("MainAbility onWindowStageCreate.")
        let properties = windowStage.getMainWindow().getWindowProperties()
        AppLog.info("onWindowStageCreate: ${properties.windowRect.width}")
        windowStage.loadContent("EntryView")
    }
}
```