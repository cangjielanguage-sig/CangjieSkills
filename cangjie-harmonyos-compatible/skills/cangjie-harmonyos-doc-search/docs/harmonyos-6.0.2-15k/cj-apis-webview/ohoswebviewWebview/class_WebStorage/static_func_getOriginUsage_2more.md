### static func getOriginUsage(String, AsyncCallback\<Int64>)

```cangjie
public static func getOriginUsage(origin: String, callback: AsyncCallback<Int64>): Unit
```

**功能：** 异步获取指定源的Web SQL数据库的存储量，存储量以字节为单位。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|origin|String|是|-|指定源的字符串索引。|
|callback|[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<Int64>|是|-|指定源的存储量。|

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
    let controller = WebviewController()
    func build() {
        Row {
            Column {
                Button("deleteHttpAuthCredentials").onClick {
                    WebDataBase.deleteHttpAuthCredentials()
                }
            }.width(100.percent)
            Web(src: "www.huawei.com", controller: controller)
        }.height(100.percent)
    }
}
```

加载的html文件，请参考[deleteOrigin](#static-func-deleteoriginstring)接口下的html文件。

### static func getOrigins(AsyncCallback\<Array\<WebStorageOrigin>>)

```cangjie
public static func getOrigins(callback: AsyncCallback<Array<WebStorageOrigin>>): Unit
```

**功能：** 以回调方式异步获取当前使用Web SQL数据库的所有源的信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<Array\<[WebStorageOrigin](#class-webstorageorigin)>>|是|-|以数组方式返回源的信息，信息内容参考WebStorageOrigin。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.|
  |17100012|Invalid web storage origin.|

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
            Button("getOrigins").onClick {
                evt =>
                AppLog.info("getOrigins")
                let callbackWebStorageOrigin: AsyncCallback<Array<WebStorageOrigin>> = {
                    errorCode: Option<AsyncError>, data: Option<Array<WebStorageOrigin>> => match (errorCode) {
                        case Some(e) => AppLog.error("callback error: errcode is ${e.code}")
                        case _ => match (data) {
                            case Some(value) =>
                                AppLog.info("callback: get data successfully and data is: ")
                                for (origin in value) {
                                    AppLog.info("origin: ${origin.origin}")
                                    AppLog.info("usage: ${origin.usage}")
                                    AppLog.info("quota: ${origin.quota}")
                                }
                            case _ => AppLog.error("callback: data is null")
                        }
                    }
                }
                WebStorage.getOrigins(callbackWebStorageOrigin)
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