# 使用Web组件加载页面

页面加载是Web组件的基本功能。根据页面加载数据来源可以分为三种常用场景，包括加载网络页面、加载本地页面、加载HTML格式的富文本数据。

页面加载过程中，若涉及网络资源获取，请在module.json5中配置网络访问权限，添加方法请参见[在配置文件中声明权限](../security/AccessToken/cj-declare-permissions.md)。

```json
"requestPermissions":[
  {
    "name" : "ohos.permission.INTERNET"
  }
]
```

## 加载网络页面

开发者可以在Web组件创建时，指定默认加载的网络页面 。在默认页面加载完成后，如果开发者需要变更此Web组件显示的网络页面，可以通过调用[loadUrl()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-loadurlstring)接口加载指定的网页。[Web组件](../../API_Reference/source_zh_cn/arkui-cj/cj-web-web.md#web)的第一个参数变量src不能通过状态变量（例如：@State）动态更改地址，如需更改，请通过[loadUrl()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-loadurlstring)重新加载。

在下面的示例中，在Web组件加载完“www.example.com”页面后，开发者可通过loadUrl接口将此Web组件显示页面变更为“www.example1.com”。

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
            Button("loadUrl").onClick {
                evt => try {
                    // 点击按钮时，通过loadUrl，跳转到www.example1.com
                    webController.loadUrl('www.example1.com')
                } catch (e: BusinessException) {
                    AppLog.error("loadUrl ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
            // 组件创建时，加载www.example.com
            Web(src: 'www.example.com', controller: webController)
        }
    }
}
```