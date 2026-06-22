## 在ExtensionAbility组件中订阅回调

[ExtensionAbility](../../cj-apis-ability/.overview.md)组件提供了[onConfigurationUpdate()](../../cj-apis-ability/.overview.md)回调方法用于订阅系统环境变量的变化。当系统环境变量发生变化时，会调用该回调方法。在该方法中，通过[AbilityConfiguration](../../cj-apis-ability/.overview.md)对象获取最新的系统环境配置信息。

> **说明：**
>
> 当使用回调方法订阅系统环境变量的变化时，该回调方法会随着ExtensionAbility的生命周期而存在，在ExtensionAbility销毁时一并销毁。

以[PhotoEditorExtensionAbility](../../cj-apis-ability/.overview.md)为例说明。例如，在[onConfigurationUpdate()](../../cj-apis-ability/.overview.md)回调方法中实现系统环境变量的变化。

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