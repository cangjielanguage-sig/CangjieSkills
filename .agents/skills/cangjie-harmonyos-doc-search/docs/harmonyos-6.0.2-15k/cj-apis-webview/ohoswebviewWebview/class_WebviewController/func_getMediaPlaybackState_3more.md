### func getMediaPlaybackState()

```cangjie
public func getMediaPlaybackState(): MediaPlaybackState
```

**功能：** 查询当前所有音视频播控状态。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[MediaPlaybackState](#enum-mediaplaybackstate)|当前网页的播控状态，具体值为NONE、PLAYING、PAUSED、STOPPED。|

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
            Button("getMediaPlaybackState").onClick {
                evt =>
                AppLog.info("getMediaPlaybackState")
                let mediaPlaybackState = webController.getMediaPlaybackState()
                match (mediaPlaybackState) {
                    case MediaPlaybackState.PLAYING => AppLog.info("getMediaPlaybackState returns PLAYING")
                    case MediaPlaybackState.PAUSED => AppLog.info("getMediaPlaybackState returns PAUSED")
                    case MediaPlaybackState.STOPPED => AppLog.info("getMediaPlaybackState returns STOPPED")
                    case MediaPlaybackState.NONE => AppLog.info("getMediaPlaybackState returns NONE")
                    case _ => throw IllegalArgumentException("The type is not supported.")
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

### func getOriginalUrl()

```cangjie
public func getOriginalUrl(): String
```

**功能：** 获取当前页面的原始URL地址。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|当前页面的原始URL地址。|

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
            Button("getOriginalUrl").onClick {
                evt =>
                AppLog.info("getOriginalUrl")
                let url = webController.getOriginalUrl()
                AppLog.info("getOriginalUrl is ${url}")
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

### func getPageHeight()

```cangjie
public func getPageHeight(): Int32
```

**功能：** 获取当前网页的页面高度。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|当前网页的页面高度。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100001|Init error. The WebviewController must be associated with a Web component.|