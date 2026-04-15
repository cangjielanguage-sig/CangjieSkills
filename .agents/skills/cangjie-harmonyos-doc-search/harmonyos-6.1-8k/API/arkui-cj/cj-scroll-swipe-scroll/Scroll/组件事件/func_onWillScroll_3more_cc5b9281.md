### func onWillScroll(?(Float64, Float64, ScrollState, ScrollSource) -> OffsetResult)

```cangjie
public func onWillScroll(handler: ?(Float64, Float64, ScrollState, ScrollSource) -> OffsetResult): This
```

**功能：** 滚动事件回调，Scroll滚动前触发该事件。

回调当前帧将要滚动的偏移量和当前滚动状态和滚动操作来源，其中回调的偏移量为计算得到的将要滚动的偏移量值，并非最终实际滚动偏移。可以通过该回调返回值指定Scroll将要滚动的偏移。

触发该事件的条件 ：

1. 滚动组件触发滚动时触发，支持键鼠操作和其他触发滚动的输入设置。

2. 通过滚动控制器API接口调用。

3. 越界回弹。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|handler|?(Float64, Float64, [ScrollState](./cj-common-types.md#enum-scrollstate), [ScrollSource](./cj-common-types.md#enum-scrollsource)) -> [OffsetResult](#class-offsetresult)|是|-|回调函数，Scroll滚动前触发。参数一：每帧滚动时水平方向的偏移量，Scroll中的内容向左滚动时偏移量为正，向右滚动时偏移量为负。单位vp。参数二：每帧滚动时竖直方向的偏移量，Scroll中的内容向上滚动时偏移量为正，向下滚动时偏移量为负。单位vp。参数三：当前滚动状态。参数四：当前滚动操作的来源。返回值：滑动偏移量对象。返回OffsetResult时按照开发者指定的偏移量滚动。初始值：{ _, _, _, _ => OffsetResult(0.0, 0.0)}。|

### func onWillScroll(?(Float64, Float64, ScrollState, ScrollSource) -> Unit)

```cangjie
public func onWillScroll(handler: ?(Float64, Float64, ScrollState, ScrollSource) -> Unit): This
```

**功能：** 滚动事件回调，Scroll滚动前触发该事件。

回调当前帧将要滚动的偏移量和当前滚动状态和滚动操作来源，其中回调的偏移量为计算得到的将要滚动的偏移量值，并非最终实际滚动偏移。可以通过该回调返回值指定Scroll将要滚动的偏移。

触发该事件的条件 ：

1. 滚动组件触发滚动时触发，支持键鼠操作和其他触发滚动的输入设置。

2. 通过滚动控制器API接口调用。

3. 越界回弹。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|handler|?(Float64, Float64, [ScrollState](./cj-common-types.md#enum-scrollstate), [ScrollSource](./cj-common-types.md#enum-scrollsource)) -> Unit|是|-|回调函数，Scroll滚动前触发。参数一：每帧滚动时水平方向的偏移量，Scroll中的内容向左滚动时偏移量为正，向右滚动时偏移量为负。单位vp。参数二：每帧滚动时竖直方向的偏移量，Scroll中的内容向上滚动时偏移量为正，向下滚动时偏移量为负。单位vp。参数三：当前滚动状态。参数四：当前滚动操作的来源。初始值：{ _, _, _, _ => }。|

### func onDidScroll(?ScrollOnScrollCallback)

```cangjie
public func onDidScroll(callback: ?ScrollOnScrollCallback): This
```

**功能：** 滚动事件回调，Scroll滚动时触发。

返回当前帧滚动的偏移量和当前滚动状态。

触发该事件的条件 ：

1. 滚动组件触发滚动时触发，支持键鼠操作和其他触发滚动的输入设置。

2. 通过滚动控制器API接口调用。

3. 越界回弹。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[ScrollOnScrollCallback](#type-scrollonscrollcallback)|是|-|回调函数，Scroll滚动时触发。参数一：每帧滚动时水平方向的偏移量，Scroll中的内容向左滚动时偏移量为正，向右滚动时偏移量为负。单位vp。参数二：每帧滚动时竖直方向的偏移量，Scroll中的内容向上滚动时偏移量为正，向下滚动时偏移量为负。单位vp。参数三：当前滚动状态。初始值：{ _, _, _ => }。|