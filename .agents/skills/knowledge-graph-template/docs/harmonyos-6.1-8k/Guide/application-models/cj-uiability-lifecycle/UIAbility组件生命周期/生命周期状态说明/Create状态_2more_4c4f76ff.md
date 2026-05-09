### Create状态

Create状态为在应用加载过程中，[UIAbility](../reference/AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)实例创建完成时触发，系统会调用[onCreate()](../reference/AbilityKit/cj-apis-app-ability-ui_ability.md#func-oncreatewant-launchparam)回调。可以在该回调中进行页面初始化操作，例如变量定义资源加载等，用于后续的UI展示。

<!-- compile -->

```cangjie
import kit.AbilityKit.UIAbility
import kit.AbilityKit.Want

class MainAbility <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
      // 页面初始化
    }
    // ...
}
```

> **说明：**
>
> [Want](../reference/AbilityKit/cj-apis-app-ability-want.md#class-want)是对象间信息传递的载体，可以用于应用组件间的信息传递。Want的详细介绍请参见[信息传递载体Want](cj-want-overview.md)。

### WindowStageCreate和WindowStageDestroy状态

[UIAbility](../reference/AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)实例创建完成之后，在进入Foreground之前，系统会创建一个WindowStage。WindowStage创建完成后会进入[onWindowStageCreate()](../reference/AbilityKit/cj-apis-app-ability-ui_ability.md#func-onwindowstagecreatewindowstage)回调，可以在该回调中设置UI加载、设置WindowStage的事件订阅。

**图2** WindowStageCreate和WindowStageDestroy状态

![Ability-Life-Cycle-WindowStage](figures/Ability-Life-Cycle-WindowStage.png)<!-- ToBeReviewd -->

在onWindowStageCreate()回调中通过[loadContent()](../reference/arkui-cj/cj-apis-window.md#func-loadcontentstring)方法设置应用要加载的页面。

<!-- compile -->

```cangjie
import kit.AbilityKit.UIAbility
import kit.ArkUI.WindowStage

class MainAbility <: UIAbility {
    // ...
    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        // 设置UI加载
        windowStage.loadContent("EntryView")
    }
}
```

> **说明：**
>
> WindowStage的相关使用请参见[窗口开发指导](../windowmanager/cj-application-window-stage.md)。