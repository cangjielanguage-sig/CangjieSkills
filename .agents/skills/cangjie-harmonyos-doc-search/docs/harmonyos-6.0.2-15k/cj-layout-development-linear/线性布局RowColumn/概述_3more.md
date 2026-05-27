## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](../../API_Reference/source_zh_cn/arkui-cj/cj-row-column-stack-row.md)和[Column](../../API_Reference/source_zh_cn/arkui-cj/cj-row-column-stack-column.md)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Column容器内子元素按照垂直方向排列，Row容器内子元素按照水平方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

**图1** Column容器内子元素排列示意图

![arrangement-child-elements-column](figures/arrangement-child-elements-column.png)

**图2** Row容器内子元素排列示意图

![arrangement-child-elements-row](figures/arrangement-child-elements-row.png)

## 基本概念

- 布局容器：具有布局能力的组件容器，可以承载其他元素作为其子元素，布局容器会对其子元素进行尺寸计算和布局排列。

- 布局子元素：布局容器内部的元素。

- 主轴：线性布局容器在布局方向上的轴线，子元素默认沿主轴排列。Row容器主轴为水平方向，Column容器主轴为垂直方向。

- 交叉轴：垂直于主轴方向的轴线。Row容器交叉轴为垂直方向，Column容器交叉轴为水平方向。

- 间距：布局子元素的间距。

## 布局子元素在排列方向上的间距

在布局容器内，可以通过space属性设置排列方向上子元素的间距，使各子元素在排列方向上有等间距效果。

### Column容器内排列方向上的间距

**图3** Column容器内排列方向的间距图

![arrangement-direction-column](figures/arrangement-direction-column.png)

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Column(20) {
            Text('space: 20').fontSize(15).fontColor(Color.GRAY).width(90.percent)
            Row().width(90.percent).height(50).backgroundColor(0xF5DEB3)
            Row().width(90.percent).height(50).backgroundColor(0xD2B48C)
            Row().width(90.percent).height(50).backgroundColor(0xF5DEB3)
        }.width(100.percent)
    }
}
```

![arrangement-direction-column01](figures/arrangement-direction-column01.PNG)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![arrangement-direction-row](figures/arrangement-direction-row.png)

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Row(35) {
            Text('space: 35').fontSize(15).fontColor(Color.GRAY)
            Row().width(10.percent).height(150).backgroundColor(0xF5DEB3)
            Row().width(10.percent).height(150).backgroundColor(0xD2B48C)
            Row().width(10.percent).height(150).backgroundColor(0xF5DEB3)
        }.width(90.percent)
    }
}
```

![image01](figures/image01.PNG)