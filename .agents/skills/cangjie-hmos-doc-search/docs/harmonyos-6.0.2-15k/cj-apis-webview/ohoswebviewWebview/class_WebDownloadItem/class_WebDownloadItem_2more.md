## class WebDownloadItem

```cangjie
public class WebDownloadItem  {
    public init()
}
```

**功能：** 表示下载任务。可以使用此对象来操作相应的下载任务。

> **说明：**
>
> 在下载过程中，下载的进程会通过[WebDownloadDelegate](#class-webdownloaddelegate)通知给使用者，使用者可以通过其中的参数WebDownloadItem来操作下载任务。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### static func deserialize(Array\<UInt8>)

```cangjie
public static func deserialize(serializedData: Array<UInt8>): WebDownloadItem
```

**功能：** 将序列化后的字节数组反序列化为一个WebDownloadItem对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|serializedData|Array\<UInt8>|是|-|序列化后的下载。|

**返回值：**

|类型|说明|
|:----|:----|
|[WebDownloadItem](#class-webdownloaditem)|从字节数组反序列化为一个WebDownloadItem对象。|

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