## 使用Web组件恢复进程退出时未下载完成的任务

在Web组件启动时，可通过[resumeDownload()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#static-func-resumedownloadwebdownloaditem)接口恢复未完成的下载任务。

在以下示例中，可借助“recovery”按钮恢复持久化的下载任务。

```cangjie
// index.cj
import ohos.state_macro_manage.*
import kit.ArkWeb.{WebviewController, WebDownloadDelegate, WebDownloadItem, WebDownloadManager}
import kit.UIKit.{Web, BusinessException}

// 用于记录失败的下载任务。
var failedData = Array<UInt8>()

@Entry
@Component
class EntryView {
    let webController = WebviewController()
    let delegate = WebDownloadDelegate()

    func build() {
        Column {
            Button("setDownloadDelegate").onClick {
                evt => try {
                    delegate.onBeforeDownload {
                        webDownloadItem: WebDownloadItem =>
                        // 传入一个下载路径，并开始下载。
                        webDownloadItem.start(
                            "/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName())
                    }
                    delegate.onDownloadUpdated {
                        webDownloadItem: WebDownloadItem =>
                        // 下载任务的唯一标识。
                        AppLog.info("download update guid: ${webDownloadItem.getGuid()}")
                        // 下载的进度。
                        AppLog.info("download update percent complete: ${webDownloadItem.getPercentComplete()}")
                    }
                    delegate.onDownloadFailed {
                        webDownloadItem: WebDownloadItem =>
                        AppLog.info("download failed guid: ${webDownloadItem.getGuid()}")
                        // 序列化失败的下载到一个字节数组。
                        failedData = webDownloadItem.serialize()
                    }
                    delegate.onDownloadFinish {
                        webDownloadItem: WebDownloadItem => AppLog.info(
                            "download finish guid: ${webDownloadItem.getGuid()}")
                    }
                    webController.setDownloadDelegate(this.delegate)
                    WebDownloadManager.setDownloadDelegate(this.delegate)
                } catch (e: BusinessException) {
                    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
            Button("startDownload").onClick {
                evt => try {
                    // 这里指定下载地址为 https://www.example.com/，Web组件会发起一个下载任务将该页面下载下来。
                    // 开发者需要替换为自己想要下载的内容的地址。
                    webController.startDownload('https://www.example.com/')
                } catch (e: BusinessException) {
                    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
            // 恢复下载任务。
            // 按钮触发时必须保证WebDownloadManager.setDownloadDelegate设置完成。
            Button("recovery").onClick {
                evt => try {
                    WebDownloadManager.resumeDownload(WebDownloadItem.deserialize(failedData))
                } catch (e: BusinessException) {
                    AppLog.error("resumeDownload ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
            Web(src: 'www.example.com', controller: this.webController)
        }
    }
}
```