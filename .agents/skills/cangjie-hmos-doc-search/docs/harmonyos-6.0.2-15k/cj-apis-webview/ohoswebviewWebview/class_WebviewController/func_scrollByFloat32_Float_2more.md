### func scrollBy(Float32, Float32, Int32)

```cangjie
public func scrollBy(deltaX: Float32, deltaY: Float32, duration!: Int32 = 0): Unit
```

**功能：** 将页面滚动指定的偏移量。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deltaX|Float32|是|-|水平偏移量，其中水平向右为正方向。|
|deltaY|Float32|是|-|垂直偏移量，其中垂直向下为正方向。|
|duration|Int32|否|0| **命名参数。** 滚动动画时间。<br>单位：ms。<br>不传入为无动画，当传入数值为负数或传入0时，按照不传入处理。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100001|Init error. The WebviewController must be associated with a Web component.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkWeb.*
import kit.UIKit.Web

@Entry
@Component
class EntryView {
    let webController = WebviewController()
    func build() {
        Column(10) {
            Button("scrollBy").onClick {
                evt =>
                AppLog.info("scrollBy")
                webController.scrollBy(50.0, 50.0)
            }.width(400.px).height(150.px)

            Web(src: ("index.html"), controller: webController).onPageBegin(
                {
                evt => AppLog.info("page begin url: ${evt.url}")
            }).onPageEnd({
                evt => AppLog.info("page end url: ${evt.url}")
            })
        }
    }
}
```

加载的html文件。需要在`entry\src\main\resources\rawfile`目录下新增`index.html`文件。

```html
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Demo</title>
    <style>
        body {
            width:3000px;
            height:3000px;
            padding-right:170px;
            padding-left:170px;
            border:5px solid blueviolet
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>
```

### func scrollByWithResult(Float32, Float32)

```cangjie
public func scrollByWithResult(deltaX: Float32, deltaY: Float32): Unit
```

**功能：**  将页面滚动指定的偏移量，返回值表示此次滚动是否执行成功。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deltaX|Float32|是|-|水平偏移量，其中水平向右为正方向。|
|deltaY|Float32|是|-|垂直偏移量，其中垂直向下为正方向。|

**异常：**

- BusinessException：对应错误码如下表，详见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|
  |17100001|Init error. The WebviewController must be associated with a Web component.|

**示例：**

<!-- compile -->

```cangjie
import ohos.state_macro_manage.rawfile
import kit.ArkWeb.*
import kit.ArkWeb.Error as webError
import kit.LocalizationKit.*
import kit.UIKit.*

@Entry
@Component
class EntryView {
    var testTitle: String = "webScroll"

    var webCtrl: WebviewController = WebviewController()

    func build() {
        Column() {
            Row() {
                Text(this.testTitle).fontSize(30).fontWeight(FontWeight.Bold).margin(5)
            }

            Row() {
                Button("scrollByWithResult").onClick(
                    {
                    _ => try {
                        this.webCtrl.scrollByWithResult(100.0, 100.0)
                    } catch (e: BusinessException) {
                        AppLog.error("ErrorCode: ${e.code}, ErrorMessage: ${e.message}")
                    }
                })
            }

            Row() {
                Web(src: @rawfile("scrollByTo.html"), controller: this.webCtrl).width(100.percent).height(600)
            }
        }.height(100.percent).width(100.percent)
    }
}
```

加载的html文件。需要在entry\src\main\resources\rawfile目录下新增[scrollByTo.html](#scrollHtml)文件。