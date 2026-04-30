### func loadData(String, String, String, String, String)

```cangjie
public func loadData(data: String, mimeType: String, encoding: String, baseUrl!: String = "", historyUrl!: String = ""): Unit
```

**功能：** 加载指定的数据。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|String|是|-|按照"Base64"或者"URL"编码后的一段字符串。|
|mimeType|String|是|-|媒体类型（MIME）。|
|encoding|String|是|-|编码类型，具体为"Base64"或者"URL"编码。|
|baseUrl|String|否|""| **命名参数。** 指定的一个URL路径（"http"/"https"/"data"协议），并由Web组件赋值给window.origin。|
|historyUrl|String|否|""| **命名参数。** 用作历史记录所使用的URL。非空时，历史记录以此URL进行管理。当baseUrl为空时，此属性无效。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.|
  |17100001|Init error. The WebviewController must be associated with a Web component.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkWeb.*
import ohos.base.*
import kit.UIKit.Web

let webController = WebviewController()

@Entry
@Component
class EntryView {
    func build() {
        Column(10) {
            Button("loadData").onClick {
                evt =>
                AppLog.info("loadData")
                let s = """
                <html><body bgcolor=\"white\">Source:<pre>source</pre></body></html>
                """
                webController.loadData(s, "text/html", "UTF-8")
            }.width(400.px).height(150.px)

            Web(src: "www.example.com", controller: webController).onPageBegin(
                {
                evt => AppLog.info("page begin url: ${evt.url}")
            }).onPageEnd({
                evt => AppLog.info("page end url: ${evt.url}")
            })
        }.width(100.percent)
    }
}
```