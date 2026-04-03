### func runJavaScriptExt(Array\<UInt8>, AsyncCallback\<JsMessageExt>)

```cangjie
public func runJavaScriptExt(script: Array<UInt8>, callback: AsyncCallback<JsMessageExt>): Unit
```

**功能：** 异步执行JavaScript脚本，并通过回调方式返回脚本执行的结果。runJavaScriptExt需要在loadUrl完成后，比如onPageEnd中调用。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|script|Array\<UInt8>|是|-|JavaScript脚本。|
|callback|[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<[JsMessageExt](#class-jsmessageext)>|是|-|回调执行JavaScript脚本结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.|
  |17100001|Init error. The WebviewController must be associated with a Web component.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import ohos.state_macro_manage.rawfile
import kit.ArkWeb.*
import kit.ArkWeb.Error as webError
import kit.UIKit.Web
import kit.LocalizationKit.*

let webController = WebviewController()

@Entry
@Component
class EntryView {
    @State
    var msg1 = ""
    @State
    var msg2 = ""
    func build() {
        Column(10) {
            Text(this.msg1).fontSize(16)
            Text(this.msg2).fontSize(16)
            Web(src: @rawfile("index.html"), controller: webController).onPageBegin(
                {
                evt => AppLog.info("page begin url: ${evt.url}")
            }).onPageEnd(
                {
                    evt =>
                    AppLog.info("page end url: ${evt.url}")
                    webController.runJavaScriptExt(
                        "test().toArray()",
                        // 异步回调函数
                        {
                            errorCode: Option<AsyncError>, data: Option<JsMessageExt> => match (errorCode) {
                                case Some(e) => AppLog.error("callback error: errcode is ${e.code}")
                                case _ => match (data) {
                                    case Some(value) =>
                                        let msgType = value.getType()
                                        match (msgType) {
                                            case JsMessageType.STRING =>
                                                this.msg1 = "result type:" + "STRING"
                                                this.msg2 = "result getString:" + ((value.getString()))
                                            case JsMessageType.NUMBER =>
                                                this.msg1 = "result type:" + "NUMBER"
                                                this.msg2 = "result getNumber: ${value.getNumber()}"
                                            case JsMessageType.BOOLEAN =>
                                                this.msg1 = "result type:" + "BOOLEAN"
                                                this.msg2 = "result getBoolean: ${value.getBoolean()}"
                                            case JsMessageType.ARRAY_BUFFER =>
                                                this.msg1 = "result type:" + "ARRAY_BUFFER"
                                                this.msg2 = "result getArrayBuffer: ${value.getArrayBuffer()}"
                                            case _ =>
                                                this.msg1 = "result type:" + "NOT_SUPPORT"
                                                this.msg2 = "result NOT_SUPPORT"
                                        }
                                    case _ => AppLog.error("callback: data is null")
                                }
                            }
                        }
                    )
                }
            )
        }.width(100.percent)
    }
}
```

加载的html文件。需要在`entry\src\main\resources\rawfile`目录下新增`index.html`文件。

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en-gb">
<body>
<h1>run JavaScript Ext demo</h1>
</body>
<script type="text/javascript">
function test() {
  return "hello, cangjie";
}
</script>
</html>
```