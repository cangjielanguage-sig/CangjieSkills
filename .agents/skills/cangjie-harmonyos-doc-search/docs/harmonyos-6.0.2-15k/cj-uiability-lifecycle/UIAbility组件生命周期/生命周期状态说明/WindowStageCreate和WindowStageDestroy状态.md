### WindowStageCreate和WindowStageDestroy状态

[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)实例创建完成之后，在进入Foreground之前，系统会创建一个WindowStage。WindowStage创建完成后会进入[onWindowStageCreate()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onwindowstagecreatewindowstage)回调，可以在该回调中设置UI加载、设置WindowStage的事件订阅。

**图2** WindowStageCreate和WindowStageDestroy状态

![Ability-Life-Cycle-WindowStage](figures/Ability-Life-Cycle-WindowStage.png)

在onWindowStageCreate()回调中通过[loadContent()](../../API_Reference/source_zh_cn/arkui-cj/cj-apis-window.md#class-windowstage)方法设置应用要加载的页面，并根据需要调用[on('windowStageEvent')](../../API_Reference/source_zh_cn/arkui-cj/cj-apis-window.md#func-onwindowcallbacktype-callback1argumentwindowstageeventtype)方法订阅[WindowStage的事件](../../API_Reference/source_zh_cn/arkui-cj/cj-apis-window.md#enum-windowstageeventtype)（获焦/失焦、切到前台/切到后台、前台可交互/前台不可交互）。

> **说明：**
>
> 不同开发场景下[WindowStage事件](../../API_Reference/source_zh_cn/arkui-cj/cj-apis-window.md#enum-windowstageeventtype)的时序可能存在差异。

```cangjie
import kit.AbilityKit.UIAbilityContext
import kit.AbilityKit.UIAbility
import kit.ArkUI.{WindowStage, WindowCallbackType, WindowStageEventType}
import ohos.base.{AppLog, Callback1Argument, BusinessException}

class WindowStageCallback <: Callback1Argument<WindowStageEventType> {
    public override func invoke(arg: WindowStageEventType) {
        match (arg) {
            case WindowStageEventType.SHOWN => // 切到前台
                AppLog.info("windowStage foreground.")
            case WindowStageEventType.ACTIVE => // 获焦状态
                AppLog.info("windowStage active.")
            case WindowStageEventType.INACTIVE => // 失焦状态
                AppLog.info("windowStage inactive.")
            case WindowStageEventType.HIDDEN => // 切到后台
                AppLog.info("windowStage background.")
            case WindowStageEventType.RESUMED => // 前台可交互状态
                AppLog.info("windowStage resumed.")
            case WindowStageEventType.PAUSED => // 前台不可交互状态
                AppLog.info("windowStage paused.")
            case _ => ()
        }
    }
}

class MainAbility <: UIAbility {
    // ...
    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        // 设置WindowStage的事件订阅（获焦/失焦、切到前台/切到后台、前台可交互/前台不可交互）
        try {
            windowStage.on(WindowStageEvent, WindowStageCallback())
        } catch (e: BusinessException) {
            AppLog.error("Failed to enable the listener for window stage event changes. Cause: ${e.message}");
        }
        // 设置UI加载
        windowStage.loadContent("EntryView")
    }
}
```

> **说明：**
>
> WindowStage的相关使用请参见[窗口开发指导](../../API_Reference/source_zh_cn/arkui-cj/cj-apis-window.md)。

对应于[onWindowStageCreate()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onwindowstagecreatewindowstage)回调。在[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)实例销毁之前，则会先进入[onWindowStageDestroy()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#let-onwindowstagedestroy)回调，可以在该回调中释放UI资源。

```cangjie
import kit.AbilityKit.UIAbility
import kit.ArkUI.WindowStage

class MainAbility <: UIAbility {
    // ...
    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        // ...
    }

    public override func onWindowStageDestroy(): Unit {
        // 释放UI资源
    }
}
```