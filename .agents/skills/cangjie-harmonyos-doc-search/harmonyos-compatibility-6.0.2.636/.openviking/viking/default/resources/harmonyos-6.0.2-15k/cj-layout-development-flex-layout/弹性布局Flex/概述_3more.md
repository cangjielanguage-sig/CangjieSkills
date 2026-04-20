## 概述

弹性布局（[Flex](../../API_Reference/source_zh_cn/arkui-cj/cj-row-column-stack-flex.md)）提供更加有效的方式对容器中的子元素进行排列、对齐和分配剩余空间。常用于页面头部导航栏的均匀分布、页面框架的搭建、多行数据的排列等。

容器默认存在主轴与交叉轴，子元素默认沿主轴排列，子元素在主轴方向的尺寸称为主轴尺寸，在交叉轴方向的尺寸称为交叉轴尺寸。

**图1** 主轴为水平方向的Flex容器示意图

![flex-layout](figures/flex-layout.png)

## 基本概念

- 主轴：Flex组件布局方向的轴线，子元素默认沿着主轴排列。主轴开始的位置称为主轴起始点，结束位置称为主轴结束点。

- 交叉轴：垂直于主轴方向的轴线。交叉轴开始的位置称为交叉轴起始点，结束位置称为交叉轴结束点。

## 布局方向

在弹性布局中，容器的子元素可以按照任意方向排列。通过设置参数direction，可以决定主轴的方向，从而控制子元素的排列方向。

弹性布局方向图如下图所示：

![flex-layout-direction](figures/flex-layout-direction.png)

- FlexDirection.Row（默认值）：主轴为水平方向，子元素从起始端沿着水平方向开始排布。

    <!-- run -->

    ```cangjie
    package ohos_app_cangjie_entry

    import kit.UIKit.*
    import ohos.state_macro_manage.*

    @Entry
    @Component
    class EntryView {
        func build() {
            Flex(FlexParams(direction: FlexDirection.Row)) {
                Text('1').width(33.percent).height(50).backgroundColor(0xF5DEB3)
                Text('2').width(33.percent).height(50).backgroundColor(0xD2B48C)
                Text('3').width(33.percent).height(50).backgroundColor(0xF5DEB3)
            }.height(70).width(90.percent).padding(10).backgroundColor(0xAFEEEE)
        }
    }
    ```

    ![Flex](figures/Flex.png)

- FlexDirection.RowReverse：主轴为水平方向，子元素从终点端沿着FlexDirection. Row相反的方向开始排布。

    <!-- run -->

    ```cangjie
    package ohos_app_cangjie_entry

    import kit.UIKit.*
    import ohos.state_macro_manage.*

    @Entry
    @Component
    class EntryView {
        func build() {
            Flex(FlexParams(direction: FlexDirection.RowReverse)) {
                Text('3').width(33.percent).height(50).backgroundColor(0xF5DEB3)
                Text('2').width(33.percent).height(50).backgroundColor(0xD2B48C)
                Text('1').width(33.percent).height(50).backgroundColor(0xF5DEB3)
            }.height(70).width(90.percent).padding(10).backgroundColor(0xAFEEEE)
        }
    }
    ```

    ![Flex](figures/Flex.png)

- FlexDirection.Column：主轴为垂直方向，子元素从起始端沿着垂直方向开始排布。

    <!-- run -->

    ```cangjie
    package ohos_app_cangjie_entry

    import kit.UIKit.*
    import ohos.state_macro_manage.*

    @Entry
    @Component
    class EntryView {
        func build() {
            Flex(FlexParams(direction: FlexDirection.Column)) {
                Text('1').width(100.percent).height(50).backgroundColor(0xF5DEB3)
                Text('2').width(100.percent).height(50).backgroundColor(0xD2B48C)
                Text('3').width(100.percent).height(50).backgroundColor(0xF5DEB3)
            }.height(70).width(90.percent).padding(10).backgroundColor(0xAFEEEE)
        }
    }
    ```

    ![Flex1](figures/Flex1.png)

- FlexDirection.ColumnReverse：主轴为垂直方向，子元素从终点端沿着FlexDirection. Column相反的方向开始排布。

    <!-- run -->

    ```cangjie
    package ohos_app_cangjie_entry

    import kit.UIKit.*
    import ohos.state_macro_manage.*

    @Entry
    @Component
    class EntryView {
        func build() {
            Flex(FlexParams(direction: FlexDirection.ColumnReverse)) {
                Text('1').width(100.percent).height(50).backgroundColor(0xF5DEB3)
                Text('2').width(100.percent).height(50).backgroundColor(0xD2B48C)
                Text('3').width(100.percent).height(50).backgroundColor(0xF5DEB3)
            }.height(70).width(90.percent).padding(10).backgroundColor(0xAFEEEE)
        }
    }
    ```

    ![Flex2](figures/Flex2.png)