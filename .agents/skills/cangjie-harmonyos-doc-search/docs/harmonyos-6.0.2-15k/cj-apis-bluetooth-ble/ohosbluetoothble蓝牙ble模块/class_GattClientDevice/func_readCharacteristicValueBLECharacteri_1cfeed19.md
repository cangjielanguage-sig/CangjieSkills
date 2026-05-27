### func readCharacteristicValue(BLECharacteristic, (?BusinessException, ?BLECharacteristic) -> Unit)

```cangjie
public func readCharacteristicValue(characteristic: BLECharacteristic,
    callback: (?BusinessException, ?BLECharacteristic) -> Unit): Unit
```

**功能：** client端读取蓝牙低功耗设备特定服务的特征值。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|characteristic|[BLECharacteristic](#class-blecharacteristic)|是|待读取的特征值。|
|callback|(?[BusinessException](../BasicServicesKit/cj-apis-base.md#class-businessexception), ?[BLECharacteristic](#class-blecharacteristic)) -> Unit|是|client读取特征值，通过注册回调函数获取。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.|
  |801|Capability not supported.|
  |2900001|Service stopped.|
  |2900011 | The operation is busy. The last operation is not complete.             |
  |2900099 | Operation failed.                        |
  |2901000 | Read forbidden.                         |
  |2901003 | The connection is not established.                |
  |2901004 | The connection is congested.                |
  |2901005 | The connection is not encrypted.                |
  |2901006 | The connection is not authenticated.                |
  |2901007 | The connection is not authorized.                |

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
    gattClient.readCharacteristicValue(characteristic) {
        error: ?BusinessException, outData: ?BLECharacteristic =>
        if (let Some(e) <- error) {
            throw e
        }
        if (let Some(c) <- outData) {
            Hilog.info(0, "Bluetooth", "read characteristic value uuid is ${c.characteristicUuid}")
            let message = StringBuilder("logCharacteristic value: ")
            for (i in 0..c.characteristicValue.size) {
                message.append(c.characteristicValue[i])
            }
            Hilog.info(0, "Bluetooth", message.toString())
        }
    }
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```