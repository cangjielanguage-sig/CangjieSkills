## enum HttpRequestEvent

```cangjie
public enum HttpRequestEvent <: Equatable<HttpRequestEvent> & Hashable {
    | HeadersReceive
    | DataReceive
    | DataEnd
    | DataReceiveProgress
    | DataSendProgress
    | ...
}
```

**功能：** HTTP请求事件类型。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

**父类型：**

- Equatable\<HttpRequestEvent>
- Hashable

### DataEnd

```cangjie
DataEnd
```

**功能：** HTTP流式响应数据接收完毕事件。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### DataReceive

```cangjie
DataReceive
```

**功能：** HTTP流式响应数据接收事件。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### DataReceiveProgress

```cangjie
DataReceiveProgress
```

**功能：** HTTP流式响应数据接收进度更新事件。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### DataSendProgress

```cangjie
DataSendProgress
```

**功能：** HTTP网络请求数据发送进度更新事件。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### HeadersReceive

```cangjie
HeadersReceive
```

**功能：** HTTP Response Header事件。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### func !=(HttpRequestEvent)

```cangjie
public operator func !=(other: HttpRequestEvent): Bool
```

**功能：** 比较两个HttpRequestEvent是否不相等。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[HttpRequestEvent](#enum-httprequestevent)|是|-|要比较的另一个HttpRequestEvent实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个HttpRequestEvent不相等则返回true，否则返回false。|

### func ==(HttpRequestEvent)

```cangjie
public operator func ==(other: HttpRequestEvent): Bool
```

**功能：** 比较两个HttpRequestEvent是否相等。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[HttpRequestEvent](#enum-httprequestevent)|是|-|要比较的另一个HttpRequestEvent实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个HttpRequestEvent相等则返回true，否则返回false。|

### func hashCode()

```cangjie
public func hashCode(): Int64
```

**功能：** 获取HttpRequestEvent的哈希值。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回HttpRequestEvent的哈希值。|