### 扩展安全区方案

- 布局阶段按照安全区范围大小进行UI元素布局。
- 布局完成后查看设置了expandSafeArea的组件边界（不包括margin）是否和安全区边界相交。
- 如果设置了expandSafeArea的组件和安全区边界相交，根据expandSafeArea传递的属性则进一步扩大组件绘制区域大小覆盖状态栏、导航条这些非安全区域。
- 上述过程仅改变组件自身绘制大小，不进行二次布局，不影响子节点和兄弟节点的大小和位置。
- 子节点可以单独设置该属性，只需要自身边界和安全区域重合就可以延伸自身大小至非安全区域内，需要确保父组件未设置clip等裁切属性。
- 配置expandSafeArea属性组件进行绘制扩展时，需要关注组件不能配置固定宽高尺寸，百分比除外。
- 组件可以设置通用属性safeAreaPadding，给自身添加组件级安全区域。该属性作为一种特殊边距，在提供布局约束的同时作为安全区可以被一些系统组件利用。
    - safeAreaPadding位于原有的padding内侧。容器自外向内各层分别为border、padding、safeAreaPadding、内容区。当border和padding确定后，若容器可用空间不足以满足safeAreaPadding的设置，则优先分配给左侧和上侧safeAreaPadding、其次分配给右侧和下侧safeAreaPadding。<br/>safeAreaPadding实际尺寸确定后，余下空间为内容区。<br/>![immerse-8](figures/immerse-8.png)
    - 系统组件如Navigation、List、Scroll、Tabs等可以利用外层或容器自身safeAreaPadding实现扩大裁剪范围等能力。

### 背景图和视频场景

设置背景图、视频控件大小为安全区域大小并配置expandSafeArea属性。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.__GenerateResource__

@Entry
@Component
class EntryView {
    func build() {
        Stack() {
            Image(@r(app.media.bg)).height(100.percent).width(100.percent).expandSafeArea(types: [SafeAreaType.SYSTEM],
                edges: [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]) // 图片组件的绘制区域扩展至状态栏和导航条。
        }.height(100.percent).width(100.percent)
    }
}
```

![immerse-9](figures/immerse-9.png)