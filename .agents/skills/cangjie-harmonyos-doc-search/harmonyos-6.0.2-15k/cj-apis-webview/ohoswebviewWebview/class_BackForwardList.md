## class BackForwardList

```cangjie
public class BackForwardList {}
```

**功能：** 当前Webview的历史信息列表。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

### prop currentIndex

```cangjie
public prop currentIndex: Int32
```

**功能：** 当前页面在历史列表中的索引。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### prop size

```cangjie
public prop size: Int32
```

**功能：** 历史列表中索引的数量，最多保存50条，超过时起始记录会被覆盖。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### func getItemAtIndex(Int32)

```cangjie
public func getItemAtIndex(index: Int32): HistoryItem
```

**功能：** 获取历史列表中指定索引的历史记录项信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|指定历史列表中的索引。|

**返回值：**

|类型|说明|
|:----|:----|
|[HistoryItem](#class-historyitem)|历史记录项。|

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
    func build() {
        Column(10) {
            Button("getItemAtIndex").onClick {
                evt =>
                AppLog.info("getItemAtIndex")
                let backForwardList = webController.getBackForwardEntries()
                let historyItem = backForwardList.getItemAtIndex(backForwardList.currentIndex)
                AppLog.info("Current historyUrl is ${historyItem.historyUrl}.")
                AppLog.info("Current historyRawUrl is ${historyItem.historyRawUrl}.")
                AppLog.info("Current title is ${historyItem.title}.")
                let pixelMap = historyItem.icon
                let byteInfo = pixelMap?.getPixelBytesNumber() ?? 0
                AppLog.info("icon byteInfo is ${byteInfo}")
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