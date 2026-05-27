### func onScrollIndex((UInt32) -> Unit)

```cangjie
public func onScrollIndex(callback: (UInt32)-> Unit): This
```

**功能：** 当前网格显示的起始位置/终止位置的item发生变化时触发。网格初始化时会触发一次。Grid显示区域上第一个子组件/最后一个组件的索引值有变化就会触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(UInt32)->Unit|是|-|当前列表显示的起始位置 item 发生变化时触发。|

### func onScrollIndex((UInt32,UInt32) -> Unit)

```cangjie
public func onScrollIndex(callback: (UInt32, UInt32)-> Unit): This
```

**功能：** 当前网格显示的起始位置/终止位置的item发生变化时触发。网格初始化时会触发一次。Grid显示区域上第一个子组件/最后一个组件的索引值有变化就会触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(UInt32,UInt32)->Unit|是|-|当前列表显示的起始位置/终止位置 item 发生变化时触发。<br>参数一：当前显示的网格起始位置的索引值。<br>参数二：当前显示的网格终止位置的索引值。|

### func onScrollStart(() -> Unit)

```cangjie
public func onScrollStart(callback: () -> Unit): This
```

**功能：** 网格滑动开始时触发。手指拖动网格或网格的滚动条触发的滑动开始时，会触发该事件。使用[Scroller](cj-scroll-swipe-scroll.md#class-scroller)滑动控制器触发的带动画的滑动，动画开始时会触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### func onScrollStop(() -> Unit)

```cangjie
public func onScrollStop(callback: () -> Unit): This
```

**功能：** 网格滑动停止时触发。手指拖动网格或网格的滚动条触发的滑动，手指离开屏幕并且滑动停止时会触发该事件。使用[Scroller](cj-scroll-swipe-scroll.md#class-scroller)滑动控制器触发的带动画的滑动，动画停止会触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19