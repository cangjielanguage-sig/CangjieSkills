### func getPercentComplete()

```cangjie
public func getPercentComplete(): Int64
```

**功能：** 获取下载的进度，100代表下载完成。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int64|下载完成的进度。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkWeb.*
import kit.UIKit.Web

let webController = WebviewController()
let webDownloadDelegate = WebDownloadDelegate()

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
                        item: WebDownloadItem => AppLog.info(
                            "download update percent complete: ${item.getPercentComplete()}")
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