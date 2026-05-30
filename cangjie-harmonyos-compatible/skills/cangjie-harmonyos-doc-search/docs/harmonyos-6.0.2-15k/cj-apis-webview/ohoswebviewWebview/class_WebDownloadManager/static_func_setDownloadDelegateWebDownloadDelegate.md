### static func setDownloadDelegate(WebDownloadDelegate)

```cangjie
public static func setDownloadDelegate(delegate: WebDownloadDelegate): Unit
```

**功能：** 设置用于接收从WebDownloadManager触发的下载进度的委托。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|delegate|[WebDownloadDelegate](#class-webdownloaddelegate)|是|-|用来接收下载进回调的委托。|

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
                            // 传入一个下载路径，并开始下载。
                            item.start("/data/storage/el2/base/cache/web/${item.getSuggestedFileName()}")
                            WebDownloadManager.setDownloadDelegate(webDownloadDelegate)
                        }
                    )
                    webDownloadDelegate.onDownloadUpdated(
                        {
                            item: WebDownloadItem =>
                            AppLog.info("download update percent complete: ${item.getPercentComplete()}")
                            download = item
                        }
                    )
                    webDownloadDelegate.onDownloadFailed(
                        {
                            item: WebDownloadItem =>
                            AppLog.info("download failed guid: ${item.getGuid()}")
                            // 序列化失败的下载到一个字节数组。
                            failedData = item.serialize()
                        }
                    )
                    webDownloadDelegate.onDownloadFinish(
                        {
                            item: WebDownloadItem =>
                            AppLog.info("download finish guid: ${item.getGuid()}")
                            AppLog.info("download finish full path: ${item.getFullPath()}")
                        }
                    )
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
                Button("resumeDownload").onClick {
                    evt =>
                    AppLog.info("resumeDownload")
                    try {
                        WebDownloadManager.resumeDownload(WebDownloadItem.deserialize(failedData))
                    } catch (e: Exception) {
                        AppLog.error("resumeDownload exception")
                        AppLog.info(e.message)
                    }
                }.width(400.px).height(150.px)
                Button("cancel").onClick {
                    evt =>
                    AppLog.info("cancel")
                    try {
                        download.cancel()
                    } catch (e: Exception) {
                        AppLog.error("startDownload exception")
                        AppLog.info(e.message)
                    }
                }.width(400.px).height(150.px)
                Button("pause").onClick {
                    evt =>
                    AppLog.info("pause")
                    try {
                        download.pause()
                    } catch (e: Exception) {
                        AppLog.error("startDownload exception")
                        AppLog.info(e.message)
                    }
                }.width(400.px).height(150.px)
                Button("resume").onClick {
                    evt =>
                    AppLog.info("resume")
                    try {
                        download.resume()
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