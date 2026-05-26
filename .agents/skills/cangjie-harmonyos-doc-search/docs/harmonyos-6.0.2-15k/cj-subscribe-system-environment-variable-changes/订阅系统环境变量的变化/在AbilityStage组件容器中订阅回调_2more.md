## 在AbilityStage组件容器中订阅回调

使用[AbilityStage.onConfigurationUpdate()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onconfigurationupdateabilityconfiguration)回调方法订阅系统环境变量的变化。当系统环境变量发生变化时，会调用该回调方法。在该方法中，通过[AbilityConfiguration](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-abilityconfiguration)对象获取最新的系统环境配置信息。可以进行相应的界面适配等操作，从而提高系统的灵活性和可维护性。

> **说明：**
>
> - AbilityStage文件的创建请参见[AbilityStage组件容器](cj-abilitystage.md)。
> - 当使用回调方法订阅系统环境变量的变化时，该回调方法会随着AbilityStage的生命周期而存在，在Module销毁时一并销毁。

例如，在[AbilityStage.onConfigurationUpdate()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onconfigurationupdateabilityconfiguration)回调方法中实现监测系统语言的变化。

```cangjie
import kit.UIKit.AppLog
import kit.AbilityKit.{AbilityStage, AbilityConfiguration}

var systemLanguage = "" // 系统当前语言

class MyAbilityStage <: AbilityStage {
    public override func onCreate(): Unit {
        systemLanguage = this.context.config.language // Module首次加载时，获取系统当前语言
        AppLog.info("systemLanguage is ${systemLanguage}")
        // ...
    }

    public override func onConfigurationUpdate(newConfig: AbilityConfiguration): Unit {
        AppLog.info("onConfigurationUpdated systemLanguage is ${systemLanguage}")
        if (systemLanguage != newConfig.language) {
            AppLog.info("systemLanguage from ${systemLanguage} changed to ${newConfig.language}")
            systemLanguage = newConfig.language // 将变化之后的系统语言保存，作为下一次变化前的系统语言
        }
    }
}
```

## 在UIAbility组件中订阅回调

[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)组件提供了[UIAbility.onConfigurationUpdate()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onconfigurationupdateabilityconfiguration-1)回调方法用于订阅系统环境变量的变化。当系统环境变量发生变化时，会调用该回调方法。在该方法中，通过[AbilityConfiguration](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-abilityconfiguration)对象获取最新的系统环境配置信息，而无需重启UIAbility。

> **说明：**
>
> 当使用回调方法订阅系统环境变量的变化时，该回调方法会随着UIAbility的生命周期而存在，在UIAbility销毁时一并销毁。

例如，在[onConfigurationUpdate()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onconfigurationupdateabilityconfiguration-1)回调方法中实现监测系统语言的变化。

```cangjie
import kit.AbilityKit.{UIAbility, Want, AbilityConfiguration, LaunchParam}
import kit.UIKit.AppLog

var systemLanguage = "" // 系统当前语言

class MainAbility <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        systemLanguage = this.context.config.language // Module首次加载时，获取系统当前语言
        AppLog.info("systemLanguage is ${systemLanguage}")
        // ...
    }

    public override func onConfigurationUpdate(newConfig: AbilityConfiguration): Unit {
        AppLog.info("onConfigurationUpdated systemLanguage is ${systemLanguage}")
        if (systemLanguage != newConfig.language) {
            AppLog.info("systemLanguage from ${systemLanguage} changed to ${newConfig.language}")
            systemLanguage = newConfig.language // 将变化之后的系统语言保存，作为下一次变化前的系统语言
        }
    }
    // ...
}
```