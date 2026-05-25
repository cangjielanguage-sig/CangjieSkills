### func onDidScroll((scrollOffset: Float64, scrollState: ScrollState) -> Unit)

```cangjie
public func onDidScroll(callback: (scrollOffset: Float64, scrollState: ScrollState) -> Unit): This
```

**功能：** 滚动组件滑动时触发，返回当前帧滑动的偏移量和当前滑动状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(scrollOffset:Float64, [scrollState:ScrollState](./cj-common-types.md#enum-scrollstate))->Unit|是|-|滚动组件滑动时触发的回调。<br> 参数一：每帧滚动的偏移量，滚动组件的内容向上滚动时偏移量为正，向下滚动时偏移量为负。单位vp。 <br> 参数二：当前滑动状态。|

### func onReachEnd(() -> Unit)

```cangjie
public func onReachEnd(callback: () -> Unit): This
```

**功能：** 滚动组件到达末尾位置时触发。滚动组件边缘效果为弹簧效果时，划动经过末尾位置时触发一次，回弹回末尾位置时再触发一次。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，滚动组件到达末尾位置时触发。|

### func onReachStart(() -> Unit)

```cangjie
public func onReachStart(callback: () -> Unit): This
```

**功能：** 滚动组件到达起始位置时触发。滚动组件初始化时会触发一次，滚动到起始位置时触发一次。边缘效果为弹簧效果时，划动经过起始位置时触发一次，回弹回起始位置时再触发一次。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，滚动组件到达起始位置时触发。|

### func onScrollStart(() -> Unit)

```cangjie
public func onScrollStart(callback: () -> Unit): This
```

**功能：** 滚动开始时触发。手指拖动滚动组件或拖动滚动组件的滚动条触发的滚动开始时，会触发该事件。使用[Scroller](./cj-scroll-swipe-scroll.md#class-scroller)滚动控制器触发的带动画的滚动，动画开始时会触发该事件。

触发该事件的条件：<br>

1、滚动组件开始滚动时触发，支持键鼠操作等其他触发滚动的输入设置。<br>

2、通过滚动控制器API接口调用后开始，带过渡动效。

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

**功能：** 滚动停止时触发。手拖动滚动组件或拖动滚动组件的滚动条触发的滚动，手离开屏幕并且滚动停止时会触发该事件。使用[Scroller](./cj-scroll-swipe-scroll.md#class-scroller)滚动控制器触发的带动画的滚动，动画停止时会触发该事件。

触发该事件的条件：<br>

1、滚动组件触发滚动后停止，支持键鼠操作等其他触发滚动的输入设置。<br>

2、通过滚动控制器API接口调用后开始，带过渡动效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，滚动停止时触发。|