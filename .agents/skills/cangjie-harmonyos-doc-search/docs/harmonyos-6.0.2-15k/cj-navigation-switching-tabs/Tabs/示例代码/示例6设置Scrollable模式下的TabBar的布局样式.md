### 示例6（设置Scrollable模式下的TabBar的布局样式）

本示例实现了barMode的ScrollableBarModeOptions参数，该参数仅在Scrollable模式下有效。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import std.collection.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    var controller: TabsController = TabsController()
    @State
    var scrollMargin: Int64 = 0
    @State
    var layoutStyle: LayoutStyle = LayoutStyle.ALWAYS_CENTER
    @State
    var text: String = "文本"

    func build() {
        Column() {
            Row() {
                Button("scrollMargin+10 ${this.scrollMargin}").width(47.percent).height(50).margin(top: 5).onClick(
                    {
                    => this.scrollMargin += 10
                }).margin(right: 6.percent, bottom: 12.vp)
                Button("scrollMargin-10 ${this.scrollMargin}").width(47.percent).height(50).onClick(
                    {
                    => this.scrollMargin -= 10
                }).margin(bottom: 12.vp)
            }

            Row() {
                Button("文本增加").width(47.percent).height(50).margin(top: 5).onClick({
                    => this.text += '文本增加'
                }).margin(right: 6.percent, bottom: 12.vp)
                Button("文本重置").width(47.percent).height(50).margin(top: 5).onClick({
                    => this.text = "文本"
                }).margin(bottom: 12.vp)
            }

            Row() {
                Button("layoutStyle.ALWAYS_CENTER").width(100.percent).height(50).margin(top: 5).fontSize(15).onClick(
                    {
                    => this.layoutStyle = LayoutStyle.ALWAYS_CENTER
                }).margin(bottom: 12.vp)
            }

            Row() {
                Button("layoutStyle.ALWAYS_AVERAGE_SPLIT").width(100.percent).height(50).margin(top: 5).fontSize(15).
                    onClick({
                    => this.layoutStyle = LayoutStyle.ALWAYS_AVERAGE_SPLIT
                }).margin(bottom: 12.vp)
            }

            Row() {
                Button("layoutStyle.SPACE_BETWEEN_OR_CENTER").width(100.percent).height(50).margin(top: 5).fontSize(15).
                    onClick({
                    => this.layoutStyle = LayoutStyle.SPACE_BETWEEN_OR_CENTER
                }).margin(bottom: 12.vp)
            }

            Tabs(BarPosition.End, this.controller) {
                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0xE67C92)
                }.tabBar(this.text)

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x00CB87)
                }.tabBar(this.text)

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x007DFF)
                }.tabBar(this.text)
            }.animationDuration(300).height(60.percent).backgroundColor(0xf1f3f5).barMode(BarMode.Scrollable,
                ScrollableBarModeOptions(margin: this.scrollMargin, nonScrollableLayoutStyle: this.layoutStyle))
        }.width(100.percent).height(500).margin(top: 5).padding(24.vp)
    }
}
```

![tab](figures/tabsExample6.gif)