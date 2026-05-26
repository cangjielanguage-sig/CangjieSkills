### static func getStoredGeolocation(Bool)

```cangjie
public static func getStoredGeolocation(incognito!: Bool = false): Array<String>
```

**功能：** 获取已存储地理位置权限状态的所有源信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|incognito|Bool|否|false| **命名参数。** true表示获取隐私模式下已存储地理位置权限状态的所有源信息，false表示获取正常非隐私模式下已存储地理位置权限状态的所有源信息。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<string>|用于获取已存储地理位置权限状态的所有源信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.|

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
            Button("getStoredGeolocation").onClick {
                evt =>
                AppLog.info("getStoredGeolocation")
                var origin = GeolocationPermissions.getStoredGeolocation(incognito: true)
                AppLog.info("getStoredGeolocation, iscongnito true: ${origin}")
                origin = GeolocationPermissions.getStoredGeolocation()
                AppLog.info("getStoredGeolocation: ${origin}")
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