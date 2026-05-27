## func getWantAgent(WantAgentInfo)

```cangjie
public func getWantAgent(info: WantAgentInfo): WantAgent
```

**功能：** 创建WantAgent。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|info|[WantAgentInfo](#class-wantagentinfo)|是|WantAgent信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[WantAgent](#class-wantagent)|创建的WantAgent。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |16000007|Service busy. There are concurrent tasks. Try again later.|
  |16000151|Invalid wantagent object.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

let wantAgentInfo = WantAgentInfo(wants: [Want(bundleName: "com.example.myapplication", abilityName: "EntryAbility")],
    actionType: START_ABILITIES, requestCode: 0, actionFlags: [UPDATE_PRESENT_FLAG])
let wantAgent = getWantAgent(wantAgentInfo)
```

## func isRamConstrainedDevice()

```cangjie
public func isRamConstrainedDevice(): Bool
```

**功能：** 查询是否为ram受限设备。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true：当前设备为ram受限设备，false：当前设备为非ram受限设备。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |16000050|Internal error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

let value = isRamConstrainedDevice()
AppLog.info("isRamConstrainedDevice = ${value}")
```

## func isRunningInStabilityTest()

```cangjie
public func isRunningInStabilityTest(): Bool
```

**功能：** 查询当前是否处于稳定性测试场景。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true: 处于稳定性测试场景，false：处于非稳定性测试场景。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |16000050|Internal error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

let value = isRunningInStabilityTest()
AppLog.info("isRunningInStabilityTest = ${value}")
```

## func restartApp()

```cangjie
public func restartApp(): Unit
```

**功能：** 重启当前进程，并拉起应用启动时第一个Ability，如果该Ability存在已经保存的状态，这些状态数据会在Ability的OnCreate生命周期回调的want参数中作为wantParam属性传入。

启动由[setRestartWant](#func-setrestartwantwant)指定的Ability。如果没有指定则按以下规则启动：

如果当前应用前台的Ability支持恢复，则重新拉起该Ability。

如果存在多个支持恢复的Ability处于前台，则只拉起最后一个。

如果没有Ability处于前台，则不拉起。

可以配合[ErrorManager](#class-errormanager)相关接口使用。两次重启的间隔应大于一分钟，一分钟之内重复调用此接口只会退出应用不会重启应用。自动重启的行为与主动重启一致。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

AppLog.info("restartApp")
restartApp()
```