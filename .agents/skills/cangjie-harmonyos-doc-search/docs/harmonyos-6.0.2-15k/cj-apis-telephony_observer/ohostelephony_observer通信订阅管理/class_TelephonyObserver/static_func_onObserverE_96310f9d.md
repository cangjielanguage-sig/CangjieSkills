### static func on(ObserverEventType, Callback0Argument)

```cangjie
public static func on(eventType: ObserverEventType, callback: Callback0Argument): Unit
```

**功能：** 订阅卡账户变化事件。

**系统能力：** SystemCapability.Telephony.StateRegistry

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[ObserverEventType](#enum-observereventtype)|是|-|事件类型，此处为卡账户变化事件。|
|callback|[Callback0Argument](../BasicServicesKit/cj-apis-base.md#class-callback0argument)|是|-|回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[电话子系统错误码](../../errorcodes/cj-errorcode-telephony.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|
  |8300001|Invalid parameter value.|
  |8300002|Operation failed. Cannot connect to service.|
  |8300003|System internal error.|
  |8300999|Unknown error code.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

// 所需要的依赖项
class CallbackVoidObj <: Callback0Argument {
    let callback_: () -> Unit
    public init(callback: () -> Unit) {
        callback_ = callback
    }
    public open func invoke(): Unit {
        callback_()
    }
}

let defaultOptions = ObserverOptions()
let callback7 = CallbackVoidObj({
    => AppLog.info("[on iccAccountInfoChange]: success")
})

TelephonyObserver.on(ObserverEventType.IccAccountInfoChange, callback7)
```