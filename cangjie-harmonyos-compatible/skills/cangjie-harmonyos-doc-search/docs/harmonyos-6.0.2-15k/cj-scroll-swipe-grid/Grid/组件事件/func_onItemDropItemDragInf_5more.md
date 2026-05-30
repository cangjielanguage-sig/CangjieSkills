### func onItemDrop((ItemDragInfo,Int32,Int32,Bool) -> Unit)

```cangjie
public func onItemDrop(callback: (ItemDragInfo, Int32, Int32, Bool) -> Unit): This
```

**功能：** 绑定该事件的网格元素可作为拖拽释放目标，当GridItem停止拖拽时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([ItemDragInfo](cj-scroll-swipe-common.md#class-itemdraginfo),Int32,Int32,Bool)->Unit|是|-|绑定该事件的网格元素可作为拖拽释放目标，当GridItem停止拖拽时触发。<br/> 参数一：拖拽点的信息。 <br/> 参数二：拖拽起始位置。 <br/> 参数三：拖拽插入位置。 <br/> 参数四：是否成功释放。当拖拽释放位置在网格元素之内时，会返回true；在网格元素之外时，会返回false。|

### func onReachEnd(() -> Unit)

```cangjie
public func onReachEnd(callback: () -> Unit): This
```

**功能：** 网格到达末尾位置时触发。

Grid边缘效果为弹簧效果时，划动经过末尾位置时触发一次，回弹回末尾位置时再触发一次。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### func onReachStart(() -> Unit)

```cangjie
public func onReachStart(callback: () -> Unit): This
```

**功能：** 网格到达起始位置时触发。

Grid初始化时会触发一次，Grid滚动到起始位置时触发一次。Grid边缘效果为弹簧效果时，划动经过起始位置时触发一次，回弹回起始位置时再触发一次。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### func onScrollBarUpdate((Int32,Float64) -> ComputedBarAttribute)

```cangjie
public func onScrollBarUpdate(callback: (Int32, Float64) -> ComputedBarAttribute): This
```

**功能：** 在Grid每帧布局结束时触发，可通过该回调设置滚动条的位置及长度。

该接口只用作设置Grid的滚动条位置，不建议开发者在此接口中做业务逻辑处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int32,Float64)->[ComputedBarAttribute](#struct-computedbarattribute)|是|-|在Grid每帧布局结束时触发，可通过该回调设置滚动条的位置及长度。<br/> 参数一：当前显示的网格起始位置的索引值。 <br/> 参数二：当前显示的网格起始位置元素相对网格显示起始位置的偏移，单位vp。|

**返回值：**

|类型|说明|
|:---|:---|
|[ComputedBarAttribute](#struct-computedbarattribute)|滚动条的位置及长度。|

### func onScrollFrameBegin((Float64,ScrollState) -> OffsetOption)

```cangjie
public func onScrollFrameBegin(callback: (Float64, ScrollState) -> OffsetOption): This
```

**功能：** 网格开始滑动时触发，事件参数传入即将发生的滑动量，事件处理函数中可根据应用场景计算实际需要的滑动量并作为事件处理函数的返回值返回，网格将按照返回值的实际滑动量进行滑动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Float64,[ScrollState](./cj-common-types.md#enum-scrollstate))->[OffsetOption](#struct-offsetoption)|是|-|网格开始滑动时触发。<br/> 参数一：即将发生的滑动量，单位vp。<br/> 参数二：当前滑动状态。|

**返回值：**

|类型|说明|
|:---|:---|
|[OffsetOption](#struct-offsetoption)|实际滑动量，单位vp。|