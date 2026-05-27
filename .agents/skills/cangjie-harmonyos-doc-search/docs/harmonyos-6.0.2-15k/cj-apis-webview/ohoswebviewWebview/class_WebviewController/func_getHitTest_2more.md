### func getHitTest()

```cangjie
public func getHitTest(): WebHitTestType
```

**功能：** 获取当前被点击区域的元素类型。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[WebHitTestType](#enum-webhittesttype)|被点击区域的元素类型。|

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
            Button("getHitTest").onClick {
                evt =>
                AppLog.info("getHitTest")
                let hitType = webController.getHitTest()
                match (hitType) {
                    case WebHitTestType.EditText => AppLog.info("getHitTest returns EditText")
                    case WebHitTestType.Email => AppLog.info("getHitTest returns Email")
                    case WebHitTestType.HttpAnchor => AppLog.info("getHitTest returns HttpAnchor")
                    case WebHitTestType.HttpAnchorImg => AppLog.info("getHitTest returns HttpAnchorImg")
                    case WebHitTestType.Img => AppLog.info("getHitTest returns Img")
                    case WebHitTestType.Map => AppLog.info("getHitTest returns Map")
                    case WebHitTestType.Phone => AppLog.info("getHitTest returns Phone")
                    case WebHitTestType.Unknown => AppLog.info("getHitTest returns Unknown")
                    case _ => ()
                }
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

### func getHitTestValue()

```cangjie
public func getHitTestValue(): HitTestValue
```

**功能：** 获取当前被点击区域的元素信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[HitTestValue](#class-hittestvalue)|点击区域的元素信息。|

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
            Button("getHitTestValue").onClick {
                evt =>
                AppLog.info("getHitTestValue")
                let hitTestValue = webController.getHitTestValue()
                match (hitTestValue.hitTestType) {
                    case WebHitTestType.EditText => AppLog.info("getHitTestValue returns EditText")
                    case WebHitTestType.Email => AppLog.info("getHitTestValue returns Email")
                    case WebHitTestType.HttpAnchor => AppLog.info("getHitTestValue returns HttpAnchor")
                    case WebHitTestType.HttpAnchorImg => AppLog.info("getHitTestValue returns HttpAnchorImg")
                    case WebHitTestType.Img => AppLog.info("getHitTestValue returns Img")
                    case WebHitTestType.Map => AppLog.info("getHitTestValue returns Map")
                    case WebHitTestType.Phone => AppLog.info("getHitTestValue returns Phone")
                    case WebHitTestType.Unknown => AppLog.info("getHitTestValue returns Unknown")
                    case _ => ()
                }
                AppLog.info("getHitTestValue extra returns ${hitTestValue.extra}")
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