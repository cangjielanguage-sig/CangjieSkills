### func createWebMessagePorts(Bool)

```cangjie
public func createWebMessagePorts(isExtentionType!: Bool = false): Array<WebMessagePort>
```

**功能：** 创建Web消息端口。完整示例代码参考[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isExtentionType|Bool|否|false| **命名参数。** 是否使用扩展增强接口，默认false不使用。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[WebMessagePort](#class-webmessageport)>|web消息端口列表。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100001|Init error. The WebviewController must be associated with a Web component.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkWeb.*
import kit.UIKit.Web
import ohos.base.*

let webController = WebviewController()
var ports = Array<WebMessagePort>()

@Entry
@Component
class EntryView {
    func build() {
        Row {
            Column {
                Button("createWebMessagePorts").onClick {
                    evt =>
                    AppLog.info("createWebMessagePorts")
                    // 创建 WebMessagePort
                    ports = webController.createWebMessagePorts()
                }.width(400.px).height(150.px)

                Web(src: "www.example.com", controller: webController).onPageBegin(
                    {
                    evt => AppLog.info("page begin url: ${evt.url}")
                }).onPageEnd({
                    evt => AppLog.info("page end url: ${evt.url}")
                })
            }.width(100.percent)
        }.height(100.percent)
    }
}
```