## enum AbilityLifecycleState

```cangjie
public enum AbilityLifecycleState <: Equatable<AbilityLifecycleState> & ToString {
    | UNINITIALIZED
    | CREATE
    | FOREGROUND
    | BACKGROUND
    | DESTROY
    | ...
}
```

**功能：** [UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)生命周期状态，该类型为枚举，可配合[AbilityDelegator](#class-abilitydelegator)的[getAbilityState](#func-getabilitystateuiability)方法返回不同ability生命周期。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**父类型：**

- Equatable\<[AbilityLifecycleState](#enum-abilitylifecyclestate)>
- ToString

### BACKGROUND

```cangjie
BACKGROUND
```

**功能：** 表示[UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)处于后台状态。

**起始版本：** 19

### CREATE

```cangjie
CREATE
```

**功能：** 表示[UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)处于已创建状态。

**起始版本：** 19

### DESTROY

```cangjie
DESTROY
```

**功能：** 表示[UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)处于已销毁状态。

**起始版本：** 19

### FOREGROUND

```cangjie
FOREGROUND
```

**功能：** 表示[UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)处于前台状态。

**起始版本：** 19

### UNINITIALIZED

```cangjie
UNINITIALIZED
```

**功能：** 表示[UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)处于无效状态。

**起始版本：** 19

### func !=(AbilityLifecycleState)

```cangjie
public operator func !=(other: AbilityLifecycleState): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AbilityLifecycleState](#enum-abilitylifecyclestate)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不等返回true，否则返回false。|

### func ==(AbilityLifecycleState)

```cangjie
public operator func ==(other: AbilityLifecycleState): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AbilityLifecycleState](#enum-abilitylifecyclestate)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|