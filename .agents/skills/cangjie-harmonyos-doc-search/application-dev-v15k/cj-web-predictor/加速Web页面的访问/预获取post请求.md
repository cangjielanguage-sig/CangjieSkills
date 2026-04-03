## 预获取post请求

可以通过[prefetchResource()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#static-func-prefetchresourcerequestinfo-arraywebheader-string-int32)预获取将要加载页面中的post请求。在页面加载结束时，可以通过[clearPrefetchedResource()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#static-func-clearprefetchedresourcearraystring)清除后续不再使用的预获取资源缓存。

以下示例，在Web组件onAppear中，对要加载页面中的post请求进行预获取。在onPageEnd中，可以清除预获取的post请求缓存。

```cangjie
// xxx.cj
import ohos.state_macro_manage.*
import kit.ArkWeb.{WebviewController, RequestInfo, WebHeader}
import kit.UIKit.{Web, BusinessException}

@Entry
@Component
class EntryView {
    let webController = WebviewController()

    func build() {
        Column {
            Web(src: 'https://www.example.com/', controller: this.webController).onAppear {
                =>
                // 预获取时，需要將"https://www.example1.com/post?e=f&g=h"替换成真实要访问的网站地址。
                let requestInfo = RequestInfo("https://www.example1.com/post?e=f&g=h", "POST", "a=x&b=y")
                let webHeader = WebHeader("c", "z")
                WebviewController.prefetchResource(requestInfo, additionalHeaders: [webHeader], cacheKey: "KeyX",
                    cacheValidTime: 500)
            }.onPageEnd {
                evt =>
                // 清除后续不再使用的预获取资源缓存。
                WebviewController.clearPrefetchedResource(["KeyX"])
            }
        }
    }
}
```

如果能够预测到Web组件将要加载页面或者即将要跳转页面中的post请求。可以通过[prefetchResource()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#static-func-prefetchresourcerequestinfo-arraywebheader-string-int32)预获取即将要加载页面的post请求。

以下示例，在onPageEnd中，触发预获取一个要访问页面的post请求。

```cangjie
// xxx.cj
import ohos.state_macro_manage.*
import kit.ArkWeb.{WebviewController, RequestInfo, WebHeader}
import kit.UIKit.{Web, BusinessException}

@Entry
@Component
class EntryView {
    let webController = WebviewController()

    func build() {
        Column {
            Web(src: 'https://www.example.com/', controller: this.webController).onPageEnd {
                evt =>
                // 预获取时，需要將"https://www.example1.com/post?e=f&g=h"替换成真实要访问的网站地址。
                let requestInfo = RequestInfo("https://www.example1.com/post?e=f&g=h", "POST", "a=x&b=y")
                let webHeader = WebHeader("c", "z")
                WebviewController.prefetchResource(requestInfo, additionalHeaders: [webHeader], cacheKey: "KeyX",
                    cacheValidTime: 500)
            }
        }
    }
}
```