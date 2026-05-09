### func onWillScroll(Option\<(Float64,ScrollState,ScrollSource) -> ScrollResult>)

```cangjie
public func onWillScroll(handler: Option<(Float64, ScrollState, ScrollSource) -> ScrollResult>): T
```

**功能：** 滚动事件回调，滚动组件滚动前触发。回调当前帧将要滚动的偏移量和当前滚动状态和滚动操作来源，其中回调的偏移量为计算得到的将要滚动的偏移量值，并非最终实际滚动偏移。可以通过该回调返回值指定滚动组件将要滚动的偏移。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|handler|Option\<(Float64, [ScrollState](./cj-common-types.md#enum-scrollstate), [ScrollSource](./cj-common-types.md#enum-scrollsource)) -> [ScrollResult](./cj-scroll-swipe-scroll.md#class-scrollresult)>|是|-|滚动组件滑动前触发的回调。<br> 参数一：每帧滑动的偏移量，滚动组件的内容向上滚动时偏移量为正，向下滚动时偏移量为负，单位vp。 <br> 参数二：当前滑动状态。 <br> 参数三：当前滑动操作的来源。<br> 返回值：将要滑动偏移量，单位vp。|

> **说明：**
>
> 调用scrollEdge和不带动画的scrollToIndex时，不触发onWillScroll。

**返回值：**

|类型|说明|
|:----|:----|
|T|返回组件实例。|

### func onWillScroll(Option\<(Float64,ScrollState,ScrollSource) -> Unit>)

```cangjie
public func onWillScroll(handler: Option<(Float64, ScrollState, ScrollSource) -> Unit>): T
```

**功能：** 滚动事件回调，滚动组件滚动前触发。回调当前帧将要滚动的偏移量和当前滚动状态和滚动操作来源，其中回调的偏移量为计算得到的将要滚动的偏移量值，并非最终实际滚动偏移。

> **说明：**
>
> 调用scrollEdge和不带动画的scrollToIndex时，不触发onWillScroll。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|handler|Option<(Float64, [ScrollState](./cj-common-types.md#enum-scrollstate), [ScrollSource](./cj-common-types.md#enum-scrollsource)) -> Unit>|是|-|滚动组件滑动前触发的回调。|

**返回值：**

|类型|说明|
|:----|:----|
|T|返回组件实例。|