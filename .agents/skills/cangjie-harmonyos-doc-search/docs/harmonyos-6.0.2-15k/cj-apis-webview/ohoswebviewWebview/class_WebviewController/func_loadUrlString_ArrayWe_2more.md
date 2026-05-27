### func loadUrl(String, Array\<WebHeader>)

```cangjie
public func loadUrl(url: String, headers: Array<WebHeader>): Unit
```

**功能：** 加载指定的URL。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|需要加载的URL。|
|headers|Array\<[WebHeader](#class-webheader)>|是|-|URL的附加HTTP请求头。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100001|Init error. The WebviewController must be associated with a Web component.|
  |17100002|Invalid url.|
  |17100003|Invalid resource path or file type.|

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
    let webController = WebviewController()
    let headers = [WebHeader("headerKey", "headerValue")]
    func build() {
        Column(10) {
            Button("loadUrl").onClick {
                evt =>
                AppLog.info("loadUrl")
                webController.loadUrl("www.example1.com", headers)
            }.width(400.px).height(150.px)

            Web(src: "www.example.com", controller: webController).onPageBegin(
                {
                evt => AppLog.info("page begin url: ${evt.url}")
            }).onPageEnd({
                evt => AppLog.info("page end url: ${evt.url}")
            })
        }
    }
}
```

### func loadUrl(AppResource, Array\<WebHeader>)

```cangjie
public func loadUrl(url: AppResource, headers: Array<WebHeader>): Unit
```

**功能：** 加载指定的URL。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|[AppResource](../LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|需要加载的URL。|
|headers|Array\<[WebHeader](#class-webheader)>|是|-|URL的附加HTTP请求头。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100001|Init error. The WebviewController must be associated with a Web component.|
  |17100002|Invalid url.|
  |17100003|Invalid resource path or file type.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkWeb.*
import kit.LocalizationKit.*
import kit.UIKit.Web

@Entry
@Component
class EntryView {
    let webController = WebviewController()
    let headers = [WebHeader("headerKey", "headerValue")]
    func build() {
        Column(10) {
            Button("loadUrl").onClick {
                evt =>
                AppLog.info("loadUrl")
                webController.loadUrl(@rawfile("index.html"), headers)
            }.width(400.px).height(150.px)

            Web(src: "www.example.com", controller: webController).onPageBegin(
                {
                evt => AppLog.info("page begin url: ${evt.url}")
            }).onPageEnd({
                evt => AppLog.info("page end url: ${evt.url}")
            })
        }
    }
}
```