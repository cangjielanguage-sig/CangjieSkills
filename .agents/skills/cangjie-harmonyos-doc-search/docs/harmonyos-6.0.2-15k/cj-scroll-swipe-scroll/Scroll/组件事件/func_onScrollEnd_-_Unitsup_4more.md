### func onScrollEnd(() -> Unit)<sup>deprecated</sup>

```cangjie
public func onScrollEnd(callback: () -> Unit): This
```

**功能：** 滚动停止时触发该事件。

触发该事件的条件 ：

1. 滚动组件触发滚动后停止，支持键鼠操作和其他触发滚动的输入设置。

2. 通过滚动控制器API接口调用后停止，带过渡动效。

该事件已废弃，可使用onScrollStop事件替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，滚动停止时触发。|

### func onScrollFrameBegin((Float64,ScrollState) -> Float64)

```cangjie
public func onScrollFrameBegin(callback: (Float64, ScrollState) -> Float64): This
```

**功能：** 每帧开始滚动时触发该事件，事件参数传入即将发生的滚动量，事件处理函数中可根据应用场景计算实际需要的滚动量并作为事件处理函数的返回值返回，Scroll将按照返回值的实际滚动量进行滚动。

支持offsetRemain为负值。

若通过onScrollFrameBegin事件和scrollBy方法实现容器嵌套滚动，需设置子滚动节点的EdgeEffect为None。如Scroll嵌套List滚动时，List组件的edgeEffect属性需设置为EdgeEffect.None。

触发该事件的条件：

1. 滚动组件触发滚动时触发，包括键鼠操作和其他触发滚动的输入设置。

2. 调用控制器接口时不触发。

3. 越界回弹不触发。

4. 拖动滚动条不触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Float64,[ScrollState](./cj-common-types.md#enum-scrollstate))->Float64|是|-|回调函数，每帧开始滚动时触发。<br>参数一：即将发生的滑动量，单位vp。<br>参数二：当前滑动状态。|

### func onScrollStart(() -> Unit)

```cangjie
public func onScrollStart(callback: () -> Unit): This
```

**功能：** 滚动开始时触发该事件。手指拖动Scroll或拖动Scroll的滚动条触发的滚动开始时，会触发该事件。使用[Scroller](#class-scroller)滚动控制器触发的带动画的滚动，动画开始时会触发该事件。

触发该事件的条件 ：

1. 滚动组件开始滚动时触发，支持键鼠操作和其他触发滚动的输入设置。

2. 通过滚动控制器API接口调用后开始，带过渡动效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，滚动开始时触发。|

### func onScrollStop(() -> Unit)

```cangjie
public func onScrollStop(callback: () -> Unit): This
```

**功能：** 滚动停止时触发该事件。手拖动Scroll或拖动Scroll的滚动条触发的滚动，手离开屏幕并且滚动停止时会触发该事件。使用Scroller滚动控制器触发的带动画的滚动，动画停止时会触发该事件。

触发该事件的条件 ：

1. 滚动组件触发滚动后停止，支持键鼠操作和其他触发滚动的输入设置。

2. 通过滚动控制器API接口调用后开始，带过渡动效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，滚动停止时触发。|