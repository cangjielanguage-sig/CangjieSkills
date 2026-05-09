### func setBleMtuSize(Int32)

```cangjie
public func setBleMtuSize(mtu: Int32): Unit
```

**功能：** client端同server端协商[MTU](../../connectivity/cj-terminology.md#mtu)（最大传输单元）大小。

- 需先调用[connect](#func-connect)方法，等GATT profile连接成功后才能使用。

- 通过[on(ClientBleMtuChange)](#func-onbluetoothblegattservercallbacktype-callback1argumentint32)，订阅MTU协商结果。

- 如果未协商，MTU大小默认为23字节。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mtu|Int32|是|-|需要协商的mtu大小，取值范围：[23, 517]，单位：Byte。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[蓝牙服务子系统错误码](./cj-errorcode-bluetooth_manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 801 | Capability not supported. |
  | 2900001 | Service stopped. |
  | 2900099 | Operation failed. |

**示例：**

<!-- compile only -->
<!-- compile -->

```cangjie
// index.cj

import ohos.business_exception.*
import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.Hilog

try {
    let gattClient = createGattClientDevice("XX:XX:XX:XX:XX:XX")  // 请替换为您的设备地址
    gattClient.setBleMtuSize(100)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}", "")
}
```