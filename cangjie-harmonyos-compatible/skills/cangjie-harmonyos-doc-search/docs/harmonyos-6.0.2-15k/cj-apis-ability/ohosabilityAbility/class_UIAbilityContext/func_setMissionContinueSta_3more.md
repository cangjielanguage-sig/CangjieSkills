### func setMissionContinueState(ContinueState)

```cangjie
public func setMissionContinueState(state: ContinueState): Unit
```

**功能：** 设置UIAbility任务中流转状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|state|[ContinueState](#enum-continuestate)|是|-|流转状态。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |16000011|The context does not exist.|
  |16000050|Internal error.|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

internal import ohos.base.{AppLog, BusinessException}
import kit.AbilityKit.*

class MainAbility <: UIAbility {
    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        AppLog.info("MainAbility onWindowStageCreate.")
        this.context.setMissionContinueState(ContinueState.INACTIVE)
    }
}
```

### func setMissionLabel(String)

```cangjie
public func setMissionLabel(label: String): Future<Unit>
```

**功能：** 设置UIAbility在任务中显示的名称（Future形式）。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|label|String|是|-|显示名称。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |16000011|The context does not exist.|
  |16000050|Internal error.|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

internal import ohos.base.{AppLog, BusinessException}
import kit.AbilityKit.*

class MainAbility <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("MainAbility OnCreated.${want.abilityName}")
        this.context.setMissionLabel("test")
    }
}
```

### func setRestoreEnabled(Bool)

```cangjie
public func setRestoreEnabled(enabled: Bool): Unit
```

**功能：** 设置UIAbility是否启用备份恢复。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enabled|Bool|是|-|表示是否启用恢复。true表示启用，false表示不启用。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |16000011|The context does not exist.|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

internal import ohos.base.{AppLog, BusinessException}
import kit.AbilityKit.*

class MainAbility <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("MainAbility OnCreated.${want.abilityName}")
        this.context.setRestoreEnabled(true)
    }
}
```