### func postMessageEvent(WebMessage)

```cangjie
public func postMessageEvent(message: WebMessage): Unit
```

**功能：** 发送[WebMessage](#enum-webmessage)类型消息给HTML5侧。完整示例代码参考[postMessage](#func-postmessagestring-arraywebmessageport-string)。

> **说明：**
>
> 必须先调用[onMessageEvent](#func-onmessageeventwebmessage---unit)，否则会发送失败。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|[WebMessage](#enum-webmessage)|是|-|要发送的消息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100010|Failed to post messages through the port.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkWeb.*
import kit.UIKit.Web

let webController = WebviewController()
var ports = Array<WebMessagePort>()

@Entry
@Component
class EntryView {
    func build() {
        Column(10) {
            Button("postMessage").onClick {
                evt =>
                AppLog.info("postMessage")
                // 1、创建两个消息端口。
                ports = webController.createWebMessagePorts()
                // 2、将另一个消息端口(如端口0)发送到HTML侧，由HTML侧保存并使用。
                webController.postMessage("__init_port__", [ports[0]], "*")
                ports[1].postMessageEvent(WebMessage.STRING("post message from ets to html5"))
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

### func postMessageEventExt(WebMessageExt)

```cangjie
public func postMessageEventExt(message: WebMessageExt): Unit
```

**功能：** 发送[WebMessageType](#enum-webmessagetype)类型消息给HTML5侧。完整示例代码参考[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

> **说明：**
>
> 必须先调用[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)，否则会发送失败。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|[WebMessageExt](#class-webmessageext)|是|-|要发送的消息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100010|Failed to post messages through the port.|