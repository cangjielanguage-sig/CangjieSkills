## enum RestartFlag

```cangjie
public enum RestartFlag <: Equatable<RestartFlag> & ToString {
    | ALWAYS_RESTART
    | RESTART_WHEN_JS_CRASH
    | RESTART_WHEN_APP_FREEZE
    | NO_RESTART
    | ...
}
```

**功能：** 应用重启标志，[enableAppRecovery](#func-enableapprecoveryrestartflag-saveoccasionflag-savemodeflag)接口重启选项参数。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**父类型：**

- Equatable\<RestartFlag>

- ToString

### ALWAYS_RESTART

```cangjie
ALWAYS_RESTART
```

**功能：** 总是重启应用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### NO_RESTART

```cangjie
NO_RESTART
```

**功能：** 总是不重启应用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### RESTART_WHEN_APP_FREEZE

```cangjie
RESTART_WHEN_APP_FREEZE
```

**功能：** 发生APP_FREEZE时重启应用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### RESTART_WHEN_JS_CRASH

```cangjie
RESTART_WHEN_JS_CRASH
```

**功能：** 发生JS_CRASH时重启应用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func !=(RestartFlag)

```cangjie
public operator func !=(other: RestartFlag): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[RestartFlag](#enum-restartflag)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(RestartFlag)

```cangjie
public operator func ==(other: RestartFlag): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[RestartFlag](#enum-restartflag)|是|-|另一个枚举值。|

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