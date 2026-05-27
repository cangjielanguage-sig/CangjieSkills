### func backToCallerAbilityWithResult(AbilityResult, String)

```cangjie
public func backToCallerAbilityWithResult(abilityResult: AbilityResult, requestCode: String): Unit
```

**功能：** 当通过[startAbilityForResult](#func-startabilityforresultwant-asynccallbackabilityresult)或[openLink](#func-openlinkstring-openlinkoptions-asynccallbackabilityresult)拉起目标方Ability，且需要目标方返回结果时，目标方可以通过该接口将结果返回并拉起调用方。与[terminateSelfWithResult](#func-terminateselfwithresultabilityresult)不同的是，本接口在返回时不会销毁当前Ability。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|abilityResult|[AbilityResult](#struct-abilityresult)|是|-|指示目标方返回给拉起方的结果。|
|requestCode|String|是|-|通过通过[startAbilityForResult](#func-startabilityforresultwant-asynccallbackabilityresult)或[openLink](#func-openlinkstring-openlinkoptions-asynccallbackabilityresult)拉起目标方Ability且需要目标方返回结果时，系统生成的用于标识本次调用的requestCode。该值可以通过[want](#class-want)中的[CALLER_REQUEST_CODE](#caller_request_code)字段获取。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|The application does not have permission to call the interface.|
  |401|Parameter error.|
  |16000009|An ability cannot be started or stopped in Wukong mode.|
  |16000011|The context does not exist.|
  |16000050|Internal error.|
  |16000074|The caller does not exist.|
  |16000075|Not support back to caller.|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

internal import kit.UIKit.{AppLog, BusinessException}
internal import kit.AbilityKit.{AbilityStage, LaunchReason}
import kit.AbilityKit.*

var globalRequstCode: ?String = None

class MainAbility <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        match (launchParam.launchReason) {
            case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
            case _ => ()
        }
    }

    public override func onNewWant(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("onNewWant!")
    }

    public override func onForeground(): Unit {
        spawn {
            let abilityResult = AbilityResult(666, Want(abilityName: "MainAbility"))
            try {
                this.context.backToCallerAbilityWithResult(abilityResult, globalRequstCode ?? "0")
            } catch (e: BusinessException) {
                AppLog.info("backToCallerAbilityWithResult error: ${e.code}")
            }
        }
    }
}
```