### func onNetConnectionPropertiesChange((NetHandle, ConnectionProperties) -> Unit)

```cangjie
public func onNetConnectionPropertiesChange(callback: (NetHandle, ConnectionProperties) -> Unit): Unit
```

**功能：** 订阅网络连接信息变化事件。

**模型约束：** 此接口调用之前需要先调用register接口，使用unregister取消订阅默认网络状态变化的通知。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([NetHandle](#class-nethandle), [ConnectionProperties](#class-connectionproperties)) -> Unit|是|-|回调函数，返回数据网络句柄（netHandle）和网络的连接信息（connectionProperties）。|

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

// 订阅网络连接信息变化事件。调用register后，才能接收到此事件通知
netCon.onNetConnectionPropertiesChange({ handle, properties =>
    Hilog.info(0, "test", "connection changed")
})

// 使用unregister接口取消订阅
netCon.unregister()
```

### func onNetLost((NetHandle) -> Unit)

```cangjie
public func onNetLost(callback: (NetHandle) -> Unit): Unit
```

**功能：** 订阅网络丢失事件。

**模型约束：** 此接口调用之前需要先调用register接口，使用unregister取消订阅默认网络状态变化的通知。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([NetHandle](#class-nethandle)) -> Unit|是|-|回调函数，数据网络句柄（netHandle）。|

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

// 订阅网络丢失事件。调用register后，才能接收到此事件通知
netCon.onNetLost({ handle =>
    Hilog.info(0, "test", "net of ${handle.netId} changed")
})

// 使用unregister接口取消订阅
netCon.unregister()
```

### func onNetUnavailable(() -> Unit)

```cangjie
public func onNetUnavailable(callback: () -> Unit): Unit
```

**功能：** 订阅网络不可用事件。

**模型约束：** 此接口调用之前需要先调用register接口，使用unregister取消订阅默认网络状态变化的通知。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|() -> Unit|是|-|回调函数，无返回结果。|

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

// 订阅网络不可用事件。调用register后，才能接收到此事件通知
netCon.onNetUnavailable({ =>
    Hilog.info(0, "test", "net unavailible")
})

// 使用unregister接口取消订阅
netCon.unregister()
```