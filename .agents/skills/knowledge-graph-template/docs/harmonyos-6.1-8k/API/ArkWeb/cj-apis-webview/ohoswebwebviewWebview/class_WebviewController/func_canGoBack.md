### func canGoBack()

```cangjie
public func canGoBack(): Bool
```

**功能：** 当前页面是否可后退，即当前页面是否有返回历史记录。

可以结合使用[getBackForwardEntries](#func-getbackforwardentries)来获取当前WebView的历史信息列表，以及使用[accessStep](#func-accessstepint32)来判断是否可以按照给定的步数前进或后退。

> **说明：**
>
> - 在Web组件首次加载过程中调用[setCustomUserAgent](#func-setcustomuseragentstring)，可能会导致在当前存在多个历史节点的情况下，获取的canGoBack实际为false，即没有后退节点。建议先调用setCustomUserAgent方法设置UserAgent，再通过loadUrl加载具体页面。
>
> - 该现象是由于在Web组件首次加载时，调用[setCustomUserAgent](#func-setcustomuseragentstring)会导致组件重新加载并保持初始历史节点的状态。随后新增的节点将替换初始历史节点，不会生成新的历史节点，导致canGoBack为false。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|当前页面可以后退返回true,否则返回false。|

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
class webview_2 {
    let webController = WebviewController()
    func build() {
        Column(space:10) {
            Button("canGoBack")
            .onClick ({
                evt =>
                Hilog.info(0, "cangjieTest", "canGoBack")
                let bool = webController.canGoBack()
                Hilog.info(0, "cangjieTest", "canGoBack returns ${bool}")
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