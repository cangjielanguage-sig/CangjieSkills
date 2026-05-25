### func setCustomUserAgent(String)

```cangjie
public func setCustomUserAgent(userAgent: String): Unit
```

**功能：** 设置自定义用户代理，会覆盖系统的用户代理。

不建议将User-Agent设置在onLoadIntercept回调事件中，会概率性出现设置失败。

当Web组件src设置为空字符串时，建议先调用setCustomUserAgent方法设置User-Agent，再通过loadUrl加载具体页面。

> **说明：**
>
> 当Web组件src设置了url，再调用setCustomUserAgent方法时，可能会出现加载的页面与实际设置User-Agent不符的异常现象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|userAgent|String|是|-|用户自定义代理信息。建议先使用[getUserAgent](#func-getuseragent)获取当前默认用户代理，在此基础上追加自定义用户代理信息。|

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
class webview_26 {
    let webController = WebviewController()
    let headers = [WebHeader("headerKey", "headerValue")]
    func build() {
        Column(space: 10) {
            Button("setCustomUserAgent")
            .onClick ({
                evt =>
                Hilog.info(0, "test", "setCustomUserAgent")
                webController.setCustomUserAgent("ua")
            }).width(400.px).height(150.px)

            Web(src: "www.example.com", controller: webController)
            .onPageBegin({evt =>
                Hilog.info(0, "test", "page begin url: ${evt.url}")
            })
            .onPageEnd({evt =>
                Hilog.info(0, "test", "page end url: ${evt.url}")
            })
        }
    }
}
```