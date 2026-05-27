# 布局概述

组件按照布局的要求依次排列，构成应用的页面。在声明式UI中，所有的页面都是由自定义组件构成，开发者可以根据自己的需求，选择合适的布局进行页面开发。

布局指用特定的组件或者属性来管理用户页面所放置UI组件的大小和位置。在实际的开发过程中，需要遵守以下流程保证整体的布局效果：

- 确定页面的布局结构。
- 分析页面中的元素构成。
- 选用适合的布局容器组件或属性控制页面中各个元素的位置和大小。

## 布局结构

布局通常为分层结构，一个常见的页面结构如下所示：

**图1** 常见页面结构图

![layout-overview-1](figures/layout-overview-1.png)

为实现上述效果，开发者需要在页面中声明对应的元素。其中，Page表示页面的根节点，Column/Row等元素为系统组件。针对不同的页面结构，ArkUI提供了不同的布局组件来帮助开发者实现对应布局的效果，例如Row用于实现线性布局。

## 布局元素的组成

布局相关的容器组件可形成对应的布局效果。例如，List组件可构成线性布局。

**图2** 布局元素组成图

![layout-overview-2](figures/layout-overview-2.png)

- 组件区域（蓝区方块）：组件区域表示组件的大小，[width](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-size.md#func-widthlength)、[height](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-size.md#func-heightlength)属性用于设置组件区域的大小。
- 组件内容区（黄色方块）：组件内容区大小为组件区域大小减去组件的[border](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-border.md)值，组件内容区大小会作为组件内容（或者子组件）进行大小测算时的布局测算限制。
- 组件内容（绿色方块）：组件内容本身占用的大小，比如文本内容占用的大小。组件内容和组件内容区不一定匹配，比如设置了固定的width和height，此时组件内容的大小就是设置的width和height减去padding和border值，但文本内容则是通过文本布局引擎测算后得到的大小，可能出现文本真实大小小于设置的组件内容区大小。当组件内容和组件内容区大小不一致时，[align](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-location.md#func-alignalignment)属性生效，定义组件内容在组件内容区的对齐方式，如居中对齐。
- 组件布局边界（虚线部分）：组件通过[margin](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-size.md#func-marginlength)属性设置外边距时，组件布局边界就是组件区域加上margin的大小。