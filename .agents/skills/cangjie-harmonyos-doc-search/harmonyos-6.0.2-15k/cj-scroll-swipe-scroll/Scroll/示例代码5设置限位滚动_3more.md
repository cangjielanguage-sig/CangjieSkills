## 示例代码5（设置限位滚动）

该示例实现了Scroll组件的限位滚动。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.ArrayList

@Entry
@Component
class EntryView {
    var scroller: Scroller = Scroller()
    private var arr: ArrayList<Int64> = ArrayList<Int64>(16, {i => i + 1})
    func build() {
        Scroll(this.scroller) {
            Column {
                ForEach(
                    this.arr,
                    itemGeneratorFunc: {
                        item: Int64, idx: Int64 => Text(item.toString()).width(90.percent).height(200).backgroundColor(
                            0xFFFFFF).borderWidth(1).borderRadius(15).fontSize(16).textAlign(TextAlign.Center)
                    }
                )
            }.width(100.percent).backgroundColor(0xDCDCDC)
        }.backgroundColor(Color.WHITE).height(100.percent).edgeEffect(EdgeEffect.Spring).scrollSnap(
            ScrollSnapOptions(ScrollSnapAlign.START, snapPagination: 400, enableSnapToStart: true, enableSnapToEnd: true
        ))
    }
}
```

![scroll5](./figures/scroll5.gif)

## 示例代码6（设置子组件索引）

该示例展示了如何获得List组件的子组件索引。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.ArrayList

@Entry
@Component
class EntryView {
    private var arr: ArrayList<Int64> = ArrayList<Int64>([])
    private var scroller: ListScroller = ListScroller()
    @State
    var listSpace: Int64 = 10
    @State
    var listIndex: Int64 = 0

    protected override func aboutToAppear() {
        for (i in 0..10) {
            this.arr.add(i)
        }
    }

    func build() {
        Column {
            List(space: this.listSpace, initialIndex: 4, scrollerEx: this.scroller) {
                ForEach(
                    this.arr,
                    itemGeneratorFunc: {
                        item: Int64, idx: Int64 => ListItem {
                            Text("item-" + item.toString()).height(100).width(90.percent).fontSize(16).textAlign(
                                TextAlign.Center).borderRadius(10).backgroundColor(Color.WHITE).onClick(
                                {
                                _ => this.listIndex = item
                            })
                        }
                    }
                )
            }.backgroundColor(Color.GRAY).layoutWeight(1).scrollBar(BarState.On).alignListItem(ListItemAlign.Center)

            Text("您当前位置Item索引为：" + this.listIndex.toString()).fontColor(Color.RED).height(50)
        }
    }
}
```

![scroll6](./figures/scroll6.gif)

## 示例代码7（设置边缘渐隐）

该示例实现了Scroll组件开启边缘渐隐效果并设置边缘渐隐长度。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.ArrayList

@Entry
@Component
class EntryView {
    var scroller: Scroller = Scroller()
    private var arr: ArrayList<Int64> = ArrayList<Int64>([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    func build() {
        Stack(Alignment.TopStart) {
            Scroll(this.scroller) {
                Column {
                    ForEach(
                        this.arr,
                        itemGeneratorFunc: {
                            item: Int64, idx: Int64 => Text(item.toString()).width(90.percent).height(150).
                                backgroundColor(0xFFFFFF).borderRadius(15).fontSize(16).textAlign(TextAlign.Center).
                                margin(top: 10)
                        }
                    )
                }.width(100.percent)
            }.fadingEdge(true, FadingEdgeOptions(fadingEdgeLength: 80))
        }.width(100.percent).height(100.percent).backgroundColor(0xDCDCDC)
    }
}
```

![scroll7](./figures/scroll7.gif)