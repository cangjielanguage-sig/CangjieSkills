### 订阅进程内Ability生命周期变化

在应用内的DFX统计场景中，如需要统计对应页面停留时间和访问频率等信息，可以使用订阅进程内[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)生命周期变化功能。

通过[ApplicationContext](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-applicationcontext)提供的能力，可以订阅进程内Ability生命周期变化。当进程内的Ability生命周期变化时，如创建、可见/不可见、获焦/失焦、销毁等，会触发相应的回调函数。每次注册回调函数时，都会返回一个监听生命周期的ID，此ID会自增+1。当超过监听上限数量2<sup>63</sup>-1时，会返回-1。以[UIAbilityContext](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiabilitycontext)中的使用为例进行说明。

```cangjie
import kit.UIKit.{AppLog, BusinessException}
import kit.AbilityKit.{UIAbility, AbilityLifecycleCallback, LaunchParam, Want, ApplicationContextType}

var globalContext: ?UIAbilityContext = None

class MainAbility <: UIAbility {
    // 定义生命周期ID
    var lifecycleId: Int32 = 0
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        // 定义生命周期回调对象
        let abilityLifecycleCallback = AbilityLifecycleCallback(
            // 当Ability创建时被调用
            onAbilityCreate: {
                ability: UIAbility => AppLog.info("AbilityLifecycle onAbilityCreate")
            },
            // 当窗口创建时被调用
            onWindowStageCreate: {
                ability: UIAbility, windowStage: WindowStage => AppLog.info("AbilityLifecycle onWindowStageCreate")
            },
            // 当窗口处于活动状态时被调用
            onWindowStageActive: {
                ability: UIAbility, windowStage: WindowStage => AppLog.info("AbilityLifecycle onWindowStageActive")
            },
            // 当窗口处于非活动状态时被调用
            onWindowStageInactive: {
                ability: UIAbility, windowStage: WindowStage => AppLog.info("AbilityLifecycle onWindowStageInactive")
            },
            // 当窗口被销毁时被调用
            onWindowStageDestroy: {
                ability: UIAbility, windowStage: WindowStage => AppLog.info("AbilityLifecycle onWindowStageDestroy")
            },
            // 当Ability被销毁时被调用
            onAbilityDestroy: {
                ability: UIAbility => AppLog.info("AbilityLifecycle onAbilityDestroy")
            },
            // 当Ability从后台转到前台时触发回调
            onAbilityForeground: {
                ability: UIAbility => AppLog.info("AbilityLifecycle onAbilityForeground")
            },
            // 当Ability从前台转到后台时触发回调
            onAbilityBackground: {
                ability: UIAbility => AppLog.info("AbilityLifecycle onAbilityBackground")
            },
            // 当Ability迁移时被调用
            onAbilityContinue: {
                ability: UIAbility => AppLog.info("AbilityLifecycle onAbilityContinue")
            }
        )
        // 获取应用上下文
        let applicationContext = this.context.getApplicationContext()
        try {
            lifecycleId = applicationContext.on(ApplicationContextType.ABILITY_LIFE_CYCLE, abilityLifecycleCallback)
        } catch (e: BusinessException) {
            AppLog.error("Failed to register applicationContext. Code is ${e.code}, message is ${e.message}")
        }

        AppLog.info("register callback number: ${lifecycleId}")
    }

    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        AppLog.info("MainAbility onWindowStageCreate.")
        let properties = windowStage.getMainWindow().getWindowProperties()
        AppLog.info("onWindowStageCreate: ${properties.windowRect.width}")
        globalContext = this.context

        windowStage.loadContent("EntryView")
    }