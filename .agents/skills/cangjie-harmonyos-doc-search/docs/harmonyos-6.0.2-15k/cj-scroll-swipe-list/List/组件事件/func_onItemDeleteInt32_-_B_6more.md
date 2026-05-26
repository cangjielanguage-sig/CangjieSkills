### func onItemDelete((Int32) -> Bool)

```cangjie
public func onItemDelete(callback: (Int32) -> Bool): This
```

**功能：** 当List组件在编辑模式时，点击ListItem右边出现的删除按钮时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int32)->Bool|是|-|当List组件在编辑模式时，点击ListItem右边出现的删除按钮时触发该事件。<br/>参数一：被删除的列表项的索引值。|

### func onItemDragEnter((ItemDragInfo) -> Unit)

```cangjie
public func onItemDragEnter(callback: (ItemDragInfo) -> Unit): This
```

**功能：** 拖拽进入列表元素范围内时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([ItemDragInfo](./cj-scroll-swipe-grid.md#func-onitemdragenteritemdraginfo---unit))->Unit|是|-|拖拽进入列表元素范围内时触发该事件。<br/>参数一：拖拽点的信息。|

### func onItemDragLeave((ItemDragInfo,Int32) -> Unit)

```cangjie
public func onItemDragLeave(callback: (ItemDragInfo, Int32) -> Unit): This
```

**功能：** 拖拽离开列表元素时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([ItemDragInfo](cj-scroll-swipe-grid.md#func-onitemdragleaveitemdraginfo-int32---unit),Int32)->Unit|是|-|参数一：拖拽点的信息。<br/>参数二：拖拽离开的列表元素索引值。|

### func onItemDragMove((ItemDragInfo,Int32,Int32) -> Unit)

```cangjie
public func onItemDragMove(callback: (ItemDragInfo, Int32, Int32) -> Unit): This
```

**功能：** 拖拽在列表元素范围内移动时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([ItemDragInfo](cj-scroll-swipe-grid.md#func-onitemdragmoveitemdraginfoint32int32---unit),Int32,Int32)->Unit|是|-|拖拽在列表元素范围内移动时触发该事件。<br/>参数一：拖拽点的信息。<br/>参数二：拖拽起始位置。<br/>参数三：拖拽插入位置。|

### func onItemDragStart((ItemDragInfo,Int32) -> Unit)

```cangjie
public func onItemDragStart(callback: (ItemDragInfo, Int32) -> Unit): This
```

**功能：** 开始拖拽列表元素时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([ItemDragInfo](cj-scroll-swipe-grid.md#func-onitemdragstartitemdraginfoint32---unit),Int32)->Unit|是|-|开始拖拽列表元素时触发该事件。<br/>参数一：拖拽点的信息。<br/>参数二：被拖拽列表元素索引值。|

### func onItemDragStart((ItemDragInfo,Int32) -> (() -> Unit))

```cangjie
public func onItemDragStart(callback: (ItemDragInfo, Int32) -> (() -> Unit)): This
```

**功能：** 开始拖拽列表元素时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([ItemDragInfo](cj-scroll-swipe-grid.md#func-onitemdragstartitemdraginfoint32------unit),Int32)->(()->Unit)|是|-|开始拖拽列表元素时触发该事件。<br/>参数一：拖拽点的信息。<br/>参数二：被拖拽列表元素索引值。|