### func serialize()

```cangjie
public func serialize(): Array<UInt8>
```

**功能：** 将失败的下载任务序列化到一个字节数组。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Uint8Array|失败的下载序列化后的字节数组。|

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
                        // 传入一个下载路径，并开始下载。
                        item: WebDownloadItem => item.start(
                            "/data/storage/el2/base/cache/web/${item.getSuggestedFileName()}")
                    })
                    webDownloadDelegate.onDownloadUpdated(
                        {
                        item: WebDownloadItem => AppLog.info(
                            "download update percent complete: ${item.getPercentComplete()}")
                    })
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