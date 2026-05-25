### func openAtomicService(String, ?AtomicServiceOptions, AsyncCallback\<AbilityResult>)

```cangjie
public func openAtomicService(appId: String, options!: ?AtomicServiceOptions = None,
    callback!: AsyncCallback<AbilityResult>): Unit
```

**功能：** 跳出式启动[EmbeddableUIAbility](#class-embeddableuiability)，并通过异步回调返回结果。仅支持在主线程调用，分为以下几种情况：

- 正常情况下可通过调用[terminateSelfWithResult](#func-terminateselfwithresultabilityresult)接口使之终止并且返回结果给调用方。
- 异常情况下比如杀死EmbeddableUIAbility会返回异常信息给调用方，异常信息中resultCode为-1。
- 如果不同应用多次调用该接口启动同一个EmbeddableUIAbility，当这个EmbeddableUIAbility调用[terminateSelfWithResult](#func-terminateselfwithresultabilityresult)接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息，异常信息中resultCode为-1。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|appId|String|是|-|应用的唯一标识，由云端统一分配。|
|options|?[AtomicServiceOptions](#class-atomicserviceoptions)|否|None| **命名参数。** 跳出式启动原子化服务所携带的参数。|
|callback|[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<[AbilityResult](#struct-abilityresult)>|是|-| **命名参数。** 通过异步回调返回[AbilityResult](#struct-abilityresult)对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |16000002|Incorrect ability type.|
  |16000003|The specified ID does not exist.|
  |16000004|Failed to start the invisible ability.|
  |16000011|The context does not exist.|
  |16000012|The application is controlled.|
  |16000050|Internal error.|
  |16000053|The ability is not on the top of the UI.|
  |16000055|Installation-free timed out.|
  |16200001|The caller has been released.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

AppLog.info("Hello Cangjie")
let uiAbilityContext = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
var resultCallback = {
    errorCode: Option<AsyncError>, data: Option<AbilityResult> => match (errorCode) {
        case Some(e) => AppLog.info("callback error: errcode is ${e.code}")
        case _ => match (data) {
            case Some(value) =>
                AppLog.info("callback data is ${value.resultCode}")
                AppLog.info("callback data is ${value.want.bundleName}")
            case _ => AppLog.info("callback data is null")
        }
    }
}
uiAbilityContext.openAtomicService(
    "5765880207854787517",
    options: AtomicServiceOptions(displayId: 1,
        withAnimation: false,
        parameters: "{\"openAtomicService_key\": \"openAtomicService_value\"}"
    ), // parameters是一个json格式的字符串
    callback: resultCallback
)
```