### func getSecurityLevel()

```cangjie
public func getSecurityLevel(): SecurityLevel
```

**功能：** 获取当前网页的安全级别。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[SecurityLevel](#enum-securitylevel)|当前网页的安全级别，具体值为NONE、SECURE、WARNING、DANGEROUS。|

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
            Button("getSecurityLevel").onClick {
                evt =>
                AppLog.info("getSecurityLevel")
                let securityLevel = webController.getSecurityLevel()
                match (securityLevel) {
                    case SecurityLevel.NONE => AppLog.info("getSecurityLevel returns NONE")
                    case SecurityLevel.SECURE => AppLog.info("getSecurityLevel returns SECURE")
                    case SecurityLevel.WARNING => AppLog.info("getSecurityLevel returns WARNING")
                    case SecurityLevel.DANGEROUS => AppLog.info("getSecurityLevel returns DANGEROUS")
                    case _ => throw IllegalArgumentException("The type is not supported.")
                }
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

### func getSurfaceId()

```cangjie
public func getSurfaceId(): String
```

**功能：** 获取ArkWeb对应Surface的ID，仅Web组件渲染模式是ASYNC_RENDER时有效。getSurfaceId需要在Web组件初始化之后才能获取到值。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|ArkWeb持有Surface的ID。|

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
            Button("getSurfaceId").onClick {
                event: ClickEvent =>
                let surfaceId = webController.getSurfaceId()
                AppLog.info("surfaceId: " + surfaceId)
            }
        }
    }
}
```

### func getTitle()

```cangjie
public func getTitle(): String
```

**功能：** 获取当前网页的标题。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|当前网页的标题。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100001|Init error. The WebviewController must be associated with a Web component.|