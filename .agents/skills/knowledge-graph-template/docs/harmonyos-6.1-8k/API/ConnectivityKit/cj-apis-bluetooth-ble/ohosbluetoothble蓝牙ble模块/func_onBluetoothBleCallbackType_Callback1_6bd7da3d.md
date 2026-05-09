## func on(BluetoothBleCallbackType, Callback1Argument\<Array\<ScanResult>>)

```cangjie
public func on(eventType: BluetoothBleCallbackType, callback: Callback1Argument<Array<ScanResult>>): Unit
```

**功能：** 订阅BLE设备扫描结果上报事件。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[BluetoothBleCallbackType](#enum-bluetoothblecallbacktype)|是|-|事件回调类型，支持的事件为BleDeviceFind，表示BLE设备扫描结果上报事件。<br>当调用[startAdvertising](#func-startadvertisingadvertisingparams) 后，开始BLE扫描，若扫描到BLE设备，触发该事件。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<Array\<[ScanResult](#class-scanresult)>>|是|-|指定订阅的回调函数，会携带扫描结果的集合。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[蓝牙服务子系统错误码](./cj-errorcode-bluetooth_manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 801 | Capability not supported. |
  | 2900099 | Operation failed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.callback_invoke.*
import ohos.business_exception.*
import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.Hilog

// 此处代码可添加在依赖项定义中
class BLEDeviceFindCallback1 <: Callback1Argument<Array<ScanResult>> {
    public func invoke(err: ?BusinessException, devices: Array<ScanResult>): Unit {
        for (device in devices) {
            Hilog.info(0, "Bluetooth", "device has find, deviceID is ${device.deviceId}, name is ${device.deviceName}")
        }
    }
}

let bleDeviceFindCallback = BLEDeviceFindCallback1()
try {
    on(BluetoothBleCallbackType.BleDeviceFind, bleDeviceFindCallback)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}", "")
}
```