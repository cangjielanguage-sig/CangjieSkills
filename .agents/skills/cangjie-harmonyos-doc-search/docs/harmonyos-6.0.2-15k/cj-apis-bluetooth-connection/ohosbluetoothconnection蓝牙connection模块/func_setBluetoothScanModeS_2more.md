## func setBluetoothScanMode(ScanMode, Int32)

```cangjie
public func setBluetoothScanMode(mode: ScanMode, duration: Int32): Unit
```

**功能：** 设置蓝牙扫描模式，可以被远端设备发现。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|mode|[ScanMode](#enum-scanmode)|是|蓝牙扫描模式。当扫描模式为SCAN_MODE_GENERAL_DISCOVERABLE时，如果超出duration持续时间（不为0），扫描模式会重新设置为SCAN_MODE_CONNECTABLE。|
|duration|Int32|是|设备可被发现的持续时间，单位为毫秒；设置为0则持续可发现。|

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
import kit.PerformanceAnalysisKit.*

try {
    setBluetoothScanMode(SCAN_MODE_CONNECTABLE_GENERAL_DISCOVERABLE, 100)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

## func setDevicePairingConfirmation(String, Bool)

```cangjie
public func setDevicePairingConfirmation(deviceId: String, accept: Bool): Unit
```

**功能：** 设置设备配对请求确认。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH 和 ohos.permission.MANAGE_BLUETOOTH（该权限仅系统应用可申请）

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|deviceId|String|是|表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。|
|accept|Bool|是|接受配对请求设置为true，否则设置为false。|

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
import kit.PerformanceAnalysisKit.*

// 此处代码可添加在依赖项定义中
class PinRequiredCallback <: Callback1Argument<PinRequiredParam> {
    public func invoke(data: PinRequiredParam): Unit {
        setDevicePairingConfirmation(data.deviceId, true)
    }
}

let onPairConfirmed = PinRequiredCallback()
try {
    on(PIN_REQUIRED, onPairConfirmed)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```