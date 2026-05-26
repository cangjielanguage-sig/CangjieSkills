### static func on(ObserverEventType, Callback1Argument\<DataFlowType>, ?ObserverOptions)

```cangjie
public static func on(eventType: ObserverEventType,
    callback: Callback1Argument<DataFlowType>, options!: ?ObserverOptions = None): Unit
```

**功能：** 订阅指定卡槽位的蜂窝数据业务的上下行数据流状态。

**系统能力：** SystemCapability.Telephony.StateRegistry

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[ObserverEventType](#enum-observereventtype)|是|-|事件类型，此处为卡账户变化事件。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[DataFlowType](cj-apis-telephony_data.md#enum-dataflowtype)>|是|-|回调函数。|
|options|?[ObserverOptions](#class-observeroptions)|否|None| **命名参数。** 电话相关事件订阅参数。|

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

let defaultOptions = ObserverOptions()
let callback5 = MyCallbackObj<DataFlowType>(
    {
        val: DataFlowType => AppLog.info("[on cellularDataFlowChange]:  ${val.getValue()}")
    })

TelephonyObserver.on(ObserverEventType.CellularDataFlowChange, callback5)
```