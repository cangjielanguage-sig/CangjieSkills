# ohos.webview（Webview）

提供web控制能力，组件提供网页显示的能力。

## 导入模块

```cangjie
import kit.ArkWeb.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[接口使用说明](../../cj-development-intro.md#接口使用说明)。

## 权限列表

ohos.permission.APPROXIMATELY_LOCATION

ohos.permission.LOCATION

ohos.permission.LOCATION_IN_BACKGROUND

ohos.permission.INTERNET

## func once(String, () -> Unit)

```cangjie
public func once(onceType: String, callback: () -> Unit): Unit
```

**功能：** 订阅一次指定类型Web事件的回调，Web事件的类型目前仅支持"webInited"，在Web引擎初始化完成时触发。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|onceType|String|是|Web事件的类型，目前支持："webInited"（Web初始化完成）。|
|callback|Callback|是|所订阅的回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

internal import kit.AbilityKit.AbilityStage
internal import kit.AbilityKit.LaunchReason
import ohos.base.*
import kit.ArkWeb.*

class MainAbility <: UIAbility {
    public init() {
        super()
        registerSelf()
    }
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("MainAbility OnCreated.${want.abilityName}")
        once(
            "webInited",
            {
                => AppLog.info("webInited")
            }
        )
        match (launchParam.launchReason) {
            case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
            case _ => ()
        }
    }
    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        AppLog.info("MainAbility onWindowStageCreate.")
        windowStage.loadContent("EntryView")
    }
}
```