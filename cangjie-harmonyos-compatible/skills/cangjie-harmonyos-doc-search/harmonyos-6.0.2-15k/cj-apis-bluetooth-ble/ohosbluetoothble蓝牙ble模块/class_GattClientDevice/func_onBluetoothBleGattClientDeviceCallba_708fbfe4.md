### func on(BluetoothBleGattClientDeviceCallbackType, Callback1Argument\<BLEConnectionChangeState>)

```cangjie
public func on(`type`: BluetoothBleGattClientDeviceCallbackType,
    callback: Callback1Argument<BLEConnectionChangeState>): Unit
```

**功能：** client端订阅MTU状态变化事件。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|\`type`|[BluetoothBleGattClientDeviceCallbackType](#enum-bluetoothblegattclientdevicecallbacktype)|是|填写BLE_CONNECTION_STATE_CHANGE，表示连接状态变化事件。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[BLEConnectionChangeState](#class-bleconnectionchangestate)>|是|返回MTU字节数的值，通过注册回调函数获取。|

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

// 此处代码可添加在依赖项定义中
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
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```