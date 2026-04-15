### func zoom(Float32)

```cangjie
public func zoom(factor: Float32): Unit
```

**功能：** 调整当前网页的缩放比例，zoomAccess需为true。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|factor|Float32|是|-|基于当前网页所需调整的相对缩放比例，入参要求大于0，当入参为1时为默认加载网页的缩放比例，入参小于1为缩小，入参大于1为放大。<br>取值范围：(0，100]。|

**异常：**

- BusinessException：对应错误码如下表，详见[Webview错误码](./cj-errorcode-webview.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17100001 | Init error. The WebviewController must be associated with a Web component. |
  | 17100004 | Function not enable. |

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
class webview_29 {
    let webController = WebviewController()
    func build() {
        Column(space: 10) {
            Button("zoom")
            .onClick ({
                evt =>
                Hilog.info(0, "test", "zoom")
                webController.zoom(2.5)
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

### func zoomIn()

```cangjie
public func zoomIn(): Unit
```

**功能：** 调用此接口将当前网页进行放大，比例为25%。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[Webview错误码](./cj-errorcode-webview.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17100001 | Init error. The WebviewController must be associated with a Web component. |
  | 17100004 | Function not enable. |

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
class webview_30 {
    let webController = WebviewController()
    func build() {
        Column(space: 10) {
            Button("zoomIn")
            .onClick ({
                evt =>
                Hilog.info(0, "test", "zoomIn")
                webController.zoomIn()
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