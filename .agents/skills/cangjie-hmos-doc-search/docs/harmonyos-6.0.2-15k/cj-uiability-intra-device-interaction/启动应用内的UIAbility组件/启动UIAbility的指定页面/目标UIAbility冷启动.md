### 目标UIAbility冷启动

目标[UIAbility](../../../cj-apis-ability/.overview.md)冷启动时，在目标Ability的[onCreate()](../../../cj-apis-ability/.overview.md)生命周期回调中，接收调用方传过来的参数。然后在目标Ability的[onWindowStageCreate()](../../../cj-apis-ability/.overview.md)生命周期回调中，解析调用方传递过来的[Want](../../../cj-apis-ability/.overview.md)参数，获取到需要加载的页面信息url，传入[windowStage.loadContent()](../../../cj-apis-window/.overview.md)方法。

```cangjie
import ohos.base.AppLog
import std.collection.HashMap
import kit.AbilityKit.{UIAbility, LaunchParam, Want}

class FuncAbilityA <: UIAbility {
    var router = "Index"
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        // 接收调用方UIAbility传过来的参数
        let funcAbilityWant = want
        // want.parameters是一个json格式的字符串，用户可通过三方json库解析出router字段的值
    }

    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        AppLog.info("FuncAbilityA onWindowStageCreate.")
        windowStage.loadContent(router)
    }
}
```