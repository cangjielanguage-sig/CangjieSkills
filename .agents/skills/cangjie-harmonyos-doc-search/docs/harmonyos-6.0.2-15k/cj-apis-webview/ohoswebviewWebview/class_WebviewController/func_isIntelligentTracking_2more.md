### func isIntelligentTrackingPreventionEnabled()

```cangjie
public func isIntelligentTrackingPreventionEnabled(): Bool
```

**功能：** 获取当前Web是否启用了智能防跟踪功能。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|当前Web是否启用了智能防跟踪功能，默认为false。|

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
            Button("isIntelligentTrackingPreventionEnabled").onClick {
                evt =>
                AppLog.info("isIntelligentTrackingPreventionEnabled")
                let intelligentTrackingPreventionEnabled = webController.isIntelligentTrackingPreventionEnabled()
                AppLog.info("isIntelligentTrackingPreventionEnabled returns: ${intelligentTrackingPreventionEnabled}")
            }.width(400.px).height(150.px)
            Web(src: "www.example.com", controller: webController)
        }
    }
}
```

### func isSafeBrowsingEnabled()

```cangjie
public func isSafeBrowsingEnabled(): Bool
```

**功能：** 获取当前网页是否启用了检查网站安全风险。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|当前网页是否启用了检查网站安全风险的功能，默认为false。|

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
            Button("isSafeBrowsingEnabled").onClick {
                evt =>
                AppLog.info("isSafeBrowsingEnabled")
                let bool = webController.isSafeBrowsingEnabled()
                AppLog.info("isSafeBrowsingEnabled returns ${bool}")
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