### func startDiscovering(HashMap\<String, ValueType>, ?HashMap\<String, ValueType>)

```cangjie
public func startDiscovering(
    discoverParam: HashMap<String, ValueType>, filterOptions!: ?HashMap<String, ValueType> = None): Unit
```

**功能：** 发现周边设备。发现状态持续两分钟，超过两分钟，会停止发现，最大发现数量99个。wifi场景要求同局域网。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|discoverParam|HashMap\<String, [ValueType](#enum-valuetype)>|是|-|发现标识。标识发现的目标类型。<br>discoverTargetType：Integer，发现目标默认为设备，值为1。|
|filterOptions|?HashMap\<String, [ValueType](#enum-valuetype)>|否|None| **命名参数。** 发现设备过滤信息。可选，默认为None，发现未上线设备。会携带以下key值：<br>availableStatus：Integer，0-1，仅发现设备可信，值为0表示设备不可信。<br>0：设备离线，客户端需要通过调用bindTarget绑定设备。<br>1：设备已在线，客户可以进行连接。<br>discoverDistance：Integer，0-100，发现距离本地一定距离内的设备，单位为cm。wifi场景不传该参数。<br>authenticationStatus：Integer，0-1，根据不同的认证状态发现设备：<br>0：设备未认证。<br>1：设备已认证。<br>authorizationType：Integer，0-2，根据不同的授权类型发现设备：<br>0：根据临时协商的会话密钥认证的设备。<br>1：基于同账号密钥进行身份验证的设备。<br>2：基于不同账号凭据密钥认证的设备。|

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