### func writeDescriptorValue(BleDescriptor, AsyncCallback\<Unit>)

```cangjie
public func writeDescriptorValue(descriptor: BleDescriptor, callback: AsyncCallback<Unit>): Unit
```

**功能：** client端向指定的server端描述符写入数据。

- 需要先调用[getServices](#func-getservicesasynccallbackarraygattservice)，获取到server端所有支持的能力，且包含指定的入参描述符UUID；否则会写入失败。

- 回调结果返回后，才能调用下一次读取或者写入操作，如[readCharacteristicValue](#func-readcharacteristicvalueblecharacteristic-asynccallbackblecharacteristic)、[readDescriptorValue](#func-readdescriptorvaluebledescriptor-asynccallbackbledescriptor)、[writeCharacteristicValue](#func-writecharacteristicvalueblecharacteristic-gattwritetype-asynccallbackunit)、[writeDescriptorValue](#func-writedescriptorvaluebledescriptor-asynccallbackunit)、[setCharacteristicChangeNotification](#func-setcharacteristicchangenotificationblecharacteristic-bool-asynccallbackunit)和[setCharacteristicChangeIndication](#func-setcharacteristicchangeindicationblecharacteristic-bool-asynccallbackunit)。

- 应用单次可写入的描述符数据长度默认限制为（MTU-3）字节，MTU大小可由[setBleMtuSize](#func-setblemtusizeint32)接口指定。

- Client Characteristic Configuration描述符（UUID：00002902-0000-1000-8000-00805f9b34fb）和 Server Characteristic Configuration描述符（UUID：00002903-0000-1000-8000-00805f9b34fb）较为特殊，蓝牙标准协议规定内容长度为2字节，写入内容长度应设置为2字节。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|descriptor|[BleDescriptor](#class-bledescriptor)|是|-|需要写入的描述符，包含写入的数据内容。|
|callback|[AsyncCallback](../arkinterop/cj-api-business_exception.md#type-asynccallbackt)\<Unit>|是|-|回调函数。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[蓝牙服务子系统错误码](./cj-errorcode-bluetooth_manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 801 | Capability not supported. |
  | 2900001 | Service stopped. |
  | 2900011 | The operation is busy. The last operation is not complete. |
  | 2900099 | Operation failed. |
  | 2901001 | Write forbidden. |
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

let descBuffer: Array<Byte> = [31, 32]
let descriptor = BleDescriptor(
    "00001810-0000-1000-8000-00805F9B34FB",
    "00001820-0000-1000-8000-00805F9B34FB",
    "00002903-0000-1000-8000-00805F9B34FB",
    Array<Byte>(2, repeat: 0)
)
let descriptors: BleDescriptor = descriptor
let charBuffer: Array<Byte> = [1, 2]
let properties = GattProperties()

try {
    let gattClient = createGattClientDevice("XX:XX:XX:XX:XX:XX")  // 请替换为您的设备地址
    gattClient.writeDescriptorValue(descriptors) {
        error: ?BusinessException, c: ?Unit => if (let Some(e) <- error) {
            throw e
        }
    }
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}", "")
}
```