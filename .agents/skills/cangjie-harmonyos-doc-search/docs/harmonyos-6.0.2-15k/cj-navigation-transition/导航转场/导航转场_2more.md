# 导航转场

导航转场是页面的路由转场方式，也就是一个界面消失，另外一个界面出现的动画效果。

导航转场推荐使用[Navigation](../../API_Reference/source_zh_cn/arkui-cj/cj-navigation-switching-navigation.md)组件实现，可搭配[NavDestination](../../API_Reference/source_zh_cn/arkui-cj/cj-navigation-switching-navdestination.md)组件实现导航功能。

## 创建导航页

实现步骤为：

1. 使用Navigation创建导航主页，并创建路由栈NavPathStack以此来实现不同页面之间的跳转。

2. 在Navigation中增加List组件，来定义导航主页中不同的一级界面。

3. 在List内的组件添加onClick方法，并在其中使用路由栈NavPathStack的pushPath方法，使组件可以在点击之后从当前页面跳转到输入参数name在路由表内对应的页面。

<!-- run -navigation -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Builder
func pageMap(name: String) {
    if (name == "PageOne") {
        PageOne()
    } else {
        PageTwo()
    }
}

@Entry
@Component
class EntryView {
    @Provide
    var pathInfos: NavPathStack = NavPathStack()
    @State
    var listArray1: Array<String> = ['WLAN', 'Bluetooth']
    @State
    var listArray2: Array<String> = ['Personal Hotpot', 'Connect & Share']
    func build() {
        Column() {
            Navigation(this.pathInfos) {
                // 通过List定义导航的一级界面
                Search(placeholder: '输入关键字搜索').width(90.percent).height(40).margin(top: 40, bottom: 15)

                List(initialIndex: 0) {
                    ForEach(
                        this.listArray1,
                        itemGeneratorFunc: {
                            item: String, _: Int64 => ListItem() {
                                Row() {
                                    Row() {
                                        Text('${item.split("")[0]}').fontColor(Color.WHITE).fontSize(14).fontWeight(
                                            FontWeight.Bold)
                                    }.width(30).height(30).backgroundColor(Color.GREY).margin(right: 20).borderRadius(
                                        20).justifyContent(FlexAlign.Center)

                                    Column() {
                                        Text(item).fontSize(16).margin(5)
                                    }.alignItems(HorizontalAlign.Start)

                                    Blank()

                                    Row().width(12).height(12).margin(15).border(width: 2.px, color: 0xCCCCCC).rotate(
                                        angle: 45.0)
                                }.borderRadius(15).shadow(radius: 100, color: 0xededed).width(90.percent).alignItems(
                                    VerticalAlign.Center).padding(left: 15, top: 15, bottom: 15).backgroundColor(
                                    Color.WHITE)
                            }.width(100.percent).margin(top: 12).onClick(
                                {
                                evt => this.pathInfos.pushPath(NavPathInfo('PageOne', '详情页面参数')) // 将name指定的NaviDestination页面信息入栈,传递的参数为param
                            })
                        }
                    )
                    ForEach(
                        this.listArray2,
                        itemGeneratorFunc: {
                            item: String, _: Int64 => ListItem() {
                                Row() {
                                    Row() {
                                        Text('${item.split("")[0]}').fontColor(Color.WHITE).fontSize(14).fontWeight(
                                            FontWeight.Bold)
                                    }.width(30).height(30).backgroundColor(Color.GREY).margin(right: 20).borderRadius(
                                        20).justifyContent(FlexAlign.Center)

                                    Column() {
                                        Text(item).fontSize(16).margin(5)
                                    }.alignItems(HorizontalAlign.Start)
                                    Blank()
                                    Row().width(12).height(12).margin(15).border(width: 2.px, color: 0xCCCCCC).rotate(
                                        angle: 45.0)
                                }.borderRadius(15).shadow(radius: 100, color: 0xededed).width(90.percent).alignItems(
                                    VerticalAlign.Center).padding(left: 15, top: 15, bottom: 15).backgroundColor(
                                    Color.WHITE)
                            }.width(100.percent).margin(top: 12).onClick(
                                {
                                evt => this.pathInfos.pushPath(NavPathInfo('PageTwo', '详情页面参数')) // 将name指定的NaviDestination页面信息入栈,传递的参数为param
                            })
                        }
                    )
                }.listDirection(Axis.Vertical).edgeEffect(EdgeEffect.Spring).sticky(StickyStyle.Header).chainAnimation(
                    false).width(100.percent).height(100.percent).padding(top: 10)
            }.navDestination(bind<String>(pageMap, this)).width(100.percent).height(100.percent)
        }.size(width: 100.percent, height: 100.percent).backgroundColor(Color.WHITE)
    }
}
```