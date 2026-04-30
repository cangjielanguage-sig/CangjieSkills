### func setNetworkAvailable(Bool)

```cangjie
public func setNetworkAvailable(enable: Bool): Unit
```

**功能：** 设置JavaScript中的window.navigator.onLine属性。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enable|Bool|是|-|是否使能window.navigator.onLine。|

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
            Button("setNetworkAvailable").onClick {
                evt =>
                AppLog.info("setNetworkAvailable")
                webController.setNetworkAvailable(true)
                AppLog.info("setNetworkAvailable success")
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
<body>
<h1>online 属性</h1>
<p id="demo"></p>
<button onclick="func()">click</button>
<script>
    let online = navigator.onLine;
    document.getElementById("demo").innerHTML = "浏览器在线：" + online;

    function func(){
      var online = navigator.onLine;
      document.getElementById("demo").innerHTML = "浏览器在线：" + online;
    }
</script>
</body>
</html>
```