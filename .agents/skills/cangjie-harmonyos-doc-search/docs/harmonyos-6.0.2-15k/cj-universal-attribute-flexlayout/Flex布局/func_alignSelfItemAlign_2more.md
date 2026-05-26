## func alignSelf(ItemAlign)

```cangjie
public func alignSelf(value: ItemAlign): This
```

**功能：** 子组件在父容器交叉轴的对齐格式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :------- | :--------- | :------- | :-------- | :--------------------------------------------------|
| value  | [ItemAlign](./cj-common-types.md#enum-itemalign) | 是 | -| 子组件在父容器交叉轴的对齐格式，会覆盖Flex、Column、Row、GridRow布局容器中的alignItems设置。<br> GridCol可以绑定alignsSelf属性来改变它自身在交叉轴方向上的布局。<br>初始值：ItemAlign.Auto。|

## 示例代码

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Column(5) {
            Text("flexBasis").fontSize(10).fontColor(0xcccccc).width(90.percent)
            Flex(FlexParams()) {
                Text("flexBasis(100)").flexBasis(100) // 这里表示宽度为100vp
                    .height(100).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
                Text("")
                    // 这里表示宽度保持原本设置的60%的宽度
                    .width(60.percent).height(100).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
            }.width(90.percent).height(120).padding(10).backgroundColor(0xAFEEEE)

            Text("flexGrow").fontSize(9).fontColor(0xCCCCCC).width(90.percent)
            // flexGrow()表示剩余空间分配给该元素的比例
            Flex(FlexParams()) {
                Text("flexGrow(2)").flexGrow(2) // 父容器分配给该Text的宽度为剩余宽度的2/3
                    .height(100).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
                Text("flexGrow(1)").flexGrow(1) // 父容器分配给该Text的宽度为剩余宽度的1/3
                    .height(100).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
            }.width(90.percent).height(120).padding(10).backgroundColor(0xAFEEEE)

            Text("flexShrink").fontSize(9).fontColor(0xCCCCCC).width(90.percent)
            // flexShrink()表示该元素的压缩比例，基于超出的总尺寸进行计算
            // 第一个text压缩比例是0,另外两个都是1,因此放不下时等比例压缩后两个,第一个不压缩
            Flex(FlexParams(direction: FlexDirection.Row)) {
                Text("flexShrink(0)").flexShrink(0).width(50.percent).height(100).backgroundColor(0xF5DEB3).textAlign(
                    TextAlign.Center)
                Text("default flexShrink") // 默认值为1
                    .width(40.percent).height(100).backgroundColor(0xD2B48C).textAlign(
                    TextAlign.Center)
                Text("flexShrink(1)").flexShrink(1).width(40.percent).height(100).backgroundColor(0xF5DEB3).textAlign(
                    TextAlign.Center)
            }.width(90.percent).height(120).padding(10).backgroundColor(0xAFEEEE)

            Text("alignSelf").fontSize(9).fontColor(0xCCCCCC).width(90.percent)
            // alignSelf会覆盖Flex布局容器中的alignItems设置
            Flex(FlexParams(direction: FlexDirection.Row, alignItems: ItemAlign.Center)) {
                Text("no alignSelf,height:70").width(33.percent).height(70).backgroundColor(0xF5DEB3).textAlign(
                    TextAlign.Center)
                Text("alignSelf End").alignSelf(ItemAlign.End).width(33.percent).height(70).backgroundColor(0xD2B48C).
                    textAlign(TextAlign.Center)
                Text("no alignSelf,height:100%").width(34.percent).height(100.percent).backgroundColor(0xF5DEB3).
                    textAlign(TextAlign.Center)
            }.width(90.percent).height(120).padding(10).backgroundColor(0xAFEEEE)
        }.width(100.percent).margin(top: 5)
    }
}
```

![uni_flex](figures/uni_flex.png)