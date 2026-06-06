### func onReachEnd(() -> Unit)

```cangjie
public func onReachEnd(callback: () -> Unit): This
```

**功能：** 瀑布流组件到底末尾位置时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|网瀑布流组件到底末尾位置时触发该事件。|

### func onReachStart(() -> Unit)

```cangjie
public func onReachStart(callback: () -> Unit): This
```

**功能：** 瀑布流组件到达起始位置时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|瀑布流组件到达起始位置时触发该事件。|

### func onScrollFrameBegin((Float64,ScrollState) -> Float64)

```cangjie
public func onScrollFrameBegin(callback: (Float64, ScrollState) -> Float64): This
```

**功能：** 瀑布流开始滑动时触发，事件参数传入即将发生的滑动量，事件处理函数中可根据应用场景计算实际需要的滑动量并作为事件处理函数的返回值返回，瀑布流将按照返回值的实际滑动量进行滑动。

触发该事件的条件：手指拖动WaterFlow、WaterFlow惯性划动时每帧开始时触发；WaterFlow超出边缘回弹、使用滚动控制器和拖动滚动条的滚动不会触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Float64,[ScrollState](cj-common-types.md#enum-scrollstate))->Float64|是|-|瀑布流开始滑动时触发的回调函数。<br/>参数一：即将发生的滑动量，单位vp。<br/>参数二：当前滑动状态。|

### func onScrollIndex((Int32,Int32) -> Unit)

```cangjie
public func onScrollIndex(callback: (Int32, Int32) -> Unit): This
```

**功能：** 当前瀑布流显示的起始位置/终止位置的子组件发生变化时触发。瀑布流初始化时会触发一次。

瀑布流显示区域上第一个子组件/最后一个组件的索引值有变化就会触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int32,Int32)->Unit|是|-|当前瀑布流显示的起始位置/终止位置的子组件发生变化时触发的回调函数。<br/>参数一：当前显示的瀑布流起始位置的索引值。<br/>取值范围：[0, 子节点总数-1]。<br/>参数二：当前显示的瀑布流终止位置的索引值。<br/>取值范围：[0, 子节点总数-1]。|