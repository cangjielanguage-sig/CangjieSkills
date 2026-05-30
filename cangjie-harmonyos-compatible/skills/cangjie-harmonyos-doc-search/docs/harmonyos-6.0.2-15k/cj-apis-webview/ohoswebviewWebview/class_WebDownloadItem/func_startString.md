### func start(String)

```cangjie
public func start(downloadPath: String): Unit
```

**功能：** 开始一个下载任务。

> **说明：**
>
> 该方法需要在[WebDownloadDelegate.onBeforeDownload](#func-onbeforedownloadwebdownloaditem---unit)回调中使用，如果[WebDownloadDelegate.onBeforeDownload](#func-onbeforedownloadwebdownloaditem---unit)中未调用start('xxx')，该下载任务会一直处于PENDING状态。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|downloadPath|String|是|-|下载文件的磁盘存储路径（包含文件名）。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed.|

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
                            item: WebDownloadItem =>
                            // 传入一个下载路径，并开始下载。
                            item.start("/data/storage/el2/base/cache/web/${item.getSuggestedFileName()}")
                            WebDownloadManager.setDownloadDelegate(webDownloadDelegate)
                        }
                    )
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