### 示例10（预加载子节点）

本示例通过preloadItems接口实现了预加载指定子节点。

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
    var currentIndex: Int32 = 1
    var tabsController: TabsController = TabsController()

    func build() {
        Column() {
            Tabs(this.tabsController, this.currentIndex) {
                TabContent() {
                    MyComponent(color: 0x00CB87)
                }.tabBar('green')

                TabContent() {
                    MyComponent(color: 0x007DFF)
                }.tabBar('blue')

                TabContent() {
                    MyComponent(color: 0xFFBF00)
                }.tabBar('yellow')

                TabContent() {
                    MyComponent(color: 0xE67C92)
                }.tabBar('pink')
            }.height(60.percent).width(100.percent).backgroundColor(0xF1F3F5).onChange(
                {
                index: Int32 => this.currentIndex = index
            })

            Button('preload items: [0, 2, 3]').margin(5).onClick(
                {
                    =>
                    // 预加载第0、2、3个子节点，提高滑动或点击切换至这些节点时的性能
                    AppLog.info('preloadItems start')
                    this.tabsController.preloadItems([0, 2, 3])
                }
            )
        }
    }
}

let colorIndex = HashMap<UInt32, Int32>([(0x00CB87, 0), (0x007DFF, 1), (0xFFBF00, 2), (0xE67C92, 3)])

@Component
class MyComponent {
    var color: UInt32

    protected override func aboutToAppear() {
        AppLog.info('aboutToAppear index:${colorIndex.get(this.color)}')
    }

    protected override func aboutToDisappear() {
        AppLog.info('aboutToDisappear index:${colorIndex.get(this.color)}')
    }

    func build() {
        Column().width(100.percent).height(100.percent).backgroundColor(this.color)
    }
}
```

### 示例11（设置TabBar平移距离和不透明度）

本示例通过setTabBarTranslate、setTabBarOpacity等接口设置了TabBar的平移距离和不透明度。

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

    func build() {
        Column() {
            Button('设置TabBar的平移距离').margin(top: 20).onClick(
                {
                => this.controller.setTabBarTranslate(TranslateOptions(x: (-20).vp, y: (-20).vp))
            })

            Button('设置TabBar的透明度').margin(top: 20).onClick({
                => this.controller.setTabBarOpacity(0.5)
            })

            Tabs(BarPosition.End, this.controller) {
                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x00CB87)
                }.tabBar(icon: @r(app.media.startIcon), text: 'green')

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0x007DFF)
                }.tabBar(icon: @r(app.media.startIcon), text: 'blue')

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0xFFBF00)
                }.tabBar(icon: @r(app.media.startIcon), text: 'yellow')

                TabContent() {
                    Column().width(100.percent).height(100.percent).backgroundColor(0xE67C92)
                }.tabBar(icon: @r(app.media.startIcon), text: 'pink')
            }.width(100.percent).height(500).margin(top: 20).barBackgroundColor(0xFFF1F3F5)
        }.width(100.percent)
    }
}
```

![tab](figures/tabsExample11.gif)