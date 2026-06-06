## func startBLEScan(Array\<ScanFilter>, ?ScanOptions)

```cangjie
public func startBLEScan(filters: Array<ScanFilter>, options!: ?ScanOptions = None): Unit
```

**功能：** 发起BLE扫描流程。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|filters|Array\<[ScanFilter](#class-scanfilter)>|是|-|表示扫描结果过滤策略集合，符合过滤条件的设备发现会保留。|
|options|?[ScanOptions](#class-scanoptions)|否|None| **命名参数。** 表示扫描的参数配置，可选参数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.|
  |801|Capability not supported.|
  |2900001|Service stopped.|
  |2900003|Bluetooth disabled.|
  |2900099|Operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import ohos.hilog.Hilog

// 此处代码可添加在依赖项定义中
class BLEDeviceFindCallback <: Callback1Argument<Array<ScanResult>> {
    public func invoke(devices: Array<ScanResult>): Unit {
        for (device in devices) {
            Hilog.info(0, "Bluetooth", "device has find, deviceID is ${device.deviceId}, name is ${device.deviceName}")
        }
    }
}

let bleDeviceFindCallback = BLEDeviceFindCallback()
try {
    on(BLE_DEVICE_FIND, bleDeviceFindCallback)
    var scanFilter = ScanFilter()
    scanFilter.serviceUuid = "00001888-0000-1000-8000-00805f9b34fb"
    let scanOptions = ScanOptions(0, SCAN_MODE_LOW_POWER, MATCH_MODE_AGGRESSIVE, PHY_LE_1M)
    startBLEScan([scanFilter], options: scanOptions)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```