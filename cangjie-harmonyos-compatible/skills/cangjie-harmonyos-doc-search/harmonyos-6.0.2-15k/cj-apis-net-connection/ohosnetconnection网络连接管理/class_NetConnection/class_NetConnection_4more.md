## class NetConnection

```cangjie
public class NetConnection {}
```

**功能：** 网络连接的句柄；设备从无网络到有网络会触发netAvailable事件、netCapabilitiesChange事件和netConnectionPropertiesChange事件； 设备从有网络到无网络状态会触发netLost事件； 设备从WiFi到蜂窝会触发netLost事件（WiFi丢失）之后触发 netAvaliable事件（蜂窝可用）。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

### func onNetAvailable((NetHandle) -> Unit)

```cangjie
public func onNetAvailable(callback: (NetHandle) -> Unit): Unit
```

**功能：** 订阅网络可用事件。

**模型约束：** 此接口调用之前需要先调用register接口，使用unregister取消订阅默认网络状态变化的通知。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([NetHandle](#class-nethandle))->Unit|是|-|回调函数，返回数据网络句柄。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*
import kit.PerformanceAnalysisKit.*

// 创建NetConnection对象
let netCon: NetConnection = createNetConnection()

// 先使用register接口注册订阅事件
netCon.register()

// 订阅网络可用事件。调用register后，才能接收到此事件通知
netCon.onNetAvailable({ netHandle =>
    Hilog.info(0, "test", "${netHandle.netId}")
})

// 使用unregister接口取消订阅
netCon.unregister()
```

### func onNetBlockStatusChange((NetHandle, Bool) -> Unit)

```cangjie
public func onNetBlockStatusChange(callback: (NetHandle, Bool) -> Unit): Unit
```

**功能：** 订阅网络阻塞状态事件。

**模型约束：** 此接口调用之前需要先调用register接口，使用unregister取消订阅默认网络状态变化的通知。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([NetHandle](#class-nethandle), Bool) -> Unit|是|-|回调函数，返回数据网络句柄（netHandle）,及网络堵塞状态（blocked）。|

### func onNetCapabilitiesChange((NetCapabilityInfo) -> Unit)

```cangjie
public func onNetCapabilitiesChange(callback: (NetCapabilityInfo) -> Unit): Unit
```

**功能：** 订阅网络能力变化事件。

**模型约束：** 此接口调用之前需要先调用register接口，使用unregister取消订阅默认网络状态变化的通知。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([NetCapabilityInfo](#class-netcapabilityinfo)) -> Unit|是|-|回调函数，返回数据网络句柄（netHandle）和网络的能力信息（netCap）。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*
import kit.PerformanceAnalysisKit.*

// 创建NetConnection对象
let netCon: NetConnection = createNetConnection()

// 先使用register接口注册订阅事件
netCon.register()

// 订阅网络能力变化事件。调用register后，才能接收到此事件通知
netCon.onNetCapabilitiesChange({ capabilities =>
    Hilog.info(0, "test", "capability changed")
})

// 使用unregister接口取消订阅
netCon.unregister()
```