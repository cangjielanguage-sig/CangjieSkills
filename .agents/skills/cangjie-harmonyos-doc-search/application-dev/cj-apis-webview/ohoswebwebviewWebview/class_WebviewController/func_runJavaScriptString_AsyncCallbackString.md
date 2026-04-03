### func runJavaScript(String, AsyncCallback\<String>)

```cangjie
public func runJavaScript(script: String, callback: AsyncCallback<String>): Unit
```

**功能：** 在当前显示页面的上下文中执行JavaScript脚本，脚本执行的结果将通过回调方式返回。此方法必须在用户界面（UI）线程上使用，并且回调也将在用户界面（UI）线程上调用。

> **说明：**
>
> - 跨导航操作（如loadUrl）时，JavaScript状态将不再保留。例如，调用loadUrl前定义的全局变量和函数在加载的页面中将不存在。
> - 建议应用程序使用registerJavaScriptProxy来确保JavaScript状态能够在页面导航间保持。
> - 目前不支持传递对象，支持传递结构体。
> - 前端页面传到Native的string数据类型会被视为json格式的数据，需要调用JSON.parse反序列化。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|script|String|是|-|JavaScript脚本。|
|callback|[AsyncCallback](../arkinterop/cj-api-business_exception.md#type-asynccallbackt)\<String>|是|-|回调执行JavaScript脚本结果。JavaScript脚本若执行失败或无返回值时，返回字符串null。|

**异常：**

- BusinessException：对应错误码如下表，详见[Webview错误码](./cj-errorcode-webview.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkUI.LengthProp
import kit.ArkUI.Button
import kit.ArkUI.Column
import kit.ArkUI.CustomView
import kit.ArkUI.CJEntry
import kit.ArkUI.loadNativeView
import kit.ArkUI.SubscriberManager
import kit.ArkUI.LocalStorage
import ohos.arkui.state_macro_manage.Entry
import ohos.arkui.state_macro_manage.Component
import kit.ArkWeb.*
import kit.ArkUI.Web
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.*
import ohos.arkui.state_macro_manage.rawfile
import ohos.resource.__GenerateResource__

let callback2: AsyncCallback<String> = {
    errorCode: Option<BusinessException>, data: Option<String> => match (errorCode) {
        case Some(e) => Hilog.error(0, "test", "callback error: errcode is ${e.code}")
        case _ =>
            match (data) {
                case Some(value) =>
                    Hilog.info(0, "test", "callback: get data successfully and data is ${value}")
                case _ => Hilog.error(0, "test", "callback: data is null")
            }
    }
}
@Entry
@Component
class webview_32 {
    let webController = WebviewController()
    func build() {
        Column(space: 10) {
            Button("runJavaScript")
            .onClick ({
                evt =>
                Hilog.info(0, "test", "runJavaScript")
                webController.runJavaScript("test()", callback2)
            }).width(400.px).height(150.px)

            Web(src: @rawfile("index.html"), controller: webController)
            .onPageBegin({evt =>
                Hilog.info(0, "test", "page begin url: ${evt.url}")
            })
            .onPageEnd({evt =>
                Hilog.info(0, "test", "page end url: ${evt.url}")
            })
        }
    }
}
```

加载的html文件。需要在`entry\src\main\resources\rawfile`目录下新增`index.html`文件。

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
  <meta charset="utf-8">
  <body>
      Hello world!
  </body>
  <script type="text/javascript">
  function test() {
      console.log('Ark WebComponent')
      return "This value is from index.html"
  }
  </script>
</html>
```