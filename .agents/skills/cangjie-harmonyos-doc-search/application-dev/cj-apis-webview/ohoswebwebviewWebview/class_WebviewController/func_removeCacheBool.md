### func removeCache(Bool)

```cangjie
public func removeCache(clearRom: Bool): Unit
```

**功能：** 清除应用中的资源缓存文件，此方法将会清除同一应用中所有Webview的缓存文件。

> **说明：**
>
> 可以通过在data/storage/el2/base/cache/web/Cache目录下查看Webview的缓存。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|clearRom|Bool|是|-|设置为true时同时清除ROM和RAM中的缓存，设置为false时只清除RAM中的缓存。|

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
class webview_35 {
    let webController = WebviewController()
    func build() {
        Column(space: 10) {
            Button("removeCache")
            .onClick ({
                evt =>
                Hilog.info(0, "test", "removeCache")
                webController.removeCache(true)
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