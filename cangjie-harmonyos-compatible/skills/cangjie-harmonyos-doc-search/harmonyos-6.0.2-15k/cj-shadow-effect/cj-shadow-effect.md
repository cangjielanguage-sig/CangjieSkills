# 阴影

阴影接口[shadow](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-imageeffect.md#func-shadowfloat64-resourcecolor-float64-float64)可以为当前组件添加阴影效果，该接口支持两种类型参数，开发者可配置[ShadowOptions](../../API_Reference/source_zh_cn/arkui-cj/cj-text-input-text.md#class-shadowoptions)自定义阴影效果。ShadowOptions模式下，当radius = 0 或者 color 的透明度为0时，无阴影效果。

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
            Column() {
                Column() {
                    Text('shadowOption').fontSize(12)
                }.width(100).aspectRatio(1).margin(10).justifyContent(FlexAlign.Center).backgroundColor(Color.WHITE).
                    borderRadius(20).shadow(radius: 10, color: Color.GRAY)

                Column() {
                    Text('shadowOption').fontSize(12)
                }.width(100).aspectRatio(1).margin(10).justifyContent(FlexAlign.Center).backgroundColor(0xa8a888).
                    borderRadius(20).shadow(radius: 10, color: Color.GRAY, offsetX: 20, offsetY: 20)
            }.width(100.percent).height(100.percent).justifyContent(FlexAlign.Center)
        }.height(100.percent)
    }
}
```

![shadow](./figures/shadow.png)
