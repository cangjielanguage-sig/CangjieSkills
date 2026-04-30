# List

一个包含一系列相同宽度的列表项的容器组件。适合连续、多行呈现同类数据，例如图片和文本。

## 子组件

仅支持[ListItem](./cj-scroll-swipe-listitem.md)、[ListItemGroup](./cj-scroll-swipe-listgroup.md)子组件。支持渲染控制类型（[if/else](../../../Dev_Guide/arkui-cj/rendering_control/cj-rendering-control-ifelse.md)、[ForEach](cj-state-rendering-foreach.md)、[LazyForEach](./cj-state-rendering-lazyforeach.md)）。

> **说明：**
>
> List的子组件的索引值计算规则：
>
> * 按子组件的顺序依次递增。
> * if/else语句中，只有条件成立的分支内的子组件会参与索引值计算，条件不成立的分支内子组件不计算索引值。
> * ForEach/LazyForEach语句中，会计算展开所有子节点索引值。
> * [if/else](../../../Dev_Guide/arkui-cj/rendering_control/cj-rendering-control-ifelse.md)、[ForEach](cj-state-rendering-foreach.md)、[LazyForEach](./cj-state-rendering-lazyforeach.md)发生变化以后，会更新子节点索引值。
> * ListItemGroup作为一个整体计算一个索引值，ListItemGroup内部的ListItem不计算索引值。
> * List子组件visibility属性设置为Hidden或None依然会计算索引值。