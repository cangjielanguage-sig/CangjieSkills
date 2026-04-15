### func on(BluetoothBleGattClientDeviceCallbackType, Callback1Argument\<BleConnectionChangeState>)

```cangjie
public func on(
    eventType: BluetoothBleGattClientDeviceCallbackType,
    callback: Callback1Argument<BleConnectionChangeState>
): Unit
```

**功能：** client端订阅GATT profile协议的连接状态变化事件。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[BluetoothBleGattClientDeviceCallbackType](#enum-bluetoothblegattclientdevicecallbacktype)|是|-|事件回调类型，支持的事件为BleConnectionStateChange，表示连接状态变化事件。<br>client和server端之间的连接状态发生变化时，触发该事件。<br>当client端调用[connect](#func-connect)或[disconnect](#func-disconnect)时，可能引起连接状态生变化。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<[BleConnectionChangeState](#class-bleconnectionchangestate)>|是|-|指定订阅的回调函数，会携带连接状态信息。|

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
class BLEConnectionStateChangeCallback1 <: Callback1Argument<BleConnectionChangeState> {
    public func invoke(err: ?BusinessException, stateInfo: BleConnectionChangeState): Unit {
        Hilog.info(0, "Bluetooth", "onGattServerStateChange: device=" + stateInfo.deviceId + ", state=" + stateInfo.state.toString())
    }
}

try {
    let gattClient = createGattClientDevice("XX:XX:XX:XX:XX:XX")  // 请替换为您的设备地址
    let bleConnectionStateChangeCallback = BLEConnectionStateChangeCallback1()
    gattClient.on(BluetoothBleGattClientDeviceCallbackType.BleConnectionStateChange, bleConnectionStateChangeCallback)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}", "")
}
```