## 使用Web组件发起一个下载任务

使用[startDownload()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-startdownloadstring)接口发起一个下载。

Web组件发起的下载会根据当前显示的url以及Web组件默认的Referrer Policy来计算referrer。

在下面的示例中，先点击setDownloadDelegate按钮向Web注册一个监听类，然后点击startDownload主动发起了一个下载，该下载任务也会通过设置的DownloadDelegate来通知app下载的进度。

```cangjie
// index.cj
import ohos.state_macro_manage.*
import kit.ArkWeb.{WebviewController, WebDownloadDelegate, WebDownloadItem}
import kit.UIKit.{Web, BusinessException}

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
                        // 当前的下载速度。
                        AppLog.info("download update speed: ${webDownloadItem.getCurrentSpeed()}")
                    }
                    delegate.onDownloadFailed {
                        webDownloadItem: WebDownloadItem =>
                        AppLog.info("download failed guid: ${webDownloadItem.getGuid()}")
                        // 下载任务失败的错误码。
                        AppLog.info("download failed last error code: ${webDownloadItem.getLastErrorCode()}")
                    }
                    delegate.onDownloadFinish {
                        webDownloadItem: WebDownloadItem => AppLog.info(
                            "download finish guid: ${webDownloadItem.getGuid()}")
                    }
                    webController.setDownloadDelegate(this.delegate)
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
            Web(src: 'www.example.com', controller: this.webController)
        }
    }
}
```

使用[DocumentViewPicker()](../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_picker.md#class-documentviewpicker)获取当前示例的默认下载目录，将该目录设置为下载目录。

1. 获取context。

    ```cangjie
    // main_ability.cj
    import kit.AbilityKit.{LaunchReason, LaunchParam, Want, UIAbility, UIAbilityContext}
    import kit.UIKit.AppLog

    var globalAbilityContext: Option<UIAbilityContext> = Option<UIAbilityContext>.None

    class MainAbility <: UIAbility {
        public init() {
            super()
            registerSelf()
        }

        public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
            AppLog.info("MainAbility OnCreated.${want.abilityName}")

            // 获取context
            globalAbilityContext = Option<UIAbilityContext>.Some(this.context)

            match (launchParam.launchReason) {
                case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
                case _ => ()
            }
        }

        // ...
    }
    ```

2. 获取和设置下载目录。

    ```cangjie
    // index.cj
    import ohos.state_macro_manage.*
    import kit.ArkWeb.{WebviewController, WebDownloadDelegate, WebDownloadItem}
    import kit.UIKit.{Web, BusinessException, AsyncError}
    import kit.CoreFileKit.*
    import kit.AbilityKit.UIAbilityContext
    import kit.LocalizationKit.{__GenerateResource__}

    @Entry
    @Component
    class EntryView {
        let webController = WebviewController()
        let delegate = WebDownloadDelegate()