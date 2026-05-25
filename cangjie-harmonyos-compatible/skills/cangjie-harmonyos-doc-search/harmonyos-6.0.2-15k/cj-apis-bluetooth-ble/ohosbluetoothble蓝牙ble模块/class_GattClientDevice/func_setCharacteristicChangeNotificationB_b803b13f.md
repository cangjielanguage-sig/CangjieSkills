### func setCharacteristicChangeNotification(BLECharacteristic, Bool)

```cangjie
public func setCharacteristicChangeNotification(characteristic: BLECharacteristic, enable: Bool): Unit
```

**功能：** 向服务端发送设置通知此特征值请求。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|characteristic|[BLECharacteristic](#class-blecharacteristic)|是|蓝牙低功耗特征。|
|enable|Bool|是|启用接收notify设置为true，否则设置为false。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.|
  |801|Capability not supported.|
  |2900001|Service stopped.|
  |2900099|Operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import ohos.hilog.Hilog

let gattClient = createGattClientDevice("XX:XX:XX:XX:XX:XX")

// 创建descriptors
let descBuffer: Array<Byte> = [31, 32]
let descriptor = BLEDescriptor(
    "00001810-0000-1000-8000-00805F9B34FB",
    "00001820-0000-1000-8000-00805F9B34FB",
    "00002902-0000-1000-8000-00805F9B34FB",
    Array<Byte>(2, repeat: 0)
)
// 创建characteristics
let descriptors: Array<BLEDescriptor> = [descriptor]
let charBuffer: Array<Byte> = [21, 22]
let properties = GattProperties()

let characteristic: BLECharacteristic = BLECharacteristic(
    "00001810-0000-1000-8000-00805F9B34FB",
    "00001820-0000-1000-8000-00805F9B34FB",
    charBuffer,
    descriptors,
    properties
)

try {
    gattClient.setCharacteristicChangeNotification(characteristic, false)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```