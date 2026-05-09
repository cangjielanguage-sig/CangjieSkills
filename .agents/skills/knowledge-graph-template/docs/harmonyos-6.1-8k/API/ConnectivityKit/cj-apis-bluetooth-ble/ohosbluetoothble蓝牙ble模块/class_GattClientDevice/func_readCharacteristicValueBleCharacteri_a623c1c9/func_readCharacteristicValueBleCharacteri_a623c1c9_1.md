### func readCharacteristicValue(BleCharacteristic, AsyncCallback\<BleCharacteristic>)

```cangjie
public func readCharacteristicValue(
    characteristic: BleCharacteristic,
    callback: AsyncCallback<BleCharacteristic>
): Unit
```

**功能：** client端从指定的server端特征值读取数据。

- 需要先调用[getServices](#func-getservicesasynccallbackarraygattservice)，获取到server端所有支持的能力，且包含指定的入参特征值UUID；否则会读取失败。

- 回调结果返回后，才能调用下一次读取或者写入操作，如[readCharacteristicValue](#func-readcharacteristicvalueblecharacteristic-asynccallbackblecharacteristic)、[readDescriptorValue](#func-readdescriptorvaluebledescriptor-asynccallbackbledescriptor)、[writeCharacteristicValue](#func-writecharacteristicvalueblecharacteristic-gattwritetype-asynccallbackunit)、[writeDescriptorValue](#func-writedescriptorvaluebledescriptor-asynccallbackunit)、[setCharacteristicChangeNotification](#func-setcharacteristicchangenotificationblecharacteristic-bool-asynccallbackunit)和[setCharacteristicChangeIndication](#func-setcharacteristicchangeindicationblecharacteristic-bool-asynccallbackunit)。

- 读取特征值过程中，需确保[BleCharacteristic](#class-blecharacteristic)入参特征值的serviceUUID、characteristicUUID准确。characteristicValue表示的数据内容长度可由用户任意指定，不会影响实际读取到的特征值数据内容。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|characteristic|[BleCharacteristic](#class-blecharacteristic)|是|-|需要读取的特征值。|
|callback|[AsyncCallback](../arkinterop/cj-api-business_exception.md#type-asynccallbackt)\<[BleCharacteristic](#class-blecharacteristic)>|是|-|回调函数。当读取成功，获取到的特征值对象，包含读取到的数据内容。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[蓝牙服务子系统错误码](./cj-errorcode-bluetooth_manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 801 | Capability not supported. |
  | 2900001 | Service stopped. |
  | 2900011 | The operation is busy. The last operation is not completed. |
  | 2900099 | Operation failed. |
  | 2901000 | Read forbidden. |
  | 2901003 | The connection is not established. |
  | 2901004 | The connection is congested. |
  | 2901005 | The connection is not encrypted. |
  | 2901006 | The connection is not authenticated. |
  | 2901007 | The connection is not authorized. |

**示例：**

<!-- compile only -->
<!-- compile -->

```cangjie
// index.cj

import ohos.business_exception.*
import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.Hilog

// 创建descriptors
let descBuffer: Array<Byte> = [31, 32]
let descriptor = BleDescriptor(
    "00001810-0000-1000-8000-00805F9B34FB",
    "00001820-0000-1000-8000-00805F9B34FB",
    "00002902-0000-1000-8000-00805F9B34FB",
    Array<Byte>(2, repeat: 0)
)
// 创建characteristics
let descriptors: Array<BleDescriptor> = [descriptor]
let charBuffer: Array<Byte> = [21, 22]
let properties = GattProperties()

let characteristic: BleCharacteristic = BleCharacteristic(
    "00001810-0000-1000-8000-00805F9B34FB",
    "00001820-0000-1000-8000-00805F9B34FB",
    charBuffer,
    descriptors,
    properties: properties
)