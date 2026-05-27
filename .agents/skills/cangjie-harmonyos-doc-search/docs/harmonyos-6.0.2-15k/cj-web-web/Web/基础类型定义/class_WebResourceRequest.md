### class WebResourceRequest

```cangjie
public class WebResourceRequest {}
```

**功能：** 描述web组件获取资源请求对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

#### func getRequestHeader()

```cangjie
public func getRequestHeader(): ArrayList<Header>
```

**功能：** 获取资源请求头信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|ArrayList\<[Header](#class-header)>|返回资源请求头信息。|

#### func getRequestMethod()

```cangjie
public func getRequestMethod(): String
```

**功能：** 获取请求方法。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|返回请求方法。|

#### func getRequestUrl()

```cangjie
public func getRequestUrl(): String
```

**功能：** 获取资源请求的URL信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|返回资源请求的URL信息。|

#### func isMainFrame()

```cangjie
public func isMainFrame(): Bool
```

**功能：** 判断资源请求是否为主frame。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回资源请求是否为主frame。true表示返回资源请求为主frame，false表示返回资源请求不为主frame。|

#### func isRedirect()

```cangjie
public func isRedirect(): Bool
```

**功能：** 判断资源请求是否被服务端重定向。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回资源请求是否被服务端重定向。true表示返回资源请求被服务端重定向，false表示返回资源请求未被服务端重定向。|

#### func isRequestGesture()

```cangjie
public func isRequestGesture(): Bool
```

**功能：** 获取资源请求是否与手势（如点击）相关联。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回资源请求是否与手势（如点击）相关联。true表示返回资源请求与手势（如点击）相关联，false表示返回资源请求与手势（如点击）不相关联。|