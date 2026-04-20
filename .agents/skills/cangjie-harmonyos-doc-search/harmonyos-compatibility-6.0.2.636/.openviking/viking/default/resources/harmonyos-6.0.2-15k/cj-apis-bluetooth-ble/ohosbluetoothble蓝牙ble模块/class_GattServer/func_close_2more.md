### func close()

```cangjie
public func close(): Unit
```

**功能：** 关闭服务端功能，去掉server在协议栈的注册。调用该接口后[GattServer](#class-gattserver)实例将不能再使用。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
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

let gattServer = createGattServer()
try {
    gattServer.close()
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func notifyCharacteristicChanged(String, NotifyCharacteristic)

```cangjie
public func notifyCharacteristicChanged(deviceId: String, notifyCharacteristic: NotifyCharacteristic): Unit
```

**功能：** server端特征值发生变化时，主动通知已连接的client设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|deviceId|String|是|接收通知的client端设备地址，例如“XX:XX:XX:XX:XX:XX”。|
|notifyCharacteristic|[NotifyCharacteristic](#class-notifycharacteristic)|是|通知的特征值数据。|

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

let gattServer = createGattServer()
try {
    let charBuffer: Array<Byte> = [21, 22]
    let notifyCharacteristic = NotifyCharacteristic(
        "00001810-0000-1000-8000-00805F9B34FB",
        "00001820-0000-1000-8000-00805F9B34FB",
        charBuffer,
        false
    )
    gattServer.notifyCharacteristicChanged("XX:XX:XX:XX:XX:XX", notifyCharacteristic)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```