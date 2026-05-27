### func postMessage(String, Array\<WebMessagePort>, String)

```cangjie
public func postMessage(name: String, ports: Array<WebMessagePort>, uri: String): Unit
```

**功能：** 发送Web消息端口到HTML。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|要发送的消息名称。|
|ports|Array\<[WebMessagePort](#class-webmessageport)>|是|-|要发送的消息端口。|
|uri|String|是|-|接收该消息的URI。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100001|Init error. The WebviewController must be associated with a Web component.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.state_macro_manage.rawfile
import kit.ArkWeb.*
import kit.ArkWeb.Error as webError
import kit.UIKit.Web
import kit.LocalizationKit.*
import ohos.base.AppLog

let webController = WebviewController()
var ports = Array<WebMessagePort>()

@Entry
@Component
class EntryView {
    @State
    var sendFromCangjie = "Send this message from cangjie to HTML"
    @State
    var receivedFromHtml = "Display received message send from HTML"
    func build() {
        Column(10) {
            // 展示接收到的来自HTML的内容
            Text(this.receivedFromHtml)
            // 输入框的内容发送到html
            TextInput(placeholder: "Send this message from cangjie to HTML").onChange(
                {
                value: String => this.sendFromCangjie = value
            })
            Button("postMessage").onClick {
                evt =>
                AppLog.info("postMessage")
                // 1、创建两个消息端口。
                ports = webController.createWebMessagePorts()
                // 2、在应用侧的消息端口(如端口1)上注册回调事件。
                ports[1].onMessageEvent(
                    {
                        message: WebMessage =>
                        var msg = "Got msg from HTML:"
                        match (message) {
                            case STRING(s) =>
                                AppLog.info("cangjie got:" + s)
                                msg = msg + s
                            case ARRAY_BUFFER(arr) =>
                                AppLog.info("cangjie got: ${arr}")
                                msg = msg + "${arr}"
                            case _ => throw IllegalArgumentException("The type is not supported.")
                        }
                        this.receivedFromHtml = msg
                    }
                )
                // 3、将另一个消息端口(如端口0)发送到HTML侧，由HTML侧保存并使用。
                webController.postMessage("__init_port__", [ports[0]], "*")
            }.width(400.px).height(150.px)
            // 4、使用应用侧的端口给另一个已经发送到html的端口发送消息。
            Button("SendDataToHTML").onClick {
                evt =>
                AppLog.info("SendDataToHTML")
                if (ports.size != 0) {
                    ports[1].postMessageEvent(WebMessage.ARRAY_BUFFER(this.sendFromCangjie.toArray()))
                } else {
                    AppLog.error("ports is null, Please initialize first")
                }
            }.width(400.px).height(150.px)

            Web(src: @rawfile("index.html"), controller: webController).onPageBegin(
                {
                evt => AppLog.info("page begin url: ${evt.url}")
            }).onPageEnd({
                evt => AppLog.info("page end url: ${evt.url}")
            })
        }.width(100.percent)
    }
}
```

加载的html文件。需要在`entry\src\main\resources\rawfile`目录下新增`index.html`文件。

```html
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebView Message Port Demo</title>
</head>

<body>
<h1>WebView Message Port Demo</h1>
<div>
    <input type="button" value="SendToCangjie" onclick="PostMsgToCangjie(msgFromCangjie.value);"/><br/>
    <input id="msgFromCangjie" type="text" value="send this message from HTML to cangjie"/><br/>
</div>
<p class="output">display received message send from cangjie</p>
</body>
<script src="xxx.js"></script>
</html>
```