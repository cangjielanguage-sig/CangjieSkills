## class WebSchemeHandlerResponse

```cangjie
public class WebSchemeHandlerResponse  {
    public init()
}
```

**功能：** 请求的响应，可以为被拦截的请求创建一个Response，并填充自定义的内容返回给Web组件。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### init()

```cangjie
public init()
```

**功能：** WebSchemeHandlerResponse的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### func getEncoding()

```cangjie
public func getEncoding(): String
```

**功能：** 获取WebSchemeHandlerResponse的字符集。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|字符集。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkWeb.*
import kit.UIKit.Web

@Entry
@Component
class EntryView {
    let controller = WebviewController();
    @State
    var message: String = "Hello Cangjie"
    func build() {
        Row {
            Column {
                Button('response').onClick {
                    _ =>
                    let response = WebSchemeHandlerResponse();
                    response.setUrl("http://www.example.com")
                    response.setStatus(200)
                    response.setStatusText("OK")
                    response.setMimeType("text/html")
                    response.setEncoding("utf-8")
                    response.setHeaderByName("header1", "value1", false)
                    response.setNetErrorCode(WebNetErrorList.NET_OK)
                    AppLog.info("[schemeHandler] getUrl:" + response.getUrl())
                    AppLog.info("[schemeHandler] getStatus: ${response.getStatus()}")
                    AppLog.info("[schemeHandler] getStatusText:" + response.getStatusText())
                    AppLog.info("[schemeHandler] getMimeType:" + response.getMimeType())
                    AppLog.info("[schemeHandler] getEncoding:" + response.getEncoding())
                    AppLog.info("[schemeHandler] getHeaderByValue:" + response.getHeaderByName("header1"))
                    AppLog.info("[schemeHandler] getNetErrorCode:" + response.getNetErrorCode().toString())
                }
                Web(src: ("www.example.com"), controller: this.controller)
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

### func getHeaderByName(String)

```cangjie
public func getHeaderByName(name: String): String
```

**功能：** 获取WebSchemeHandlerResponse的字符集。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|头部（header）的名称。|

**返回值：**

|类型|说明|
|:----|:----|
|String|头部（header）的值。|

### func getMimeType()

```cangjie
public func getMimeType(): String
```

**功能：** 获取WebSchemeHandlerResponse的媒体类型。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|媒体类型。|

### func getNetErrorCode()

```cangjie
public func getNetErrorCode(): WebNetErrorList
```

**功能：** 获取WebSchemeHandlerResponse的网络错误码。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[WebNetErrorList](cj-apis-web-net_error_list.md#enum-webneterrorlist)|获取Response的网络错误码。|

### func getStatus()

```cangjie
public func getStatus(): Int32
```

**功能：** 获取WebSchemeHandlerResponse的Http状态码。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|Response的Http状态码。|

### func getStatusText()

```cangjie
public func getStatusText(): String
```

**功能：** 获取WebSchemeHandlerResponse的状态文本。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|状态文本。|