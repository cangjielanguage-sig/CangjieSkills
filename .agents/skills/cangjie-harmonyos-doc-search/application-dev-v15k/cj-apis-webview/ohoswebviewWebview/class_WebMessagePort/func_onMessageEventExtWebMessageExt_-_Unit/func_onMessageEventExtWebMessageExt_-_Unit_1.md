### func onMessageEventExt((WebMessageExt) -> Unit)

```cangjie
public func onMessageEventExt(callback: (WebMessageExt) -> Unit): Unit
```

**功能：** 注册回调函数，接收HTML5侧发送过来的[WebMessageType](#enum-webmessagetype)类型消息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([WebMessageExt](#class-webmessageext))->Unit|是|-|接收到的消息。|

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
import kit.ArkWeb.Error as webError
import kit.LocalizationKit.*