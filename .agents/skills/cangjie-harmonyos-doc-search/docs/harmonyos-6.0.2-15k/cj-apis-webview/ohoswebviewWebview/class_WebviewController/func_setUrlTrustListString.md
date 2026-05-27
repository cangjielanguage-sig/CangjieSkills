### func setUrlTrustList(String)

```cangjie
public func setUrlTrustList(urlTrustList: String): Unit
```

**功能：** 设置当前web的url白名单，只有白名单内的url才能允许加载/跳转，否则将拦截并弹出告警页。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|urlTrustList|String|是|-|url白名单列表，使用json格式配置，最大支持10MB。 白名单设置接口为覆盖方式，多次调用接口时，以最后一次设置为准。 当本参数为空字符串时，表示取消白名单，放行所有url的访问。 json格式示例：<br>{<br>&ensp;“UrlPermissionList”: [<br>&ensp;&ensp;{<br>&ensp;&ensp;&ensp;“scheme”: “https”,<br>&ensp;&ensp;&ensp;“host”: “www.example1.com”,<br>&ensp;&ensp;&ensp;“port”: 443,<br>&ensp;&ensp;&ensp;“path”: “pathA/pathB”<br>&ensp;&ensp;},<br>&ensp;&ensp;{<br>&ensp;&ensp;&ensp;“scheme”: “http”,<br>&ensp;&ensp;&ensp;“host”: “www.example2.com”,<br>&ensp;&ensp;&ensp;“port”: 80,<br>&ensp;&ensp;&ensp;“path”: “test1/test2/test3”<br>&ensp;&ensp;}]<br>}|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.2. Parameter string is too long.3. Parameter verification failed.|
  |17100001|Init error. The WebviewController must be associated with a Web component.|

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
    let urltrustList: String = "{\"UrlPermissionList\":[{\"scheme\":\"http\", \"host\":\"trust.example.com\", \"port\":80, \"path\":\"test\"}]}"
    func build() {
        Column(10) {
            Button('Setting the trustlist').onClick {
                _ => try {
                    // 设置白名单，只允许访问trust网页
                    webController.setUrlTrustList(this.urltrustList)
                } catch (e: BusinessException) {
                    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
            Button('Cancel the trustlist.').onClick {
                _ => try {
                    // 白名单传入空字符串表示关闭白名单机制，所有url都可以允许访问
                    webController.setUrlTrustList("")
                } catch (e: BusinessException) {
                    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
            Button('Access the trust web').onClick {
                _ => try {
                    // 白名单生效，可以访问untrust网页
                    webController.loadUrl('http://trust.example.com/test')
                } catch (e: BusinessException) {
                    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
            Button('Access the untrust web').onClick {
                _ => try {
                    // 白名单生效，此时不可以访问untrust网页，并弹出错误页
                    webController.loadUrl('http://untrust.example.com/test')
                } catch (e: BusinessException) {
                    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
            Web(src: "http://untrust.example.com/test", controller: webController).onPageBegin {
                _ => try {
                    // onControllerAttached回调中设置白名单，可以保证在加载url之前生效，此时不可以访问untrust网页，并弹出错误页
                    webController.setUrlTrustList(this.urltrustList)
                } catch (e: BusinessException) {
                    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
        }
    }
}
```