### 设置相对于锚点的对齐位置

设置了锚点之后，可以通过[alignRules](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-location.md#func-alignrulesalignruleoption)属性设置相对于锚点的对齐位置。

在水平方向上，对齐位置可以设置为HorizontalAlign.Start、HorizontalAlign.Center、HorizontalAlign.End。

![alignment-relative-anchor-horizontal](figures/alignment-relative-anchor-horizontal.png)

在竖直方向上，对齐位置可以设置为VerticalAlign.Top、VerticalAlign.Center、VerticalAlign.Bottom。

![alignment-relative-anchor-vertical](figures/alignment-relative-anchor-vertical.png)

### 子组件位置偏移

子组件经过相对位置对齐后，位置可能还不是目标位置，开发者可根据需要进行额外偏移设置额外偏移（offset）。当使用offset调整位置的组件作为锚点时，对齐位置为设置offset之前的位置。建议使用[bias](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-location.md#class-bias)来设置额外偏移。

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
                }.justifyContent(FlexAlign.Center).width(100).height(100).backgroundColor(0xa3cf62).alignRules(
                    AlignRuleOption(
                        top: VerticalAnchor("__container__", VerticalAlign.Top),
                        left: HorizontalAnchor("__container__", HorizontalAlign.Start)
                    )
                ).id("row1")

                Row() {
                    Text('row2')
                }.justifyContent(FlexAlign.Center).width(100).backgroundColor(0x00ae9d).alignRules(
                    AlignRuleOption(
                        top: VerticalAnchor("__container__", VerticalAlign.Top),
                        right: HorizontalAnchor("__container__", HorizontalAlign.End),
                        bottom: VerticalAnchor("row1", VerticalAlign.Center)
                    )
                ).offset(x: -40, y: -20).id("row2")

                Row() {
                    Text('row3')
                }.justifyContent(FlexAlign.Center).height(100).backgroundColor(0x0a59f7).alignRules(
                    AlignRuleOption(
                        top: VerticalAnchor("row1", VerticalAlign.Bottom),
                        left: HorizontalAnchor("row1", HorizontalAlign.End),
                        right: HorizontalAnchor("row2", HorizontalAlign.Start)
                    )
                ).offset(x: -10, y: -20).id("row3")

                Row() {
                    Text('row4')
                }.justifyContent(FlexAlign.Center).backgroundColor(0x2ca9e0).alignRules(
                    AlignRuleOption(
                        top: VerticalAnchor("row3", VerticalAlign.Bottom),
                        bottom: VerticalAnchor("__container__", VerticalAlign.Bottom),
                        left: HorizontalAnchor("__container__", HorizontalAlign.Start),
                        right: HorizontalAnchor("row1", HorizontalAlign.End)
                    )
                ).offset(x: -10, y: -30).id("row4")
                Row() {
                    Text('row5')
                }.justifyContent(FlexAlign.Center).backgroundColor(0x30c9f7).alignRules(
                    AlignRuleOption(
                        top: VerticalAnchor("row3", VerticalAlign.Bottom),
                        bottom: VerticalAnchor("__container__", VerticalAlign.Bottom),
                        left: HorizontalAnchor("row2", HorizontalAlign.Start),
                        right: HorizontalAnchor("row2", HorizontalAlign.End)
                    )
                ).offset(x: 10, y: 20).id("row5")
                Row() {
                    Text('row6')
                }.justifyContent(FlexAlign.Center).backgroundColor(0xff33ffb5).alignRules(
                    AlignRuleOption(
                        top: VerticalAnchor("row3", VerticalAlign.Bottom),
                        bottom: VerticalAnchor("row4", VerticalAlign.Bottom),
                        left: HorizontalAnchor("row3", HorizontalAlign.Start),
                        right: HorizontalAnchor("row3", HorizontalAlign.End)
                    )
                ).offset(x: -15, y: 10).backgroundImagePosition(Alignment.Bottom).backgroundImageSize(ImageSize.Cover).
                    id("row6")
            }.width(300).height(300).margin(left: 50).border(width: 2, color: 0x6699FF)
        }.height(100.percent)
    }
}
```

![Simplify-Component-Layout](figures/simplify-component-layout-image2.png)