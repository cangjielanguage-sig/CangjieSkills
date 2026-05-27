### func onItemDrop((ItemDragInfo,Int32,Int32,Bool) -> Unit)

```cangjie
public func onItemDrop(callback: (ItemDragInfo, Int32, Int32, Bool) -> Unit): This
```

**功能：** 绑定该事件的列表元素可作为拖拽释放目标，当在列表元素内停止拖拽时触发该事件。

跨List拖拽时，当拖拽释放的位置绑定了onItemDrop时， Bool会返回true，否则为false。List内部拖拽时，Bool为onItemMove事件的返回值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([ItemDragInfo](cj-scroll-swipe-grid.md#func-onitemdropitemdraginfoint32int32bool---unit),Int32,Int32,Bool)->Unit|是|-|参数一：拖拽点的信息。<br/>参数二：拖拽起始位置。<br/>参数三：拖拽插入位置。<br/>参数四：是否成功释放。|

### func onItemMove((Int32,Int32) -> Bool)

```cangjie
public func onItemMove(callback: (start: Int32, end: Int32) -> Bool): This
```

**功能：** 列表元素发生移动时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(start: Int32, end: Int32) -> Bool|是|-|列表元素发生移动时触发该事件。<br/>参数一：移动前索引值。<br/>参数二：移动后索引值。<br/>返回值：是否已经移动。返回值为true时列表元素发生移动，返回值为false时列表元素没有移动。|

### func onReachEnd(() -> Unit)

```cangjie
public func onReachEnd(callback: () -> Unit): This
```

**功能：** 列表到底末尾位置时触发该事件。List边缘效果为弹簧效果时，划动经过末尾位置时触发一次，回弹回末尾位置时再触发一次。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|列表到底末尾位置事件回调。|

### func onReachStart(() -> Unit)

```cangjie
public func onReachStart(callback: () -> Unit): This
```

**功能：** 列表到达起始位置时触发该事件。List初始化时如果initialIndex为0会触发一次，List滚动到起始位置时触发一次。List边缘效果为弹簧效果时，划动经过起始位置时触发一次，回弹回起始位置时再触发一次。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|列表到达起始位置事件回调。|

### func onScroll((Float64,ScrollState) -> Unit)

```cangjie
public func onScroll(callback: (Float64, ScrollState) -> Unit): This
```

**功能：** 列表滑动时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Float64,[ScrollState](cj-common-types.md#enum-scrollstate))->Unit|是|-|列表滑动时触发该事件。 <br/>参数一：每帧滚动的偏移量，List的内容向上滚动时偏移量为正，向下滚动时偏移量为负。单位vp。 <br/>参数二：当前滑动状态。|