## 示例代码

示例效果请以真机为准，系统路由表不支持预览器，跨平台以及模拟器。

### 示例1（Navigation页面布局）

该示例主要演示Navigation页面的布局包括标题栏(title)，菜单栏(menus)，内容区和工具栏(toolbarConfiguration)。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import ohos.state_macro_manage.*
import ohos.resource_manager.__GenerateResource__
import ohos.hilog.Hilog
import ohos.component.*
import ohos.base.*
import ohos.state_manage.*

@Entry
@Component
class EntryView {
    private var arr: Array<Int> = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    private var toolconfig: Array<ToolBarItem> = [ToolBarItem(value: "111"), ToolBarItem(value: "222")]
    @State
    var currentIndex: Int = 0
    var menutest: Array<NavigationMenuItem> = [NavigationMenuItem(value: "menus", icon: "123")]
    var titleoption: NavigationTitleOptions = NavigationTitleOptions(backgroundColor: Color.RED)

    @Builder
    func TextBuilder() {
        Text("I am description").fontSize(20).textAlign(TextAlign.Center).width(80.percent)
    }

    @Builder
    func NavigationTitle() {
        Column() {
            Text("Title").fontColor(Color.BLACK).fontSize(30).lineHeight(41).fontWeight(FontWeight.W700)
            Text("subTitle").fontColor(Color.BLACK).fontSize(14).lineHeight(19).opacity(0.4).margin(top: 2, bottom: 20)
        }.alignItems(HorizontalAlign.Start)
    }

    @Builder
    func NavigationMenus() {
        Row() {
            Image(@r(app.media.startIcon)).width(24).height(24).backgroundColor(Color.RED)
            Image(@r(app.media.startIcon)).width(24).height(24).margin(left: 24).backgroundColor(Color.BLUE)
            Image(@r(app.media.startIcon)).height(24).width(24).margin(left: 24).backgroundColor(Color.PINK)
        }
    }

    func build() {
        Column() {
            Navigation() {
                TextInput(placeholder: "search...").width(90.percent).height(40).backgroundColor(Color.WHITE).margin(
                    top: 8)

                List(space: 12, initialIndex: 0) {
                    ForEach(
                        this.arr,
                        {
                            item: Int, index: Int => ListItem() {
                                Text(" " + item.toString()).width(90.percent).height(72).backgroundColor(Color.WHITE).
                                    borderRadius(24).fontSize(16).fontWeight(FontWeight.W500).textAlign(
                                    TextAlign.Center)
                            }
                        }
                    )
                }.height(324).width(100.percent).margin(top: 12, left: 10.percent)
            }.title({=> bind(this.NavigationTitle, this)()}).menus({=> bind(this.NavigationMenus, this)()}).titleMode(
                NavigationTitleMode.Full).hideBackButton(false).toolbarConfiguration(
                this.toolconfig,
                options: NavigationToolbarOptions(backgroundColor: Color.BLUE, backgroundBlurStyle: BlurStyle.Thick,
                    barStyle: BarStyle.Stack)
            ).navBarPosition(NavBarPosition.Start).mode(NavigationMode.Auto).backButtonIcon("backbutton").titleMode(
                NavigationTitleMode.Free).systemBarStyle(Color.BLUE)
        }.width(100.percent).height(100.percent).backgroundColor(Color.GRAY)
    }
}
```

![navigation](figures/navigation1.png)