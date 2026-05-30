### 示例1 （添加滚动事件）

该示例实现了设置纵向列表，并在当前显示界面发生改变时回调索引。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    let arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    func build() {
        Stack(Alignment.TopStart) {
            Column() {
                List(space: 20, initialIndex: 0) {
                    ForEach(
                        this.arr,
                        itemGeneratorFunc: {
                            item: Int64, _: Int64 => ListItem() {
                                Text("${item}").width(100.percent).height(100).fontSize(16).textAlign(TextAlign.Center).
                                    borderRadius(10).backgroundColor(0xFFFFFF)
                            }
                        }
                    )
                }.id("list").listDirection(Axis.Vertical) // 排列方向
                    .scrollBar(BarState.Off)
                    //.friction(0.6)
                    .divider(strokeWidth: 2.px,
                    color: Color(0xFFFFFF), startMargin: 20.px, endMargin: 20.px) // 每行之间的分界线
                        .edgeEffect(EdgeEffect.Spring) // 边缘效果设置为Spring
                        .
                    onScrollIndex(
                    {
                        firstIndex: Int32, lastIndex: Int32 =>
                        BaseLog.info("first" + firstIndex.toString())
                        BaseLog.info("last" + lastIndex.toString())
                    }
                ).width(90.percent)
            }.width(100.percent).height(100.percent).backgroundColor(0xDCDCDC).padding(top: 5.px)
        }
    }
}
```

![list1](figures/list1.gif)

### 示例2 （设置子元素对齐）

该示例展示了不同ListItemAlign枚举值下，List组件交叉轴方向子元素对齐效果。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    let arr: Array<String> = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
        "16", "17", "18", "19"]
    @State
    var alignListItem: ListItemAlign = ListItemAlign.Start

    func build() {
        Column() {
            List(space: 20, initialIndex: 0) {
                ForEach(
                    this.arr,
                    itemGeneratorFunc: {
                        item: String, _: Int64 => ListItem() {
                            Text("${item}").width(100.percent).height(100).fontSize(16).textAlign(TextAlign.Center).
                                borderRadius(10).backgroundColor(0xFFFFFF)
                        }.border(width: 2.px, color: Color.GREEN).width(55)
                    }
                )
            }.height(300).width(90.percent).border(width: 3.px, color: Color.RED).lanes(6).alignListItem(
                this.alignListItem).scrollBar(BarState.Off)
            Button("点击更改alignListItem:${this.alignListItem.getValue()}").onClick(
                {
                => match (this.alignListItem) {
                    case ListItemAlign.Start => this.alignListItem = ListItemAlign.Center
                    case ListItemAlign.Center => this.alignListItem = ListItemAlign.End
                    case ListItemAlign.End => this.alignListItem = ListItemAlign.Start
                    case _ => return
                }
            })
        }.width(100.percent).height(100.percent).backgroundColor(0xDCDCDC).padding(top: 5.px)
    }
}
```

![list2](figures/list2.gif)