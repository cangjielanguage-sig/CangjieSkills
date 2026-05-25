## func startAdvertising(AdvertiseSetting, AdvertiseData, ?AdvertiseData)

```cangjie
public func startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse!: ?AdvertiseData = None): Unit
```

**功能：** 开始发送BLE广播。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|setting|[AdvertiseSetting](#class-advertisesetting)|是|-|BLE广播的相关参数。|
|advData|[AdvertiseData](#class-advertisedata)|是|-|BLE广播包内容。|
|advResponse|?[AdvertiseData](#class-advertisedata)|否|None| **命名参数。** BLE回复扫描请求回复响应。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.|
  |801|Capability not supported.|
  |2900001|Service stopped.|
  |2900003|Bluetooth disabled.|
  |2900010 | The number of advertising resources reaches the upper limit.       |
  |2900099 | Operation failed.                        |
  |2902054 | The length of the advertising data exceeds the upper limit.        |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import ohos.hilog.Hilog

let advertisingSettings = AdvertiseSetting(32, 0, true)
let manufactureDataUnit = ManufactureData(
    4567u16,
    [1, 2, 3, 4]
)
let serviceDataUnit = ServiceData(
    "00001888-0000-1000-8000-00805f9b34fb",
    [5, 6, 7, 8]
)
let advertisingData = AdvertiseData(
    ["00001888-0000-1000-8000-00805f9b34fb"],
    [manufactureDataUnit],
    [serviceDataUnit],
    includeDeviceName: true
)
let advertisingResponse = AdvertiseData(
    ["00001888-0000-1000-8000-00805f9b34fb"],
    [manufactureDataUnit],
    [serviceDataUnit]
)
try {
    startAdvertising(advertisingSettings, advertisingData, advResponse: advertisingResponse)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```