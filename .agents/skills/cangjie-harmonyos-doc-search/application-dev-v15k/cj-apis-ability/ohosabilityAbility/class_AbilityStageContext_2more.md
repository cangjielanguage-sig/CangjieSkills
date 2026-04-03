## class AbilityStageContext

```cangjie
public class AbilityStageContext <: Context {
    public var hapModuleInfo: Option<CurrentHapInfo> = None
}
```

**功能：** [AbilityStageContext](#class-abilitystagecontext)提供允许访问特定于`abilityStage`的资源的能力，包括获取[AbilityStage](#class-abilitystage)对应的`hapModuleInfo`对象、环境变化对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**父类型：**

- [Context](#class-context)

### prop config

```cangjie
public prop config: AbilityConfiguration
```

**功能：** 环境变化对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [AbilityConfiguration](#class-abilityconfiguration)

**读写能力：** 只读

**起始版本：** 19

### prop currentHapModuleInfo

```cangjie
public prop currentHapModuleInfo: HapModuleInfo
```

**功能：** [AbilityStage](#class-abilitystage)对应的`hapModuleInfo`对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [HapModuleInfo](./cj-apis-bundle_manager.md#struct-hapmoduleinfo)

**读写能力：** 只读

**起始版本：** 19

### var hapModuleInfo

```cangjie
public var hapModuleInfo: Option<CurrentHapInfo> = None
```

**功能：** Hap模块信息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Option\<[CurrentHapInfo](#class-currenthapinfo)>

**读写能力：** 可读写

**起始版本：** 12

## class AbilityStartCallback

```cangjie
public class AbilityStartCallback {
    public AbilityStartCallback(
        public let onError: (Int32, String, String) -> Unit,
        public let onResult!: ?(AbilityResult) -> Unit = None
    )
}
```

**功能：** 定义拉起UIExtensionAbility执行结果的回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### let onError

```cangjie
public let onError: (Int32, String, String) -> Unit
```

**功能：** 拉起UIExtensionAbility执行失败的回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** (Int32, String, String)->Unit

**读写能力：** 只读

**起始版本：** 19

### let onResult

```cangjie
public let onResult: ?(AbilityResult) -> Unit = None
```

**功能：** 拉起UIExtensionAbility终止时的回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ?([AbilityResult](#struct-abilityresult))->Unit

**读写能力：** 只读

**起始版本：** 19

### AbilityStartCallback((Int32,String,String) -> Unit, ?(AbilityResult) -> Unit)

```cangjie
public AbilityStartCallback(
    public let onError: (Int32, String, String) -> Unit,
    public let onResult!: ?(AbilityResult) -> Unit = None
)
```

**功能：** AbilityStartCallback的主构造器。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onError|(Int32, String, String)->Unit|是|-|拉起UIExtensionAbility执行失败的回调。|
|onResult|?([AbilityResult](#struct-abilityresult))->Unit|否|None| **命名参数。** 拉起UIExtensionAbility终止时的回调。|