### func searchNext(Bool)

```cangjie
public func searchNext(foward: Bool): Unit
```

**功能：** 滚动到下一个匹配的查找结果并高亮。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|foward|Bool|是|-|从前向后或者逆向查找。|

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
            Button("searchNext").onClick {
                evt =>
                AppLog.info("searchNext")
                webController.searchNext(true)
                AppLog.info("searchNext success")
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

### func serializeWebState()

```cangjie
public func serializeWebState(): Array<UInt8>
```

**功能：** 将当前Webview的页面状态历史记录信息序列化。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt8>|当前Webview的页面状态历史记录序列化后的数据。|

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

let webController = WebviewController()
let con = WebviewController()

@Entry
@Component
class EntryView {
    func build() {
        Column(10) {
            Web(src: "www.example.com", controller: webController).height(200)

            Button("serialize and restore WebState").onClick {
                evt =>
                AppLog.info("serialize and restore WebState")
                let state = webController.serializeWebState()
                con.restoreWebState(state)
            }.width(400.px).height(150.px)
            Web(src: "www.example.com", controller: con).height(200)
        }.width(100.percent)
    }
}
```