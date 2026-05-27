## class EnvironmentCallback

```cangjie
public class EnvironmentCallback {
    public EnvironmentCallback(
        public let onConfigurationUpdated!: (AbilityConfiguration) -> Unit,
        public let onMemoryLevel!: (MemoryLevel) -> Unit
    )
}
```

**功能：** EnvironmentCallback类提供应用上下文[ApplicationContext](#class-applicationcontext)对系统环境变化监听回调的能力。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

### let onConfigurationUpdated

```cangjie
public let onConfigurationUpdated:(AbilityConfiguration) -> Unit
```

**功能：** 注册系统环境变化的监听后，在系统环境变化时触发回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ([AbilityConfiguration](#class-abilityconfiguration))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onMemoryLevel

```cangjie
public let onMemoryLevel:(MemoryLevel) -> Unit
```

**功能：** 注册系统环境变化的监听后，在系统内存变化时触发回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ([MemoryLevel](#enum-memorylevel))->Unit

**读写能力：** 只读

**起始版本：** 19