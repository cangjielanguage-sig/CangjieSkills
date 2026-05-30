**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.AbilityKit.*

var callId: Int32 = 0

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
        let abilityLifecycleCallback = AbilityLifecycleCallback(
            onAbilityCreate: {
                ability: UIAbility => AppLog.info("AbilityLifecycle onAbilityCreate")
            },
            onWindowStageCreate: {
                ability: UIAbility, windowStage: WindowStage => AppLog.info("AbilityLifecycle onWindowStageCreate")
            },
            onWindowStageActive: {
                ability: UIAbility, windowStage: WindowStage => AppLog.info("AbilityLifecycle onWindowStageActive")
            },
            onWindowStageInactive: {
                ability: UIAbility, windowStage: WindowStage => AppLog.info("AbilityLifecycle onWindowStageInactive")
            },
            onWindowStageDestroy: {
                ability: UIAbility, windowStage: WindowStage => AppLog.info("AbilityLifecycle onWindowStageDestroy")
            },
            onAbilityDestroy: {
                ability: UIAbility => AppLog.info("AbilityLifecycle onAbilityDestroy")
            },
            onAbilityForeground: {
                ability: UIAbility => AppLog.info("AbilityLifecycle onAbilityForeground")
            },
            onAbilityBackground: {
                ability: UIAbility => AppLog.info("AbilityLifecycle onAbilityBackground")
            },
            onAbilityContinue: {
                ability: UIAbility => AppLog.info("AbilityLifecycle onAbilityContinue")
            },
            onAbilityWillCreate: {
                ability: UIAbility => AppLog.info("AbilityLifecycle onAbilityWillCreate")
            },
            onWindowStageWillCreate: {
                ability: UIAbility, windowStage: WindowStage => AppLog.info("AbilityLifecycle onWindowStageWillCreate")
            },
            onWindowStageWillDestroy: {
                ability: UIAbility, windowStage: WindowStage => AppLog.info("AbilityLifecycle onWindowStageWillDestroy")
            },
            onAbilityWillForeground: {
                ability: UIAbility => AppLog.info("AbilityLifecycle onAbilityWillForeground")
            },
            onAbilityWillDestroy: {
                ability: UIAbility => AppLog.info("AbilityLifecycle onAbilityWillDestroy")
            },
            onAbilityWillBackground: {
                ability: UIAbility => AppLog.info("AbilityLifecycle onAbilityWillBackground")
            },
            onWillNewWant: {
                ability: UIAbility => AppLog.info("AbilityLifecycle onWillNewWant")
            },
            onNewWant: {
                ability: UIAbility => AppLog.info("AbilityLifecycle onNewWant")
            },
            onAbilityWillContinue: {
                ability: UIAbility => AppLog.info("AbilityLifecycle onAbilityWillContinue")
            },
            onWindowStageWillRestore: {
                ability: UIAbility, windowStage: WindowStage => AppLog.info("AbilityLifecycle onWindowStageWillRestore")
            },
            onWindowStageRestore: {
                ability: UIAbility, windowStage: WindowStage => AppLog.info("AbilityLifecycle onWindowStageRestore")
            },
            onAbilityWillSaveState: {
                ability: UIAbility => AppLog.info("AbilityLifecycle onAbilityWillSaveState")
            },
            onAbilitySaveState: {
                ability: UIAbility => AppLog.info("AbilityLifecycle onAbilitySaveState")
            }
        )
        let appcontext = this.context.getApplicationContext()
        callId = appcontext.on(ApplicationContextType.ABILITY_LIFE_CYCLE, abilityLifecycleCallback)
        AppLog.info("Register AbilityLifecycle success and id is ${callId}.")
    }

    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        AppLog.info("MainAbility onWindowStageCreate.")
        let properties = windowStage.getMainWindow().getWindowProperties()
        AppLog.info("onWindowStageCreate: ${properties.windowRect.width}")
        windowStage.loadContent("EntryView")
    }
}
```