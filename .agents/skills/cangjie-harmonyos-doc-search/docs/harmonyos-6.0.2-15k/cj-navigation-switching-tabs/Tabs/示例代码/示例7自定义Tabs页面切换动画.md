### 示例7（自定义Tabs页面切换动画）

本示例通过customContentTransition实现了自定义Tabs页面的切换动画。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import std.collection.*
import ohos.state_macro_manage.*

class ItemType {
    public ItemType(public let text: String, public let backgroundColor: Color) {}
}

@Entry
@Component
class EntryView {
    @State
    var data: Array<ItemType> = [
        ItemType('Red', Color(0xff0000)),
        ItemType('Yellow', Color(0xFFBF00)),
        ItemType('Blue', Color(0x007DFF))
    ]
    @State
    var opacityList: ObservedArrayList<Float64> = ObservedArrayList<Float64>([1.0, 1.0, 1.0])
    @State
    var scaleList: ObservedArrayList<Float32> = ObservedArrayList<Float32>([1.0, 1.0, 1.0])

    var durationList: Array<Int32> = Array<Int32>()
    var timeoutList: Array<Int32> = Array<Int32>()
    var customContentTransition: (from: Int32, to: Int32) -> Option<TabContentAnimatedTransition> = {
        from: Int32, to: Int32 => Option.None
    }

    protected override func aboutToAppear() {
        this.durationList = [1000, 2000, 3000]
        this.timeoutList = [1000, 2000, 3000]
        this.customContentTransition = {
            from: Int32, to: Int32 =>
            AppLog.info("customContentTransition from:${from}, to:${to}")
            let tabContentAnimatedTransition = TabContentAnimatedTransition(
                timeout: this.timeoutList[Int64(from)],
                transition: {
                    proxy: TabContentTransitionProxy =>
                    AppLog.info("tabContentTransitionProxy proxy.from:${proxy.from}, proxy.to:${proxy.to}")
                    this.scaleList[Int64(from)] = 1.0
                    this.scaleList[Int64(to)] = 0.5
                    this.opacityList[Int64(from)] = 1.0
                    this.opacityList[Int64(to)] = 0.5
                    animateTo(
                        AnimateParam(duration: this.durationList[Int64(from)], onFinish: {=> proxy.finishTransition()}),
                        {
                            =>
                            this.scaleList[Int64(from)] = 0.5
                            this.scaleList[Int64(to)] = 1.0
                            this.opacityList[Int64(from)] = 0.5
                            this.opacityList[Int64(to)] = 1.0
                        }
                    )
                }
            )
            return Some(tabContentAnimatedTransition)
        }
    }

    func build() {
        Column() {
            Tabs() {
                ForEach(
                    this.data,
                    itemGeneratorFunc: {
                        item: ItemType, index: Int64 => TabContent() {}.tabBar(item.text).backgroundColor(
                            item.backgroundColor)
                                // 自定义动画变化透明度、缩放页面等
                                .opacity(this.opacityList[index]).scale(x: this.scaleList[index],
                            y: this.scaleList[index])
                    }
                )
            }.backgroundColor(0xf1f3f5).width(100.percent).height(500).customContentTransition(
                this.customContentTransition)
        }
    }
}
```

![tab](figures/tabsExample7.gif)