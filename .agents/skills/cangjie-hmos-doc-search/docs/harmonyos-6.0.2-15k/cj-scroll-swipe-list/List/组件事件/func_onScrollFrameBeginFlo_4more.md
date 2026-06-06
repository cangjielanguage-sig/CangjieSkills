### func onScrollFrameBegin((Float64,ScrollState) -> Float64)

```cangjie
public func onScrollFrameBegin(callback: (Float64, ScrollState) -> Float64): This
```

**功能：** 列表开始滑动时触发，事件参数传入即将发生的滑动量，事件处理函数中可根据应用场景计算实际需要的滑动量并作为事件处理函数的返回值返回，列表将按照返回值的实际滑动量进行滑动。

当listDirection的值为Axis.Vertical时，返回垂直方向滑动量，当listDirection的值为Axis.Horizontal时，返回水平方向滑动量。

触发该事件的条件：手指拖动List、List惯性划动时每帧开始时触发；List超出边缘回弹、使用滚动控制器和拖动滚动条的滚动不会触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Float64,[ScrollState](cj-common-types.md#enum-scrollstate))->Float64|是|-|列表开始滑动时触发。 <br/>参数一：即将发生的滑动量，单位vp。 <br/>参数二：List组件当前的滑动状态。 <br/>返回值：实际滑动量，单位vp。|

### func onScrollIndex((Int32,Int32) -> Unit)

```cangjie
public func onScrollIndex(callback: (Int32, Int32) -> Unit): This
```

**功能：** 有子组件划入或划出List显示区域时触发。计算索引值时，ListItemGroup作为一个整体占一个索引值，不计算ListItemGroup内部ListItem的索引值。

List的边缘效果为弹簧效果时，在List划动到边缘继续划动和松手回弹过程不会触发onScrollIndex事件。

触发该事件的条件：列表初始化时会触发一次，List显示区域内第一个子组件的索引值或最后一个子组件的索引值有变化时会触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int32,Int32)->Unit|是|-|有子组件划入或划出List显示区域时触发。<br/>参数一：List显示区域内第一个子组件的索引值。<br/>参数二：List显示区域内最后一个子组件的索引值。|

### func onScrollIndex((Int32,Int32,Int32) -> Unit)

```cangjie
public func onScrollIndex(callback: (Int32, Int32, Int32) -> Unit): This
```

**功能：** 列表滑动开始时触发。手指拖动列表或列表的滚动条触发的滑动开始时，会触发该事件。使用Scroller滑动控制器触发的带动画的滑动，动画开始时会触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int32,Int32,Int32)->Unit|是|-|列表滑动事件回调。<br/>参数一：List显示区域内第一个子组件的索引值。<br/>参数二：List显示区域内最后一个子组件的索引值。<br/>参数三：List显示区域内中间位置子组件的索引值。|

### func onScrollStart(() -> Unit)

```cangjie
public func onScrollStart(callback: () -> Unit): This
```

**功能：** 列表滑动开始时触发。手指拖动列表或列表的滚动条触发的滑动开始时，会触发该事件。使用[Scroller](./cj-scroll-swipe-scroll.md#class-scroller)滑动控制器触发的带动画的滑动，动画开始时会触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|列表滑动开始事件回调。手指拖动列表或列表的滚动条触发的滑动开始时，会触发该事件。使用[Scroller](./cj-scroll-swipe-scroll.md#class-scroller)滑动控制器触发的带动画的滑动，动画开始时会触发该事件。|