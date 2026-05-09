## func startBleScanning(Array\<ScanFilter>, ?ScanOptions)

```cangjie
public func startBleScanning(filters: Array<ScanFilter>, options!: ?ScanOptions = None): Unit
```

**功能：** 发起BLE扫描流程。

- 扫描结果会通过[on(BleDeviceFind)](#func-onbluetoothblecallbacktype-callback1argumentarrayscanresult)的回调函数获取到。只能扫描BLE设备，调用[stopBleScanning](#func-stopblescanning)可以停止该方法开启的扫描流程。

- 该接口只支持单路扫描，即应用同时只能调用一次，下一次调用前，需要先调用[stopBleScanning](#func-stopblescanning)停止上一次的扫描流程。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|filters|Array\<[ScanFilter](#class-scanfilter)>|是|-|表示扫描结果过滤策略集合，符合过滤条件的设备发现会保留。<br>-若该参数设置为[]，将扫描所有可发现的周边BLE设备，但是不建议使用此方式，可能扫描到非预期设备，并增加功耗。|
|options|?[ScanOptions](#class-scanoptions)|否|None|**命名参数。** 表示扫描的参数配置，可选参数。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[蓝牙服务子系统错误码](./cj-errorcode-bluetooth_manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 801 | Capability not supported. |
  | 2900001 | Service stopped. |
  | 2900003 | Bluetooth disabled. |
  | 2900099 | Operation failed. |

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
class BLEDeviceFindCallback2 <: Callback1Argument<Array<ScanResult>> {
    public func invoke(err: ?BusinessException, devices: Array<ScanResult>): Unit {
        for (device in devices) {
            Hilog.info(0, "Bluetooth", "device has find, deviceID is ${device.deviceId}, name is ${device.deviceName}")
        }
    }
}

let bleDeviceFindCallback = BLEDeviceFindCallback2()
try {
    on(BluetoothBleCallbackType.BleDeviceFind, bleDeviceFindCallback)
    var scanFilter = ScanFilter()
    scanFilter.serviceUUID = "00001888-0000-1000-8000-00805f9b34fb"  // 请替换为您的 serviceUUid
    let scanOptions = ScanOptions(interval: 0, dutyMode: ScanDuty.ScanModeLowPower, matchMode: MatchMode.MatchModeAggressive, phyType: PhyType.PhyLe1M)
    startBleScanning([scanFilter], options: scanOptions)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}", "")
}
```