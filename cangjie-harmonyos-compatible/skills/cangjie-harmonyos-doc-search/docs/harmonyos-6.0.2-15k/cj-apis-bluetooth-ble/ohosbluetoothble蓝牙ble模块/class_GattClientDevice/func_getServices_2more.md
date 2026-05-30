### func getServices()

```cangjie
public func getServices(): Array<GattService>
```

**功能：** client端获取蓝牙低功耗设备的所有服务，即服务发现。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[GattService](#class-gattservice)>|client进行服务发现。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.|
  |801|Capability not supported.|
  |2900001|Service stopped.|
  |2900099|Operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import ohos.hilog.Hilog

let gattClient = createGattClientDevice("XX:XX:XX:XX:XX:XX")
try {
    let services = gattClient.getServices()
    Hilog.info(0, "Bluetooth", "getServices success")
    for (service in services) {
        Hilog.info(0, "Bluetooth", "find serviceUuid : ${service.serviceUuid}")
    }
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func off(BluetoothBleGattClientDeviceCallbackType, ?CallbackObject)

```cangjie
public func off(`type`: BluetoothBleGattClientDeviceCallbackType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消订阅 client 端蓝牙低功耗设备事件。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type`|[BluetoothBleGattClientDeviceCallbackType](#enum-bluetoothblegattclientdevicecallbacktype)|是|-|特征值变化事件。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None| **命名参数。** 取消订阅 client 端蓝牙低功耗设备事件。不填该参数则取消订阅该type对应的所有回调。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

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

let gattClient = createGattClientDevice("XX:XX:XX:XX:XX:XX")
let device = "XX:XX:XX:XX:XX:XX"
var connectState = STATE_DISCONNECTED
class BLEConnectionStateChangeCallback <: Callback1Argument<BLEConnectionChangeState> {
    public func invoke(stateInfo: BLEConnectionChangeState): Unit {
        Hilog.info(0, "Bluetooth", "onGattServerStateChange: device=" + stateInfo.deviceId + ", state=" + stateInfo.state.toString())
        if (stateInfo.deviceId == device) {
            connectState = stateInfo.state
        }
    }
}

let bleConnectionStateChangeCallback = BLEConnectionStateChangeCallback()
try {
    gattClient.on(BLE_CONNECTION_STATE_CHANGE, bleConnectionStateChangeCallback)
    gattClient.off(BLE_CONNECTION_STATE_CHANGE, callback: bleConnectionStateChangeCallback)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```