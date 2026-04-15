### func getBackForwardEntries()

```cangjie
public func getBackForwardEntries(): BackForwardList
```

**功能：** 获取当前Webview的历史信息列表。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[BackForwardList](#class-backforwardlist)|当前Webview的历史信息列表。|

**异常：**

- BusinessException：对应错误码如下表，详见[Webview错误码](./cj-errorcode-webview.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkUI.LengthProp
import kit.ArkUI.Button
import kit.ArkUI.Column
import kit.ArkUI.CustomView
import kit.ArkUI.CJEntry
import kit.ArkUI.loadNativeView
import kit.ArkUI.SubscriberManager
import kit.ArkUI.LocalStorage
import ohos.arkui.state_macro_manage.Entry
import ohos.arkui.state_macro_manage.Component
import kit.ArkWeb.*
import kit.ArkUI.Web
import kit.PerformanceAnalysisKit.Hilog

@Entry
@Component
class webview_9 {
    let webController = WebviewController()
    func build() {
        Column(space: 10) {
            Button("getBackForwardEntries")
            .onClick ({
                evt =>
                Hilog.info(0, "cangjieTest", "getBackForwardEntries")
                let backForwardList = webController.getBackForwardEntries()
                Hilog.info(0, "cangjieTest", "backForwardList currentIndex is ${backForwardList.currentIndex}")
                Hilog.info(0, "cangjieTest", "backForwardList size is ${backForwardList.size}")
            }).width(400.px).height(150.px)

            Web(src: "www.example.com", controller: webController)
            .onPageBegin({evt =>
                Hilog.info(0, "cangjieTest", "page begin url: ${evt.url}")
            })
            .onPageEnd({evt =>
                Hilog.info(0, "cangjieTest", "page end url: ${evt.url}")
            })
        }
    }
}
```

### func getCustomUserAgent()

```cangjie
public func getCustomUserAgent(): String
```

**功能：** 获取自定义用户代理。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|用户自定义代理信息。|

**异常：**

- BusinessException：对应错误码如下表，详见[Webview错误码](./cj-errorcode-webview.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkUI.LengthProp
import kit.ArkUI.Button
import kit.ArkUI.Column
import kit.ArkUI.CustomView
import kit.ArkUI.CJEntry
import kit.ArkUI.loadNativeView
import kit.ArkUI.SubscriberManager
import kit.ArkUI.LocalStorage
import ohos.arkui.state_macro_manage.Entry
import ohos.arkui.state_macro_manage.Component
import kit.ArkWeb.*
import kit.ArkUI.Web
import kit.PerformanceAnalysisKit.Hilog

@Entry
@Component
class webview_10 {
    let webController = WebviewController()
    let headers = [WebHeader("headerKey", "headerValue")]
    func build() {
        Column(space: 10) {
            Button("getCustomUserAgent")
            .onClick ({
                evt =>
                Hilog.info(0, "cangjieTest", "getCustomUserAgent")
                let agent = webController.getCustomUserAgent()
                Hilog.info(0, "cangjieTest", "getCustomUserAgent returns ${agent}")
            }).width(400.px).height(150.px)

            Web(src: "www.example.com", controller: webController)
            .onPageBegin({evt =>
                Hilog.info(0, "cangjieTest", "page begin url: ${evt.url}")
            })
            .onPageEnd({evt =>
                Hilog.info(0, "cangjieTest", "page end url: ${evt.url}")
            })
        }
    }
}
```