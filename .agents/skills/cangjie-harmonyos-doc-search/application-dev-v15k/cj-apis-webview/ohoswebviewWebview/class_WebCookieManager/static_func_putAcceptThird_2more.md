### static func putAcceptThirdPartyCookieEnabled(Bool)

```cangjie
public static func putAcceptThirdPartyCookieEnabled(accept: Bool): Unit
```

**功能：** 设置WebCookieManager实例是否拥有发送和接收第三方cookie的权限。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|accept|Bool|是|-|设置是否拥有发送和接收第三方cookie的权限。true表示设置拥有发送和接收第三方cookie的权限，false表示设置无发送和接收第三方cookie的权限。默认为false。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkWeb.*

WebCookieManager.putAcceptThirdPartyCookieEnabled(true)
```

### static func saveCookie(() -> Unit)

```cangjie
public static func saveCookie(callback: () -> Unit): Unit
```

**功能：** 将当前存在内存中的cookie异步保存到磁盘中。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|() -> Unit|是|-|callback回调，用于获取cookie是否成功保存。|

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
    func build() {
        Column(10) {
            Button("saveCookie").onClick {
                evt =>
                AppLog.info("saveCookie")
                WebCookieManager.saveCookie({
                    => AppLog.info("save!")
                })
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