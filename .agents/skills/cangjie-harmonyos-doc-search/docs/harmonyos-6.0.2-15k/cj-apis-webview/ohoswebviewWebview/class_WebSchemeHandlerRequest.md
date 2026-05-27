## class WebSchemeHandlerRequest

```cangjie
public class WebSchemeHandlerRequest {}
```

**功能：** 通过[WebSchemeHandler](#class-webschemehandlerrequest)拦截到的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### func getFrameUrl()

```cangjie
public func getFrameUrl(): String
```

**功能：** 获取触发此请求的Frame的URL。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回触发此请求的Frame的URL。|

### func getHeader()

```cangjie
public func getHeader(): Array<WebHeader>
```

**功能：** 获取资源请求头信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[WebHeader](#class-webheader)>|返回资源请求头信息。|

### func getHttpBodyStream()

```cangjie
public func getHttpBodyStream(): WebHttpBodyStream
```

**功能：** 获取资源请求中的[WebHttpBodyStream](#class-webhttpbodystream)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[WebHttpBodyStream](#class-webhttpbodystream)|返回资源请求中的WebHttpBodyStream，如果没有则返回None。|

### func getReferrer()

```cangjie
public func getReferrer(): String
```

**功能：** 获取referrer。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|获取到的referrer。|

### func getRequestMethod()

```cangjie
public func getRequestMethod(): String
```

**功能：** 获取请求方法。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回请求方法。|

### func getRequestResourceType()

```cangjie
public func getRequestResourceType(): WebResourceType
```

**功能：** 获取资源请求的资源类型。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[WebResourceType](#enum-webresourcetype)|返回资源请求的资源类型。|

### func getRequestUrl()

```cangjie
public func getRequestUrl(): String
```

**功能：** 获取资源请求的URL信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回资源请求的URL信息。|

### func hasGesture()

```cangjie
public func hasGesture(): Bool
```

**功能：** 获取资源请求是否与手势（如点击）相关联。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回资源请求是否与手势（如点击）相关联。|

### func isMainFrame()

```cangjie
public func isMainFrame(): Bool
```

**功能：** 判断资源请求是否为主frame。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|判断资源请求是否为主frame。|