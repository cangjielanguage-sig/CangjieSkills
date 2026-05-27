# ohos.ability（Ability）

程序框架服务提供了应用程序开发和运行的应用模型，是系统为开发者提供的应用程序所需能力的抽象提炼，它提供了应用程序必备的组件和运行机制。有了应用模型，开发者可以基于一套统一的模型进行应用开发，使应用开发更简单、高效。

## 导入模块

```cangjie
import kit.AbilityKit.*
```

## 权限列表

ohos.permission.DISTRIBUTED_DATASYNC

ohos.permission.PREPARE_APP_TERMINATE

ohos.permission.PRIVACY_WINDOW

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func cancel(WantAgent)

```cangjie
public func cancel(agent: WantAgent): Unit
```

**功能：** 取消WantAgent实例。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|agent|[WantAgent](#class-wantagent)|是| WantAgent对象。|

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
let uid = cancel(wantAgent)
```

## func createModuleContext(Context, String)

```cangjie
public func createModuleContext(context: Context, moduleName: String): Context
```

**功能：** 根据入参context创建相应模块的[Context](#class-context)。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|context|[Context](#class-context)|是|表示应用上下文。|
|moduleName|String|是|表示应用模块名。|

**返回值：**

|类型|说明|
|:----|:----|
|[Context](#class-context)|返回创建的Context。|

**示例：**

<!-- compile -->

```cangjie
// ability_stage.cj

import ohos.base.*
import kit.AbilityKit.*

class MyAbilityStage <: AbilityStage {
    public override func onCreate(): Unit {
        AppLog.info("MyAbilityStage onCreated.")
        let hapInfo = this.context.currentHapModuleInfo
        try {
            let ctx = createModuleContext(this.context, hapInfo.name)
        } catch (e: BusinessException) {
            AppLog.info("MyAbilityStage create moduleContext failed")
        }
        AppLog.info("MyAbilityStage create ctx success")
    }
}
```