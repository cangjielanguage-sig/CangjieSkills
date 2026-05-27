### 示例2（Grid嵌套滚动）

nestedScroll和onScrollFrameBegin的使用。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import ohos.state_macro_manage.Entry
import ohos.state_macro_manage.Component
import ohos.state_macro_manage.State
import ohos.state_macro_manage.r
import ohos.base.*
import ohos.component.*
import ohos.state_manage.*
import ohos.state_macro_manage.*
import std.collection.{ArrayList, HashMap}

@Entry
@Component
class EntryView {
    @State
    var colors: Array<UInt32> = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F]
    @State
    var numbers: ArrayList<String> = ArrayList<String>()
    @State
    var translateY: Int64 = 0
    var scroller: Scroller = Scroller()
    var gridScroller: Scroller = Scroller()
    var touchDown: Bool = false
    var listTouchDown: Bool = false
    var scrolling: Bool = false

    protected override func aboutToAppear() {
        for (i in 1..100) {
            this.numbers.add("${i}")
        }
    }

    func build() {
        Stack() {
            Column() {
                Row() {
                    Text("Head")
                }

                Column() {
                    List(scroller: this.scroller) {
                        ListItem() {
                            Grid() {
                                GridItem() {
                                    Text("GoodsTypeList1")
                                }.backgroundColor(this.colors[0]).columnStart(0).columnEnd(1)

                                GridItem() {
                                    Text("GoodsTypeList2")
                                }.backgroundColor(this.colors[1]).columnStart(0).columnEnd(1)

                                GridItem() {
                                    Text("GoodsTypeList3")
                                }.backgroundColor(this.colors[2]).columnStart(0).columnEnd(1)

                                GridItem() {
                                    Text("GoodsTypeList4")
                                }.backgroundColor(this.colors[3]).columnStart(0).columnEnd(1)

                                GridItem() {
                                    Text("GoodsTypeList5")
                                }.backgroundColor(this.colors[4]).columnStart(0).columnEnd(1)
                            }.scrollBar(BarState.Off).columnsGap(15).rowsGap(10).rowsTemplate("1fr 1fr 1fr 1fr 1fr").
                                columnsTemplate("1fr").width(100.percent).height(200)
                        }

                        ListItem() {
                            Grid(this.gridScroller) {
                                ForEach(
                                    this.numbers,
                                    itemGeneratorFunc: {
                                        item: String, idx: Int64 => GridItem() {
                                            Text(item + "").fontSize(16).backgroundColor(0xF9CF93).width(100.percent).
                                                height(100.percent).textAlign(TextAlign.Center)
                                        }.width(100.percent).height(40).shadow(radius: 10, color: Color(0x909399),
                                            offsetX: 1, offsetY: 1).borderRadius(10).translate(x: 0, y: this.translateY)
                                    }
                                )
                            }.columnsTemplate("1fr 1fr").friction(0.3).columnsGap(15).rowsGap(10).scrollBar(
                                BarState.Off).width(100.percent).height(100.percent).layoutDirection(
                                GridDirection.Column).nestedScroll(
                                NestedScrollOptions(NestedScrollMode.PARENT_FIRST, NestedScrollMode.SELF_FIRST)).onTouch(
                                {
                                event => if (event.eventType.getValue() == TouchType.Down.getValue()) {
                                    this.listTouchDown = true
                                } else if (event.eventType.getValue() == TouchType.Up.getValue()) {
                                    this.listTouchDown = false
                                }
                            })
                        }
                    }.scrollBar(BarState.Off).edgeEffect(EdgeEffect.None).onTouch(
                        {
                        event => if (event.eventType.getValue() == TouchType.Down.getValue()) {
                            this.touchDown = true
                        } else if (event.eventType.getValue() == TouchType.Up.getValue()) {
                            this.touchDown = false
                        }
                    }).onScrollFrameBegin(
                        {
                            offset: Float64, state: ScrollState =>
                            if (this.scrolling && offset > 0.0) {
                                let newOffset = this.scroller.currentOffset().yOffset
                                if (newOffset >= 590.0) {
                                    this.gridScroller.scrollBy(xOffset: 0.0, yOffset: offset)
                                    return 0.0
                                } else if (newOffset + offset > 590.0) {
                                    this.gridScroller.scrollBy(xOffset: 0.0, yOffset: newOffset + offset - 590.0)
                                    return 590.0 - newOffset
                                }
                            }
                            return offset
                        }
                    ).onScrollStart({
                        => if (this.touchDown && !this.listTouchDown) {
                            this.scrolling = true
                        }
                    }).onScrollStop({
                        => this.scrolling = false
                    })
                }.width(100.percent).height(100.percent).padding(left: 10, right: 10)
            }