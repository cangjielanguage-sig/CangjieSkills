# Web组件嵌套滚动

Web组件嵌套滚动的典型应用场景为，在一个页面中，有多个独立的区域需要进行滚动，当用户滚动Web区域内容时，可带动其他滚动区域进行滚动，以达到上下滑动页面的用户体验。

内嵌在可滚动容器（[Scroll](../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-scroll.md)、[List](../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-list.md)中的Web组件，接收到滑动手势事件，需要对接ArkUI框架的[NestedScrollMode](../../API_Reference/source_zh_cn/arkui-cj/cj-common-types.md#enum-nestedscrollmode)枚举类型，使得Web组件可以嵌套ArkUI可滚动容器，进行嵌套滚动。开发者可以在Web组件创建时，使用[nestedScroll](../../API_Reference/source_zh_cn/arkui-cj/cj-web-web.md#func-nestedscrollnestedscrollmode-nestedscrollmode)属性接口指定默认的嵌套滚动模式，也允许在过程中动态改变嵌套滚动的模式。

nestedScroll有两个入参，分别为scrollForward和scrollBackward，均为[NestedScrollMode](../../API_Reference/source_zh_cn/arkui-cj/cj-common-types.md#enum-nestedscrollmode)枚举类型。

当Web组件被多个可滚动容器组件嵌套时，未被Web组件消费的与父组件方向一致的偏移量、速度值将被传递给距Web组件最近且方向一致的父组件，使得父组件可以继续滚动。一次手势滑动只能沿X轴或Y轴一个方向嵌套滚动，当手势斜向滑动时，滚动方向为偏移量或速度在X轴、Y轴绝对值较大的方向；当偏移量或速度绝对值在X轴、Y轴绝对值相同时，滚动方向为距Web组件最近的可滚动组件的方向。

> **说明：**
>
> - 支持嵌套滚动的容器：[Grid](../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-grid.md)、[List](../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-list.md)、[Scroll](../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-scroll.md)、[Swiper](../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-swiper.md)、[Tabs](../../API_Reference/source_zh_cn/arkui-cj/cj-navigation-switching-tabs.md)、[WaterFlow](../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-waterflow.md)、[Refresh](../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-refresh.md)、[bindSheet](../../API_Reference/source_zh_cn/arkui-cj/cj-animation-transition.md)。
> - 支持嵌套滚动的输入事件：使用手势、鼠标、触控板。

```cangjie
// index.cj
import ohos.state_macro_manage.*
import kit.ArkWeb.WebviewController
import kit.UIKit.*

@Entry
@Component
class EntryView {
    var scrollerForScroll: Scroller = Scroller()
    let controller = WebviewController()
    let controller2 = WebviewController()
    // NestedScrollMode设置成SELF_ONLY时，Web网页滚动到页面边缘后，不与父组件联动，父组件仍无法滚动。
    @State
    var nestedScrollMode0: NestedScrollMode = NestedScrollMode.SELF_ONLY
    // NestedScrollMode设置成SELF_FIRST时，Web网页滚动到页面边缘后，父组件继续滚动。
    @State
    var nestedScrollMode1: NestedScrollMode = NestedScrollMode.SELF_FIRST
    // NestedScrollMode设置为PARENT_FIRST时，父组件先滚动，滚动至边缘后通知Web继续滚动。
    @State
    var nestedScrollMode2: NestedScrollMode = NestedScrollMode.PARENT_FIRST
    // NestedScrollMode设置为PARALLEL时，父组件与Web同时滚动。
    @State
    var nestedScrollMode3: NestedScrollMode = NestedScrollMode.PARALLEL
    @State
    var nestedScrollModeF: NestedScrollMode = NestedScrollMode.SELF_FIRST
    @State
    var nestedScrollModeB: NestedScrollMode = NestedScrollMode.SELF_FIRST
    // scroll竖向的滚动
    @State
    var scrollDirection: ScrollDirection = ScrollDirection.Vertical