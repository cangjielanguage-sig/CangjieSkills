### static func customizeSchemes(Array\<WebCustomScheme>)

```cangjie
public static func customizeSchemes(schemes: Array<WebCustomScheme>): Unit
```

**功能：** 对Web内核赋予自定义协议url的跨域请求与fetch请求的权限。当Web在跨域fetch自定义协议url时，该fetch请求可被onInterceptRequest事件接口所拦截，从而开发者可以进一步处理该请求。建议在任何Web组件初始化之前调用该接口。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|schemes|Array\<[WebCustomScheme](#class-webcustomscheme)>|是|-|自定义协议配置，最多支持同时配置10个自定义协议。|

**异常：**

- BusinessException：对应错误码如下表，详见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|
  |17100020|Failed to register custom schemes.|

**示例：**

<!-- compile -->

```cangjie
import kit.ArkWeb.*
import kit.UIKit.Web
import kit.LocalizationKit.*
import kit.UIKit.*

@Entry
@Component
class EntryView {
    var webCtrl: WebviewController = WebviewController()

    func build() {
        Row {
            Column {
                Web(src: "https://www.example.com/", controller: webCtrl)
            }.width(100.percent)
        }.height(100.percent)
    }

    protected override func aboutToAppear() {
        try {
            let scheme1 = WebCustomScheme("name1")
            scheme1.isSupportCORS = true
            scheme1.isSupportFetch = true

            let scheme2 = WebCustomScheme("name2")
            scheme2.isSupportCORS = true
            scheme2.isSupportFetch = true

            let scheme3 = WebCustomScheme("name3")
            scheme3.isSupportCORS = true
            scheme3.isSupportFetch = true

            WebviewController.customizeSchemes([scheme1, scheme2, scheme3])
        } catch (e: BusinessException) {
            AppLog.error("ErrorCode: ${e.code}, ErrorMessage: ${e.message}")
        }
    }
}
```