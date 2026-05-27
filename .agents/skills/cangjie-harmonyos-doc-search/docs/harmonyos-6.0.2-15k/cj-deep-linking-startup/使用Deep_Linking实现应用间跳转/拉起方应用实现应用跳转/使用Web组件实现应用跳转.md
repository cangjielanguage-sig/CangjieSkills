### 使用Web组件实现应用跳转

Web组件需要跳转DeepLink链接应用时，可通过拦截回调[onLoadIntercept](../../API_Reference/source_zh_cn/arkui-cj/cj-web-web.md#func-onloadinterceptwebresourcerequest---bool)中对定义的事件进行处理，实现应用跳转。

示例代码如下：

```cangjie
// index.cj
import ohos.state_macro_manage.rawfile
import kit.AbilityKit.{UIAbilityContext, Want}
import kit.UIKit.{AppLog, Button, BusinessException, Web}
import kit.ArkWeb.WebviewController
import kit.LocalizationKit.__GenerateResource__

// 见获取UIAbility的上下文信息章节
func getContext(): UIAbilityContext {
    return globalContext.getOrThrow()
}

let webController = WebviewController()

@Entry
@Component
class EntryView {
    @State
    var message: String = "Hello World"

    func build() {
        Row {
            Column {
                Web(src: @rawfile("index.html"), controller: webController).onLoadIntercept(
                    {
                        evt =>
                        let url = evt.getRequestUrl()
                        if (url == "link://www.example.com") {
                            try {
                                getContext().openLink(url)
                                AppLog.info("open link success.")
                            } catch (e: BusinessException) {
                                AppLog.error("Failed to start link. Code is ${e.code}, message is ${e.message}")
                            }
                            return true
                        }
                        // 返回true表示阻止此次加载，否则允许此次加载
                        return false
                    }
                )
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

前端页面代码：

```html
// index.html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
<h1>Hello World</h1>
<!--方式一、通过绑定事件window.open方法实现跳转-->
<button class="doOpenLink" onclick="doOpenLink()">跳转其他应用一</button>
<!--方式二、通过超链接实现跳转-->
<a href="link://www.example.com">跳转其他应用二</a>
</body>
</html>
<script>
    function doOpenLink() {
        window.open("link://www.example.com")
    }
</script>
```