### WindowStageWillDestroy状态

对应[onWindowStageWillDestroy()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#let-onwindowstagewilldestroy)回调，在WindowStage销毁前执行，此时WindowStage可以使用。

```cangjie
import kit.AbilityKit.UIAbility
import kit.ArkUI.{WindowStage, WindowCallbackType}
import ohos.base.{AppLog, BusinessException}

class MainAbility <: UIAbility {
    // ...
    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        // ...
    }

    public override func onWindowStageWillDestroy(windowStage: WindowStage): Unit {
        // 释放通过windowStage对象获取的资源
        // 在onWindowStageWillDestroy()中注销WindowStage事件订阅（获焦/失焦、切到前台/切到后台、前台可交互/前台不可交互）
        try {
            windowStage.off(WindowStageEvent)
        } catch (e: BusinessException) {
            AppLog.error(
                "Failed to disable the listener for windowStageEvent. Code is ${e.code}, message is ${e.message}")
        }
    }

    public override func onWindowStageDestroy(): Unit {
        // 释放UI资源
    }
}
```

> **说明：**
>
> WindowStage的相关使用请参见[窗口开发指导](../../API_Reference/source_zh_cn/arkui-cj/cj-apis-window.md)。