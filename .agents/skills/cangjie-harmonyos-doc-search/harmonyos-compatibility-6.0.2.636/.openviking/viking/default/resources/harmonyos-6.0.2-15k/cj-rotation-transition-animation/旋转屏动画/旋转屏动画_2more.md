# 旋转屏动画

旋转屏动画主要分为两类：[布局切换的旋转屏动画](#布局切换的旋转屏动画)和[透明度变化的旋转屏动画](#透明度变化的旋转屏动画)，旨在实现屏幕显示方向变化时的自然过渡。布局切换的旋转屏动画实现较为简便，例如在module.json5中配置自动旋转（或设置窗口显示方向）即可实现。而透明度变化的旋转屏动画则需在module.json5配置的基础上，预备两套视图，在屏幕旋转时，通过视图切换，使消失的视图呈现渐隐效果，新出现的视图则渐显，从而营造流畅的视觉体验。

## 布局切换的旋转屏动画

布局切换时的旋转屏动画，是在屏幕显示方向改变时，为窗口与应用视图同步旋转而设计的大小和位置过渡动画。这种布局切换的旋转屏动画是系统默认的，便于开发者实现。当屏幕显示方向变化时，系统会生成窗口旋转动画，并自动调整窗口大小以匹配旋转后的尺寸。在此过程中，窗口会通知对应的应用，要求其根据新的窗口大小重新布局，产生与窗口旋转动画参数相同的布局动画。

切换屏幕方向即可实现布局切换的旋转屏动画效果。

<!--run-->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.__GenerateResource__

@Entry
@Component
class EntryView {
    func build() {
        Column() {
            Image(@r(app.media.foreground)).position(x: 0, y: 0).size(width: 100, height: 100).id('image1').
                backgroundColor(Color.BLUE)
        }
    }
}
```

需要在项目的module.json5文件中的abilities列表里添加"orientation"，指定为"auto_rotation"。

```json
"orientation": "auto_rotation",
```

布局切换的旋转屏动画，会对同步旋转的窗口与应用视图做大小和位置的过渡。

![Alt text](./figures/rotation-transition1.gif)