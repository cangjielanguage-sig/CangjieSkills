### static func enableBackForwardCache(BackForwardCacheSupportedFeatures)

```cangjie
public static func enableBackForwardCache(features: BackForwardCacheSupportedFeatures): Unit
```

**功能：** 开启Web组件前进后退缓存功能，通过参数指定是否允许使用特定的页面进入前进后退缓存。需要在[initializeWebEngine](#static-func-initializewebengine)初始化内核之前调用。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|features|[BackForwardCacheSupportedFeatures](#class-backforwardcachesupportedfeatures)|是|-|允许使用特定的页面进入前进后退缓存中。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.ArkWeb.*

class MainAbility <: UIAbility {
    public init() {
        super()
        registerSelf()
    }
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        let features = BackForwardCacheSupportedFeatures(true, true)
        // 如果一个页面同时使用了同层渲染和视频托管的能力，需要 nativeEmbed 和
        // mediaTakeOver 同时设置为 true，该页面才可以进入前进后退缓存中。
        WebviewController.enableBackForwardCache(features)
        WebviewController.initializeWebEngine()
        AppStorage.setOrCreate("abilityWant", want)
    }
}
```

### static func enableWholeWebPageDrawing()

```cangjie
public static func enableWholeWebPageDrawing(): Unit
```

**功能：** 设置开启网页全量绘制能力。仅在web初始化时设置。

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
    let headers = [WebHeader("headerKey", "headerValue")]
    func build() {
        Column(10) {
            Button("enableWholeWebPageDrawing").onClick {
                evt =>
                AppLog.info("enableWholeWebPageDrawing")
                WebviewController.enableWholeWebPageDrawing()
            }.width(400.px).height(150.px)
            Web(src: "www.example.com", controller: webController)
        }
    }
}
```

### static func getRenderProcessMode()

```cangjie
public static func getRenderProcessMode(): RenderProcessMode
```

**功能：** 查询ArkWeb的渲染子进程模式。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[RenderProcessMode](#enum-renderprocessmode)|渲染子进程模式类型。|

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
        Column() {
            Button('getRenderProcessMode').onClick {
                =>
                let mode = WebviewController.getRenderProcessMode()
                AppLog.info("getRenderProcessMode: " + mode)
            }

            Web(src: 'www.example.com', controller: this.controller)
        }
    }
}
```

### static func initializeWebEngine()

```cangjie
public static func initializeWebEngine(): Unit
```

**功能：** 在Web组件初始化之前，通过此接口加载Web引擎的动态库文件，以提高启动性能。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### static func pauseAllTimers()

```cangjie
public static func pauseAllTimers(): Unit
```

**功能：** 暂停所有WebView的定时器。

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
    func build() {
        Column(10) {
            Button("pauseAllTimers").onClick {
                evt =>
                AppLog.info("pauseAllTimers")
                webController.pauseAllTimers()
            }.width(400.px).height(150.px)
            Web(src: "www.example.com", controller: webController)
        }
    }
}
```