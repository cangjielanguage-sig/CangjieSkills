## class DeviceManager

```cangjie
public class DeviceManager {}
```

**功能：** 设备管理类，用于获取可信设备和本地设备的相关信息，并提供了发现、绑定周边设备的方法。在调用DeviceManager的方法前，需要先通过createDeviceManager构建一个DeviceManager实例。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

### func bindTarget(String, HashMap\<String, ValueType>)

```cangjie
public func bindTarget(deviceId: String, bindParam: HashMap<String, ValueType>): String
```

**功能：** 认证设备。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deviceId|String|是|-|设备标识。|
|bindParam|HashMap\<String, [ValueType](#enum-valuetype)>|是|-|认证参数。由开发者自行决定传入的键值对。默认会携带以下key值：<br>bindType: Integer，此值是绑定的类型，必填。<br>- 1：PIN码。<br>targetPkgName: Str，绑定目标的包名。<br>appName：Str，尝试绑定目标的应用程序名称。<br>appOperation：Str，应用程序要绑定目标的原因。<br>customDescription Str，操作的详细说明。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回认证设备的deviceId。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[设备管理错误码](../../errorcodes/cj-errorcode-distributed_device_manager.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied. The application does not have the permission required to call the API.|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified deviceId is greater than 255.|
  |11600101|Failed to execute the function.|
  |11600103|Authentication unavailable.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.DistributedServiceKit.*
import std.collection.*

let dm = createDeviceManager("com.example.myapplication")
let deviceId = "XXXXXXXXX"   //实际情况下，添加具体的deviceId
let bindParam = HashMap<String, ValueType>(
    [("bindType", Integer(1)), ("targetPkgName", Str("xxxx"))])
dm.bindTarget(deviceId, bindParam)
```