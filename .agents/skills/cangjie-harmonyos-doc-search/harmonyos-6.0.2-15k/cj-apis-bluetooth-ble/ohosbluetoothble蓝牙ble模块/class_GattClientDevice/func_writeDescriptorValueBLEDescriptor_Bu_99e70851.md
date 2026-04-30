### func writeDescriptorValue(BLEDescriptor, (?BusinessException) -> Unit)

```cangjie
public func writeDescriptorValue(descriptor: BLEDescriptor, callback: (?BusinessException) -> Unit): Unit
```

**功能：** client端向低功耗蓝牙设备特定的描述符写入二进制数据。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|descriptor|[BLEDescriptor](#class-bledescriptor)|是|蓝牙设备描述符的二进制值及其它参数。|
|callback|(?[BusinessException](../BasicServicesKit/cj-apis-base.md#class-businessexception)) -> Unit|是|回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.|
  |801|Capability not supported.|
  |2900011 | The operation is busy. The last operation is not complete.             |
  |2900099 | Operation failed.                        |
  |2901001 | Write forbidden.                        |
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

let descBuffer: Array<Byte> = [31, 32]
let descriptor = BLEDescriptor(
    "00001810-0000-1000-8000-00805F9B34FB",
    "00001820-0000-1000-8000-00805F9B34FB",
    "00002903-0000-1000-8000-00805F9B34FB",
    Array<Byte>(2, repeat: 0)
)
let descriptors: BLEDescriptor = descriptor
let charBuffer: Array<Byte> = [1, 2]
let properties = GattProperties()

try {
    gattClient.writeDescriptorValue(descriptors) {
        error: ?BusinessException => if (let Some(e) <- error) {
            throw e
        }
    }
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```