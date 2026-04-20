# 加速Web页面的访问

当Web页面加载缓慢时，可以使用预连接、预加载和预获取post请求的能力加速Web页面的访问。

## 预解析和预连接

可以通过[prepareForPageLoad()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#static-func-prepareforpageloadstring-bool-int32)来预解析或者预连接将要加载的页面。

在下面的示例中，在Web组件的onAppear中对要加载的页面进行预连接。

```cangjie
// xxx.cj
import ohos.state_macro_manage.*
import kit.ArkWeb.WebviewController
import kit.UIKit.{Web, BusinessException}

@Entry
@Component
class EntryView {
    let webController = WebviewController()

    func build() {
        Column {
            Button("accessBackward").onClick {
                evt => try {
                    if (webController.accessForward()) {
                        webController.backward()
                    }
                } catch (e: BusinessException) {
                    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
            Web(src: 'https://www.example.com/', controller: this.webController).onAppear {
                =>
                // 指定第二个参数为true，代表要进行预连接，如果为false该接口只会对网址进行dns预解析
                // 第三个参数为要预连接socket的个数。最多允许6个。
                WebviewController.prepareForPageLoad('https://www.example.com/', true, 2)
            }
        }
    }
}
```

## 预加载

如果能够预测到Web组件将要加载的页面或者即将要跳转的页面。可以通过[prefetchPage()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-prefetchpagestring)来预加载即将要加载页面。

预加载会提前下载页面所需的资源，包括主资源子资源，但不会执行网页JavaScript代码。预加载是WebviewController的实例方法，需要一个已经关联好Web组件的WebviewController实例。

在下面的示例中，在onPageEnd的时候触发下一个要访问的页面的预加载。

```cangjie
// xxx.cj
import ohos.state_macro_manage.*
import kit.ArkWeb.WebviewController
import kit.UIKit.Web

@Entry
@Component
class EntryView {
    let webController = WebviewController()

    func build() {
        Column {
            Web(src: 'https://www.example.com/', controller: this.webController).onPageEnd {
                evt =>
                // 预加载地址https://www.example2.com，实际使用时请替换成真实要访问的网站地址。
                webController.prefetchPage("https://www.example2.com")
            }
        }
    }
}
```