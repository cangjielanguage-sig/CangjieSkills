### 示例4（设置TabBar叠加在TabContent内容上）

本示例通过barOverlap实现了TabBar是否背后变模糊并叠加在TabContent之上。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import std.collection.*
import kit.LocalizationKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    var controller: TabsController = TabsController()
    @State
    var barOverlap: Bool = true
    @State
    var barBackgroundColor: UInt32 = 0x88888888

    func getMarginTop(): Length {
        if (this.barOverlap) {
            return 56.vp
        }
        return 0.vp
    }

    func build() {
        Column() {
            Button("barOverlap变化").width(100.percent).margin(bottom: 12.vp).onClick(
                {
                => if (this.barOverlap) {
                    this.barOverlap = false
                } else {
                    this.barOverlap = true
                }
            })

            Tabs(BarPosition.Start, this.controller, 0) {
                TabContent() {
                    Column() {
                        Text("barOverlap ${this.barOverlap}").fontSize(16).margin(top: this.getMarginTop())
                        Text("barBackgroundColor ${this.barBackgroundColor}").fontSize(16)
                    }.width(100.percent).height(100.percent).backgroundColor(0xE67C92)
                }.tabBar(icon: @r(app.media.startIcon), text: "1")

                TabContent() {
                    Column() {
                        Text("barOverlap ${this.barOverlap}").fontSize(16).margin(top: this.getMarginTop())
                        Text("barBackgroundColor ${this.barBackgroundColor}").fontSize(16)
                    }.width(100.percent).height(100.percent).backgroundColor(0xFFBF00)
                }.tabBar(icon: @r(app.media.startIcon), text: "2")

                TabContent() {
                    Column() {
                        Text("barOverlap ${this.barOverlap}").fontSize(16).margin(top: this.getMarginTop())
                        Text("barBackgroundColor ${this.barBackgroundColor}").fontSize(16)
                    }.width(100.percent).height(100.percent).backgroundColor(0x00CB87)
                }.tabBar(icon: @r(app.media.startIcon), text: "3")
            }.vertical(false).barMode(BarMode.Fixed).height(60.percent).barOverlap(this.barOverlap).scrollable(true).
                animationDuration(10).barBackgroundColor(this.barBackgroundColor)
        }.height(500).padding(top: 24.vp, left: 24.vp, right: 24.vp)
    }
}
```

![tab](figures/tabsExample4.gif)