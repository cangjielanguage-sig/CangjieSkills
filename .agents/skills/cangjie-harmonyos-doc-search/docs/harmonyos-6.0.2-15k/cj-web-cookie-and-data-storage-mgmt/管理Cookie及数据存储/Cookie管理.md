## Cookie管理

Cookie是网络访问过程中，由服务端发送给客户端的一小段数据。客户端可持有该数据，并在后续访问该服务端时，方便服务端快速对客户端身份、状态等进行识别。

当Cookie SameSite属性未指定时，默认值为SameSite=Lax，只在用户导航到cookie的源站点时发送cookie，不会在跨站请求中被发送。

Web组件提供了[WebCookieManager](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#class-webcookiemanager)类，用于管理Web组件的Cookie信息。Cookie信息保存在应用沙箱路径下/proc/{pid}/root/data/storage/el2/base/cache/web/Cookiesd的文件中。

下面以[configCookieSync()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#static-func-configcookiestring-string-bool)接口举例，为“www\.example.com”设置单个Cookie的值“value=test”。其他Cookie的相关功能及使用，请参见[WebCookieManager()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#class-webcookiemanager)API文档。

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
            Button("configCookie").onClick {
                evt => try {
                    WebCookieManager.configCookie('https://www.example.com', 'value=test')
                    AppLog.info("configCookie success")
                } catch (e: BusinessException) {
                    AppLog.error("configCookie ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
            Web(src: 'www.example.com', controller: webController)
        }
    }
}
```