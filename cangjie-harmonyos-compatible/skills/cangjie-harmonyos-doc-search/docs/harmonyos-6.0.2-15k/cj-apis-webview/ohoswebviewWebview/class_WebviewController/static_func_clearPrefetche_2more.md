### static func clearPrefetchedResource(Array\<String>)

```cangjie
public static func clearPrefetchedResource(cacheKeyList: Array<String>): Unit
```

**功能：** 清除指定缓存key列表对应的预获取资源缓存。入参中的缓存key必须是[prefetchResource](#static-func-prefetchresourcerequestinfo-arraywebheader-string-int32)指定预获取到的资源缓存key。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cacheKeyList|Array\<String>|是|-|用于后续查询预获取资源缓存的key。仅支持字母和数字，传入空则取默认url作为key。|

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
        Column(10) {
            Web(src: "https://www.example.com/", controller: controller).onAppear {
                =>
                // 预获取时，需要將"https://www.example1.com/post?e=f&g=h"替换成真实要访问的网站地址。
                WebviewController.prefetchResource(
                    RequestInfo("https://www.example1.com/post?e=f&g=h", "POST", "a=x&b=y"),
                    additionalHeaders: [WebHeader("c", "z")], cacheKey: "KeyX", cacheValidTime: 500)
            }.onPageEnd({
                val =>
                // 清除后续不再使用的预获取缓存。
                WebviewController.clearPrefetchedResource(["KeyX"])
            })
        }
    }
}
```

### static func clearServiceWorkerWebSchemeHandler()

```cangjie
public static func clearServiceWorkerWebSchemeHandler(): Unit
```

**功能：** 清除应用中设置的所有用于拦截ServiceWorker的WebSchemeHandler。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

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
    let schemeHandler = WebSchemeHandler()
    func build() {
        Column(10) {
            Button('clearServiceWorkerWebSchemeHandler').onClick {
                _ => try {
                    WebviewController.clearServiceWorkerWebSchemeHandler()
                } catch (e: BusinessException) {
                    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
        }
    }
}
```