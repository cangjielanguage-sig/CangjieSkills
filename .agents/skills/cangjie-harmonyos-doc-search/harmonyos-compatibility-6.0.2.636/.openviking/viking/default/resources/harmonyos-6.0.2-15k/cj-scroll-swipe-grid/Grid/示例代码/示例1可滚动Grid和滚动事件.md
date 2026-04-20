### 示例1（可滚动Grid和滚动事件）

可滚动Grid，包括所有滚动属性和事件。

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
    var numbers: Array<String> = ['0', '1', '2', '3', '4']
    var scroller: Scroller = Scroller()
    @State
    var gridPosition: Int64 = 0 //0代表滚动到grid顶部，1代表中间值，2代表滚动到grid底部。

    func build() {
        Column(5) {
            Text("scroll").fontColor(0xCCCCCC).fontSize(9).width(90.percent)
            Grid(this.scroller) {
                ForEach(
                    this.numbers,
                    itemGeneratorFunc: {
                        day: String, idx: Int64 => ForEach(
                            this.numbers,
                            itemGeneratorFunc: {
                                day: String, idx: Int64 => GridItem() {
                                    Text(day).fontSize(16).backgroundColor(0xF9CF93).width(100.percent).height(80).
                                        textAlign(TextAlign.Center)
                                }
                            }
                        )
                    }
                )
            }.columnsTemplate("1fr 1fr 1fr 1fr 1fr").columnsGap(10).rowsGap(10).friction(0.6).enableScrollInteraction(
                true).supportAnimation(false).multiSelectable(false).edgeEffect(EdgeEffect.Spring).scrollBar(
                BarState.On).scrollBarColor(Color.GRAY).scrollBarWidth(4).width(90.percent).backgroundColor(0xFAEEE0).
                height(300).onScrollIndex(
                {
                    first: UInt32, last: UInt32 =>
                    AppLog.info(first.toString())
                    AppLog.info(last.toString())
                }
            ).onScrollBarUpdate(
                {
                    index: Int32, offset: Float64 =>
                    AppLog.info(
                        "XXX" + 'Grid onScrollBarUpdate,index : ' + index.toString() + ",offset" + offset.toString())
                    return ComputedBarAttribute(Float64((index / 5) * (80 + 10)) - offset, Float64(80 * 5 + 10 * 4))
                }
            ).onScrollStart({
                => AppLog.info("XXX" + "Grid onScrollStart")
            }).onScrollStop({
                => AppLog.info("XXX" + "Grid onScrollStop")
            }).onReachStart(
                {
                    =>
                    this.gridPosition = 0
                    AppLog.info("XXX" + "Grid onReachStart")
                }
            ).onReachEnd(
                {
                    =>
                    this.gridPosition = 2
                    AppLog.info("XXX" + "Grid onReachEnd")
                }
            )

            Button('next page').onClick({
                => // 点击后滑到下一页
                this.scroller.scrollPage(true)
            })
        }.width(100.percent).margin(top: 5)
    }
}
```

![griditem](figures/grid1.gif)