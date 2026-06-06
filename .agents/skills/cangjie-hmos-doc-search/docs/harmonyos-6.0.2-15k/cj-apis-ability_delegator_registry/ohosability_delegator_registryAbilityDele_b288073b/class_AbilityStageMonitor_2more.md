## class AbilityStageMonitor

```cangjie
public class AbilityStageMonitor {
    public AbilityStageMonitor(
        public var moduleName: String,
        public var srcEntrance: String
    )
}
```

**功能：** [AbilityStageMonitor](#class-abilitystagemonitor)模块提供用于匹配满足指定条件的受监视的[AbilityStage](../AbilityKit/cj-apis-ability.md#class-abilitystage)对象的方法。最近匹配的[AbilityStage](../AbilityKit/cj-apis-ability.md#class-abilitystage)对象将保存在[AbilityStageMonitor](#class-abilitystagemonitor)中。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### var moduleName

```cangjie
public var moduleName: String
```

**功能：** 要监视的abilityStage的模块名。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var srcEntrance

```cangjie
public var srcEntrance: String
```

**功能：** 要监视的abilityStage的源路径。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### AbilityStageMonitor(String, String)

```cangjie
public AbilityStageMonitor(
    public var moduleName: String,
    public var srcEntrance: String
)
```

**功能：** 构造一个[AbilityStageMonitor](#class-abilitystagemonitor)对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|moduleName|String|是|-|要监视的abilityStage的模块名。|
|srcEntrance|String|是|-|要监视的abilityStage的源路径。|

## class ShellCmdResult

```cangjie
public class ShellCmdResult {}
```

**功能：** Shell命令执行结果。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### func dump()

```cangjie
public func dump(): String
```

**功能：** 获取[ShellCmdResult](#class-shellcmdresult)对象的字符串表示形式。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|[ShellCmdResult](#class-shellcmdresult)对象的字符串表示形式。|

### func getExitCode()

```cangjie
public func getExitCode(): Int32
```

**功能：** 获取结果码。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|结果码。|

### func getStdResult()

```cangjie
public func getStdResult(): String
```

**功能：** 获取标准输出内容。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|标准输出内容。|