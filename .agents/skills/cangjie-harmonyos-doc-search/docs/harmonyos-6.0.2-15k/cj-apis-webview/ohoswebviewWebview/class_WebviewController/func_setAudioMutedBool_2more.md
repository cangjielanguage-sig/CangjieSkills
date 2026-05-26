### func setAudioMuted(Bool)

```cangjie
public func setAudioMuted(mute: Bool): Unit
```

**功能：** 设置网页静音。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mute|Bool|是|-|表示是否将网页设置为静音状态，true表示设置为静音状态，false表示取消静音状态。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.|
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
    @State
    var muted: Bool = false
    func build() {
        Column(10) {
            Button("Toggle Mute").onClick {
                evt =>
                AppLog.info("Toggle Mute")
                this.muted = !this.muted
                webController.setAudioMuted(this.muted)
                AppLog.info("setAudioMuted success")
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

### func setBackForwardCacheOptions(BackForwardCacheOptions)

```cangjie
public func setBackForwardCacheOptions(options: BackForwardCacheOptions): Unit
```

**功能：** 可以设置Web组件中前进后退缓存的相关选项。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[BackForwardCacheOptions](#class-backforwardcacheoptions)|是|-|用来控制Web组件前进后退缓存相关选项。|

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
            Button("Add options").onClick {
                event: ClickEvent =>
                let options = BackForwardCacheOptions(3, 10)
                webController.setBackForwardCacheOptions(options)
            }
            Button("Backward").onClick {
                event: ClickEvent => webController.backward()
            }
            Button("Forward").onClick {
                event: ClickEvent => webController.forward()
            }
            Web(src: "www.example.com", controller: webController)
        }
    }
}
```