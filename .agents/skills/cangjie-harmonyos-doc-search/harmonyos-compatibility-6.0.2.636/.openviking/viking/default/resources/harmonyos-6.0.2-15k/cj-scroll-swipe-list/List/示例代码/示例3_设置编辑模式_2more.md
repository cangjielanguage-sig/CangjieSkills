### 示例3 （设置编辑模式）

该示例展示了如何设置当前List组件是否处于可编辑模式。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var arr: ObservedArrayList<Int64> = ObservedArrayList<Int64>([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    @State
    var editFlag: Bool = false

    func build() {
        Stack(Alignment.TopStart) {
            Column() {
                List(space: 20, initialIndex: 0) {
                    ForEach(
                        this.arr,
                        itemGeneratorFunc: {
                            item: Int64, index: Int64 => ListItem() {
                                Flex(FlexParams(direction: FlexDirection.Row, alignItems: ItemAlign.Center)) {
                                    Text("${item}").width(100.percent).height(80).fontSize(20).textAlign(
                                        TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF).flexShrink(1)
                                    if (this.editFlag) {
                                        Button() {
                                            Text("delete").fontSize(16)
                                        }.width(30.percent).height(40).onClick(
                                            {
                                            event => if (index >= 0 && index < this.arr.size) {
                                                //BaseLog.info( "${this.arr[index]}Delete")
                                                this.arr.remove(index)
                                                //AppLog.info(this.arr.size.toString())
                                                this.editFlag = false
                                            }
                                        }).stateEffect(true)
                                    }
                                }
                            }
                        }
                    )
                }.width(90.percent).scrollBar(BarState.Off)
            }.width(100.percent)

            Button("edit list").onClick({
                event => this.editFlag = !this.editFlag
            }).margin(top: 5, left: 20)
        }.width(100.percent).height(100.percent).backgroundColor(0xDCDCDC).padding(top: 5)
    }
}
```

![list3](figures/list3.gif)

### 示例4 （设置限位对齐）

该示例展示了List组件设置居中限位的实现效果。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.ArrayList

@Entry
@Component
class EntryView {
    let arr: ArrayList<Int64> = ArrayList<Int64>([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    let scrollerForList = Scroller()

    func build() {
        Column() {
            Row() {
                List(space: 20, initialIndex: 3, scroller: this.scrollerForList) {
                    ForEach(
                        this.arr,
                        itemGeneratorFunc: {
                            item: Int64, _: Int64 => ListItem() {
                                Text("${item}").width(100.percent).height(100).fontSize(16).textAlign(TextAlign.Center)
                            }.borderRadius(10).backgroundColor(0xFFFFFF).width(60.percent).height(80.percent)
                        }
                    )
                }.chainAnimation(true).edgeEffect(EdgeEffect.Spring).listDirection(Axis.Horizontal).height(100.percent).
                    width(100.percent).borderRadius(10.px).backgroundColor(0xDCDCDC)
            }.width(100.percent).height(100.percent).backgroundColor(0xDCDCDC).padding(top: 10.px)
        }
    }
}
```

![list4](figures/list4.gif)