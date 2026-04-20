### func pageUp(Bool)

```cangjie
public func pageUp(top: Bool): Unit
```

**功能：** 将Webview的内容向上滚动半个视框大小或者跳转到页面最顶部，通过top入参控制。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|top|Bool|是|-|是否跳转到页面最顶部。<br>false表示将页面内容向上滚动半个视框大小，true表示跳转到页面最顶部。|

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
class webview_22 {
    let webController = WebviewController()
    func build() {
        Column(space: 10) {
            Button("pageUp")
            .onClick ({
                evt =>
                Hilog.info(0, "cangjieTest", "pageUp")
                webController.pageUp(true)
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

### func reload()

```cangjie
public func reload(): Unit
```

**功能：** 调用此接口通知Web组件刷新网页。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

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
class webview_23 {
    let webController = WebviewController()
    let headers = [WebHeader("headerKey", "headerValue")]
    func build() {
        Column(space: 10) {
            Button("reload")
            .onClick ({
                evt =>
                Hilog.info(0, "cangjieTest", "reload")
                webController.reload()
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