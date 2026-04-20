### func requestGlobalSwitch(Context, SwitchType, AsyncCallback\<Bool>)

```cangjie
public func requestGlobalSwitch(context: Context, switchType: SwitchType, callback: AsyncCallback<Bool>): Unit
```

**功能：** 用于拉起全局开关设置弹框。

部分情况下，录音、拍照等功能禁用，应用可拉起此弹框请求用户同意开启对应功能。如果当前全局开关的状态为开启，则不拉起弹框。

> **说明：**
>
> 仅支持UIAbility/UIExtensionAbility。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[Context](cj-apis-ability.md#class-context)|是|-|请求权限的UIAbility/UIExtensionAbility的Context。|
|switchType|[SwitchType](#enum-switchtype)|是|-|全局开关类型。|
|callback|AsyncCallback\<Bool>|是|-|回调函数，返回全局开关状态。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[访问控制错误码](../../errorcodes/cj-errorcode-access-token.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.|
  |12100001|Invalid parameter. Possible causes: 1. The context is invalid because it does not belong to the application itself; 2. The type of global switch is not support.|
  |12100010|The request already exists.|
  |12100013|The specific global switch is already open.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*
import ohos.base.AsyncCallback
import ohos.base.AsyncError

// 此处代码可添加在依赖项定义中
var resCallback:  AsyncCallback<Bool> = {
    errorCode: Option<AsyncError>, data: Option<Bool> => match (errorCode) {
        case Some(e) => AppLog.info("CallBack request error: errcode is ${e.code}")
        case _ =>
            match (data) {
                case Some(value) =>
                    AppLog.info("CallBack global switch status: ${value}")
                case _ => AppLog.info("CallBack request error: data is null")
            }
    }
}

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let atManager = AbilityAccessCtrl.createAtManager()
atManager.requestGlobalSwitch(ctx, SwitchType.MICROPHONE, resCallback)
```