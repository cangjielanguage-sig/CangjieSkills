# 应用侧调用前端页面函数

应用侧可以通过[runJavaScript()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-runjavascriptstring-asynccallbackstring)和[runJavaScriptExt()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-runjavascriptextstring-asynccallbackjsmessageext)方法调用前端页面的JavaScript相关函数。

[runJavaScript()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-runjavascriptstring-asynccallbackstring)和[runJavaScriptExt()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-runjavascriptextstring-asynccallbackjsmessageext)在参数类型上有些差异。[runJavaScriptExt()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-runjavascriptextstring-asynccallbackjsmessageext)入参类型不仅支持string还支持ArrayBuffer（从文件中获取JavaScript脚本数据），另外可以通过AsyncCallback的方式获取执行结果。

在下面的示例中，单击应用侧的“runJavaScript”按钮时，来触发前端页面的htmlTest()方法。

- 前端页面代码：

    ```html
    <!-- resources/rawfile/test_java_script.html  -->
    <!DOCTYPE html>
    <html>
    <body>
    <button type="button" onclick="callCangjie()">Click Me!</button>
    <h1 id="text">这是一个测试信息，默认字体为黑色，调用runJavaScript方法后字体为绿色，调用runJavaScriptCodePassed方法后，点击button，字体变为红色</h1>
    <script>
        // 调用有参函数时实现。
        var param = "param: JavaScript Hello World!";
        function htmlTest(param) {
            document.getElementById('text').style.color = 'green';
            console.log(param);
        }
        // 调用无参函数时实现。
        function htmlTest() {
            document.getElementById('text').style.color = 'green';
        }
        // Click Me！触发前端页面callCangjie()函数执行JavaScript传递的代码。
        function callCangjie() {
            changeColor();
        }
    </script>
    </body>
    </html>
    ```

- 应用侧代码：

    ```cangjie
    // index.cj
    import ohos.state_macro_manage.*
    import kit.LocalizationKit.{__GenerateResource__}
    import kit.UIKit.{Web, AsyncError, AsyncCallback, BusinessException}
    import kit.ArkWeb.WebviewController

    let callback: AsyncCallback<String> = {
        errorCode: Option<AsyncError>, data: Option<String> => match (errorCode) {
            case Some(e) => AppLog.error("callback error: errcode is ${e.code}")
            case _ => match (data) {
                case Some(value) => AppLog.info("callback: get data successfully and data is ${value}")
                case _ => AppLog.error("callback: data is null")
            }
        }
    }

    @Entry
    @Component
    class EntryView {
        let webController = WebviewController()

        public func aboutToAppear(): Unit {
            try {
                // 配置Web开启调试模式
                WebviewController.setWebDebuggingAccess(true);
            } catch (e: BusinessException) {
                AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}");
            }
        }

        func build() {
            Column() {
                Button("runJavaScript").onClick {
                    evt => try {
                        // 前端页面函数无参时，将param删除
                        webController.runJavaScript("htmlTest(param)", callback)
                        AppLog.info("runJavaScript success")
                    } catch (e: BusinessException) {
                        AppLog.error("runJavaScript ErrorCode: ${e.code},  Message: ${e.message}")
                    }
                }
                Button("runJavaScriptCodePassed").onClick {
                    evt => try {
                        // 传递runJavaScript侧代码方法，修改text颜色为红色
                        webController.runJavaScript(
                            "function changeColor(){document.getElementById('text').style.color = 'red'}", callback)
                        AppLog.info("runJavaScript success")
                    } catch (e: BusinessException) {
                        AppLog.error("runJavaScript ErrorCode: ${e.code},  Message: ${e.message}")
                    }
                }

                Web(src: @rawfile("test_java_script.html"), controller: webController)
            }
        }
    }
    ```
