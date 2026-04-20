### 示例5（设置TabBar栅格化可见区域）

本示例通过barGridAlign实现了以栅格化方式设置TabBar的可见区域。

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
    var gridMargin: Int64 = 10
    @State
    var gridGutter: Int64 = 10
    @State
    var sm: Int32 = -2
    @State
    var clickedContent: String = "";

    func build() {
        Column() {
            Row() {
                Button("gridMargin+10 ${this.gridMargin}").id("gridMarginAdd").width(47.percent).height(50).margin(
                    top: 5).onClick({
                    => this.gridMargin += 10
                }).margin(right: 6.percent, bottom: 12.vp)
                Button("gridMargin-10 ${this.gridMargin}").id("gridMarginSub").width(47.percent).height(50).margin(
                    top: 5).onClick({
                    => this.gridMargin -= 10
                }).margin(bottom: 12.vp)
            }
            Row() {
                Button("gridGutter+10 ${this.gridGutter}").id("gridGutterAdd").width(47.percent).height(50).margin(
                    top: 5).onClick({
                    => this.gridGutter += 10
                }).margin(right: 6.percent, bottom: 12.vp)
                Button("gridGutter-10 ${this.gridGutter}").id("gridGutterSub").width(47.percent).height(50).margin(
                    top: 5).onClick({
                    => this.gridGutter -= 10
                }).margin(bottom: 12.vp)
            }
            Row() {
                Button("sm+2 ${this.sm}").id("smAdd").width(47.percent).height(50).margin(top: 5).onClick(
                    {
                    => this.sm += 2
                }).margin(right: 6.percent, bottom: 12.vp)
                Button("sm-2 ${this.sm}").id("smSub").width(47.percent).height(50).margin(top: 5).onClick(
                    {
                    => this.sm -= 2
                }).margin(bottom: 12.vp)
            }

            Text("点击内容:${this.clickedContent}").width(100.percent).height(200).margin(top: 5)

            Tabs(BarPosition.End, this.controller) {
                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0xE67C92)
                }.id("TabContent0").tabBar(icon: @r(app.media.startIcon), text: "1")

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x00CB87)
                }.id("TabContent1").tabBar(icon: @r(app.media.startIcon), text: "2")

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x007DFF)
                }.id("TabContent2").tabBar(icon: @r(app.media.startIcon), text: "3")
            }.width(350.vp).animationDuration(300).height(60.percent).barGridAlign(
                BarGridColumnOptions(sm: this.sm, margin: this.gridMargin, gutter: this.gridGutter)).backgroundColor(
                0xf1f3f5).onTabBarClick({
                index: Int32 => this.clickedContent += "now index ${index} is clicked\n"
            })
        }.width(100.percent).height(500).margin(top: 5).padding(10.vp)
    }
}
```

![tab](figures/tabsExample5.gif)