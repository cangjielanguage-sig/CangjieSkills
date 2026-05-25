# 创建网格（Grid/GridItem）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

## 概述

网格布局是由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。网格布局具有较强的页面均分能力，子组件占比控制能力，是一种重要自适应布局，其使用场景有九宫格图片展示、日历、计算器等。

ArkUI提供了[Grid](../reference/arkui-cj/cj-scroll-swipe-grid.md)容器组件和子组件[GridItem](../reference/arkui-cj/cj-scroll-swipe-griditem.md)，用于构建网格布局。Grid用于设置网格布局相关参数，GridItem定义子组件相关特征。Grid组件支持使用[条件渲染](./rendering_control/cj-rendering-control-ifelse.md)、[循环渲染](./rendering_control/cj-rendering-control-foreach.md)、[懒加载](./rendering_control/cj-rendering-control-lazyforeach.md)等方式生成子组件。

## 布局与约束

Grid组件为网格容器，其中容器内各条目对应一个GridItem组件，如下图1所示。

**图1** Grid与GridItem组件关系

![GridItem](figures/GridItem.png)

> **说明：**
>
> Grid的子组件必须是GridItem组件。

网格布局是一种二维布局。Grid组件支持自定义行列数和每行每列尺寸占比、设置子组件横跨几行或者几列，同时提供了垂直和水平布局能力。当网格容器组件尺寸发生变化时，所有子组件以及间距会等比例调整，从而实现网格布局的自适应能力。根据Grid的这些布局能力，可以构建出不同样式的网格布局，如下图2所示。

**图2** 网格布局

![GridItem1](figures/GridItem1.png)

如果Grid组件设置了宽高属性，则其尺寸为设置值。如果没有设置宽高属性，Grid组件的尺寸默认适应其父组件的尺寸。

Grid组件根据行列数量与占比属性的设置，可以分为三种布局情况：

- 行、列数量与占比同时设置：Grid只展示固定行列数的元素，其余元素不展示，且Grid不可滚动。（推荐使用该种布局方式）

- 只设置行、列数量与占比中的一个：元素按照设置的方向进行排布，超出的元素可通过滚动的方式展示。

- 行列数量与占比都不设置：元素在布局方向上排布，其行列数由布局方向、单个网格的宽高等多个属性共同决定。超出行列容纳范围的元素不展示，且Grid不可滚动。

## 设置排列方式

### 设置行列数量与占比

通过设置行列数量与尺寸占比可以确定网格布局的整体排列方式。Grid组件提供了rowsTemplate和columnsTemplate属性用于设置网格布局行列数量与尺寸占比。

rowsTemplate和columnsTemplate属性值是一个由多个空格和'数字+fr'间隔拼接的字符串，fr的个数即网格布局的行或列数，fr前面的数值大小，用于计算该行或列在网格布局宽度上的占比，最终决定该行或列宽度。

**图3** 行列数量占比示例

![GridItem2](figures/GridItem2.png)

如上图3所示，构建的是一个三行三列的网格布局，其在垂直方向上分为三等份，每行占一份；在水平方向上分为四等份，第一列占一份，第二列占两份，第三列占一份。

只要将rowsTemplate的值为"1fr 1fr 1fr"，同时将columnsTemplate的值为"1fr 2fr 1fr"，即可实现上述网格布局。

<!-- code_no_check -->

```cangjie
Grid() {
  // ...
}
.rowsTemplate("1fr 1fr 1fr")
.columnsTemplate("1fr 2fr 1fr")
```

> **说明：**
>
> 当Grid组件设置了rowsTemplate或columnsTemplate时，Grid的layoutDirection、cellLength属性不生效，属性说明可参考[Grid-属性](../reference/arkui-cj/cj-scroll-swipe-grid.md#组件属性)。