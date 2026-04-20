### class ConsoleMessage

```cangjie
public class ConsoleMessage {}
```

**功能：** Web组件获取控制台信息对象。示例代码参考[onConsole](#class-onconsoleevent)事件。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### func getLineNumber()

```cangjie
public func getLineNumber(): Int32
```

**功能：** 获取ConsoleMessage的行数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回ConsoleMessage的行数。|

#### func getMessage()

```cangjie
public func getMessage(): String
```

**功能：** 获取ConsoleMessage的日志信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回ConsoleMessage的日志信息。|

#### func getMessageLevel()

```cangjie
public func getMessageLevel(): MessageLevel
```

**功能：** 获取ConsoleMessage的信息级别。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[MessageLevel](#enum-messagelevel)|返回ConsoleMessage的信息级别。|

#### func getSourceId()

```cangjie
public func getSourceId(): String
```

**功能：** 获取网页源文件路径和名字。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回网页源文件路径和名字。|

### class PermissionRequest

```cangjie
public class PermissionRequest {}
```

**功能：** Web组件返回授权或拒绝权限功能的对象。示例代码参考[onPermissionRequest](#class-onpermissionrequestevent)事件。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### func deny()

```cangjie
public func deny(): Unit
```

**功能：** 拒绝网页所请求的权限。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### func getAccessibleResource()

```cangjie
public func getAccessibleResource(): Array<String>
```

**功能：** 获取网页所请求的权限资源列表。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|网页所请求的权限资源列表。|

#### func getOrigin()

```cangjie
public func getOrigin(): String
```

**功能：** 获取网页来源。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前请求权限网页的来源。|

#### func grant(Array\<String>)

```cangjie
public func grant(resources: Array<String>): Unit
```

**功能：** 对网页访问的屏幕捕获操作进行授权。

> **说明：**
>
>需要配置权限：ohos.permission.MICROPHONE。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resources|Array\<String>|是|-|屏幕捕获配置。|

### class WebResourceError

```cangjie
public class WebResourceError {}
```

**功能：** Web组件资源管理错误信息对象。示例代码参考[onErrorReceive](#onerrorreceiveeventwebresourcerequest-webresourceerror)事件。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### func getErrorCode()

```cangjie
public func getErrorCode(): Int32
```

**功能：** 获取加载资源的错误码。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回加载资源的错误码。错误码的含义可以参考[WebNetErrorList](../apis/ArkWeb/cj-apis-web-net_error_list.md)|

#### func getErrorInfo()

```cangjie
public func getErrorInfo(): String
```

**功能：** 获取加载资源的错误信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回加载资源的错误信息。|