## enum ExecuteMode

```cangjie
public enum ExecuteMode <: Equatable<ExecuteMode> & ToString {
    | UIAbilityForeground
    | UIAbilityBackground
    | UIExtensionAbility
    | ...
}
```

**功能：** 意图调用执行模式。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 20

**父类型：**

- Equatable\<ExecuteMode>
- ToString

### UIAbilityBackground

```cangjie
UIAbilityBackground
```

**功能：** 将UIAbility在前台显示。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 20

### UIAbilityForeground

```cangjie
UIAbilityForeground
```

**功能：** 将UIAbility在后台拉起。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 20

### UIExtensionAbility

```cangjie
UIExtensionAbility
```

**功能：** 拉起UIExtensionAbility。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 20

### func !=(ExecuteMode)

```cangjie
public operator func !=(other: ExecuteMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ExecuteMode](#enum-executemode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ExecuteMode)

```cangjie
public operator func ==(other: ExecuteMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ExecuteMode](#enum-executemode)|是|-|另一个枚举值。|

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

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|