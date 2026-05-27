### func onWillScroll((Float64,ScrollState,ScrollSource) -> Float64)

```cangjie
public func onWillScroll(callback: (Float64, ScrollState, ScrollSource) -> Float64): This
```

**功能：** 滚动事件回调，滚动组件滚动前触发。回调当前帧将要滚动的偏移量和当前滚动状态和滚动操作来源，其中回调的偏移量为计算得到的将要滚动的偏移量值，并非最终实际滚动偏移。可以通过该回调返回值指定滚动组件将要滚动的偏移。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Float64,[ScrollState](./cj-common-types.md#enum-scrollstate),[ScrollSource](./cj-common-types.md#enum-scrollsource))->Float64|是|-|滚动组件滑动前触发的回调。<br> 参数一：每帧滑动的偏移量，滚动组件的内容向上滚动时偏移量为正，向下滚动时偏移量为负，单位vp。 <br> 参数二：当前滑动状态。 <br> 参数三：当前滑动操作的来源。<br> 返回值：将要滑动偏移量，单位vp。|

> **说明：**
>
> 调用ScrollEdge和不带动画的ScrollToIndex时，不触发onWillScroll。

### func onWillScroll((Float64,ScrollState,ScrollSource) -> Unit)

```cangjie
public func onWillScroll(callback: (Float64, ScrollState, ScrollSource) -> Unit): This
```

**功能：** 滚动事件回调，滚动组件滚动前触发。回调当前帧将要滚动的偏移量和当前滚动状态和滚动操作来源，其中回调的偏移量为计算得到的将要滚动的偏移量值，并非最终实际滚动偏移。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Float64,[ScrollState](./cj-common-types.md#enum-scrollstate),[ScrollSource](./cj-common-types.md#enum-scrollsource))->Unit|是|-|滚动组件滑动前触发的回调。|

> **说明：**
>
> 调用ScrollEdge和不带动画的ScrollToIndex时，不触发onWillScroll。

### func onScroll((OffsetResult) -> Unit)<sup>(deprecated)</sup>

```cangjie
public func onScroll(callback: (OffsetResult) -> Unit): This
```

**功能：** 滚动组件滑动时触发。Scroll组件的onScroll事件在布局之前触发，建议使用[onWillScroll](#func-onwillscrollfloat64scrollstatescrollsource---float64)替代；[List](cj-scroll-swipe-list.md)、[Grid](cj-scroll-swipe-grid.md)和[WaterFlow](cj-scroll-swipe-waterflow.md)组件的onScroll事件在布局之后触发，建议使用[onDidScroll](#func-ondidscrollscrolloffset-float64-scrollstate-scrollstate---unit)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([OffsetResult](cj-scroll-swipe-scroll.md#struct-offsetresult)) -> Unit|是|-|回调函数，Scroll滚动时触发。<br> 参数：每帧滚动时水平、竖直方向的偏移量。<br> **说明：** <br> 对于水平方向偏移量，Scroll的内容向左滚动时偏移量为正，向右滚动时偏移量为负。对于竖直方向偏移量，Scroll的内容向上滚动时偏移量为正，向下滚动时偏移量为负。单位vp。|