## func on(BluetoothConnectionCallbackType, Callback1Argument\<PinRequiredParam>)

```cangjie
public func on(`type`: BluetoothConnectionCallbackType, callback: Callback1Argument<PinRequiredParam>): Unit
```

**功能：** 订阅远端蓝牙设备的配对请求事件。使用Callback异步回调。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|\`type`|[BluetoothConnectionCallbackType](#enum-bluetoothconnectioncallbacktype)|是|填写`PIN_REQUIRED`，表示配对请求事件。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[PinRequiredParam](#class-pinrequiredparam)>|是|表示回调函数的入参，配对请求。回调函数由用户创建通过该接口注册。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :---------------------------- |
  |201 | Permission denied. |
  |401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
  |801 | Capability not supported. |
  |2900099 | Operation failed.|

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

## func pairDevice(String)

```cangjie
public func pairDevice(deviceId: String): Unit
```

**功能：** 发起蓝牙配对。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|deviceId|String|是|表示配对的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。|

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
    pairDevice("XX:XX:XX:XX:XX:XX") // 用户自定义设备地址
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```