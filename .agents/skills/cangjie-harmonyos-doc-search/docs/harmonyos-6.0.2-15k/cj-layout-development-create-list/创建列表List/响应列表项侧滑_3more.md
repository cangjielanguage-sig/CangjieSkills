## 响应列表项侧滑

侧滑菜单在许多应用中都很常见。例如，通讯类应用通常会给消息列表提供侧滑删除功能，即用户可以通过向左侧滑列表的某一项，再点击删除按钮删除消息，如下图15所示。其中，列表项头像右上角标记设置参考[给列表项添加标记](#给列表项添加标记)。

**图15** 侧滑删除列表项

![List14](figures/List14.gif)

ListItem的[swipeAction属性](../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-listitem.md#func-swipeaction---unit----unit-swipeedgeeffect-float64---unit)可用于实现列表项的左右滑动功能。swipeAction属性方法初始化时有必填参数SwipeActionOptions，其中，start参数表示设置列表项右滑时起始端滑出的组件，end参数表示设置列表项左滑时尾端滑出的组件。

在消息列表中，end参数表示设置ListItem左滑时尾端划出自定义组件，即删除按钮。在初始化end方法时，将滑动列表项的索引传入删除按钮组件，当用户点击删除按钮时，可以根据索引值来删除列表项对应的数据，从而实现侧滑删除功能。

- 实现尾端滑出组件的构建。

    ```cangjie
    @Builder
    func itemEnd(index: Int64) {
        // 构建尾端滑出组件
        Button(ButtonOptions(shape: ButtonType.Circle)) {
            Image(@r(app.media.ic_public_delete_filled)).width(20).height(20)
        }.onClick({
            event =>
            // this.messages为列表数据源，可根据实际场景构造。点击后从数据源删除指定数    据项。
            this.message.remove(index)
        })
    }
    ```

- 绑定swipeAction属性到可左滑的ListItem上。

    ```cangjie
    // 构建List时，通过ForEach基于数据源this.messages循环渲染ListItem。
    ListItem(){
        Text('1111').height(20)
    }
    .swipeAction(end: { => bind(this.itemEnd, this)(index)}) // index为该    ListItem在List中的索引值
    ```

## 给列表项添加标记

添加标记是一种无干扰性且直观的方法，用于显示通知或将注意力集中到应用内的某个区域。例如，当消息列表接收到新消息时，通常对应的联系人头像的右上方会出现标记，提示有若干条未读消息，如下图16所示。

**图16** 给列表项添加标记

![List15](figures/List15.png)

在ListItem中使用[Badge](../../API_Reference/source_zh_cn/arkui-cj/cj-information-display-badge.md)组件可实现给列表项添加标记功能。Badge是可以附加在单个组件上用于信息标记的容器组件。

在消息列表中，若希望在联系人头像右上角添加标记，可在实现消息列表项ListItem的联系人头像时，将头像Image组件作为Badge的子组件。

在Badge组件中，count和position参数用于设置需要展示的消息数量和提示点显示位置，还可以通过style参数灵活设置标记的样式。

```cangjie
ListItem(){
  Badge(
    BadgeParams(count: 1, style: BadgeStyle(color: 0xfa2a2d, badgeSize: 16),
        position: BadgePosition.RightTop),{ =>
        Image(@r(app.media.startIcon))
    })
}
```

## 下拉刷新与上拉加载

页面的下拉刷新与上拉加载功能在移动应用中十分常见，例如，新闻页面的内容刷新和加载。这两种操作的原理都是通过响应用户的[触摸事件](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-event-touch.md)，在顶部或者底部显示一个刷新或加载视图，完成后再将此视图隐藏。

以下拉刷新为例，其实现主要分成三步：

1. 监听手指按下事件，记录其初始位置的值。

2. 监听手指按压移动事件，记录并计算当前移动的位置与初始值的差值，大于0表示向下移动，同时设置一个允许移动的最大值。

3. 监听手指抬起事件，若此时移动达到最大值，则触发数据加载并显示刷新视图，加载完成后将此视图隐藏。

> **说明：**
>
> 页面的下拉刷新操作推荐使用[Refresh](../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-refresh.md)组件实现。