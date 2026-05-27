## class HttpRequest

```cangjie
public class HttpRequest {}
```

**功能：** HTTP请求任务。在调用HttpRequest的方法前，需要先通过[createHttp](../NetworkKit/cj-apis-net-http.md#func-createhttp)创建一个任务。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

### func destroy()

```cangjie
public func destroy(): Unit
```

**功能：** 中断请求任务。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

let httpRequest = createHttp()

httpRequest.destroy()
```

### func offDataEnd()

```cangjie
public func offDataEnd(): Unit
```

**功能：** 取消订阅HTTP流式响应数据接收完毕事件。

> **说明：**
>
> 清空所有订阅。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

let httpRequest = createHttp()
httpRequest.onDataEnd({ =>
    AppLog.info("data end")
})
httpRequest.offDataEnd()
```

### func offDataReceive()

```cangjie
public func offDataReceive(): Unit
```

**功能：** 取消订阅HTTP流式响应数据接收事件。

> **说明：**
>
> 清空所有订阅。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

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
httpRequest.offDataReceive()
```

### func offDataReceiveProgress()

```cangjie
public func offDataReceiveProgress(): Unit
```

**功能：** 取消订阅HTTP流式响应数据接收进度事件。

> **说明：**
>
> 清空所有订阅。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

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
httpRequest.offDataReceiveProgress()
```

### func offDataSendProgress()

```cangjie
public func offDataSendProgress(): Unit
```

**功能：** 取消订阅HTTP网络请求数据发送进度事件。

> **说明：**
>
> 清空所有订阅。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

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
httpRequest.offDataSendProgress()
```

### func offHeadersReceive()

```cangjie
public func offHeadersReceive(): Unit
```

**功能：** 取消订阅HTTP Response Header事件。

> **说明：**
>
> 清空所有订阅。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

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
httpRequest.offHeadersReceive()
```

### func onDataEnd(() -> Unit)

```cangjie
public func onDataEnd(callback: () -> Unit): Unit
```

**功能：** 订阅HTTP流式响应数据接收完毕事件。

> **说明：**
>
> 暂不支持订阅HTTP流式数据上传的相关事件。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|() -> Unit|是|-|回调函数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

let httpRequest = createHttp()
httpRequest.onDataEnd({ =>
    AppLog.info("data end")
})
```