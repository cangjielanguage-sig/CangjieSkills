## func getRemoteProfileUuids(String)

```cangjie
public func getRemoteProfileUuids(deviceId: String): Array<ProfileUuids>
```

**功能：** 获取对端蓝牙设备支持的Profile UUID。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|deviceId|String|是|表示配对的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[ProfileUuids](cj-apis-bluetooth-constant.md#enum-profileuuids)>|对端蓝牙设备支持的Profile UUID。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameter.|
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
import kit.PerformanceAnalysisKit.*

try {
    getRemoteProfileUuids("XX:XX:XX:XX:XX:XX") // 用户自定义设备地址
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

## func isBluetoothDiscovering()

```cangjie
public func isBluetoothDiscovering(): Bool
```

**功能：** 查询设备的蓝牙发现状态。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|设备已开启蓝牙发现为true，否则为false。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
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
import kit.PerformanceAnalysisKit.*

try {
    let res: Bool = isBluetoothDiscovering()
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```