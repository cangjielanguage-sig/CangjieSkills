### 示例13（设置TabBar的布局模式）

本示例通过barMode分别实现了页签均分布局和以实际长度布局，且展示了当页签布局长度之和超过了TabBar总长度后可滑动的效果。

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
    var text: String = "文本"
    @State
    var barMode: BarMode = BarMode.Fixed

    func build() {
        Column() {
            Row() {
                Button("文本增加 ").width(47.percent).height(50).onClick({event => this.text += "文本"}).margin(
                    right: 6.percent, bottom: 12)

                Button("文本重置").width(47.percent).height(50).onClick({event => this.text = "文本"}).margin(
                    bottom: 12)
            }

            Row() {
                Button("BarMode.Fixed").width(47.percent).height(50).onClick({event => this.barMode = BarMode.Fixed}).
                    margin(right: 6.percent, bottom: 12)

                Button("BarMode.Scrollable").width(47.percent).height(50).onClick(
                    {event => this.barMode = BarMode.Scrollable}).margin(bottom: 12)
            }
            Tabs() {
                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(Color.PINK)
                }.tabBar(SubTabBarStyle.of(this.text))

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(Color.GREEN)
                }.tabBar(SubTabBarStyle.of(this.text))

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(Color.BLUE)
                }.tabBar(SubTabBarStyle.of(this.text))
            }.height(60.percent).backgroundColor(0xf1f3f5).barMode(this.barMode)
        }.width(100.percent).height(500).padding(24)
    }
}
```

![tab](figures/tabsExample13.gif)

### 示例14（设置边缘滑动效果）

本示例通过edgeEffect实现了不同的边缘滑动效果。

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
    var edgeEffect: EdgeEffect = EdgeEffect.Spring

    func build() {
        Column() {
            Tabs() {
                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x00CB87)
                }.tabBar('green')

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x007DFF)
                }.tabBar('blue')

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0xFFBF00)
                }.tabBar('yellow')

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0xE67C92)
                }.tabBar('pink')
            }.width(360).height(296).margin(top: 52).backgroundColor(0xF1F3F5).edgeEffect(this.edgeEffect)

            Button('EdgeEffect.Spring').width(50.percent).margin(top: 20).onClick(
                {event => this.edgeEffect = EdgeEffect.Spring})

            Button('EdgeEffect.Fade').width(50.percent).margin(top: 20).onClick(
                {event => this.edgeEffect = EdgeEffect.Fade})

            Button('EdgeEffect.None').width(50.percent).margin(top: 20).onClick(
                {event => this.edgeEffect = EdgeEffect.None})
        }.width(100.percent)
    }
}
```

![tab](figures/tabsExample14.gif)