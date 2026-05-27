### func getDeviceType(String)

```cangjie
public func getDeviceType(networkId: String): Int32
```

**功能：** 通过指定设备的网络标识获取该设备类型。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|networkId|String|是|-|设备的网络标识。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回指定设备类型。目前仅支持以下设备类型：<br>0: UNKNOWN。<br>14: PHONE。<br>17: PAD。<br>156: TV。<br>131: CAR。<br>109: WATCH。<br>8: WiFiCamera。<br>2562: SMART_DISPLAY。<br>2607: 2in1。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[设备管理错误码](../../errorcodes/cj-errorcode-distributed_device_manager.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied. The application does not have the permission required to call the API.|
  |401|Parameter error. Possible causes: 1. Parameter verification failed; 2. The size of specified networkId is greater than 255.|
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
    let deviceType = dm.getDeviceType(networkId)
} catch (e: BusinessException) {
    AppLog.error(e.toString())
}
```

### func getLocalDeviceId()

```cangjie
public func getLocalDeviceId(): String
```

**功能：** 获取本地设备id，实际值为udid-hash与appid和盐值基于sha256方式进行混淆后的值。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回本地设备id。|

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
    let deviceId = dm.getLocalDeviceId()
} catch (e: BusinessException) {
    AppLog.error(e.toString())
}
```

### func getLocalDeviceName()

```cangjie
public func getLocalDeviceName(): String
```

**功能：** 获取本地设备名称。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回本地设备名称。|

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
    let deviceName = dm.getLocalDeviceName()
} catch (e: BusinessException) {
    AppLog.error(e.toString())
}
```