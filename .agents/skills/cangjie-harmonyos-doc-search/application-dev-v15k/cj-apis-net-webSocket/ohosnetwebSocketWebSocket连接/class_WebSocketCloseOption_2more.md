## class WebSocketCloseOptions

```cangjie
public class WebSocketCloseOptions {
    public WebSocketCloseOptions(
        public let code !: UInt32 = 1000,
        public let reason !: String = ""
    )
}
```

**功能：** 关闭WebSocket连接时，可选参数的类型和说明。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

### let code

```cangjie
public let code: UInt32 = 1000
```

**功能：** 错误码，关闭WebSocket连接时的可选参数，可根据实际情况来填。默认值为1000。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let reason

```cangjie
public let reason: String = ""
```

**功能：** 原因值，关闭WebSocket连接时的可选参数，可根据实际情况来填。默认值为空字符串（""）。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### WebSocketCloseOptions(UInt32, String)

```cangjie
public WebSocketCloseOptions(
    public let code !: UInt32 = 1000,
    public let reason !: String = ""
)
```

**功能：** WebSocketCloseOptions构造函数。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|code|UInt32|否|1000| **命名参数。** 错误码，关闭WebSocket连接时的可选参数，可根据实际情况来填。默认值为1000。|
|reason|String|否|""| **命名参数。** 原因值，关闭WebSocket连接时的可选参数，可根据实际情况来填。默认值为空字符串（“”）。|

## class WebSocketErrorCallback

```cangjie
open public class WebSocketErrorCallback <: Callback1Argument<BusinessException> {
    public WebSocketErrorCallback(let f:(BusinessException) -> Unit)
}
```

**功能：** Error事件的callback类型。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**父类型：**

- [Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[BusinessException](../BasicServicesKit/cj-apis-base.md#class-businessexception)>

### WebSocketErrorCallback((BusinessException) -> Unit)

```cangjie
public WebSocketErrorCallback(let f:(BusinessException) -> Unit)
```

**功能：** WebSocketErrorCallback构造函数。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|f|([BusinessException](../BasicServicesKit/cj-apis-base.md#class-businessexception)) -> Unit|是|-|回调方法。|

### func invoke(BusinessException)

```cangjie
public open func invoke(arg1: BusinessException)
```

**功能：** 执行入参回调方法。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arg1|[BusinessException](../BasicServicesKit/cj-apis-base.md#class-businessexception)|是|-|BusinessException 返回值。|