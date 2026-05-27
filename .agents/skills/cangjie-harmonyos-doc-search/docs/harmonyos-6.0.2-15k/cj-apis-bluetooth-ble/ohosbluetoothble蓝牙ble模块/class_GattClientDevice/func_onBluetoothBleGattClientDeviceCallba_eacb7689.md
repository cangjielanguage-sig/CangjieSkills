### func on(BluetoothBleGattClientDeviceCallbackType, Callback1Argument\<BLECharacteristic>)

```cangjie
public func on(`type`: BluetoothBleGattClientDeviceCallbackType, callback: Callback1Argument<BLECharacteristic>): Unit
```

**功能：** client端订阅MTU状态变化事件。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|\`type`|[BluetoothBleGattClientDeviceCallbackType](#enum-bluetoothblegattclientdevicecallbacktype)|是|填写BLE_CHARACTERISTIC_CHANGE，表示特征值变化事件。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[BLECharacteristic](#class-blecharacteristic)>|是|返回MTU字节数的值，通过注册回调函数获取。|

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
class BLECharacteristicChangeCallback <: Callback1Argument<BLECharacteristic> {
    public func invoke(characteristic: BLECharacteristic): Unit {
        Hilog.info(0, "Bluetooth", "characteristic ${characteristic.serviceUuid} has change")
    }
}

let gattClient = createGattClientDevice("XX:XX:XX:XX:XX:XX")
let bleCharacteristicChangeCallback = BLECharacteristicChangeCallback()
try {
    gattClient.on(BLE_CHARACTERISTIC_CHANGE, bleCharacteristicChangeCallback)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```