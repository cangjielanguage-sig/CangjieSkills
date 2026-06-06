### 示例9（自定义TabBar切换动画）

本示例通过onChange、onAnimationStart、onAnimationEnd、onGestureSwipe等接口实现了自定义TabBar的切换动画。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import std.collection.{HashMap}
import std.math.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var currentIndex: Int32 = 0
    @State
    var animationDuration: Int32 = 300
    @State
    var indicatorLeftMargin: Float64 = 0.0
    @State
    var indicatorWidth: Float64 = 0.0
    var tabsWidth: Float64 = 0.0
    var textInfos: Array<Array<Float64>> = Array(Int64(4), repeat: Array<Float64>())
    var isStartAnimateTo: Bool = false

    @Builder
    func tabBuilder(index: Int32, name: String) {
        Column() {
            Text(name).fontSize(16).fontColor(if (this.currentIndex == index) {
                0x007DFF
            } else {
                0x182431
            }).fontWeight(if (this.currentIndex == index) {
                FontWeight.W500
            } else {
                FontWeight.W400
            }).id(index.toString()).onAreaChange(
                {
                oldValue: Area, newValue: Area => this.textInfos[Int64(index)] = [newValue.globalPosition.x,
                    newValue.width]
            })
        }.width(100.percent)
    }

    func build() {
        Stack(Alignment.TopStart) {
            Tabs(BarPosition.Start) {
                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x00CB87)
                }.tabBar({=> bind(this.tabBuilder, this)(0, 'green')})

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x007DFF)
                }.tabBar({=> bind(this.tabBuilder, this)(1, 'blue')})

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0xFFBF00)
                }.tabBar({=> bind(this.tabBuilder, this)(2, 'yellow')})

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0xE67C92)
                }.tabBar({=> bind(this.tabBuilder, this)(3, 'pink')})
            }.onAreaChange(
                {
                    oldValue: Area, newValue: Area =>
                    this.tabsWidth = newValue.width
                    if (!this.isStartAnimateTo) {
                        this.setIndicatorAttr(this.textInfos[Int64(this.currentIndex)][0],
                            this.textInfos[Int64(this.currentIndex)][1])
                    }
                }
            ).barWidth(100.percent).barHeight(56).width(100.percent).height(296).backgroundColor(0xF1F3F5).
                animationDuration(this.animationDuration).onChange({
                index: Int32 => this.currentIndex = index // 监听索引index的变化，实现页签内容的切换。
            }).onAnimationStart(
                {
                    index: Int32, targetIndex: Int32, event: TabsAnimationEvent =>
                    // 切换动画开始时触发该回调。下划线跟着页面一起滑动，同时宽度渐变。
                    this.currentIndex = targetIndex
                    this.startAnimateTo(this.animationDuration, this.textInfos[Int64(targetIndex)][0],
                        this.textInfos[Int64(targetIndex)][1])
                }
            ).onAnimationEnd(
                {
                    index: Int32, event: TabsAnimationEvent =>
                    // 切换动画结束时触发该回调。下划线动画停止。
                    let currentIndicatorInfo = this.getCurrentIndicatorInfo(index, event)
                    this.startAnimateTo(0, currentIndicatorInfo["left"], currentIndicatorInfo["width"])
                }
            ).onGestureSwipe(
                {
                    index: Int32, event: TabsAnimationEvent =>
                    // 在页面跟手滑动过程中，逐帧触发该回调。
                    let currentIndicatorInfo = this.getCurrentIndicatorInfo(index, event)
                    this.currentIndex = Int32(currentIndicatorInfo["index"])
                    this.setIndicatorAttr(currentIndicatorInfo["left"], currentIndicatorInfo["width"])
                }
            )

            Column().height(2).width(this.indicatorWidth).margin(left: this.indicatorLeftMargin, top: 48.0).
                backgroundColor(0x007DFF)
        }.width(100.percent)
    }

    func getCurrentIndex(swipeRatio: Float64, nextIndex: Int32, index: Int32): Int32 {
        if (swipeRatio > 0.5) {
            return nextIndex
        }
        return index
    }