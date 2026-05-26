## enum Params

```cangjie
public enum Params <: Equatable<Params> & ToString {
    | ABILITY_BACK_TO_OTHER_MISSION_STACK
    | ABILITY_RECOVERY_RESTART
    | CONTENT_TITLE_KEY
    | SHARE_ABSTRACT_KEY
    | SHARE_URL_KEY
    | SUPPORT_CONTINUE_PAGE_STACK_KEY
    | SUPPORT_CONTINUE_SOURCE_EXIT_KEY
    | CALLER_REQUEST_CODE
    | APP_CLONE_INDEX_KEY
    | PARAMS_STREAM
    | SHOW_MODE_KEY
    | SUB_PACKAGE_NAME
    | BUILD_FUNCTION
    | PAGE_SOURCE_FILE
    | ROUTER_NAME
    | PAGE_PATH
    | ...
}
```

**功能：** [Want](#class-want)的Params操作。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 12

**父类型：**

- Equatable\<Params>

- ToString

### ABILITY_BACK_TO_OTHER_MISSION_STACK

```cangjie
ABILITY_BACK_TO_OTHER_MISSION_STACK
```

**功能：** 表示是否支持跨任务链返回。值为：ability.params.backToOtherMissionStack。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### ABILITY_RECOVERY_RESTART

```cangjie
ABILITY_RECOVERY_RESTART
```

**功能：** 指示当前Ability是否发生了故障恢复重启。值为：ohos.ability.params.abilityRecoveryRestart。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### APP_CLONE_INDEX_KEY

```cangjie
APP_CLONE_INDEX_KEY
```

**功能：** 指示分身应用索引。值为：ohos.extra.param.key.appCloneIndex。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### BUILD_FUNCTION

```cangjie
BUILD_FUNCTION
```

**功能：** 指示构建函数。值为：ohos.param.atomicservice.buildFunction。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### CALLER_REQUEST_CODE

```cangjie
CALLER_REQUEST_CODE
```

**功能：** 当调用[startAbilityForResult](#func-startabilityforresultwant-asynccallbackabilityresult)拉起目标方[UIAbility](#class-uiability)时, 需要目标方返回结果。为了确保目标方能够将结果准确返回到调用方，系统会自动生成唯一的requestCode，以标识本次调用。值为：ohos.extra.param.key.callerRequestCode。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### CONTENT_TITLE_KEY

```cangjie
CONTENT_TITLE_KEY
```

**功能：** 指示元服务支持分享标题的参数的操作。值为：ohos.extra.param.key.contentTitle。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### PAGE_PATH

```cangjie
PAGE_PATH
```

**功能：** 指示页面路径。值为：ohos.param.atomicservice.pagePath。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### PAGE_SOURCE_FILE

```cangjie
PAGE_SOURCE_FILE
```

**功能：** 指示页面源文件。值为：ohos.param.atomicservice.pageSourceFile。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### PARAMS_STREAM

```cangjie
PARAMS_STREAM
```

**功能：** 指示携带的文件URI要授权给目标方。对应的value必须是String类型的文件URI数组。值为：ability.params.stream。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### ROUTER_NAME

```cangjie
ROUTER_NAME
```

**功能：** 指示路由名。值为：ohos.param.atomicservice.routerName。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### SHARE_ABSTRACT_KEY

```cangjie
SHARE_ABSTRACT_KEY
```

**功能：** 指示元服务支持分享内容的参数的操作。值为：ohos.extra.param.key.shareAbstract。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### SHARE_URL_KEY

```cangjie
SHARE_URL_KEY
```

**功能：** 指示元服务支持分享链接的参数的操作。值为：ohos.extra.param.key.shareUrl。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12