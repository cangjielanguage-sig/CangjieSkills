### func hasImage(AsyncCallback\<Bool>)

```cangjie
public func hasImage(callback: AsyncCallback<Bool>): Unit
```

**功能：** 通过Callback方式异步查找当前页面是否存在图像。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<Bool>|是|-|返回查找页面是否存在图像。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|
  |17100001|Init error. The WebviewController must be associated with a Web component.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkWeb.*
import kit.UIKit.Web

let webController = WebviewController()
let callbackBool: AsyncCallback<Bool> = {
    errorCode: Option<AsyncError>, data: Option<Bool> => match (errorCode) {
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
    func build() {
        Column(10) {
            Button("hasImageCb").onClick {
                evt =>
                AppLog.info("hasImageCb")
                webController.hasImage(callbackBool)
            }.width(400.px).height(150.px)

            Web(src: "www.example.com", controller: webController).onPageBegin(
                {
                evt => AppLog.info("page begin url: ${evt.url}")
            }).onPageEnd({
                evt => AppLog.info("page end url: ${evt.url}")
            })
        }.width(100.percent)
    }
}
```

### func injectOfflineResources(Array\<OfflineResourceMap>)

```cangjie
public func injectOfflineResources(resourceMaps: Array<OfflineResourceMap>): Unit
```

**功能：** 将本地离线资源注入到内存缓存中，以提升页面首次启动速度。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resourceMaps|Array\<[OfflineResourceMap](#class-offlineresourcemap)>|是|-|本地离线资源配置对象，单次调用最大支持注入30个资源，单个资源最大支持10Mb。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Invalid input parameter.Possible causes: 1. Mandatory parameters are left unspecified.2. Parameter verification failed.|
  |17100001|Init error. The WebviewController must be associated with a Web component.|
  |17100002|Invalid url.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkWeb.*

@Entry
@Component
class EntryView {
    let webController = WebviewController()
    func build() {
        Column(10) {
            Button("injectOfflineResources").onClick {
                event: ClickEvent => try {
                    webController.injectOfflineResources(
                        OfflineResourceMap(
                        ["https://www.example.com/", "https://www.example.com/path1/example.png",
                        "https://www.example.com/path2/example.png"], Array<Byte>(),
                        [WebHeader("Content-Type", "image/png")], OfflineResourceType.IMAGE))
                } catch (e: BusinessException) {
                    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
        }
    }
}
```