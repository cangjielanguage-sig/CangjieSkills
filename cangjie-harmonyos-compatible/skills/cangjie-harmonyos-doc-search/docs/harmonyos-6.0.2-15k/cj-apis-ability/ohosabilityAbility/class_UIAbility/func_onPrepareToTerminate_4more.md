### func onPrepareToTerminate()

```cangjie
public open func onPrepareToTerminate(): Bool
```

**功能：** UIAbility生命周期回调，当系统预关闭开关打开后（配置系统参数persist.sys.prepare_terminate为true打开），在UIAbility关闭时触发，可在回调中定义操作来决定是否继续执行关闭UIAbility的操作。如果UIAbility在退出时需要与用户交互确认是否关闭Ability，可在此生命周期回调中定义预关闭操作配合[terminateSelf](#func-terminateself)接口退出，如弹窗确认是否关闭，并配置预关闭生命周期返回true取消正常关闭。

**需要权限：** ohos.permission.PREPARE_APP_TERMINATE

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|是否执行UIAbility关闭操作，返回true表示本次UIAbility关闭流程取消，不再退出，返回false表示UIAbility继续正常关闭。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.AppLog
import kit.AbilityKit.*

class MainAbility <: UIAbility {
    public override func onPrepareToTerminate(): Bool {
        AppLog.info("MainAbility onPrepareToTerminate.")
        return false
    }
}
```

### func onSaveState(StateType, String)

```cangjie
public open func onSaveState(reason: StateType, wantParam: String): OnSaveResult
```

**功能：** 在应用故障时，如果使能了自动保存状态，框架将回调onSaveState保存UIAbility状态。该方法配合appRecovery使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|reason|[StateType](#enum-statetype)|是|-|回调保存状态的原因。|
|wantParam|String|是|-|want相关参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[OnSaveResult](#enum-onsaveresult)|是否同意保存当前UIAbility的状态。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.AppLog
import kit.AbilityKit.*

class MainAbility <: UIAbility {
    public override func onSaveState(reason: StateType, wantParam: String): OnSaveResult {
        AppLog.info("MainAbility onSaveState.")
        return OnSaveResult.RECOVERY_AGREE
    }
}
```

### func onShare(String)

```cangjie
public open func onShare(wantParam: String): Unit
```

**功能：** 在跨端分享场景下，在UIAbility中设置分享方设备要分享的数据。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|wantParam|String|是|-|待分享的数据。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.AppLog
import kit.AbilityKit.*

class MainAbility <: UIAbility {
    public override func onShare(wantParam: String): Unit {
        AppLog.info("MainAbility onShare.")
    }
}
```

### func onWindowStageCreate(WindowStage)

```cangjie
public open func onWindowStageCreate(windowStage: WindowStage): Unit
```

**功能：** 当WindowStage创建后调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|windowStage|[WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage)|是|-|[WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage)相关信息。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.AppLog
import kit.AbilityKit.*

class MainAbility <: UIAbility {
    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        AppLog.info("MainAbility onWindowStageCreate.")
        windowStage.loadContent("EntryView")
    }
}
```