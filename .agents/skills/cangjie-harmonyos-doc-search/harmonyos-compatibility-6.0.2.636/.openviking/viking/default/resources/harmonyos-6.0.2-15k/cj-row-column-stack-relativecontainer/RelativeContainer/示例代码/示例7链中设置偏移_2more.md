### 示例7（链中设置偏移）

本示例通过[chainMode](cj-universal-attribute-location.md#func-chainmodeaxis-chainstyle)和[bias](cj-universal-attribute-location.md#class-bias)接口实现了水平方向的带偏移的[PACKED链](cj-universal-attribute-location.md#enum-chainstyle)。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Row() {
            RelativeContainer() {
                Row() {
                    Text('row1')
                }.justifyContent(FlexAlign.Center).width(80).height(80).backgroundColor(0xa3cf62).alignRules(
                    AlignRuleOption(
                        left: HorizontalAnchor("__container__", HorizontalAlign.Start),
                        right: HorizontalAnchor("row2", HorizontalAlign.Start),
                        center: VerticalAnchor("__container__", VerticalAlign.Center),
                        bias: Bias(horizontal: 0.0)
                    )
                ).id("row1").chainMode(Axis.Horizontal, ChainStyle.PACKED)

                Row() {
                    Text('row2')
                }.justifyContent(FlexAlign.Center).width(80).height(80).backgroundColor(0x00ae9d).alignRules(
                    AlignRuleOption(
                        left: HorizontalAnchor("row1", HorizontalAlign.End),
                        right: HorizontalAnchor("row3", HorizontalAlign.Start),
                        top: VerticalAnchor("row1", VerticalAlign.Top),
                    )
                ).id("row2")

                Row() {
                    Text('row3')
                }.justifyContent(FlexAlign.Center).width(80).height(80).backgroundColor(0x0a59f7).alignRules(
                    AlignRuleOption(
                        left: HorizontalAnchor("row2", HorizontalAlign.End),
                        right: HorizontalAnchor("__container__", HorizontalAlign.End),
                        top: VerticalAnchor("row1", VerticalAlign.Top),
                    )
                ).id("row3")
            }.width(300).height(300).margin(left: 50).border(width: 2, color: 0x6699FF)
        }.height(100.percent)
    }
}
```

![relativecontainer8](figures/relativecontainer8.png)

### 示例8（设置镜像模式）

本示例展示了在镜像模式（direction声明Direction.Rtl）下以屏障为锚点时使用[LocalizedAlignRuleOptions](cj-universal-attribute-location.md#class-localizedalignruleoptions)和[LocalizedBarrierDirection](#enmu-localizedbarrierdirection)设置对齐方式的用法。

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
                Row().width(100).height(100).backgroundColor(0xff3333).id("row1")

                Row().width(100).height(100).backgroundColor(0xFFCC00).alignRules(
                    AlignRuleOption(
                        top: VerticalAnchor("row1", VerticalAlign.Bottom),
                        middle: HorizontalAnchor("row1", HorizontalAlign.End)
                    )
                ).id("row2")

                Row().height(100).width(100).backgroundColor(0xFF6633).alignRules(
                    AlignRuleOption(
                        top: VerticalAnchor("row1", VerticalAlign.Top),
                        left: HorizontalAnchor("barrier1", HorizontalAlign.End)
                    )
                ).id("row3")

                Row().width(50).height(50).backgroundColor(0xFF9966).alignRules(
                    AlignRuleOption(
                        top: VerticalAnchor("barrier2", VerticalAlign.Bottom),
                        left: HorizontalAnchor("row1", HorizontalAlign.Start),
                    )
                ).id("row4")
            }.width(300).height(300).margin(left: 50.vp).border(width: 2.vp, color: Color(0x6699ff)).direction(
                Direction.Rtl).barrier(
                [LocalizedBarrierStyle("barrier1", LocalizedBarrierDirection.END, ["row1", "row2"]),
                LocalizedBarrierStyle("barrier2", LocalizedBarrierDirection.BOTTOM, ["row1", "row2"])])
        }.height(100.percent)
    }
}
```

![relativecontainer6](figures/relativecontainer6.jpg)