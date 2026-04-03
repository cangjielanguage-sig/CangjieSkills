### func reportDrawnCompleted(AsyncCallback\<Unit>)

```cangjie
public func reportDrawnCompleted(callback: AsyncCallback<Unit>): Unit
```

**功能：** 当页面加载完成（loadContent成功）时，为开发者提供打点功能（callback形式）。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<Unit>|是|-|页面加载完成打点的回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
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
        var callback = {
            errorCode: Option<AsyncError>, data: Option<Unit> => match (errorCode) {
                case Some(e) => AppLog.info("callback request error: errcode is ${e.code}")
                case _ => AppLog.info("callback success")
            }
        }
        this.context.reportDrawnCompleted(callback)
    }
}
```

### func requestDialogService(Want, AsyncCallback\<DialogRequestResult>)

```cangjie
public func requestDialogService(want: Want, callback: AsyncCallback<DialogRequestResult>): Unit
```

**功能：** 启动支持模式对话框的ServiceExtensionAbility，并使用回调返回结果。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

| 参数名 | 参数类型 | 必填 | 默认值 | 描述 |
|:------|:------|:------|:------|:------|
| want | [Want](#class-want) |  是 | - |  需要启动的目标ServiceExtensionAbility的want信息。 |
| callback | [AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<[DialogRequestResult](#class-dialogrequestresult)> | 是 | - | 用于返回结果的回调。 |

### func requestDialogService(Want)

```cangjie
public func requestDialogService(want: Want): Future<DialogRequestResult>
```

**功能：** 启动支持模式对话框的ServiceExtensionAbility，并返回结果。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

| 参数名 | 参数类型 | 必填 | 默认值 | 描述 |
|:------|:------|:------|:------|:------|
| want | [Want](#class-want) |  是 | - |  需要启动的目标ServiceExtensionAbility的want信息。 |

**返回值：**

|类型|说明|
|:----|:----|
|Future\<[DialogRequestResult](#class-dialogrequestresult)>| 返回执行结果。|