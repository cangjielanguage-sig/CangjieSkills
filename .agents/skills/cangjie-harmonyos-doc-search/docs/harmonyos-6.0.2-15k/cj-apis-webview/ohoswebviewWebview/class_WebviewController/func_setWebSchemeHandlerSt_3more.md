### func setWebSchemeHandler(String, WebSchemeHandler)

```cangjie
public func setWebSchemeHandler(scheme: String, handler: WebSchemeHandler): Unit
```

**功能：** 为当前Web组件设置WebSchemeHandler，此类用于拦截指定scheme的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100001|Init error. The WebviewController must be associated with a Web component.|

### func slideScroll(Float32, Float32)

```cangjie
public func slideScroll(vx: Float32, vy: Float32): Unit
```

**功能：** 按照指定速度模拟对页面的轻扫滚动动作。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|vx|Float32|是|-|轻扫滚动的水平速度分量，其中水平向右为速度正方向。|
|vy|Float32|是|-|轻扫滚动的垂直速度分量，其中垂直向下为速度正方向。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100001|Init error.|

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
            Button("slideScroll").onClick {
                evt =>
                AppLog.info("slideScroll")
                webController.slideScroll(500.0, 500.0)
                AppLog.info("slideScroll success")
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

### func startCamera()

```cangjie
public func startCamera(): Unit
```

**功能：** 开启当前网页摄像头捕获。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

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
            Button("startCamera").onClick {
                evt =>
                AppLog.info("startCamera")
                webController.startCamera()
            }.width(400.px).height(150.px)
            Web(src: "www.example.com", controller: webController)
        }
    }
}
```