## 加载HTML格式的文本数据

Web组件可以通过data url方式直接加载HTML字符串。

<!-- compile -->

```cangjie
// index.cj
import ohos.arkui.state_macro_manage.*
import ohos.web.webview.WebviewController
import kit.ArkUI.Web

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