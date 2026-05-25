## enum ContinueState

```cangjie
public enum ContinueState <: Equatable<ContinueState> & ToString {
    | ACTIVE
    | INACTIVE
    | ...
}
```

**功能：** 流转状态枚举值。用于表示当前应用任务流转的状态。可配合AbilityContext的[setMissionContinueState](#func-setmissioncontinuestatecontinuestate)方法进行设置。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**父类型：**

- Equatable\<ContinueState>

- ToString

### ACTIVE

```cangjie
ACTIVE
```

**功能：** 指示当前应用任务流转处于激活状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### INACTIVE

```cangjie
INACTIVE
```

**功能：** 指示当前应用任务流转处于未激活状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func !=(ContinueState)

```cangjie
public operator func !=(other: ContinueState): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ContinueState](#enum-continuestate)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ContinueState)

```cangjie
public operator func ==(other: ContinueState): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ContinueState](#enum-continuestate)|是|-|另一个枚举值。|

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