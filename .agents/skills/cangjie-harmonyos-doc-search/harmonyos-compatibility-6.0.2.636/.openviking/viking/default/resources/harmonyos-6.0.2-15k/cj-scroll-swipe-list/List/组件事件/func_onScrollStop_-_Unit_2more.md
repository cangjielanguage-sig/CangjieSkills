### func onScrollStop(() -> Unit)

```cangjie
public func onScrollStop(callback: () -> Unit): This
```

**功能：** 列表滑动停止时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|列表滑动停止事件回调。手拖动列表或列表的滚动条触发的滑动，手离开屏幕并且滑动停止时会触发该事件；使用[Scroller](./cj-scroll-swipe-scroll.md#class-scroller)滑动控制器触发的滑动，不会触发该事件。|

### func onScrollVisibleContentChange((VisibleListContentInfo,VisibleListContentInfo) -> Unit)

```cangjie
public func onScrollVisibleContentChange(callback: (VisibleListContentInfo, VisibleListContentInfo) -> Unit): This
```

**功能：** 有子组件划入或划出List显示区域时触发。计算触发条件时，每一个ListItem、ListItemGroup中的header或footer都算一个子组件。

List的边缘效果为弹簧效果时，在List划动到边缘继续划动和松手回弹过程不会触发onScrollVisibleContentChange事件。

触发该事件的条件：列表初始化时会触发一次，List显示区域内第一个子组件的索引值或最后一个子组件的索引值有变化时会触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([VisibleListContentInfo](#class-visiblelistcontentinfo),[VisibleListContentInfo](#class-visiblelistcontentinfo))->Unit|是|-|当前显示内容发生改变的时候触发回调。<br/>参数一：<br/>1. 通过该参数获取List显示区域第一个子组件在List中的索引值。<br/>2. 如果当前List显示区域第一个子组件是ListItemGroup，可以获取当前List显示区域第一个组件属于该ListItemGroup的哪一区域。<br/>3. 如果当前List显示区域第一个组件是ListItemGroup内的ListItem，可以获取该ListItem在ListItemGroup内的索引值。<br/>参数二：<br/>1. 通过该参数获取List显示区域最后一个子组件在List中的索引值。<br/>2. 如果当前List显示区域最后一个子组件是ListItemGroup，可以获取当前List显示区域最后一个组件属于该ListItemGroup的哪一区域。<br/>3. 如果当前List显示区域最后一个组件是ListItemGroup内的ListItem，可以获取该ListItem在ListItemGroup内的索引值。|