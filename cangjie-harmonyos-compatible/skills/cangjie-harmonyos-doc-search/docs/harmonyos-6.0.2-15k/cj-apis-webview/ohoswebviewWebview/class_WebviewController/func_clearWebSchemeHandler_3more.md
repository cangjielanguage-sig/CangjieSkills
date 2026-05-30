### func clearWebSchemeHandler()

```cangjie
public func clearWebSchemeHandler(): Unit
```

**功能：** 清除当前Web组件设置的所有WebSchemeHandler。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

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

@Entry
@Component
class EntryView {
    let webController = WebviewController()
    let schemeHandler = WebSchemeHandler()

    func build() {
        Column(10) {
            Button('clearWebSchemeHandler').onClick {
                _ => try {
                    webController.clearWebSchemeHandler()
                } catch (e: BusinessException) {
                    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
        }
    }
}
```

### func closeAllMediaPresentations()

```cangjie
public func closeAllMediaPresentations(): Unit
```

**功能：** 控制网页所有全屏视频关闭。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

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
            Button("closeAllMediaPresentations").onClick {
                evt =>
                AppLog.info("closeAllMediaPresentations")
                webController.closeAllMediaPresentations()
            }.width(400.px).height(150.px)

            Web(src: "www.example.com", controller: webController)
        }
    }
}
```

### func closeCamera()

```cangjie
public func closeCamera(): Unit
```

**功能：** 关闭当前网页摄像头捕获。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

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
            Button("closeCamera").onClick {
                evt =>
                AppLog.info("closeCamera")
                webController.closeCamera()
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