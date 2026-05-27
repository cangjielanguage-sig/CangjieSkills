## class LaunchParam

```cangjie
public class LaunchParam {
    public var launchReason: LaunchReason = LaunchReason.UNKNOWN
    public var lastExitReason: LastExitReason = LastExitReason.NORMAL
    public var lastExitMessage: String = ""

    public init(launchReason!: LaunchReason = LaunchReason.UNKNOWN, lastExitReason!: LastExitReason = LastExitReason.NORMAL)
    public init(lastExitMessage: String, launchReason!: LaunchReason = LaunchReason.UNKNOWN, lastExitReason!: LastExitReason = LastExitReason.NORMAL)
}
```

**功能：** 启动参数。Ability启动时由系统自动传入，开发者无需修改。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### var lastExitMessage

```cangjie
public var lastExitMessage: String
```

**功能：** 表示最后退出详细原因。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var lastExitReason

```cangjie
public var lastExitReason: LastExitReason = LastExitReason.NORMAL
```

**功能：** 枚举类型，表示最后退出原因。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [LastExitReason](#enum-lastexitreason)

**读写能力：** 可读写

**起始版本：** 12

### var launchReason

```cangjie
public var launchReason: LaunchReason = LaunchReason.UNKNOWN
```

**功能：** 枚举类型，表示启动原因。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [LaunchReason](#enum-launchreason)

**读写能力：** 可读写

**起始版本：** 12

### init(LaunchReason, LastExitReason)

```cangjie
public init(launchReason!: LaunchReason = LaunchReason.UNKNOWN, lastExitReason!: LastExitReason = LastExitReason.NORMAL)
```

**功能：** LaunchParam结构的构造器。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|launchReason|[LaunchReason](#enum-launchreason)|否|LaunchReason.UNKNOWN| **命名参数。** 表示启动原因。|
|lastExitReason|[LastExitReason](#enum-lastexitreason)|否|LastExitReason.NORMAL| **命名参数。** 表示最后退出原因。|

### init(String, LaunchReason, LastExitReason)

```cangjie
public init(lastExitMessage: String, launchReason!: LaunchReason = LaunchReason.UNKNOWN, lastExitReason!: LastExitReason = LastExitReason.NORMAL)
```

**功能：** LaunchParam结构的构造器。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|lastExitMessage|String|是|-| 表示最后退出详细原因。|
|launchReason|[LaunchReason](#enum-launchreason)|否|LaunchReason.UNKNOWN| **命名参数。** 表示启动原因。|
|lastExitReason|[LastExitReason](#enum-lastexitreason)|否|LastExitReason.NORMAL| **命名参数。** 表示最后退出原因。|