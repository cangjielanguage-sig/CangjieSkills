## 在ExtensionAbility组件中订阅回调

[ExtensionAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-extensionability)组件提供了[onConfigurationUpdate()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onconfigurationupdateabilityconfiguration-1)回调方法用于订阅系统环境变量的变化。当系统环境变量发生变化时，会调用该回调方法。在该方法中，通过[AbilityConfiguration](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-abilityconfiguration)对象获取最新的系统环境配置信息。

> **说明：**
>
> 当使用回调方法订阅系统环境变量的变化时，该回调方法会随着ExtensionAbility的生命周期而存在，在ExtensionAbility销毁时一并销毁。

以[PhotoEditorExtensionAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-photoeditorextensionability)为例说明。例如，在[onConfigurationUpdate()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onconfigurationupdateabilityconfiguration-1)回调方法中实现系统环境变量的变化。

```cangjie
import kit.AbilityKit.{PhotoEditorExtensionAbility, AbilityConfiguration}

class ExamplePhotoEditorAbility <: PhotoEditorExtensionAbility {
    public override func onCreate(): Unit {
        AppLog.info("ExamplePhotoEditorAbility OnCreated.")
    }

    public override func onConfigurationUpdate(newConfig: AbilityConfiguration): Unit {
        AppLog.info("[ExamplePhotoEditorAbility] onConfigurationUpdate: ${newConfig.language}")
    }
    // ...
}
```