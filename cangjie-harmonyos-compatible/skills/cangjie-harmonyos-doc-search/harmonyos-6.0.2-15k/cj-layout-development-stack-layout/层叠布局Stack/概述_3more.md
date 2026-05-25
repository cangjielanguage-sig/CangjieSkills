## 概述

层叠布局（StackLayout）用于在屏幕上预留一块区域来显示组件中的元素，提供元素可以重叠的布局。层叠布局通过[Stack](../../API_Reference/source_zh_cn/arkui-cj/cj-row-column-stack-stack.md)容器组件实现位置的固定定位与层叠，容器中的子元素依次入栈，后一个子元素覆盖前一个子元素，子元素可以叠加，也可以设置位置。

层叠布局具有较强的页面层叠、位置定位能力，其使用场景有广告、卡片层叠效果等。

如图1，Stack作为容器，容器内的子元素的顺序为Item1-&gt;Item2-&gt;Item3。

**图1** 层叠布局

![stack-layout](figures/stack-layout.png)

## 开发布局

Stack组件为容器组件，容器内可包含各种子元素。其中子元素默认进行居中堆叠。子元素被约束在Stack下，进行样式定义以及排列。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Column() {
            Stack() {
                Column() {}.width(90.percent).height(100.percent).backgroundColor(0xff58b87c)
                Text('text').width(60.percent).height(60.percent).backgroundColor(0xffc3f6aa)
                Button('button').width(30.percent).height(30.percent).backgroundColor(0xff8ff3eb).fontColor(0x000)
            }.width(100.percent).height(150).margin(top: 50)
        }
    }
}
```

![stack-layout-sample](figures/stack-layout-sample.png)

## 对齐方式

Stack组件通过[alignContent参数](../../API_Reference/source_zh_cn/arkui-cj/cj-row-column-stack-stack.md#func-aligncontentalignment)实现位置的相对移动。如图2所示，支持九种对齐方式。

**图2** Stack容器内元素的对齐方式

![alignContent1](figures/alignContent.png)

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Stack(Alignment.TopStart) {
            Text('Stack').width(90.percent).height(100.percent).backgroundColor(0xe1dede).align(Alignment.BottomEnd)
            Text('Item 1').width(70.percent).height(80.percent).backgroundColor(0xd2cab3).align(Alignment.BottomEnd)
            Text('Item 2').width(50.percent).height(60.percent).backgroundColor(0xc1cbac).align(Alignment.BottomEnd)
        }.width(100.percent).height(150).margin(top: 5)
    }
}
```