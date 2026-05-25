### func getMethod()

```cangjie
public func getMethod(): String
```

**功能：** 获取下载任务的请求方式。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|下载的请求方式。|

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
                            AppLog.info("will start a download, method: ${item.getMethod()}")
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