## Web组件与ArkUI组件焦点控制

- 应用侧通用获焦回调接口[onFocus](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-event-focus.md#func-onfocus---unit)，获焦事件回调，绑定该接口的组件获焦时，回调响应。
- 应用侧通用失焦回调接口[onBlur](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-event-focus.md#func-onblur---unit)，失焦事件回调，绑定该接口的组件失焦时，回调响应。
- 应用侧主动请求焦点接口[requestFocus](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-requestfocus)，组件主动请求焦点。

**示例：**

1. requestFocus能够让应用开发者主动选择控制组件走焦到Web组件上。
2. onFocus和onBlur两个接口通常成对使用，来监听组件的焦点变化。

```cangjie
// xxx.cj
import ohos.state_macro_manage.*
import kit.ArkWeb.WebviewController
import kit.UIKit.{Web, BusinessException, Color}

@Entry
@Component
class EntryView {
    let webController = WebviewController()
    let webController2 = WebviewController()

    @State
    var webborderColor: Color = Color.RED
    @State
    var webborderColor2: Color = Color.RED

    func build() {
        Column {
            Row {
                Button("web1 requestFocus").onClick {
                    evt => try {
                        webController.requestFocus()
                        AppLog.info("requestFocus success")
                    } catch (e: BusinessException) {
                        AppLog.error("requestFocus ErrorCode: ${e.code},  Message: ${e.message}")
                    }
                }
                Button("web2 requestFocus").onClick {
                    evt => try {
                        webController.requestFocus()
                        AppLog.info("2 requestFocus success")
                    } catch (e: BusinessException) {
                        AppLog.error("2 requestFocus ErrorCode: ${e.code},  Message: ${e.message}")
                    }
                }
            }
            // 实际使用时，src替换成有效的参数
            Web(src: 'www.example.com', controller: webController).onFocus {
                => webborderColor = Color.GREEN
            }.onBlur {
                => webborderColor = Color.RED
            }.margin(3).borderWidth(10).borderColor(this.webborderColor).height(45.percent)
            // 实际使用时，src替换成有效的参数
            Web(src: 'www.example.com', controller: webController).onFocus {
                => webborderColor2 = Color.GREEN
            }.onBlur {
                => webborderColor2 = Color.RED
            }.margin(3).borderWidth(10).borderColor(this.webborderColor2).height(45.percent)
        }
    }
}
```

通过requestfocus接口主动请求获焦，并监听通用接口onFocus、onBlur事件，改变Web组件边框颜色。

**图1**  组件焦点获焦/失焦事件

![web-focus1.gif](figures/web-focus1.gif)