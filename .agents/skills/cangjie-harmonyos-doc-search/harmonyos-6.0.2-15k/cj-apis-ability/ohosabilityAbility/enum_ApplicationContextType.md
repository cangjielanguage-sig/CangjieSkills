## enum ApplicationContextType

```cangjie
public enum ApplicationContextType <: Equatable<ApplicationContextType> {
    | ENVIRONMENT
    | ABILITY_LIFE_CYCLE
    | APPLICATION_STATE_CHANGE
    | ...
}
```

**功能：** 用于描述注册回调所支持的数据类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**父类型：**

- Equatable\<ApplicationContextType>

### ABILITY_LIFE_CYCLE

```cangjie
ABILITY_LIFE_CYCLE
```

**功能：** 监听应用内生命周期。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### APPLICATION_STATE_CHANGE

```cangjie
APPLICATION_STATE_CHANGE
```

**功能：** 监听当前应用前后台变化。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### ENVIRONMENT

```cangjie
ENVIRONMENT
```

**功能：** 监听系统环境变化。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func !=(ApplicationContextType)

```cangjie
public operator func !=(other: ApplicationContextType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ApplicationContextType](#enum-applicationcontexttype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ApplicationContextType)

```cangjie
public operator func ==(other: ApplicationContextType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ApplicationContextType](#enum-applicationcontexttype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|