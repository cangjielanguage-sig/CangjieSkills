### func getLastJavascriptProxyCallingFrameUrl()

```cangjie
public func getLastJavascriptProxyCallingFrameUrl(): String
```

**功能：** 注入JavaScript对象到window对象中。该接口可以获取最后一次调用注入的对象的frame的url。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前页面的原始url地址。|

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

class TestObj {
    var mycontroller: WebviewController

    public init(controller: WebviewController) {
        this.mycontroller = controller
    }

    func testString(testStr: String): String {
        AppLog.info('Web Component str' + testStr + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl())
        return testStr
    }

    func toString(): Unit {
        AppLog.info('Web Component toString ' + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl())
    }

    func testNumber(testNum: Int64): Int64 {
        AppLog.info(
            "Web Component number ${testNum}" + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl())
        return testNum
    }

    func testBool(testBol: Bool): Bool {
        AppLog.info(
            'Web Component boolean' + testBol.toString() + " url " +
            this.mycontroller.getLastJavascriptProxyCallingFrameUrl())
        return testBol
    }
}

class WebObj {
    var mycontroller: WebviewController

    init(controller: WebviewController) {
        this.mycontroller = controller
    }

    func webTest(str: String): String {
        AppLog.info('Web test ' + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
        return "Web test"
    }

    func webString(): Unit {
        AppLog.info('Web test toString ' + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
    }
}

@Entry
@Component
class EntryView {
    let controller = WebviewController()
    @State
    var testObjtest: TestObj = TestObj(this.controller)

    @State
    var webTestObj: WebObj = WebObj(this.controller)
    func build() {
        Column() {
            Button('refresh').onClick {
                _ => try {
                    this.controller.refresh()
                } catch (e: BusinessException) {
                    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
            Button('Register JavaScript To Window').onClick {
                _ => try {
                    this.controller.registerJavaScriptProxy([this.testObjtest.testString], "objName", ["testString"])
                    this.controller.registerJavaScriptProxy([this.webTestObj.webTest], "objTestName", ["webTest"])
                } catch (e: BusinessException) {
                    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
            Web(src: ('index.html'), controller: this.controller).onPageBegin(
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
<!-- index.html -->
<!DOCTYPE html>
<html>
    <meta charset="utf-8">
    <body>
      <button type="button" onclick="htmlTest()">Click Me!</button>
      <p id="demo"></p>
      <p id="webDemo"></p>
    </body>
    <script type="text/javascript">
    function htmlTest() {
      // This function call expects to return "ArkUI Web Component"
      let str=objName.test("webtest data");
      objName.testNumber(1);
      objName.testBool(true);
      document.getElementById("demo").innerHTML=str;
      console.log('objName.test result:'+ str)

      // This function call expects to return "Web test"
      let webStr = objTestName.webTest();
      document.getElementById("webDemo").innerHTML=webStr;
      console.log('objTestName.webTest result:'+ webStr)
    }
</script>
</html>
```