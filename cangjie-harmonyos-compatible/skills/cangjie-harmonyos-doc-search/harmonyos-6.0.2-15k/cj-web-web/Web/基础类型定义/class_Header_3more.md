### class Header

```cangjie
public class Header {}
```

**功能：** 描述Web组件返回的请求/响应头对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

#### var headerKey

```cangjie
public var headerKey: String
```

**功能：** 请求/响应头的key。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

#### var headerValue

```cangjie
public var headerValue: String
```

**功能：** 请求/响应头的Value。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### class OnAlertEvent

```cangjie
public class OnAlertEvent {
    public OnAlertEvent(
        public let url: String,
        public let message: String,
        public let result: WebResult
    )
}
```

**功能：** 描述定义网页触发alert()告警弹窗的参数结构。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### let message

```cangjie
public let message: String
```

**功能：** 弹窗中显示的信息。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

#### let result

```cangjie
public let result: WebResult
```

**功能：** 通知Web组件用户操作行为。

**类型：** [WebResult](#class-webresult)

**读写能力：** 只读

**起始版本：** 19

#### let url

```cangjie
public let url: String
```

**功能：** 当前显示弹窗所在网页的URL。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

#### OnAlertEvent(String, String, WebResult)

```cangjie
public OnAlertEvent(
    public let url: String,
    public let message: String,
    public let result: WebResult
)
```

**功能：** 定义网页触发alert()告警弹窗时触发回调。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|当前显示弹窗所在网页的URL。|
|message|String|是|-|弹窗中显示的信息。|
|result|[WebResult](#class-webresult)|是|-|通知Web组件用户操作行为。|

### class OnBeforeUnloadEvent

```cangjie
public class OnBeforeUnloadEvent {
    public OnBeforeUnloadEvent(
        public let url: String,
        public let message: String,
        public let result: WebResult
    )
}
```

**功能：** 描述定义刷新或关闭场景下，在即将离开当前页面的参数结构。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### let message

```cangjie
public let message: String
```

**功能：** 弹窗中显示的信息。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

#### let result

```cangjie
public let result: WebResult
```

**功能：** 通知Web组件用户操作行为。

**类型：** [WebResult](#class-webresult)

**读写能力：** 只读

**起始版本：** 19

#### let url

```cangjie
public let url: String
```

**功能：** 当前显示弹窗所在网页的URL。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

#### OnBeforeUnloadEvent(String, String, WebResult)

```cangjie
public OnBeforeUnloadEvent(
    public let url: String,
    public let message: String,
    public let result: WebResult
)
```

**功能：** 定义刷新或关闭场景下，在即将离开当前页面时触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|当前显示弹窗所在网页的URL。|
|message|String|是|-|弹窗中显示的信息。|
|result|[WebResult](#class-webresult)|是|-|通知Web组件用户操作行为。|