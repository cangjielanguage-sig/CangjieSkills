### 目标UIAbility冷启动

目标[UIAbility](../reference/AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)冷启动时，在目标Ability的[onCreate()](../reference/AbilityKit/cj-apis-app-ability-ui_ability.md#func-oncreatewant-launchparam)生命周期回调中，接收调用方传过来的参数。然后在目标Ability的[onWindowStageCreate()](../reference/AbilityKit/cj-apis-app-ability-ui_ability.md#func-onwindowstagecreatewindowstage)生命周期回调中，解析调用方传递过来的[Want](../reference/AbilityKit/cj-apis-app-ability-want.md#class-want)参数，获取到需要加载的页面信息url，传入[windowStage.loadContent()](../reference/arkui-cj/cj-apis-window.md#class-windowstage)方法。

<!-- compile -->

```cangjie
import std.collection.HashMap
import kit.AbilityKit.{UIAbility, LaunchParam, Want}
import kit.PerformanceAnalysisKit.Hilog

class FuncAbilityA <: UIAbility {
    var router = "Index"
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        // 接收调用方UIAbility传过来的参数
        let funcAbilityWant = want
        // want.parameters是一个json格式的字符串，用户可通过三方json库解析出router字段的值
    }

    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        Hilog.info(0, "device_interaction", "FuncAbilityA onWindowStageCreate.")
        windowStage.loadContent(router)
    }
}
```