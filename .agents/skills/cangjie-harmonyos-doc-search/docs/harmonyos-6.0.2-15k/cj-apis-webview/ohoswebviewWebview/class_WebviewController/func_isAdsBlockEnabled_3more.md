### func isAdsBlockEnabled()

```cangjie
public func isAdsBlockEnabled() : Bool
```

**功能：** 查询广告过滤功能是否开启，默认该功能未启用。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true代表广告过滤功能已开启，返回false代表广告过滤功能关闭。|

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
            Button("isAdsBlockEnabled").onClick {
                evt =>
                AppLog.info("isAdsBlockEnabled")
                let adsBlockEnabled = webController.isAdsBlockEnabled()
                AppLog.info("isAdsBlockEnabled returns: ${adsBlockEnabled}")
            }.width(400.px).height(150.px)
            Web(src: "www.example.com", controller: webController)
        }
    }
}
```

### func isAdsBlockEnabledForCurPage()

```cangjie
public func isAdsBlockEnabledForCurPage(): Bool
```

**功能：** 查询当前网页是否开启广告过滤功能。

当Web组件使能广告过滤功能后，默认所有页面都是开启广告过滤的，支持通过[addAdsBlockDisallowedList](#static-func-addadsblockallowedlistarraystring)指定域名禁用广告过滤。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true代表此网页已开启广告过滤，返回false代表当前网页已关闭广告过滤。|

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
            Button("isAdsBlockEnabledForCurPage").onClick {
                evt =>
                AppLog.info("isAdsBlockEnabledForCurPage")
                let adsBlockEnabledForCurPage = webController.isAdsBlockEnabledForCurPage()
                AppLog.info("isAdsBlockEnabledForCurPage returns: ${adsBlockEnabledForCurPage}")
            }.width(400.px).height(150.px)
            Web(src: "www.example.com", controller: webController)
        }
    }
}
```

### func isIncognitoMode()

```cangjie
public func isIncognitoMode(): Bool
```

**功能：** 查询当前是否是隐私模式的Webview。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回是否是隐私模式的Webview。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100001|Init error. The WebviewController must be associated with a Web component.|

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
            Button("isIncognitoMode").onClick {
                evt =>
                AppLog.info("isIncognitoMode")
                let bool = webController.isIncognitoMode()
                AppLog.info("isIncognitoMode returns ${bool}")
            }.width(400.px).height(150.px)

            Web(src: "www.example.com", controller: webController).onPageBegin(
                {
                evt => AppLog.info("page begin url: ${evt.url}")
            }).onPageEnd({
                evt => AppLog.info("page end url: ${evt.url}")
            })
        }
    }
}
```