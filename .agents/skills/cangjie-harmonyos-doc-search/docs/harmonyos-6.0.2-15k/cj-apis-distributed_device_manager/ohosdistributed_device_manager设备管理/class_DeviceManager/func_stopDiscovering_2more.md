### func stopDiscovering()

```cangjie
public func stopDiscovering(): Unit
```

**功能：** 停止发现周边设备。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[设备管理错误码](../../errorcodes/cj-errorcode-distributed_device_manager.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied. The application does not have the permission required to call the API.|
  |401|Parameter error. Possible caused by parameter verification failed.|
  |11600101|Failed to execute the function.|
  |11600104|Discovery unavailable.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.DistributedServiceKit.*
import std.collection.*

// 所需要的依赖项
class Callback1ArgumentImpl<A> <: Callback1Argument<A> {
    Callback1ArgumentImpl(let callback: (A) -> Unit) {}

    public func invoke(arg: A): Unit {
        callback(arg)
    }
}

let discoverSuccessCallback = Callback1ArgumentImpl<DeviceBasicInfo> {
    info: DeviceBasicInfo =>
    AppLog.info("in callback, current thread id: ${Thread.currentThread.id}")
    AppLog.info("discover device success, the device info will be printed.")
}

try {
    let dm = createDeviceManager("com.example.myapplication")
    dm.startDiscovering(HashMap<String, ValueType>([("discoverTargetType", Integer(1))]))
    dm.on(DISCOVER_SUCCESS, discoverSuccessCallback)
    sleep(Duration.second * 10) // 发现设备中
    dm.off(DISCOVER_SUCCESS, discoverSuccessCallback)
    dm.stopDiscovering()
} catch (e: BusinessException) {
    AppLog.error(e.toString())
}
```

### func unBindTarget(String)

```cangjie
public func unBindTarget(deviceId: String): Unit
```

**功能：** 解除认证设备。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deviceId|String|是|-|设备标识。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[设备管理错误码](../../errorcodes/cj-errorcode-distributed_device_manager.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied. The application does not have the permission required to call the API.|
  |401|Parameter error. Possible causes: 1. Parameter verification failed; 2. The size of specified deviceId is greater than 255.|
  |11600101|Failed to execute the function.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.DistributedServiceKit.*
import std.collection.*

try {
    let dm = createDeviceManager("com.example.myapplication")
    let deviceId = "XXXXXXXXX"   //实际情况下，添加具体的deviceId
    let bindParam = HashMap<String, ValueType>(
        [("bindType", Integer(1)), ("targetPkgName", Str("xxxx"))])
    dm.unBindTarget(deviceId)
} catch (e: BusinessException) {
    AppLog.error(e.toString())
}
```