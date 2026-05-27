## class GeolocationPermissions

```cangjie
public class GeolocationPermissions {}
```

**功能：** Web组件地理位置权限管理对象。

> **说明：**
>
> 目前，调用GeolocationPermissions下的方法之前都需要先加载Web组件。

**需要权限：** 访问地理位置时需添加权限 ohos.permission.LOCATION、ohos.permission.APPROXIMATELY_LOCATION、ohos.permission.LOCATION_IN_BACKGROUND。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### static func allowGeolocation(String, Bool)

```cangjie
public static func allowGeolocation(origin: String, incognito!: Bool = false): Unit
```

**功能：** 允许指定来源使用地理位置接口。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|origin|String|是|-|指定源的字符串索引。|
|incognito|Bool|否|false| **命名参数。** true表示隐私模式下允许指定来源使用地理位置，false表示正常非隐私模式下允许指定来源使用地理位置。|

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
            Button("allowGeolocation").onClick {
                evt =>
                AppLog.info("allowGeolocation")
                let origin = "file:///"
                GeolocationPermissions.allowGeolocation(origin, incognito: true)
                GeolocationPermissions.allowGeolocation("file:///a")
                GeolocationPermissions.allowGeolocation("file:///b")
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

### static func deleteAllGeolocation(Bool)

```cangjie
public static func deleteAllGeolocation(incognito!: Bool = false): Unit
```

**功能：** 清除所有来源的地理位置权限状态。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|incognito|Bool|否|false| **命名参数。** true表示清除隐私模式下所有来源的地理位置权限状态，false表示清除正常非隐私模式下所有来源的地理位置权限状态。|

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
            Button("deleteAllGeolocation").onClick {
                evt =>
                AppLog.info("deleteAllGeolocation")
                GeolocationPermissions.deleteAllGeolocation(incognito: true)
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