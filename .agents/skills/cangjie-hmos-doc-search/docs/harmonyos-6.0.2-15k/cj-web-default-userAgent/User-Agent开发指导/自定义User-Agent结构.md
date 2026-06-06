## 自定义User-Agent结构

在下面的示例中，通过调用[getUserAgent()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-getuseragent)接口获取当前默认的用户代理（User-Agent）字符串。这一接口提供的默认User-Agent信息为开发者提供了基础，使开发者能够基于这个默认信息进行定制或扩展。

```cangjie
// index.cj
import kit.ArkWeb.*
import kit.UIKit.{Web, BusinessException}

@Entry
@Component
class EntryView {
    let webController = WebviewController()

    func build() {
        Column {
            Button("getUserAgent").onClick {
                evt => try {
                    let userAgent = webController.getUserAgent()
                    AppLog.info("userAgent: ${userAgent}")
                } catch (e: BusinessException) {
                    AppLog.error("getUserAgent ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
            Web(src: 'www.example.com', controller: webController)
        }
    }
}
```

以下示例通过[setCustomUserAgent()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-setcustomuseragentstring)接口设置自定义用户代理，但请注意，此操作会覆盖系统的用户代理。因此，我们建议将扩展字段追加在默认用户代理的末尾，比如三方应用程序的开发场景，可以在系统默认用户代理字符串的末尾追加特定的APP标识，这样既能保留原有用户代理信息，又能增加自定义的应用识别信息。

当Web组件src设置了url时，建议在onControllerAttached回调事件中设置User-Agent，设置方式请参考示例。不建议将User-Agent设置在onLoadIntercept回调事件中，会概率性出现设置失败。如果未在onControllerAttached回调事件中设置User-Agent。再调用setCustomUserAgent方法时，可能会出现加载的页面与实际设置User-Agent不符的异常现象。

当Web组件src设置为空字符串时，建议先调用setCustomUserAgent方法设置User-Agent，再通过loadUrl加载具体页面。

```cangjie
// index.cj
import kit.ArkWeb.*
import kit.UIKit.{Web, BusinessException}

@Entry
@Component
class EntryView {
    let webController = WebviewController()

    func build() {
        Column {
            Web(src: 'www.example.com', controller: webController).onControllerAttached(
                {
                    =>
                    AppLog.info("controller attached")
                    try {
                        let customUserAgent: String = 'DemoApp'
                        let userAgent = webController.getUserAgent() + customUserAgent
                        AppLog.info("userAgent: ${userAgent}")
                        webController.setCustomUserAgent(userAgent)
                    } catch (e: BusinessException) {
                        AppLog.error("setCustomUserAgent ErrorCode: ${e.code},  Message: ${e.message}")
                    }
                }
            )
        }
    }
}
```

在下面的示例中，通过[getCustomUserAgent()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-getcustomuseragent)接口获取自定义用户代理。

```cangjie
// index.cj
import kit.ArkWeb.*
import kit.UIKit.{Web, BusinessException}

@Entry
@Component
class EntryView {
    let webController = WebviewController()

    func build() {
        Column {
            Button("getUserAgent").onClick {
                evt => try {
                    let customUserAgent = webController.getCustomUserAgent()
                    AppLog.info("customUserAgent: ${customUserAgent}")
                } catch (e: BusinessException) {
                    AppLog.error("getCustomUserAgent ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
            Web(src: 'www.example.com', controller: webController)
        }
    }
}
```