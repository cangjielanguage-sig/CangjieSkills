### func forward()

```cangjie
public func forward(): Unit
```

**功能：** 按照历史栈，前进一个页面。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

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
            Button("forward").onClick {
                evt =>
                AppLog.info("forward")
                webController.forward()
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

### func getBackForwardEntries()

```cangjie
public func getBackForwardEntries(): BackForwardList
```

**功能：** 获取当前Webview的历史信息列表。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[BackForwardList](#class-backforwardlist)|当前Webview的历史信息列表。|

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
            Button("getBackForwardEntries").onClick {
                evt =>
                AppLog.info("getBackForwardEntries")
                let backForwardList = webController.getBackForwardEntries()
                AppLog.info("backForwardList currentIndex is ${backForwardList.currentIndex}")
                AppLog.info("backForwardList size is ${backForwardList.size}")
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