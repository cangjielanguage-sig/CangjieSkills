### func getAvailableDeviceList()

```cangjie
public func getAvailableDeviceList(): Array<DeviceBasicInfo>
```

**功能：** 同步获取所有可信设备列表。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[DeviceBasicInfo](#class-devicebasicinfo)>|返回可信设备列表。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[设备管理错误码](../../errorcodes/cj-errorcode-distributed_device_manager.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied. The application does not have the permission required to call the API.|
  |401|Parameter error. Possible caused by parameter verification failed.|
  |11600101|Failed to execute the function.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.DistributedServiceKit.*

try {
    let dm = createDeviceManager("com.example.myapplication")
    let deviceInfoList = dm.getAvailableDeviceList()
} catch (e: BusinessException) {
    AppLog.error(e.toString())
}
```

### func getDeviceName(String)

```cangjie
public func getDeviceName(networkId: String): String
```

**功能：** 通过指定设备的网络标识获取该设备名称。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|networkId|String|是|-|设备的网络标识。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回指定设备名称。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[设备管理错误码](../../errorcodes/cj-errorcode-distributed_device_manager.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied. The application does not have the permission required to call the API.|
  |401|Parameter error. Possible causes: 1.Parameter verification failed; 2. The size of specified networkId is greater than 255.|
  |11600101|Failed to execute the function.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.DistributedServiceKit.*

try {
    let dm = createDeviceManager("com.example.myapplication")
    let networkId = "XXXX"   //实际情况下，添加具体的networkId
    let deviceName = dm.getDeviceName(networkId)
} catch (e: BusinessException) {
    AppLog.error(e.toString())
}
```