## 接口说明

[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)备份恢复接口由[UIAbilityContext](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiabilitycontext)模块提供，开发者可以通过在[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)中通过this.context直接调用，详情请参见[开发步骤](#开发步骤)。

| 接口名称                                                       | 说明                                                 |
| ------------------------------------------------------------ | ---------------------------------------------------- |
| setRestoreEnabled(enabled: Bool): Unit | 设置当[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)从后台切换回时是否启用恢复。|

**[setRestoreEnabled](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-setrestoreenabledbool)：** 需要在应用初始化阶段调用（[onForeground](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onforeground)前），比如[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)的[onCreate](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-oncreatewant-launchparam)调用。

## 开发步骤

开发者需要在应用模块初始化时启用[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)备份恢复功能。

```cangjie
import kit.AbilityKit.{UIAbility, UIAbilityContext, LaunchParam, Want}

class MainAbility <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        this.context.setRestoreEnabled(true)
    }
}
```

开发者主动保存数据，在UIAbility启动时恢复。

```cangjie
import kit.UIKit.AppLog
import kit.AbilityKit.{UIAbility, UIAbilityContext, Want, LaunchParam, OnSaveResult, StateType}

class MainAbility <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        this.context.setRestoreEnabled(true)
        if (want.parameters != "") {
            // parameters是一个json格式的字符串，用户可通过三方json库解析出myData字段的值
        }
    }

    public override func onSaveState(reason: StateType, wantParam: String): OnSaveResult {
        // Ability has called to save app data
        if (wantParam != "") {
            // wantParam是一个json格式的字符串，用户可通过三方json库解析出myData字段的值
        }
        return OnSaveResult.ALL_AGREE
    }
}
```