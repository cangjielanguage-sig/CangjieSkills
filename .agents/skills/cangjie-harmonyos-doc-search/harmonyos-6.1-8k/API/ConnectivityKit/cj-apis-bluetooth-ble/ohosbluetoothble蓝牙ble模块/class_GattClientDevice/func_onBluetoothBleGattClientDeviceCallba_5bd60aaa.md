### func on(BluetoothBleGattClientDeviceCallbackType, Callback1Argument\<BleCharacteristic>)

```cangjie
public func on(eventType: BluetoothBleGattClientDeviceCallbackType, callback: Callback1Argument<BleCharacteristic>): Unit
```

**功能：** client端订阅server端特征值变化事件。

- 需调用[setCharacteristicChangeNotification](#func-setcharacteristicchangenotificationblecharacteristic-bool-asynccallbackunit)或者[setCharacteristicChangeIndication](#func-setcharacteristicchangeindicationblecharacteristic-bool-asynccallbackunit)，且启用通知或者指示能力后，才能接收到server端的特征值内容变更通知或者指示。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[BluetoothBleGattClientDeviceCallbackType](#enum-bluetoothblegattclientdevicecallbacktype)|是|-|事件回调类型，支持的事件为BleCharacteristicChange，表示server端特征值变化事件。<br>当client端收到server端特征值内容变更的通知或者指示时，触发该事件。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<[BleCharacteristic](#class-blecharacteristic)>|是|-|指定订阅的回调函数，会携带server端变化后的特征值内容。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 801 | Capability not supported. |

**示例：**

<!-- compile only -->
<!-- compile -->

```cangjie
// index.cj

import ohos.callback_invoke.*
import ohos.business_exception.*
import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.Hilog

// 此处代码可添加在依赖项定义中
class BLECharacteristicChangeCallback <: Callback1Argument<BleCharacteristic> {
    public func invoke(err: ?BusinessException, characteristic: BleCharacteristic): Unit {
        Hilog.info(0, "Bluetooth", "characteristic ${characteristic.serviceUUID} has change")
    }
}

try {
    let gattClient = createGattClientDevice("XX:XX:XX:XX:XX:XX")  // 请替换为您的设备地址
    let bleCharacteristicChangeCallback = BLECharacteristicChangeCallback()
    gattClient.on(BluetoothBleGattClientDeviceCallbackType.BleCharacteristicChange, bleCharacteristicChangeCallback)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}", "")
}
```