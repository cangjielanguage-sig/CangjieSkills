## enum OnContinueResult

```cangjie
public enum OnContinueResult {
    | AGREE
    | REJECT
    | MISMATCH
    | ...
}
```

**功能：** 表示同意。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### AGREE

```cangjie
AGREE
```

**功能：** 表示同意。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### MISMATCH

```cangjie
MISMATCH
```

**功能：** 表示版本不匹配：迁移发起端应用可以在[onContinue](cj-apis-ability.md#func-oncontinuestring)中获取到迁移目标端应用的版本号，进行协商后，如果版本不匹配导致无法迁移，可以返回该错误。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### REJECT

```cangjie
REJECT
```

**功能：** 表示拒绝：如应用在[onContinue](cj-apis-ability.md#func-oncontinuestring)中异常会导致迁移以后数据恢复时显示异常，则可以建议REJECT。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12