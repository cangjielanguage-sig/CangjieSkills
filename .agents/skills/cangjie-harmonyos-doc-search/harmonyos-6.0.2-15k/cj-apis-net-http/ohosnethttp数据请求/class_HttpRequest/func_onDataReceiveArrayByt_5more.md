### func onDataReceive((Array\<Byte>) -> Unit)

```cangjie
public func onDataReceive(callback: (Array<Byte>) -> Unit): Unit
```

**功能：** 订阅HTTP流式响应数据接收事件。

> **说明：**
>
> 暂不支持订阅HTTP流式数据上传的相关事件。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Array\<Byte>) -> Unit|是|-|回调函数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

let httpRequest = createHttp()
httpRequest.onDataReceive({ data =>
    AppLog.info("data receive: ${data}")
})
```

### func onDataReceiveProgress((DataReceiveProgressInfo) -> Unit)

```cangjie
public func onDataReceiveProgress(callback: (DataReceiveProgressInfo) -> Unit): Unit
```

**功能：** 订阅HTTP流式响应数据接收进度事件。

> **说明：**
>
> 暂不支持订阅HTTP流式数据上传的相关事件。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([DataReceiveProgressInfo](#class-datareceiveprogressinfo)) -> Unit|是|-|回调函数。返回数据接收进度信息。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

let httpRequest = createHttp()
httpRequest.onDataReceiveProgress({ receiveInfo =>
    AppLog.info("receive data ${receiveInfo.receiveSize}, total: ${receiveInfo.totalSize}")
})
```

### func onDataSendProgress((DataSendProgressInfo) -> Unit)

```cangjie
public func onDataSendProgress(callback: (DataSendProgressInfo) -> Unit): Unit
```

**功能：** 订阅HTTP网络请求数据发送进度事件。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([DataSendProgressInfo](#class-datasendprogressinfo)) -> Unit|是|-|回调函数。返回数据发送进度信息。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

let httpRequest = createHttp()
httpRequest.onDataSendProgress({ sendInfo =>
    AppLog.info("send data ${sendInfo.sendSize}, total: ${sendInfo.totalSize}")
})
```

### func onHeadersReceive((HashMap\<String,String>) -> Unit)

```cangjie
public func onHeadersReceive(callback: (HashMap<String, String>) -> Unit): Unit
```

**功能：** 订阅HTTP Response Header事件。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(HashMap\<String,String>) -> Unit|是|-|回调函数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

let httpRequest = createHttp()
httpRequest.onHeadersReceive({ headers =>
    AppLog.info("headers: ${headers}")
})
```

### func onceHeadersReceive((HashMap\<String,String>) -> Unit)

```cangjie
public func onceHeadersReceive(callback: (HashMap<String, String>) -> Unit): Unit
```

**功能：** 订阅HTTP Response Header事件，但是只触发一次。一旦触发之后，此函数注册的订阅器就会被移除。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(HashMap\<String,String>) -> Unit|是|-|回调函数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

let httpRequest = createHttp()
httpRequest.onceHeadersReceive({ headers =>
    AppLog.info("headers: ${headers}")
})
```