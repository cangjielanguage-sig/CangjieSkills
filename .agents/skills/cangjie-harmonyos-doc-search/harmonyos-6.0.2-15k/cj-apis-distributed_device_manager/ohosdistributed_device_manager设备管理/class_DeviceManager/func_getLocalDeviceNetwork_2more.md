### func getLocalDeviceNetworkId()

```cangjie
public func getLocalDeviceNetworkId(): String
```

**功能：** 获取本地设备网络标识。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回本地设备网络标识。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[设备管理错误码](../../errorcodes/cj-errorcode-distributed_device_manager.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied. The application does not have the permission required to call the API.|
  |11600101|Failed to execute the function.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.DistributedServiceKit.*

try {
    let dm = createDeviceManager("com.example.myapplication")
    let networkId = dm.getLocalDeviceNetworkId()
} catch (e: BusinessException) {
    AppLog.error(e.toString())
}
```

### func getLocalDeviceType()

```cangjie
public func getLocalDeviceType(): Int32
```

**功能：** 获取本地设备类型。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回本地[设备类型](#func-getdevicetypestring)。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[设备管理错误码](../../errorcodes/cj-errorcode-distributed_device_manager.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied. The application does not have the permission required to call the API.|
  |11600101|Failed to execute the function.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.DistributedServiceKit.*

try {
    let dm = createDeviceManager("com.example.myapplication")
    let deviceType = dm.getLocalDeviceType()
} catch (e: BusinessException) {
    AppLog.error(e.toString())
}
```