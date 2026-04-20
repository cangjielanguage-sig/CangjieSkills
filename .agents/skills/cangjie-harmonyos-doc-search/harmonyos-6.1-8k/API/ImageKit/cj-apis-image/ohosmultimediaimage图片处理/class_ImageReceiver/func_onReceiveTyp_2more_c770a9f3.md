### func on(ReceiveType, Callback0Argument)

```cangjie
public func on(eventType: ReceiveType, callback: Callback0Argument): Unit
```

**功能：** 接收图片时注册回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[ReceiveType](#enum-receivetype)|是|-|注册事件的类型，固定为ImageArrival，接收图片时触发。|
|callback|[Callback0Argument](../arkinterop/cj-api-callback_invoke.md#class-callback0argument)|是|-|回调函数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException
import ohos.callback_invoke.*

class Callback <: Callback0Argument {
    public func invoke(res: ?BusinessException): Unit {
        Hilog.info(0, "test", "invoke success")
    }
}

try {
    let size = Size(8, 8192)
    let receiver = createImageReceiver(size, ImageFormat.Jpeg, 8)
    let callback = Callback()
    receiver.on(ImageArrival, callback)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func off(ReceiveType)

```cangjie
public func off(eventType: ReceiveType): Unit
```

**功能：** 释放buffer时移除注册回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[ReceiveType](#enum-receivetype)|是|-|注册事件的类型，固定为ImageArrival，释放buffer时触发。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException
import ohos.callback_invoke.*

class Callback1 <: Callback0Argument {
    public func invoke(res: ?BusinessException): Unit {
        Hilog.info(0, "test", "invoke success")
    }
}

try {
    let size = Size(8, 8192)
    let receiver = createImageReceiver(size, ImageFormat.Jpeg, 8)
    let callback = Callback1()
    receiver.on(ImageArrival, callback)
    receiver.off(ImageArrival)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```