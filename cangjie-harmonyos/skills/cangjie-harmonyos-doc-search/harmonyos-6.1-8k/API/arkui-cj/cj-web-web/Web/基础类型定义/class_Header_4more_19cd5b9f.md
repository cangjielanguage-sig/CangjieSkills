### class Header

```cangjie
public class Header {
    public var headerKey: ?String
    public var headerValue: ?String
}
```

**功能：** 描述Web组件返回的请求/响应头对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

#### var headerKey

```cangjie
public var headerKey: ?String
```

**功能：** 请求/响应头的key。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

#### var headerValue

```cangjie
public var headerValue: ?String
```

**功能：** 请求/响应头的Value。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

### class OnLoadInterceptEvent

```cangjie
public class OnLoadInterceptEvent {
    public var data: WebResourceRequest
    public init(data: WebResourceRequest)
}
```

**功能：** 当资源加载被拦截时，加载拦截事件。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

#### var data

```cangjie
public var data: WebResourceRequest
```

**功能：** 网页请求的封装信息。

**类型：** [WebResourceRequest](#class-webresourcerequest)

**读写能力：** 可读写

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

#### init(WebResourceRequest)

```cangjie
public init(data: WebResourceRequest)
```

**功能：** 构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|[WebResourceRequest](#class-webresourcerequest)|是|-|请求的信息。|

### class OnPageBeginEvent

```cangjie
public class OnPageBeginEvent {
    public var url: String
    public init(url: String)
}
```

**功能：** 定义网页加载开始时触发的函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

#### var url

```cangjie
public var url: String
```

**功能：** 当前加载页面的URL。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

#### init(String)

```cangjie
public init(url: String)
```

**功能：** 构造一个OnPageBeginEvent类型的对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|当前加载页面的URL。|

### class OnPageEndEvent

```cangjie
public class OnPageEndEvent {
    public var url: String
    public init(url: String)
}
```

**功能：** 定义网页加载结束时触发的函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

#### var url

```cangjie
public var url: String
```

**功能：** 当前加载页面的URL。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

#### init(String)

```cangjie
public init(url: String)
```

**功能：** OnPageEndEvent的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|当前加载页面的URL。|