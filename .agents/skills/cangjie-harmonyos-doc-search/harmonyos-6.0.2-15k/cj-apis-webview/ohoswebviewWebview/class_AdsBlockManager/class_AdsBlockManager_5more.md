## class AdsBlockManager

```cangjie
public class AdsBlockManager {}
```

**功能：** 通过AdsBlockManager可以在Web组件中设置自定义的广告过滤配置、关闭特定网站的广告过滤功能，其中每个应用中的所有Web组件都共享一个AdsBlockManager实例。

下文中的AllowedList指广告过滤开启列表，DisallowList指广告过滤禁用列表。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### static func addAdsBlockAllowedList(Array\<String>)

```cangjie
public static func addAdsBlockAllowedList(domainSuffixes: Array<String>): Unit
```

**功能：** 向AdsBlockManager的AllowedList中添加一组域名，主要用于重新开启DisallowList中的部分网站的广告过滤。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|domainSuffixes|Array\<String>|是|-|一组域名列表，例如['example.com', 'abcd.efg.com']。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|

### static func addAdsBlockDisallowedList(Array\<String>)

```cangjie
public static func addAdsBlockDisallowedList(domainSuffixes: Array<String>): Unit
```

**功能：** 向AdsBlockManager的DisallowedList中添加一组域名。广告过滤功能开启时，将禁用这些网站的广告过滤功能。

> **说明：**
>
> - 此接口设置的域名不会持久化，应用重启需要重新设置。
> - 广告过滤特性会使用后缀匹配的方式判断domainSuffix和当前站点的url是否能匹配，例如，当前Web组件打开的网站是<https://www.example.com>，设置的DisallowList中有'example.com'或者'www.example.com'，后缀匹配成功，此网站将禁用广告过滤，访问'https://m.example.com'也将禁用广告过滤。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|domainSuffixes|Array\<String>|是|-|一组域名列表，例如['example.com', 'abcd.efg.com']。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|

### static func clearAdsBlockAllowedList()

```cangjie
public static func clearAdsBlockAllowedList(): Unit
```

**功能：** 清空AdsBlockManager的AllowedList。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkWeb.*
import kit.UIKit.{Web, TextInput}

@Entry
@Component
class EntryView {
    @State
    var input_text = "https://www.example.com"
    let webController = WebviewController()
    func build() {
        Row {
            Column {
                TextInput().id("input_url").height(50).margin(5).onChange({
                    value => this.input_text = value
                })
                Button("Go").onClick {
                    evt =>
                    AppLog.info("Go begin.")
                    webController.loadUrl(this.input_text)
                }
                Button("clearAdsBlockAllowedList").onClick {
                    evt =>
                    AppLog.info("Go begin.")
                    AdsBlockManager.clearAdsBlockAllowedList()
                }
                Web(src: "https://www.example.com", controller: webController).onPageBegin(
                    {
                    value => webController.enableAdsBlock(true)
                }).height(50)
            }
        }
    }
}
```

### static func clearAdsBlockDisallowedList()

```cangjie
public static func clearAdsBlockDisallowedList(): Unit
```

**功能：** 清空AdsBlockManager的DisallowedList。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19