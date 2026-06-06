## enum StateType

```cangjie
public enum StateType <: Equatable<StateType> & ToString {
    | CONTINUATION
    | APP_RECOVERY
    | ...
}
```

**功能：** 保存应用数据场景原因，该类型为枚举，可配合Ability的[onSaveState(reason, wantParam)](cj-apis-ability.md#func-onsavestatestatetype-string)方法根据reason的不同类型执行相应操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**父类型：**

- Equatable\<StateType>

### APP_RECOVERY

```cangjie
APP_RECOVERY
```

**功能：** 应用恢复保存状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### CONTINUATION

```cangjie
CONTINUATION
```

**功能：** 迁移保存状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func !=(StateType)

```cangjie
public operator func !=(other: StateType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[StateType](#enum-statetype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(StateType)

```cangjie
public operator func ==(other: StateType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[StateType](#enum-statetype)|是|-|另一个枚举值。|

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