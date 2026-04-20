## 示例代码1（设置scroller控制器）

该示例展示了Scroll组件部分属性和scroller控制器的使用。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.ArrayList

@Entry
@Component
class EntryView {
    let scroller = Scroller()
    var arr: ArrayList<String> = ArrayList(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

    func build() {
        Stack(Alignment.TopStart) {
            Scroll(this.scroller) {
                Column {
                    ForEach(
                        this.arr,
                        itemGeneratorFunc: {
                            item: String, idx: Int64 => Text(item).width(90.percent).height(150).backgroundColor(
                                0xFFFFFF).borderRadius(15).textAlign(TextAlign.Center).fontSize(16).margin(top: 10)
                        }
                    )
                }
            }.scrollable(ScrollDirection.Vertical) // 滚动方向纵向
                .scrollBar(BarState.On) // 滚动条常驻显示
                .scrollBarColor(Color.GRAY) // 滚动条颜色
                .scrollBarWidth(
                10.px) // 滚动条宽度
                    .friction(0.6).edgeEffect(EdgeEffect.None).onScrollEdge(
                {
                edge => match (edge) {
                    case Edge.Top => nativeLog("Top")
                    case Edge.Bottom => nativeLog("Bottom")
                    case _ => nativeLog("None")
                }
            }).onScrollStop({
                => nativeLog("Scroll Stop")
            })

            Button("scroll 150").onClick({
                evt => // 点击后下滑指定距离150.0vp
                this.scroller.scrollBy(xOffset: 0, yOffset: 150)
            }).margin(top: 10, left: 20)

            Button("scroll 100").onClick(
                {
                    evt => //点击后滑动到指定位置，即下滑100.0vp的距离
                    nativeLog("current offset ${this.scroller.currentOffset().yOffset}")
                    nativeLog("CALCULATE offset ${this.scroller.currentOffset().yOffset + 100.0}")
                    let curyOffset = this.scroller.currentOffset().yOffset
                    this.scroller.scrollTo(xOffset: 0.vp, yOffset: (curyOffset + 100.0).vp, duration: 0.0,
                        curve: Curve.Ease)
                }
            ).margin(top: 60, left: 20)

            Button("back top").onClick({
                evt => // 点击后回到顶部
                this.scroller.scrollEdge(Edge.Top)
            }).margin(top: 110, left: 20)

            Button("next page").onClick({
                evt => // 点击后滑到下一页
                this.scroller.scrollPage(true, animation: false)
            }).margin(top: 160, left: 20)

            Button("fling -3000").onClick({
                evt => // 点击后触发初始速度为-3000vp/s的惯性滚动
                this.scroller.fling(-3000)
            }).margin(top: 210, left: 20)

            Button("next page slowly").onClick({
                evt => // 点击后滑到下一页，滑动过程开启动画
                this.scroller.scrollPage(true, animation: true)
            }).margin(top: 260, left: 20)
        }.width(100.percent).height(100.percent).backgroundColor(0xDCDCDC)
    }
}
```

![scroll1](./figures/scroll1.gif)