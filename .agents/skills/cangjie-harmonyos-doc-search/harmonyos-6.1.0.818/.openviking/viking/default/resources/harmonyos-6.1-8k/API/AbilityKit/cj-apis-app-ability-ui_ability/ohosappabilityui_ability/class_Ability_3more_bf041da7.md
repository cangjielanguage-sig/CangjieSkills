## class Ability

```cangjie
abstract sealed class Ability {}
```

**功能：** [UIAbility](#class-uiability)和ExtensionAbility的基类，提供系统配置更新回调和系统内存调整回调。不支持开发者直接继承该基类。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 22

## class AbilityStageContext

```cangjie
public class AbilityStageContext <: Context {
    public var currentHapModuleInfo: HapModuleInfo
}
```

**功能：** AbilityStageContext是AbilityStage的上下文环境。

AbilityStageContext提供允许访问特定于abilityStage的资源的能力，包括获取AbilityStage对应的ModuleInfo对象、环境变化对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**父类型：**

- [Context](./cj-apis-app-ability-ui_ability.md#class-context)

### var currentHapModuleInfo

```cangjie
public var currentHapModuleInfo: HapModuleInfo
```

**功能：** AbilityStage对应的ModuleInfo对象。

**类型：** [HapModuleInfo](./cj-apis-bundle_manager.md#class-hapmoduleinfo)

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*

class MyAbilityStage5 <: AbilityStage {
    public override func onCreate(): Unit {
        let info = this.context.currentHapModuleInfo
    }
}
```

## class ApplicationContext

```cangjie
public class ApplicationContext <: Context {}
```

**功能：** ApplicationContext作为应用上下文，提供了应用生命周期监听、进程管理、应用环境设置等应用级别的管控能力。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**父类型：**

- [Context](./cj-apis-app-ability-ui_ability.md#class-context)