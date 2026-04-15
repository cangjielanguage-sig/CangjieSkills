### func setCharacteristicChangeIndication(BleCharacteristic, Bool, AsyncCallback\<Unit>)

```cangjie
public func setCharacteristicChangeIndication(characteristic: BleCharacteristic, enable: Bool, callback: AsyncCallback<Unit>): Unit
```

**功能：** client端启用或者禁用接收server端特征值内容变更指示的能力。

- 需要先调用[getServices](#func-getservicesasynccallbackarraygattservice)，获取到server端所有支持的能力，且需包含指定的入参特征值UUID。

- server端对应的特征值需包含标准协议定义的Client Characteristic Configuration描述符UUID（00002902-0000-1000-8000-00805f9b34fb），server端才能支持发送变更指示。

- 若启用该能力，系统蓝牙服务会自动往server端写Client Characteristic Configuration描述符，启用server端的指示能力。

- 若禁用该能力，系统蓝牙服务会自动往server端写Client Characteristic Configuration描述符，禁用server端的指示能力。

- 通过[on(BleCharacteristicChange)](#func-onbluetoothblegattclientdevicecallbacktype-callback1argumentblecharacteristic)接收server端特征值内容变更指示。

- 若client端收到server端特征值内容变更指示后，系统蓝牙服务会主动回复确认，应用无需关注。

- 回调结果返回后，才能调用下一次读取或者写入操作，如[readCharacteristicValue](#func-readcharacteristicvalueblecharacteristic-asynccallbackblecharacteristic)、[readDescriptorValue](#func-readdescriptorvaluebledescriptor-asynccallbackbledescriptor)、[writeCharacteristicValue](#func-writecharacteristicvalueblecharacteristic-gattwritetype-asynccallbackunit)、[writeDescriptorValue](#func-writedescriptorvaluebledescriptor-asynccallbackunit)、[setCharacteristicChangeNotification](#func-setcharacteristicchangenotificationblecharacteristic-bool-asynccallbackunit)和[setCharacteristicChangeIndication](#func-setcharacteristicchangeindicationblecharacteristic-bool-asynccallbackunit)。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|characteristic|[BleCharacteristic](#class-blecharacteristic)|是|-|需要管理的server端特征值。|
|enable|Bool|是|-|蓝牙设备特征的写入类型。|
|callback|[AsyncCallback](../arkinterop/cj-api-business_exception.md#type-asynccallbackt)\<Unit>|是|-|回调函数。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[蓝牙服务子系统错误码](./cj-errorcode-bluetooth_manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 801 | Capability not supported. |
  | 2900001 | Service stopped. |
  | 2900011 | The operation is busy. The last operation is not completed. |
  | 2900099 | Operation failed. |
  | 2901003 | The connection is not established. |

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