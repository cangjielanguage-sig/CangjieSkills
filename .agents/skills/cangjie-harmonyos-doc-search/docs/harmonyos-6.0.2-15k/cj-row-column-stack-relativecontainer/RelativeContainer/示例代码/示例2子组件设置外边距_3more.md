### 示例2（子组件设置外边距）

本示例展示了容器内子组件设置外边距的用法。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.*

@Entry
@Component
class EntryView {
    func build() {
        Row() {
            RelativeContainer() {
                Row().width(100).height(100).backgroundColor(0xff3333).alignRules(
                    AlignRuleOption(
                        top: VerticalAnchor("__container__", VerticalAlign.Top),
                        left: HorizontalAnchor("__container__", HorizontalAlign.Start)
                    )
                ).id("row1").margin(10)
                Row().width(100).height(100).backgroundColor(0xFFCC00).alignRules(
                    AlignRuleOption(
                        top: VerticalAnchor("row1", VerticalAlign.Top),
                        left: HorizontalAnchor("row1", HorizontalAlign.End)
                    )
                ).id("row2")
                Row().height(100).width(100).backgroundColor(0xFF6633).alignRules(
                    AlignRuleOption(
                        top: VerticalAnchor("row1", VerticalAlign.Bottom),
                        left: HorizontalAnchor("row1", HorizontalAlign.Start)
                    )
                ).id("row3")
                Row().width(100).height(100).backgroundColor(0xFF9966).alignRules(
                    AlignRuleOption(
                        top: VerticalAnchor("row2", VerticalAlign.Bottom),
                        left: HorizontalAnchor("row3", HorizontalAlign.End),
                    )
                ).id("row4").margin(10)
            }.width(300).height(300).margin(left: 50.vp).border(width: 2.vp, color: Color(0x6699ff))
        }.height(100.percent)
    }
}
```

![relativecontainer2](figures/relativecontainer2.jpg)

### 示例3（设置偏移）

本示例通过[bias](cj-universal-attribute-location.md#class-bias)实现了子组件的位置在竖直方向的两个锚点间偏移的效果。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.*

@Entry
@Component
class EntryView {
    func build() {
        Row() {
            RelativeContainer() {
                Row().width(100).height(100).backgroundColor(0xff3333).alignRules(
                    AlignRuleOption(
                        top: VerticalAnchor("__container__", VerticalAlign.Top),
                        bottom: VerticalAnchor("__container__", VerticalAlign.Bottom),
                        left: HorizontalAnchor("__container__", HorizontalAlign.Start),
                        right: HorizontalAnchor("__container__", HorizontalAlign.End),
                        bias: Bias(vertical: 0.3)
                    )
                ).id("row1")
            }.width(300).height(300).margin(left: 50.vp).border(width: 2.vp, color: Color(0x6699ff))
        }.height(100.percent)
    }
}
```

![relativecontainer4](figures/relativecontainer3.jpg)

### 示例4（设置辅助线）

本示例展示了相对布局组件通过[guideLine](#func-guidelinearrayguidelinestyle)接口设置辅助线，子组件以辅助线为锚点的功能。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.*

@Entry
@Component
class EntryView {
    func build() {
        Row() {
            RelativeContainer() {
                Row().width(100).height(100).backgroundColor(0xff3333).alignRules(
                    AlignRuleOption(
                        top: VerticalAnchor("guideline2", VerticalAlign.Top),
                        left: HorizontalAnchor("guideline1", HorizontalAlign.End),
                    )
                ).id("row1")
            }.width(300).height(300).margin(left: 50.vp).border(width: 2.vp, color: Color(0x6699ff)).guideLine(
                [GuideLineStyle("guideline1", Axis.Vertical, GuideLinePosition(start: 50.vp)),
                GuideLineStyle("guideline2", Axis.Horizontal, GuideLinePosition(start: 50.vp))])
        }.height(100.percent)
    }
}
```

![relativecontainer5](figures/relativecontainer4.jpg)