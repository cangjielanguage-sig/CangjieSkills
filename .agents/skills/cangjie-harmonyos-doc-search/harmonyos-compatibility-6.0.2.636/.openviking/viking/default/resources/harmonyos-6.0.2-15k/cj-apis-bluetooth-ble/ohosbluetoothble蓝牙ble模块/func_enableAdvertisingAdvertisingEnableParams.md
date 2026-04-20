## func enableAdvertising(AdvertisingEnableParams)

```cangjie
public func enableAdvertising(advertisingEnableParams: AdvertisingEnableParams): Unit
```

**功能：** 临时启动BLE广播。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|advertisingEnableParams|[AdvertisingEnableParams](#class-advertisingenableparams)|是|临时启动BLE广播的相关参数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|
  |801|Capability not supported.|
  |2900001|Service stopped.|
  |2900003|Bluetooth disabled.|
  |2900099|Operation failed.|
  |2902055 | Invalid advertising id.                        |

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
let advertisingParams = AdvertisingParams(
    advertisingSettings,
    advertisingData,
    advertisingResponse,
    duration: 300
)

var advHandle: UInt32 = 0xFF

try {
    advHandle = startAdvertising(advertisingParams)

    let advertisingEnableParams = AdvertisingEnableParams(advHandle, duration: 1000)
    enableAdvertising(advertisingEnableParams)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```