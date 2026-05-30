## 色彩

通过颜色渐变接口，可以设置组件的背景颜色渐变效果，实现在两个或多个指定的颜色之间进行平稳的过渡。

| 接口 | 说明 |
| :-------- | :-------- |
| [linearGradient](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-gradientcolor.md#func-lineargradientoptionfloat64-gradientdirection-arraycolorfloat64-bool) | 为当前组件添加线性渐变的颜色渐变效果。 |
| [sweepGradient](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-gradientcolor.md#func-sweepgradientlengthlength-float64-float64-float64-arraycolorfloat64-bool) | 为当前组件添加角度渐变的颜色渐变效果。 |
| [radialGradient](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-gradientcolor.md#func-radialgradientlengthlength-float64-arraycolorfloat64-bool) | 为当前组件添加径向渐变的颜色渐变效果。 |

## 为组件添加线性渐变效果

<!--run-->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import kit.LocalizationKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Grid() {
            GridItem() {
                Column() {
                    Text('angle: 180').fontSize(15)
                }.width(100).height(100).justifyContent(FlexAlign.Center).borderRadius(10).linearGradient(
                    colors: [(Color(0xf56c6c), 0.0), (Color(0xffffff), 1.0)])
            }

            GridItem() {
                Column() {
                    Text('angle: 45').fontSize(15)
                }.width(100).height(100).justifyContent(FlexAlign.Center).borderRadius(10).linearGradient(angle: 45.0,
                    colors: [(Color(0xf56c6c), 0.0), (Color(0xffffff), 1.0)])
            }

            GridItem() {
                Column() {
                    Text('repeat: true').fontSize(15)
                }.width(100).height(100).justifyContent(FlexAlign.Center).borderRadius(10).linearGradient(
                    repeating: true, colors: [(Color(0xf56c6c), 0.0), (Color(0xE6A23C), 0.3)])
            }

            GridItem() {
                Column() {
                    Text('repeat: false').fontSize(15)
                }.width(100).height(100).justifyContent(FlexAlign.Center).borderRadius(10).linearGradient(
                    repeating: false, colors: [(Color(0xf56c6c), 0.0), (Color(0xE6A23C), 0.3)])
            }
        }.columnsGap(10).rowsGap(10).columnsTemplate('1fr 1fr').rowsTemplate('1fr 1fr 1fr').width(100.percent).height(
            100.percent)
    }
}
```

![color-effect](./figures/color-effect.png)