### static func getOriginQuota(String, AsyncCallback\<Int64>)

```cangjie
public static func getOriginQuota(origin: String, callback: AsyncCallback<Int64>): Unit
```

**功能：** 获取指定源的Web SQL数据库的存储配额，配额以字节为单位。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|origin|String|是|-|指定源的字符串索引。|
|callback|[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<Int64>|是|-|指定源的存储配额。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.|
  |17100011|Invalid origin.|

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
            Button("getOriginQuota").onClick {
                evt =>
                AppLog.info("getOriginQuota")
                let callbackInt: AsyncCallback<Int64> = {
                    errorCode: Option<AsyncError>, data: Option<Int64> => match (errorCode) {
                        case Some(e) => AppLog.error("callback error: errcode is ${e.code}")
                        case _ => match (data) {
                            case Some(value) => AppLog.info("callback: get data successfully and data is ${value}")
                            case _ => AppLog.error("callback: data is null")
                        }
                    }
                }
                WebStorage.getOriginQuota("resource://rawfile/", callbackInt)
            }.width(400.px).height(150.px)
            Web(src: ("storage.html"), controller: webController).onPageBegin(
                {
                evt => AppLog.info("page begin url: ${evt.url}")
            }).onPageEnd({
                evt => AppLog.info("page end url: ${evt.url}")
            })
        }
    }
}
```

加载的html文件，请参考[deleteOrigin](#static-func-deleteoriginstring)接口下的html文件。