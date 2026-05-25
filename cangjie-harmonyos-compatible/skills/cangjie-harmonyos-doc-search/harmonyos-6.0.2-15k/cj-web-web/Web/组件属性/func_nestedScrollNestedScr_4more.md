### func nestedScroll(NestedScrollMode, NestedScrollMode)

```cangjie
public func nestedScroll(
    scrollForward !: NestedScrollMode = NestedScrollMode.SELF_FIRST,
    scrollBackward !: NestedScrollMode = NestedScrollMode.SELF_FIRST
): This
```

**功能：** 设置向前向后两个方向上的嵌套滚动模式，实现与父组件的滚动联动。

> **说明：**
>
> - 可以设置上下左右四个方向，或者设置向前、向后两个方向的嵌套滚动模式，实现与父组件的滚动联动。
> - value为NestedScrollOptionsExt（上下左右四个方向）类型时，scrollUp、scrollDown、scrollLeft、scrollRight默认滚动选项为[NestedScrollMode.SELF_FIRST](../arkui-cj/cj-common-types.md)。
> - value为NestedScrollOptions（向前、向后两个方向）类型时，scrollForward、scrollBackward默认滚动选项为NestedScrollMode.SELF_FIRST。
> - 支持嵌套滚动的容器：[Grid](./cj-grid-layout-gridcol.md)、[List](./cj-scroll-swipe-list.md)、[Scroll](./cj-scroll-swipe-scroll.md)、[Swiper](./cj-scroll-swipe-swiper.md)、[Tabs](./cj-navigation-switching-tabs.md)、[WaterFlow](./cj-scroll-swipe-waterflow.md)、[Refresh](./cj-scroll-swipe-refresh.md)、[bindSheet](./cj-animation-transition.md)。
> - 支持嵌套滚动的输入事件：使用手势、鼠标、触控板。
> - 嵌套滚动场景下，由于Web滚动到边缘时会优先触发过滚动的过界回弹效果，建议设置overScrollMode为OverScrollMode.NEVER，避免影响此场景的用户体验。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scrollForward|[NestedScrollMode](./cj-common-types.md#enum-nestedscrollmode)|否|NestedScrollMode.SELF_FIRST| **命名参数。** 向前滚动方向。|
|scrollBackward|[NestedScrollMode](./cj-common-types.md#enum-nestedscrollmode)|否|NestedScrollMode.SELF_FIRST| **命名参数。** 向后滚动方向。|

### func overScrollMode(OverScrollMode)

```cangjie
public func overScrollMode(mode: OverScrollMode): This
```

**功能：** 设置Web过滚动模式，默认关闭。当过滚动模式开启时，当用户在Web根页面上滑动到边缘时，Web会通过弹性动画弹回界面，根页面上的内部页面不会触发回弹。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[OverScrollMode](#enum-overscrollmode)|是|-|Web的过滚动模式为关闭或开启。<br> 初始值：OverScrollMode.NEVER。|

### func overviewModeAccess(Bool)

```cangjie
public func overviewModeAccess(overviewModeAccess: Bool): This
```

**功能：** 设置是否使用概览模式加载网页，默认使用该方式。当前仅支持移动设备。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|overviewModeAccess|Bool|是|-|设置是否使用概览模式加载网页。true表示设置使用概览模式加载网页，false表示设置不使用概览模式加载网页。<br> 初始值：true。|

### func pinchSmooth(Bool)

```cangjie
public func pinchSmooth(isEnabled: Bool): This
```

**功能：** 设置网页是否开启捏合流畅模式，默认不开启。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isEnabled|Bool|是|-|网页是否开启捏合流畅模式。true表示设置网页开启捏合流畅模式，false表示设置网页不开启捏合流畅模式。<br> 初始值：false。|