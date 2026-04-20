### func onActive()

```cangjie
public func onActive(): Unit
```

**功能：** 调用此接口通知Web组件进入前台激活状态。激活状态是应用与用户互动的状态。应用会保持这种状态，直到发生某些事件（例如收到来电或设备屏幕关闭）时将焦点从应用移开。

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
            Button("onActive").onClick {
                evt =>
                AppLog.info("onActive")
                webController.onActive()
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

### func onCreateNativeMediaPlayer(CreateNativeMediaPlayerCallback)

```cangjie
public func onCreateNativeMediaPlayer(callback: CreateNativeMediaPlayerCallback): Unit
```

**功能：** 注册回调函数，开启应用接管网页媒体播放功能后，当网页中有播放媒体时，触发注册的回调函数。 如果应用接管网页媒体播放功能未开启，则注册的回调函数不会被触发。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[CreateNativeMediaPlayerCallback](#type-createnativemediaplayercallback)|是|-|接管网页媒体播放的回调函数。|

### func onInactive()

```cangjie
public func onInactive(): Unit
```

**功能：** 调用此接口通知Web组件进入未激活状态。开发者可以在此回调中实现应用失去焦点时应表现的恰当行为。

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
            Button("onInactive").onClick {
                evt =>
                AppLog.info("onInactive")
                webController.onInactive()
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