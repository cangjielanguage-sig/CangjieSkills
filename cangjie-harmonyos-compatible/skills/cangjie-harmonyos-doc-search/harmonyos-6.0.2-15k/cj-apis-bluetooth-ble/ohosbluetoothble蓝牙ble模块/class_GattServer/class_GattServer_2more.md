## class GattServer

```cangjie
public class GattServer {}
```

**功能：** server端类。使用server端方法之前需要创建该类的实例进行操作，通过[createGattServer()](#func-creategattserver)方法构造此实例。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func addService(GattService)

```cangjie
public func addService(service: GattService): Unit
```

**功能：** server端添加服务。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|service|[GattService](#class-gattservice)|是|服务端的service数据。BLE广播的相关参数。|

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

// 创建descriptors
let descBuffer: Array<Byte> = [31, 32]
let descriptors0 = BLEDescriptor(
    "00001810-0000-1000-8000-00805F9B34FB",
    "00001820-0000-1000-8000-00805F9B34FB",
    "00002902-0000-1000-8000-00805F9B34FB",
    Array<Byte>(2, repeat: 0)
)
let descriptors1 = BLEDescriptor(
    "00001810-0000-1000-8000-00805F9B34FB",
    "00001820-0000-1000-8000-00805F9B34FB",
    "00002903-0000-1000-8000-00805F9B34FB",
    descBuffer
)

// 创建characteristics
let descriptors: Array<BLEDescriptor> = [descriptors0, descriptors1]
let charBuffer: Array<Byte> = [21, 22]
let properties = GattProperties()

let characteristic: BLECharacteristic = BLECharacteristic(
    "00001810-0000-1000-8000-00805F9B34FB",
    "00001820-0000-1000-8000-00805F9B34FB",
    charBuffer,
    descriptors,
    properties
)

let characteristics: Array<BLECharacteristic> = [characteristic]
let gattService: GattService = GattService(
    "00001810-0000-1000-8000-00805F9B34FB",
    true,
    characteristics,
    Array<GattService>()
)

try {
    //构造gattServer
    let gattServer = createGattServer()
    gattServer.addService(gattService)
} catch (e: BusinessException) {
    AppLog.error("add Service error because ${e}")
}
```