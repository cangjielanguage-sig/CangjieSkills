# UIAbility组件基本用法

[UIAbility](../../cj-apis-ability/.overview.md)组件的基本用法包括：指定UIAbility的启动页面以及获取uiability的上下文信息[UIAbilityContext](../../cj-apis-ability/.overview.md)。

## 指定UIAbility的启动页面

应用中的[UIAbility](../../cj-apis-ability/.overview.md)在启动过程中，需要指定启动页面，否则应用启动后会因为没有默认加载页面而导致白屏。可以在UIAbility的[onWindowStageCreate()](../../cj-apis-ability/.overview.md)生命周期回调中，通过[WindowStage](../../cj-apis-window/.overview.md)对象的[loadContent()](../../cj-apis-window/.overview.md)方法设置启动页面。

```cangjie
import kit.AbilityKit.UIAbility
import kit.ArkUI.WindowStage

class MainAbility <: UIAbility {
    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        // Main window is created, set main page for this ability
        windowStage.loadContent("EntryView")
    }
    // ...
}
```

> **说明：**
>
> 在DevEco Studio中创建的UIAbility中，该UIAbility实例默认会加载Index页面，根据需要将Index页面类名替换为需要的页面类名即可。