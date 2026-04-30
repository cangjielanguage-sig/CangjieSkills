## 加载HTML格式的文本数据

Web组件可以通过[loadData()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-loaddatastring-string-string-string-string)s接口实现加载HTML格式的文本数据。当开发者不需要加载整个页面，只需要显示一些页面片段时，可通过此功能来快速加载页面，当加载大量html文件时，需设置第四个参数baseUrl为"data"。

```cangjie
// index.cj
import ohos.state_macro_manage.*
import kit.ArkWeb.WebviewController
import kit.UIKit.{Web, BusinessException}

@Entry
@Component
class EntryView {
    let webController = WebviewController()

    func build() {
        Column {
            Button("loadData").onClick {
                evt => try {
                    // 点击按钮时，通过loadData，加载HTML格式的文本数据
                    webController.loadData(
                        "<html><body bgcolor=\"white\">Source:<pre>source</pre></body></html>",
                        "text/html",
                        "UTF-8"
                    )
                } catch (e: BusinessException) {
                    AppLog.error("loadData ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
            // 组件创建时，加载www.example.com
            Web(src: 'www.example.com', controller: webController)
        }
    }
}
```

Web组件可以通过data url方式直接加载HTML字符串。

```cangjie
// index.cj
import ohos.state_macro_manage.*
import kit.ArkWeb.WebviewController
import kit.UIKit.Web

@Entry
@Component
class EntryView {
    let webController = WebviewController()
    let htmlStr: String = "data:text/html, <html><body bgcolor=\"white\">Source:<pre>source</pre></body></html>"

    func build() {
        Column {
            // 组件创建时，加载www.example.com
            Web(src: htmlStr, controller: webController)
        }
    }
}
```