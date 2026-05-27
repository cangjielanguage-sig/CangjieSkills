### static func off(ObserverEventType, Callback1Argument\<Array\<SignalInformation>>)

```cangjie
public static func off(eventType: ObserverEventType, callback: Callback1Argument<Array<SignalInformation>>): Unit
```

**功能：** 取消订阅信号状态变化事件。

**系统能力：** SystemCapability.Telephony.StateRegistry

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[ObserverEventType](#enum-observereventtype)|是|-|事件类型。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Array\<[SignalInformation](cj-apis-telephony_radio.md#class-signalinformation)>>|是|-|信号状态变化回调函数。|

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
class MyCallbackObj<T> <: Callback1Argument<T> {
    let callback_: (T) -> Unit
    public init(callback: (T) -> Unit) {
        callback_ = callback
    }
    public open func invoke(val: T): Unit {
        callback_(val)
    }
}

let callback2 = MyCallbackObj<Array<SignalInformation>>(
    {
        val: Array<SignalInformation> =>
        AppLog.info("[on signalInfoChange] Array.size: ${val.size}")
        if (val.size > 0) {
            let count = 0
            for (obj in val) {
                AppLog.info(
                    "data_${count}: {signalType: ${obj.signalType.getValue()}, signalLevel: ${obj.signalLevel}, dBm: ${obj.dBm}}"
                )
            }
        }
    }
)

TelephonyObserver.off(ObserverEventType.SignalInfoChange, callback2)
```