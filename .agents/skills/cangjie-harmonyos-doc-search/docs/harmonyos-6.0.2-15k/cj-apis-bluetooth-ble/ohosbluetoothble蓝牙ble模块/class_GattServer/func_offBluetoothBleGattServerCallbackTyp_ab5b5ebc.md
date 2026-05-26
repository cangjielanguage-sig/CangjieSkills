### func off(BluetoothBleGattServerCallbackType, ?CallbackObject)

```cangjie
public func off(`type`: BluetoothBleGattServerCallbackType, callback!: ?CallbackObject = None): Unit
```

**功能：** server端取消订阅事件。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type`|[BluetoothBleGattServerCallbackType](#enum-bluetoothblegattservercallbacktype)|是|-|表示特征值读请求事件。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None| **命名参数。** 表示取消订阅事件上报。不填该参数则取消订阅该type对应的所有回调。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.|
  |801|Capability not supported.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import ohos.hilog.Hilog

// 此处代码可添加在依赖项定义中
class StateChangeCallback <: Callback1Argument<BLEConnectionChangeState> {
    public func invoke(state: BLEConnectionChangeState): Unit {
        Hilog.info(0, "Bluetooth", "onGattServerStateChange: device=" + state.deviceId + ", state=" + state.state.toString())
    }
}

let stateChangeCallback = StateChangeCallback()
let gattServer = createGattServer()
try {
    gattServer.on(BluetoothBleGattServerCallbackType.CONNECTION_STATE_CHANGE, stateChangeCallback)
    gattServer.off(BluetoothBleGattServerCallbackType.CONNECTION_STATE_CHANGE, callback: stateChangeCallback)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```