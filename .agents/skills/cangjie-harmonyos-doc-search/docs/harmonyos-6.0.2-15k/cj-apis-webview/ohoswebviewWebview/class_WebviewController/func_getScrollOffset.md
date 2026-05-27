### func getScrollOffset()

```cangjie
public func getScrollOffset(): ScrollOffset
```

**功能：**  获取网页当前的滚动偏移量。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[ScrollOffset](#class-scrolloffset)|网页当前的滚动偏移量。|

**异常：**

- BusinessException：对应错误码如下表，详见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|
  |17100001|Init error. The WebviewController must be associated with a Web component.|

**示例：**

<!-- compile -->

```cangjie
import ohos.base.*
import ohos.state_macro_manage.rawfile
import kit.ArkWeb.*
import kit.ArkWeb.Error as webError
import kit.UIKit.Web
import kit.LocalizationKit.*

@Entry
@Component
class EntryView {
    @State
    var controllerX: Float32 = -100.0
    @State
    var controllerY: Float32 = -100.0

    var testTitle: String = "webScroll"

    var webCtrl: WebviewController = WebviewController()

    func build() {
        Column() {
            Row() {
                Text(this.testTitle).fontSize(30).fontWeight(FontWeight.Bold).margin(5)
            }

            Row() {
                Text("controllerX: ${this.controllerX}, controllerY: ${this.controllerY}")
            }

            Row() {
                Web(src: @rawfile("scrollByTo.html"), controller: this.webCtrl).width(100.percent).height(600).onTouch(
                    {
                    _ => try {
                        this.controllerX = this.webCtrl.getScrollOffset().x
                        this.controllerY = this.webCtrl.getScrollOffset().y
                    } catch (e: BusinessException) {
                        AppLog.error("ErrorCode: ${e.code}, ErrorMessage: ${e.message}")
                    }
                })
            }
        }.height(100.percent).width(100.percent)
    }
}
```

加载的html文件。需要在entry\src\main\resources\rawfile目录下新增<span id="scrollHtml">scrollByTo.html</span>文件。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>滚动条测试页面</title>
    <style>
        body {
          margin: 0;
          padding: 0;
        }
        .container {
          width: 3000px;
          background: linear-gradient(to right, #ffcccc, #ccffcc, #ccccff);
          padding: 20px;
        }
        .content {
          font-size: 24px;
        }
        p {
            height: 200px;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="content">
        <p>这里是滚动测试内容。</p>
        <p>段落 1</p>
        <p>段落 2</p>
        <p>段落 3</p>
        <p>段落 4</p>
        <p>段落 5</p>
        <p>段落 6</p>
        <p>段落 7</p>
        <p>段落 8</p>
        <p>段落 9</p>
        <p>段落 10</p>
        <p>段落 11</p>
        <p>段落 12</p>
        <p>段落 13</p>
        <p>段落 14</p>
        <p>段落 15</p>
        <p>段落 16</p>
        <p>段落 17</p>
        <p>段落 18</p>
        <p>段落 19</p>
        <p>段落 20</p>
    </div>
</div>
</body>
</html>
```