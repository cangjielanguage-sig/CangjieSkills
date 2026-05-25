### 示例3（设置TabBar渐隐）

本示例通过fadingEdge实现了切换子页签渐隐和不渐隐

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import std.collection.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var message: String = 'Hello World'
    private var controller: TabsController = TabsController()
    private var controller1: TabsController = TabsController()
    @State
    var selfFadingFade: Bool = true

    func build() {
        Column() {
            Button('子页签设置渐隐').id("fadingEdgeTrue").width(100.percent).margin(bottom: 12.vp).onClick(
                {
                => this.selfFadingFade = true
            })

            Button('子页签设置不渐隐').id("fadingEdgeFalse").width(100.percent).margin(bottom: 12.vp).onClick(
                {
                => this.selfFadingFade = false
            })

            Tabs(this.controller) {
                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0xE67C92)
                }.tabBar('pink')

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0xFFBF00)
                }.tabBar('yellow')

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x007DFF)
                }.tabBar('blue')

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x00CB87)
                }.tabBar('green')

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x00CB87)
                }.tabBar('green')

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x00CB87)
                }.tabBar('green')

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x00CB87)
                }.tabBar('green')

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x00CB87)
                }.tabBar('green')
            }.vertical(false).scrollable(true).barMode(BarMode.Scrollable).barPosition(BarPosition.End).barHeight(80).
                animationDuration(400).onChange({
                index: Int32 => AppLog.info("${index}")
            }).fadingEdge(this.selfFadingFade).height(30.percent).width(100.percent)

            Tabs(BarPosition.Start, this.controller1) {
                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0xE67C92)
                }.tabBar('pink')

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0xFFBF00)
                }.tabBar('yellow')

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x007DFF)
                }.tabBar('blue')

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x00CB87)
                }.tabBar('green')

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x00CB87)
                }.tabBar('green')

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x00CB87)
                }.tabBar('green')
            }.vertical(true).scrollable(true).barMode(BarMode.Scrollable).barHeight(200).barWidth(80).animationDuration(
                400).onChange({
                index: Int32 => AppLog.info("${index}")
            }).fadingEdge(this.selfFadingFade).height(30.percent).width(100.percent)
        }.padding(top: 24.vp, left: 24.vp, right: 24.vp)
    }
}
```

![tab](figures/tabsExample3.gif)