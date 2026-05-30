## class WebDownloadDelegate

```cangjie
public class WebDownloadDelegate {
    public init()
}
```

**功能：** 通过该类的回调接口将下载任务的状态通知给用户。

**系统能力：** SystemCapability.Web.Webview.Core

### init()

```cangjie
public init()
```

**功能：** 构造WebDownloadDelegate对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### func onBeforeDownload((WebDownloadItem) -> Unit)

```cangjie
public func onBeforeDownload(callback: (WebDownloadItem) -> Unit): Unit
```

**功能：** 下载开始前通知给用户，用户需要在此接口中调用WebDownloadItem.start("xxx")并提供下载路径，否则下载会一直处于PENDING状态。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([WebDownloadItem](#class-webdownloaditem))->Unit|是|-|触发下载的回调。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkWeb.*
import kit.UIKit.Web

let webController = WebviewController()
let webDownloadDelegate = WebDownloadDelegate()
var failedData = Array<UInt8>()
var download = WebDownloadItem()

@Entry
@Component
class EntryView {
    func build() {
        Row {
            Column {
                Button("setDownloadDelegate").onClick {
                    evt =>
                    AppLog.info("setDownloadDelegate")
                    webDownloadDelegate.onBeforeDownload(
                        {
                            item: WebDownloadItem =>
                            AppLog.info("will start a download.")
                            // 传入一个下载路径，并开始下载。
                            item.start("/data/storage/el2/base/cache/web/" + "filename.mp4")
                        }
                    )
                    webDownloadDelegate.onDownloadUpdated(
                        {
                        item: WebDownloadItem => AppLog.info("download update guid: ${item.getGuid()}")
                    })
                    webDownloadDelegate.onDownloadFailed(
                        {
                        item: WebDownloadItem => AppLog.info("download failed guid: ${item.getGuid()}")
                    })
                    webDownloadDelegate.onDownloadFinish(
                        {
                        item: WebDownloadItem => AppLog.info("download finish guid: ${item.getGuid()}")
                    })
                    webController.setDownloadDelegate(webDownloadDelegate)
                }.width(400.px).height(150.px)
                Button("startDownload").onClick {
                    evt =>
                    AppLog.info("startDownload")
                    try {
                        webController.startDownload("https://www.example.com")
                    } catch (e: Exception) {
                        AppLog.error("startDownload exception")
                        AppLog.info(e.message)
                    }
                }.width(400.px).height(150.px)
                Web(src: "www.example.com", controller: webController).onPageBegin(
                    {
                    evt => AppLog.info("page begin url: ${evt.url}")
                }).onPageEnd({
                    evt => AppLog.info("page end url: ${evt.url}")
                })
            }.width(100.percent)
        }.height(100.percent)
    }
}
```