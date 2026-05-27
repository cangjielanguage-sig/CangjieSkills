### func getPrintBackground()

```cangjie
public func getPrintBackground(): Bool
```

**功能：** 查询webview是否打印网页背景。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回Webview是否打印网页背景。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100001|Init error. The WebviewController must be associated with a Web component.|

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
    var message: String = "Hello World"
    func build() {
        Column(10) {
            Button("getPrintBackground")
            Text(this.message).onClick {
                evt =>
                AppLog.info("getPrintBackground")
                let printBackground = webController.getPrintBackground()
                AppLog.info("getPrintBackgroud returns: ${printBackground}")
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

### func getScrollable()

```cangjie
public func getScrollable(): Bool
```

**功能：** 获取当前网页是否允许滚动。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|当前网页是否允许滚动，true为允许滚动，false为禁止滚动。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100001|Init error. The WebviewController must be associated with a Web component.|

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
    func build() {
        Column(10) {
            Button("getScrollable").onClick {
                evt =>
                AppLog.info("getScrollable")
                let scrollable = webController.getScrollable()
                AppLog.info("getScrollable returns: ${scrollable}")
            }.width(400.px).height(150.px)
            Web(src: "www.example.com", controller: webController)
        }
    }
}
```