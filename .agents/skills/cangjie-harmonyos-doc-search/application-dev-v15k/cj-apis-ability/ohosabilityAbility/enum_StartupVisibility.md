## enum StartupVisibility

```cangjie
public enum StartupVisibility <: Equatable<StartupVisibility> & ToString {
    | STARTUP_HIDE
    | STARTUP_SHOW
    | ...
}
```

**功能：** Ability启动后的可见性。该功能仅在平板类设备上生效。
StartupVisibility作为[StartOptions](#class-startoptions)的一个属性，仅在[UIAbilityContext.startAbility](#func-startabilitywant-startoptions)中生效，用来指定目标Ability启动后的可见性。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**父类型：**

- Equatable\<StartupVisibility>

- ToString

### STARTUP_HIDE

```cangjie
STARTUP_HIDE
```

**功能：** 目标Ability启动后，进入隐藏状态。不会调用Ability的onForeground生命周期。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### STARTUP_SHOW

```cangjie
STARTUP_SHOW
```

**功能：** 目标Ability启动后，正常显示。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func !=(StartupVisibility)

```cangjie
public operator func !=(other: StartupVisibility): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[StartupVisibility](#enum-startupvisibility)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(StartupVisibility)

```cangjie
public operator func ==(other: StartupVisibility): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[StartupVisibility](#enum-startupvisibility)|是|-|另一个枚举值。|

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