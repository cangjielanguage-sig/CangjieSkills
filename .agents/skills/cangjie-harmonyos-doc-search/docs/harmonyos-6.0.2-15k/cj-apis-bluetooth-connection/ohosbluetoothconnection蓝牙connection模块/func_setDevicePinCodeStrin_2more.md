## func setDevicePinCode(String, String)

```cangjie
public func setDevicePinCode(deviceId: String, code: String): Unit
```

**功能：** 当蓝牙配对类型PinType为PIN_TYPE_ENTER_PIN_CODE或PIN_TYPE_PIN_16_DIGITS时调用此接口，请求用户输入PIN码。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|deviceId|String|是|表示远端设备MAC地址，例如："XX:XX:XX:XX:XX:XX"。|
|code|String|是|用户输入的PIN码。|

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
    setDevicePinCode("XX:XX:XX:XX:XX:XX", "xxxxx") // 用户自定义设备地址和PIN码
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

## func setLocalName(String)

```cangjie
public func setLocalName(name: String): Unit
```

**功能：** 设置蓝牙本地设备名称。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|name|String|是|要设置的蓝牙名称，最大长度为248字节数。|

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
    setLocalName("device_name")
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```