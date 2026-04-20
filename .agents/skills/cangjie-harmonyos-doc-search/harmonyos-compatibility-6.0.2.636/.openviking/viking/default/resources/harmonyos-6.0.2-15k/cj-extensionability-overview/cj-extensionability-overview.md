# ExtensionAbility组件

[ExtensionAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-extensionability)组件是基于特定场景（例如服务卡片、输入法等）提供的应用组件，以便满足更多的使用场景。

每一个具体场景对应一个[ExtensionAbilityType](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-bundle_manager.md#enum-extensionabilitytype)，开发者只能使用（包括实现和访问）系统已定义的类型。各类型的ExtensionAbility组件均由相应的系统服务统一管理。

当前系统已定义的ExtensionAbility类型如下表所示。

> **说明：**
>
> - “是否允许三方应用实现”是指：对于一类ExtensionAbility，三方应用能否继承该ExtensionAbility父类实现自己的业务逻辑。
> - “是否允许三方应用访问”是指：有些ExtensionAbility会对外提供一些服务，这些ExtensionAbility可能允许三方访问，也可能不允许。
> - “是否有独立Extension沙箱”是指：已经开发Extension都是和主应用共沙箱运行，API18及其之后新增Extension默认独立沙箱运行，输入法Extension由于安全机制管控改为独立沙箱运行。
> - “启动Extension传递共享数据是否严格模式访问”是指：共享数据可通过配置应用的data-group-ids和ExtensionAbility的[dataGroupIds](../cj-start/basic-knowledge/module-configuration-file.md)实现。严格模式访问表示只读，非严格模式访问表示可以读写。

对于系统应用，不受下表约束，允许实现系统已定义的各类ExtensionAbility，也允许访问提供的各类对外服务。

| ExtensionAbility类型                 | 功能描述 | 是否允许三<br/>方应用实现                  | 是否允许三<br/>方应用访问                                                 | 是否有独立<br/>Extension沙箱                  | 启动Extension<br/>传递共享数据<br/>是否严格模式访问                  |
| ------------------------ | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [EmbeddedUIExtensionAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-embeddeduiextensionability) | EMBEDDED_UI类型的ExtensionAbility组件，用于提供跨进程界面嵌入的能力。 | 是 | 是 | 否 | 非严格模式访问共享数据，可以读写共享数据。 |
| [ShareExtensionAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-shareextensionability) | SHARE类型的ExtensionAbility组件，用于提供分享模板服务扩展的能力。 | 是 | 是 | 否 | 非严格模式访问共享数据，可以读写共享数据。 |

## 访问指定类型的ExtensionAbility组件

所有类型的[ExtensionAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-extensionability)组件均不能被应用直接启动，而是由相应的系统管理服务拉起，以确保其生命周期受系统管控，使用时拉起，使用完销毁。ExtensionAbility组件的调用方无需关心目标ExtensionAbility组件的生命周期。

> **说明：**
>
> 同一应用内的所有同类型的ExtensionAbility运行在同一独立进程，跟UIAbility组件不在同一进程，Stage模型的进程模型请参见[进程模型](./cj-process-model-stage.md)。
