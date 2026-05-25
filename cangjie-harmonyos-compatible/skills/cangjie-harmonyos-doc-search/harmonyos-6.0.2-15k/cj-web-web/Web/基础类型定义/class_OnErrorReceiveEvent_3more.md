### class OnErrorReceiveEvent

```cangjie
public class OnErrorReceiveEvent {
    public OnErrorReceiveEvent(
        public let request: WebResourceRequest,
        public let error: WebResourceError
    )
}
```

**功能：** 描述网页加载遇到错误时触发该回调的参数结构。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### let error

```cangjie
public let error: WebResourceError
```

**功能：** 网页加载资源错误的封装信息 。

**类型：** [WebResourceError](#class-webresourceerror)

**读写能力：** 只读

**起始版本：** 19

#### let request

```cangjie
public let request: WebResourceRequest
```

**功能：** 网页请求的封装信息。

**类型：** [WebResourceRequest](#class-webresourcerequest)

**读写能力：** 只读

**起始版本：** 19

#### OnErrorReceiveEvent(WebResourceRequest, WebResourceError)

```cangjie
public OnErrorReceiveEvent(
    public let request: WebResourceRequest,
    public let error: WebResourceError
)
```

**功能：** 定义网页加载遇到错误时触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|request|[WebResourceRequest](#class-webresourcerequest)|是|-|网页请求的封装信息。|
|error|[WebResourceError](#class-webresourceerror)|是|-|网页加载资源错误的封装信息。|

### class OnHttpErrorReceiveEvent

```cangjie
public class OnHttpErrorReceiveEvent {
    public OnHttpErrorReceiveEvent(
        public let request: WebResourceRequest,
        public let response: WebResourceResponse
    )
}
```

**功能：** 描述网页收到加载资源加载HTTP错误时触发。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### let request

```cangjie
public let request: WebResourceRequest
```

**功能：** 网页请求的封装信息。

**类型：** [WebResourceRequest](#class-webresourcerequest)

**读写能力：** 只读

**起始版本：** 19

#### let response

```cangjie
public let response: WebResourceResponse
```

**功能：** 资源响应的封装信息。

**类型：** [WebResourceResponse](#class-webresourceresponse)

**读写能力：** 只读

**起始版本：** 19

#### OnHttpErrorReceiveEvent(WebResourceRequest, WebResourceResponse)

```cangjie
public OnHttpErrorReceiveEvent(
    public let request: WebResourceRequest,
    public let response: WebResourceResponse
)
```

**功能：** 定义网页收到加载资源加载HTTP错误时触发。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|request|[WebResourceRequest](#class-webresourcerequest)|是|-|网页请求的封装信息。|
|response|[WebResourceResponse](#class-webresourceresponse)|是|-|资源响应的封装信息。|

### class OnPageEvent

```cangjie
public class OnPageEvent {
    public OnPageEvent(
        public var url: String
    )
}
```

**功能：** 描述Web组件加载时的回调信息参数结构。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var url

```cangjie
public var url: String
```

**功能：** 当前加载页面的URL。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

#### OnPageEvent(String)

```cangjie
public OnPageEvent(
    public var url: String
)
```

**功能：** Web组件加载时的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|当前加载页面的URL。|