## func getProfileConnectionState(?ProfileId)

```cangjie
public func getProfileConnectionState(profileId!: ?ProfileId = None): ProfileConnectionState
```

**功能：** 获取蓝牙Profile的连接状态。如果携带ProfileId，则返回的是当前Profile的连接状态。如果未携带ProfileId，任一Profile已连接则返回STATE_CONNECTED，否则返回STATE_DISCONNECTED。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|profileId|?[ProfileId](cj-apis-bluetooth-constant.md#enum-profileid)|否|None| **命名参数。** 表示profile的枚举值，例如：PROFILE_A2DP_SOURCE。|

**返回值：**

|类型|说明|
|:----|:----|
|[ProfileConnectionState](cj-apis-bluetooth-constant.md#enum-profileconnectionstate)|profile的连接状态。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameter. Possible causes: 1. Incorrect parameter types.|
  |801|Capability not supported.|
  |2900001|Service stopped.|
  |2900003|Bluetooth disabled.|
  |2900004|Profile not supported.|
  |2900099|Operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.*

try {
    getProfileConnectionState(profileId: ProfileId.PROFILE_A2DP_SOURCE)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

## func getRemoteDeviceBatteryInfo(String)

```cangjie
public func getRemoteDeviceBatteryInfo(deviceId: String): BatteryInfo
```

**功能：** 获取蓝牙远端设备的电量信息。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|deviceId|String|是|表示远端设备MAC地址，例如："XX:XX:XX:XX:XX:XX"。|

**返回值：**

|类型|说明|
|:----|:----|
|[BatteryInfo](#class-batteryinfo)|蓝牙远端设备的电量信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.|
  |2900001|Service stopped.|
  |2900003|Bluetooth disabled.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.*

try {
    getRemoteDeviceBatteryInfo("XX:XX:XX:XX:XX:XX") // 用户自定义设备地址
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```