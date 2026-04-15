### func storeWebArchive(String, Bool, AsyncCallback\<String>)

```cangjie
public func storeWebArchive(baseName: String, autoName: Bool, callback: AsyncCallback<String>): Unit
```

**功能：** 以回调方式保存当前页面。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|baseName|String|是|-|生成的离线网页存储位置，该值不能为空。|
|autoName|Bool|是|-|决定是否自动生成文件名。如果为false，则按baseName的文件名存储；如果为true，则根据当前Url自动生成文件名，并按baseName的文件目录存储。|
|callback|[AsyncCallback](../arkinterop/cj-api-business_exception.md#type-asynccallbackt)\<String>|是|-|返回文件存储路径，保存网页失败会返回空字符串。|

**异常：**

- BusinessException：对应错误码如下表，详见[Webview错误码](./cj-errorcode-webview.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17100001 | Init error. The WebviewController must be associated with a Web component. |
  | 17100003 | Invalid resource path or file type. |

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

let callback1: AsyncCallback<String> = {
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
class webview_28 {
    let webController = WebviewController()
    func build() {
        Column(space: 10) {
            Button("storeWebArchive")
            .onClick ({
                evt =>
                Hilog.info(0, "test", "storeWebArchive")
                webController.storeWebArchive("/data/storage/el2/base/", true, callback1)
            }).width(400.px).height(150.px)

            Web(src: "www.example.com", controller: webController)
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