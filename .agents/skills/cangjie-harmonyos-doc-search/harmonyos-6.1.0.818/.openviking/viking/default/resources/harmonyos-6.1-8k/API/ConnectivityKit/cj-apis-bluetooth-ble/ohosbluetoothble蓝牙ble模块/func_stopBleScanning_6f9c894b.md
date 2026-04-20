## func stopBleScanning()

```cangjie
public func stopBleScanning(): Unit
```

**功能：** 停止BLE扫描流程。

- 停止的BLE扫描由[startBleScanning](#func-startblescanningarrayscanfilter-scanoptions)触发。

- 当应用不再需要扫描BLE设备时，需主动调用该方法停止扫描。

- 调用此接口后将不再收到扫描结果上报，重新开启BLE扫描即可再次扫到BLE设备。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

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
    stopBleScanning()
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}", "")
}
```