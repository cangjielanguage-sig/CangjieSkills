### static func deleteGeolocation(String, Bool)

```cangjie
public static func deleteGeolocation(origin: String, incognito!: Bool = false): Unit
```

**功能：** 清除指定来源的地理位置权限状态。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|origin|String|是|-|指定源的字符串索引。|
|incognito|Bool|否|false| **命名参数。** true表示清除隐私模式下指定来源的地理位置权限状态，false表示清除正常非隐私模式下指定来源的地理位置权限状态。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100011|Invalid origin.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkWeb.*
import kit.UIKit.Web

let webController = WebviewController()

@Entry
@Component
class EntryView {
    func build() {
        Column(10) {
            Button("deleteGeolocation").onClick {
                evt =>
                AppLog.info("deleteGeolocation")
                let origin = "file:///"
                GeolocationPermissions.deleteGeolocation(origin, incognito: true)
                GeolocationPermissions.deleteGeolocation("file:///a")
                GeolocationPermissions.deleteGeolocation("file:///b")
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

### static func getAccessibleGeolocation(String, Bool)

```cangjie
public static func getAccessibleGeolocation(origin: String, incognito!: Bool = false): Bool
```

**功能：** 获取指定源的地理位置权限状态。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|origin|String|是|-|指定源的字符串索引。|
|incognito|Bool|否|false| **命名参数。** true表示获取隐私模式下指定源的地理位置权限状态，false表示获取正常非隐私模式下指定源的地理位置权限状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|获取指定源的权限状态，true表示已授权，false表示拒绝访问。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100011|Invalid origin.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkWeb.*
import kit.UIKit.Web

let webController = WebviewController()

@Entry
@Component
class EntryView {
    func build() {
        Column(10) {
            Button("getAccessibleGeolocation").onClick {
                evt =>
                AppLog.info("getAccessibleGeolocation")
                let origin = "file:///"
                try {
                    let bool = GeolocationPermissions.getAccessibleGeolocation(origin, incognito: true)
                    AppLog.info("getAccessibleGeolocation, iscongnito true: ${bool}")
                } catch (e: Exception) {
                    AppLog.info("getAccessibleGeolocation erro: ${e.message}")
                }
                try {
                    let bool = GeolocationPermissions.getAccessibleGeolocation(origin)
                    AppLog.info("getAccessibleGeolocation, iscongnito true: ${bool}")
                } catch (e: Exception) {
                    AppLog.info("getAccessibleGeolocation erro: ${e.message}")
                }
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