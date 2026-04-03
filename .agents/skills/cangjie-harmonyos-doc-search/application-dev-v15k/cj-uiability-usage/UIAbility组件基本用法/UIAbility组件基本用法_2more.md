# UIAbility组件基本用法

[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)组件的基本用法包括：指定UIAbility的启动页面以及获取uiability的上下文信息[UIAbilityContext](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiabilitycontext)。

## 指定UIAbility的启动页面

应用中的[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)在启动过程中，需要指定启动页面，否则应用启动后会因为没有默认加载页面而导致白屏。可以在UIAbility的[onWindowStageCreate()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onwindowstagecreatewindowstage)生命周期回调中，通过[WindowStage](../../API_Reference/source_zh_cn/arkui-cj/cj-apis-window.md#class-windowstage)对象的[loadContent()](../../API_Reference/source_zh_cn/arkui-cj/cj-apis-window.md#class-windowstage)方法设置启动页面。

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