### func onItemDragEnter((ItemDragInfo) -> Unit)

```cangjie
public func onItemDragEnter(callback: (ItemDragInfo) -> Unit): This
```

**功能：** 拖拽进入网格元素范围内时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([ItemDragInfo](cj-scroll-swipe-common.md#class-itemdraginfo))->Unit|是|-|拖拽进入网格元素范围内时触发。<br/> 参数一：拖拽点的信息。|

### func onItemDragLeave((ItemDragInfo, Int32) -> Unit)

```cangjie
public func onItemDragLeave(callback: (ItemDragInfo, Int32) -> Unit): This
```

**功能：** 拖拽离开网格元素时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([ItemDragInfo](cj-scroll-swipe-common.md#class-itemdraginfo),Int32)->Unit|是|-|拖拽离开网格元素时触发。<br/> 参数一：拖拽点的信息。 <br/> 参数二：拖拽离开的网格元素索引值。|

### func onItemDragMove((ItemDragInfo,Int32,Int32) -> Unit)

```cangjie
public func onItemDragMove(callback: (ItemDragInfo, Int32, Int32) -> Unit): This
```

**功能：** 拖拽在网格元素范围内移动时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([ItemDragInfo](cj-scroll-swipe-common.md#class-itemdraginfo),Int32,Int32)->Unit|是|-|拖拽在网格元素范围内移动时触发。<br/> 参数一：拖拽点的信息。 <br/> 参数二：拖拽起始位置。<br/> 参数三：拖拽插入位置。|

### func onItemDragStart((ItemDragInfo,Int32) -> Unit)

```cangjie
public func onItemDragStart(callback: (ItemDragInfo, Int32) -> Unit): This
```

**功能：** 开始拖拽网格元素时触发。返回Unit表示不能拖拽。

手指长按GridItem时触发该事件。

由于拖拽检测也需要长按，且事件处理机制优先触发子组件事件，GridItem上绑定LongPressGesture时无法触发拖拽。如有长按和拖拽同时使用的需求可以使用通用拖拽事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([ItemDragInfo](cj-scroll-swipe-common.md#class-itemdraginfo),Int32)->Unit|是|-|开始拖拽网格元素时触发。<br>参数一：拖拽点的信息。<br>参数二：被拖拽网格元素索引值。|

### func onItemDragStart((ItemDragInfo,Int32) -> (() -> Unit))

```cangjie
public func onItemDragStart(callback: (ItemDragInfo, Int32) -> (() -> Unit)): This
```

**功能：** 开始拖拽网格元素时触发。返回() -> Unit表示能拖拽。

手指长按GridItem时触发该事件。

由于拖拽检测也需要长按，且事件处理机制优先触发子组件事件，GridItem上绑定LongPressGesture时无法触发拖拽。如有长按和拖拽同时使用的需求可以使用通用拖拽事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([ItemDragInfo](cj-scroll-swipe-common.md#class-itemdraginfo),Int32)->(()->Unit)|是|-|开始拖拽网格元素时触发。<br>参数一：拖拽点的信息。<br>参数二：被拖拽网格元素索引值。|