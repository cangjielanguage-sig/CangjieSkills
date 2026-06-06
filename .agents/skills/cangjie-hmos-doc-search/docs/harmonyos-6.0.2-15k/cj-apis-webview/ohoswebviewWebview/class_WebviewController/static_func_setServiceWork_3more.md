### static func setServiceWorkerWebSchemeHandler(String, WebSchemeHandler)

```cangjie
public static func setServiceWorkerWebSchemeHandler(scheme: String, handler: WebSchemeHandler): Unit
```

**功能：** 为当前应用的所有Web组件设置的[WebSchemeHandler](#class-webschemehandler)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

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
    let schemeHandler = WebSchemeHandler()
    func build() {
        Column(10) {
            Button('setServiceWorkerWebSchemeHandler').onClick {
                _ => try {
                    WebviewController.setServiceWorkerWebSchemeHandler("https", schemeHandler)
                } catch (e: BusinessException) {
                    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
        }
    }
}
```

### static func setWebDebuggingAccess(Bool)

```cangjie
public static func setWebDebuggingAccess(webDebuggingAccess: Bool): Unit
```

**功能：** 设置是否启用网页调试功能。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|webDebuggingAccess|Bool|是|-|设置是否启用网页调试功能。|

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
    let headers = [WebHeader("headerKey", "headerValue")]
    func build() {
        Column(10) {
            Button("setWebDebuggingAccess").onClick {
                evt =>
                AppLog.info("setWebDebuggingAccess")
                WebviewController.setWebDebuggingAccess(true)
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

### static func warmupServiceWorker(String)

```cangjie
public static func warmupServiceWorker(url: String): Unit
```

**功能：** 提前加载对应地址的服务以便于在具体使用的时候能够快速响应。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|需要提前加载的地址。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100002|Invalid url.|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.*
import kit.ArkWeb.*

class MainAbility <: UIAbility {
    public init() {
        super()
        registerSelf()
    }
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("MainAbility OnCreated.${want.abilityName}")
        WebviewController.initializeWebEngine()
        WebviewController.warmupServiceWorker("https://www.example.com")
    }
    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        AppLog.info("MainAbility onWindowStageCreate.")
        windowStage.loadContent("EntryView")
    }
}
```