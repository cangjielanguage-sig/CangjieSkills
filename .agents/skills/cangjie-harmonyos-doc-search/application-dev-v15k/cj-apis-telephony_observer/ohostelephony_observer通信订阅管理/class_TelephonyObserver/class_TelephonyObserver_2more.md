## class TelephonyObserver

```cangjie
public class TelephonyObserver {}
```

**功能：** 通信事件订阅类，提供各种静态方法如：`on/off`等订阅/取消订阅事件。

**系统能力：** SystemCapability.Telephony.StateRegistry

**起始版本：** 19

### static func off(ObserverEventType, Callback1Argument\<NetworkState>)

```cangjie
public static func off(eventType: ObserverEventType, callback: Callback1Argument<NetworkState>): Unit
```

**功能：** 取消订阅网络状态变化事件。

**系统能力：** SystemCapability.Telephony.StateRegistry

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[ObserverEventType](#enum-observereventtype)|是|-|事件类型。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[NetworkState](cj-apis-telephony_radio.md#class-networkstate)>|是|-|网络状态变化回调函数。|

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
    public init(callback: (T) -> Unit) {callback_ = callback}
    public open func invoke(val: T): Unit {
        callback_(val)
    }
}

let callback1 = MyCallbackObj<NetworkState>({
    val: NetworkState =>
        AppLog.info("[on networkStateChange] data.longOperatorName: ${val.longOperatorName}, data.shortOperatorName: ${val.shortOperatorName}, data.isRoaming: ${val.isRoaming}")
})

TelephonyObserver.off(ObserverEventType.NetworkStateChange, callback1)
```