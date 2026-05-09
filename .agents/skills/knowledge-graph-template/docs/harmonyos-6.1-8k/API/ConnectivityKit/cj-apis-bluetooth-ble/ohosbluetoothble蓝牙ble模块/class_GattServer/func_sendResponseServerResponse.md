### func sendResponse(ServerResponse)

```cangjie
public func sendResponse(serverResponse: ServerResponse): Unit
```

**功能：** server端收到client的请求操作后，需要调用此接口回复client，否则可能导致链路异常，超时后断连。

client请求是指通过下述接口订阅回调收到的请求消息：

- [on(CharacteristicRead)](#func-onbluetoothblegattservercallbacktype-callback1argumentcharacteristicreadrequest)
- [on(CharacteristicWrite)](#func-onbluetoothblegattservercallbacktype-callback1argumentcharacteristicwriterequest)，需根据[CharacteristicWriteRequest](#class-characteristicwriterequest)中的needRsp决定是否需要回复。
- [on(DescriptorRead)](#func-onbluetoothblegattservercallbacktype-callback1argumentdescriptorreadrequest)
- [on(DescriptorWrite)](#func-onbluetoothblegattservercallbacktype-callback1argumentdescriptorwriterequest)，需根据[DescriptorWriteRequest](#class-descriptorwriterequest)中的needRsp决定是否需要回复。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|serverResponse|ServerResponse|是|-|server端回复client的响应数据。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[蓝牙服务子系统错误码](./cj-errorcode-bluetooth_manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 801 | Capability not supported. |
  | 2900001 | Service stopped. |
  | 2900003 | Bluetooth disabled. |
  | 2900099 | Operation failed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.business_exception.*
import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.Hilog

try {
    let rspBuffer = Array<Byte>()
    let serverResponse: ServerResponse = ServerResponse(
        "XX:XX:XX:XX:XX:XX", 0, 0, 0,
        rspBuffer
    )
    let gattServer = createGattServer()
    gattServer.sendResponse(serverResponse)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}", "")
}
```