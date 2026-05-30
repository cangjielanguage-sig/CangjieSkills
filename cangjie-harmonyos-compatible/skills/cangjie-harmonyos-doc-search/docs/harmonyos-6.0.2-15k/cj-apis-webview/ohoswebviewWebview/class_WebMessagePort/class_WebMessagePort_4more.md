## class WebMessagePort

```cangjie
public class WebMessagePort {}
```

**功能：** 通过WebMessagePort可以进行消息的发送以及接收。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### prop isExtentionType

```cangjie
public prop isExtentionType: Bool
```

**功能：** 判断创建WebMessagePort时是否指定使用扩展增强接口，[postMessageEventExt](#func-postmessageeventextwebmessageext)、[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

true表示使用扩展增强接口，false表示不使用扩展增强接口。默认false。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### func close()

```cangjie
public func close(): Unit
```

**功能：** 关闭该消息端口。在使用close方法前，请先使用[createWebMessagePorts](#func-createwebmessageportsbool)创建消息端口。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

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
            Button("createWebMessagePorts").onClick {
                evt =>
                AppLog.info("createWebMessagePorts")
                // 1、创建两个消息端口。
                ports = webController.createWebMessagePorts()
            }.width(400.px).height(150.px)

            Button("close").onClick {
                evt =>
                AppLog.info("close")
                if (ports.size != 0) {
                    ports[1].close()
                } else {
                    AppLog.error("ports is null, Please initialize first")
                }
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

### func onMessageEvent((WebMessage) -> Unit)

```cangjie
public func onMessageEvent(callback: (WebMessage) -> Unit): Unit
```

**功能：** 注册回调函数，接收HTML侧发送过来的[WebMessage](#enum-webmessage)类型消息。完整示例代码参考[postMessage](#func-postmessagestring-arraywebmessageport-string)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([WebMessage](#enum-webmessage))->Unit|是|-|接收到的消息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100006|Failed to register a message event for the port.|

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
            Button("onMessageEvent").onClick {
                evt =>
                AppLog.info("onMessageEvent")
                // 1、创建两个消息端口。
                ports = webController.createWebMessagePorts()
                // 2、在应用侧的消息端口(如端口1)上注册回调事件。
                ports[1].onMessageEvent(
                    {
                    message: WebMessage => match (message) {
                        case STRING(s) => AppLog.info("cangjie got:" + s)
                        case ARRAY_BUFFER(arr) => AppLog.info("cangjie got: ${arr}")
                        case _ => throw IllegalArgumentException("The type is not supported.")
                    }
                })
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