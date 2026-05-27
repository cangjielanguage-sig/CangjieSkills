### func setScrollable(Bool, ScrollType)

```cangjie
public func setScrollable(enable: Bool, `type`!: ScrollType): Unit
```

**功能：**  设置网页是否允许滚动。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enable|Bool|是|-|表示是否将网页设置为允许滚动。<br>true表示设置为允许滚动，false表示禁止滚动。|
|\`type\`|[ScrollType](#enum-scrolltype)|否|-|网页可触发的滚动类型，支持缺省配置。<br>- enable为false时，表示禁止ScrollType类型的滚动，当ScrollType缺省时表示禁止所有类型网页滚动。<br>- enable为true时，ScrollType缺省与否，都表示允许所有类型的网页滚动。|

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
import kit.UIKit.Web
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
                Button("setScrollable").onClick(
                    {
                    _ => try {
                        this.webCtrl.setScrollable(false, `type`: ScrollType.EVENT)
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