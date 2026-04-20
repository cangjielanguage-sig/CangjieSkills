### 示例2（设置事件派发策略为FORWARD）

点击List下方空白区域后拖动，可以滑动List。点击Button按钮时，Button不会响应onClick事件。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.{ArrayList, HashMap}

@Entry
@Component
class EntryView {
    @State
    var value: Int32 = 1
    @State
    var text: String = "Button"
    let numbers: ArrayList<Int64> = ArrayList<Int64>([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    func touchTestInfo(touchinfo: Array<TouchTestInfo>): TouchResult {
        let items = ArrayList<TouchTestInfo>()
        for (item in touchinfo) {
            if (item.id == 'MyList') {
                return TouchResult(TouchTestStrategy.FORWARD, id: item.id)
            }
        }
        return TouchResult(TouchTestStrategy.DEFAULT, id: "")
    }

    func build() {
        Column {
            List(space: 10, initialIndex: 0) {
                ForEach(
                    this.numbers,
                    itemGeneratorFunc: {
                        item: Int64, _: Int64 => ListItem() {
                            Text("${item}").width(100.percent).height(56).fontSize(16).textAlign(TextAlign.Center).
                                borderRadius(10).backgroundColor(0xFFFFFF)
                        }.backgroundColor(Color.WHITE).borderRadius(24).padding(12)
                    }
                )
            }.scrollBar(BarState.Off).width(80.percent).onScrollIndex(
                {
                first: Int32, last: Int32 => AppLog.info("first: " + first.toString() + " last: " + last.toString())
            }).width(100.percent).height(65.percent).id("MyList")

            Button(this.text).width(312).height(40).id("Mybutton").onClick(
                {
                    evt =>
                    this.text = "click the button"
                    PromptAction.showToast(message: "you click the button", duration: 3000)
                }
            )
        }.width(100.percent).height(100.percent).onChildTouchTest(touchTestInfo)
    }
}
```

![touch_event](figures/onChildTouchTest.gif)

### 示例3（设置事件派发策略为DEFAULT）

点击List下方空白区域后拖动，List不会滑动。点击Button按钮时，Button会响应onClick事件。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.{ArrayList, HashMap}

@Entry
@Component
class EntryView {
    @State
    var value: Int32 = 1
    @State
    var text: String = "Button"
    let numbers: ArrayList<Int64> = ArrayList<Int64>([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    func touchTestInfo(touchinfo: Array<TouchTestInfo>): TouchResult {
        return TouchResult(TouchTestStrategy.DEFAULT, id: "")
    }

    func build() {
        Column {
            List(space: 10, initialIndex: 0) {
                ForEach(
                    this.numbers,
                    itemGeneratorFunc: {
                        item: Int64, _: Int64 => ListItem() {
                            Text("${item}").width(100.percent).height(56).fontSize(16).textAlign(TextAlign.Start)
                        }.backgroundColor(Color.WHITE).borderRadius(24).padding(left: 12, right: 12)
                    }
                )
            }.listDirection(Axis.Vertical).scrollBar(BarState.Off).edgeEffect(EdgeEffect.Spring).onScrollIndex(
                {
                first: Int32, last: Int32 => AppLog.info("first: " + first.toString() + " last: " + last.toString())
            }).onDidScroll(
                {
                scrollOffset: Float64, scrollState: ScrollState => AppLog.info(
                    'onScroll scrollState = ScrollState.${scrollState.toString()}, scrollOffset = ${scrollOffset}')
            }).width(100.percent).height(65.percent).id("MyList")

            Button(this.text).width(312).height(40).id("Mybutton").margin(top: 80).fontSize(16).fontWeight(
                FontWeight.Medium).onClick(
                {
                    evt =>
                    this.text = "click the button"
                    PromptAction.showToast(message: "you click the button", duration: 3000)
                }
            )
        }.width(100.percent).height(100.percent).backgroundColor(0xF1F3F5).justifyContent(FlexAlign.End).padding(
            left: 12, right: 12, bottom: 24).onChildTouchTest(touchTestInfo)
    }
}
```

![childrentouch](./figures/childrentouch-3.gif)