### func registerJavaScriptProxy(Array\<(String) -> String>, String, Array\<String>)

```cangjie
public func registerJavaScriptProxy(funcs: Array<(String) -> String>, name: String, methodList: Array<String>): Unit
```

**功能：** 注入仓颉方法到Window对象中，并在window对象中调用该方法。注册后，须调用[refresh](#func-refresh)接口生效。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|funcs|Array\<(String) -> String>|是|-|参与注册的应用侧仓颉方法数组。注册的仓颉方法的入参和返回值都是String类型。|
|name|String|是|-|注册仓颉方法数组的名称，与window中调用的对象名一致。注册后window对象可以通过此名字访问应用侧仓颉方法。|
|methodList|Array\<String>|是|-|参与注册的应用侧仓颉方法名，此数组的长度需要与funcs数组一致。注册完成后，后续funcs的判等会通过methodList来判断。因此后续如果想注册新的、或更改funcs，需要传入新的methodList。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|WebviewController registerJavaScriptProxy failed: the funcs and methodList must have the same size.|
  |17100001|Init error. The WebviewController must be associated with a Web component.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkWeb.*
import kit.UIKit.Web

let webController = WebviewController()
let callback: AsyncCallback<String> = {
    errorCode: Option<AsyncError>, data: Option<String> => match (errorCode) {
        case Some(e) => AppLog.error("callback error: errcode is ${e.code}")
        case _ => match (data) {
            case Some(value) =>
                AppLog.info("callback: get data successfully and data is ${value.toArray()}")
                AppLog.info("callback: get data successfully and data is ${value}")
            case _ => AppLog.error("callback: data is null")
        }
    }
}

@Entry
@Component
class EntryView {
    func build() {
        Row {
            Column {
                Button("refresh").onClick {
                    evt =>
                    AppLog.info("refresh")
                    webController.refresh()
                }.width(400.px).height(150.px)
                Button("proxy").onClick {
                    evt =>
                    AppLog.info("registerJavaScriptProxy")
                    let funcA1 = {
                        a: String =>
                        AppLog.info("funcA1 ${a}")
                        return "funcA1 " + a
                    }
                    let funcA2 = {
                        a: String =>
                        AppLog.info("funcA2 ${a}")
                        return "funcA2 " + a
                    }
                    let funcA3 = {
                        a: String =>
                        AppLog.info("funcA3 ${a}")
                        return "funcA3 " + a
                    }
                    let funcB1 = {
                        a: String =>
                        AppLog.info("funcB1 ${a}")
                        return "funcB1 " + a
                    }
                    let funcB2 = {
                        a: String =>
                        AppLog.info("funcB2 ${a}")
                        return "funcB2 " + a
                    }
                    let funcB3 = {
                        a: String =>
                        AppLog.info("funcB3 ${a}")
                        return "funcB3 " + a
                    }
                    let funcsA = [funcA1, funcA2, funcA3]
                    let funcsB = [funcB1, funcB2, funcB3]
                    let methodListA = ["testFunA1", "testFunA2", "testFunA3"]
                    let methodListB = ["testFunB1", "testFunB2", "testFunB3"]
                    try {
                        webController.registerJavaScriptProxy(funcsA, "testObjA", methodListA)
                        webController.registerJavaScriptProxy(funcsB, "testObjB", methodListB)
                    } catch (e: Exception) {
                        AppLog.info(e.message)
                    }
                }.width(400.px).height(150.px)
                Button("deleteJavaScriptRegister").onClick {
                    evt =>
                    AppLog.info("deleteJavaScriptRegister")
                    webController.deleteJavaScriptRegister("testObjA")
                }.width(400.px).height(150.px)
                Button("runProxy").onClick {
                    evt =>
                    AppLog.info("runProxy")
                    webController.runJavaScript("testObjA.testFunA2('someData')", callback)
                    webController.runJavaScript("testObjB.testFunB2('someData')", callback)
                }.width(400.px).height(150.px)