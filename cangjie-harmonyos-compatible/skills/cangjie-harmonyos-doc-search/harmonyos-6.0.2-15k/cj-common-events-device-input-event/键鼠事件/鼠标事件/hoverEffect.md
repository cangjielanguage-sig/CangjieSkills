### hoverEffect

```cangjie
public func hoverEffect(value: HoverEffect)
```

鼠标悬浮态效果设置的通用属性。参数类型为HoverEffect，HoverEffect提供的Auto、Scale、Highlight效果均为固定效果，开发者无法自定义设置效果参数。

| HoverEffect枚举值                    | 效果说明                                      |
|:---------------------------------------- |:---------------------------------------- |
|  Auto | 组件默认提供的悬浮态效果，由各组件定义。|
|  Scale | 动画播放方式，鼠标悬浮时：组件大小从100%放大至105%，鼠标离开时：组件大小从105%缩小至100%。|
|  Highlight | 动画播放方式，鼠标悬浮时：组件背景色叠加一个5%透明度的白色，视觉效果是组件的原有背景色变暗，鼠标离开时：组件背景色恢复至原有样式。|
|  None | 禁用悬浮态效果。|

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Column(10) {
            Text("Auto").width(170).height(70).backgroundColor(Color.PINK)
            Text("Scale").width(170).height(70).hoverEffect(HoverEffect.Scale).backgroundColor(Color.PINK)
            Text("Highlight").width(170).height(70).hoverEffect(HoverEffect.Highlight).backgroundColor(Color.PINK)
            Text("None").width(170).height(70).hoverEffect(HoverEffect.None).backgroundColor(Color.PINK)
        }.width(100.percent).height(100.percent).justifyContent(FlexAlign.Center)
    }
}
```

![hoverEffect](./figures/hoverEffect.gif)

Text默认的悬浮态效果就是None，None会禁用悬浮态效果，Scale会让组件缩放，Highlight会使背板颜色变暗。