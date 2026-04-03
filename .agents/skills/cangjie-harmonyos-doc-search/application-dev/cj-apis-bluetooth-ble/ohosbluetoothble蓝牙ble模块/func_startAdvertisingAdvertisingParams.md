## func startAdvertising(AdvertisingParams)

```cangjie
public func startAdvertising(advertisingParams: AdvertisingParams): UInt32
```

**功能：** 首次启动发送BLE广播报文。

- 启动成功后，蓝牙子系统会分配相关资源，并返回该广播的标识。

- 若携带了发送广播持续时间，则一定时间后，广播会停止发送，但分配的广播资源还存在。

- 应用可多次调用，支持发起多路广播，每一路广播通过不同的ID标识管理。

- 当应用不再需要该广播时，需调用[stopAdvertising](#func-stopadvertisinguint32)完全停止该广播，不要[stopAdvertising](#func-stopadvertising)混用。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|advertisingParams|[AdvertisingParams](#class-advertisingparams)|是|-|启动BLE广播的相关参数。|

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|广播ID标识。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[蓝牙服务子系统错误码](./cj-errorcode-bluetooth_manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 801 | Capability not supported. |
  | 2900001 | Service stopped. |
  | 2900003 | Bluetooth disabled. |
  | 2900010 | The numeber of advertising resources reaches the upper limit. |
  | 2900099 | Operation failed. |
  | 2902054 | The length of the advertising data exceeds the upper limit. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

let advertisingSettings = AdvertiseSetting()
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
    advertisingResponse: advertisingResponse,
    duration: 300
)
try {
    let advHandle = startAdvertising(advertisingParams)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}", "")
}
```