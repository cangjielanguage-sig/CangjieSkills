## func onDrop((DragEvent, ?String) -> Unit)

```cangjie
public func onDrop(callback: (DragEvent, ?String)->Unit): This
```

**功能：** 绑定此事件的组件可作为拖拽释放目标，当在本组件范围内停止拖拽行为时，触发回调。如果开发者没有在onDrop中主动调用event.setResult()设置拖拽接收的结果，若拖拽组件为系统支持默认拖入的组件，以系统实际处理数据结果为准，其它组件则系统按照数据接收成功处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([DragEvent](#class-dragevent), ?String)->Unit|是|-|回调函数，本组件范围内停止拖拽行为时触发。<br/>第一个参数为拖拽事件信息，包括拖拽点坐标。<br/> 第二个参数为拖拽事件额外信息，需要解析为Json格式，参考[extraParams说明](#extraparams说明)。|

## func onDrop((DragInfo) -> Unit)

```cangjie
public func onDrop(callback: (DragInfo)->Unit): This
```

**功能：** 绑定此事件的组件可作为拖拽释放目标，当在本组件范围内停止拖拽行为时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([DragInfo](#class-draginfo))->Unit|是|-|回调函数，本组件范围内停止拖拽行为时触发。<br/>传入参数为拖拽事件信息，包括拖拽点坐标。|

## func onDragEnd((DragEvent, ?String) -> Unit)

```cangjie
public func onDragEnd(callback: (DragEvent, ?String)->Unit): This
```

**功能：** 绑定此事件的组件触发的拖拽结束后，触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([DragEvent](#class-dragevent), ?String)->Unit|是|-|回调函数，拖拽结束后触发。<br/>第一个参数为拖拽事件信息，包括拖拽点坐标。<br/> 第二个参数为拖拽事件额外信息，需要解析为Json格式，参考[extraParams说明](#extraparams说明)。|

## func onPreDrag((PreDragStatus) -> Unit)

```cangjie
public func onPreDrag(callback: (PreDragStatus)->Unit): This
```

**功能：** 绑定此事件的组件，当触发拖拽发起前的不同阶段时，触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([PreDragStatus](#enum-predragstatus))->Unit|是|-|回调函数，拖拽发起前触发。|

## extraParams说明

用于返回组件在拖拽中需要用到的额外信息。

extraParams是Json对象转换的String字符串。通过Json库转换后可以获取如下属性。

| 参数名      | 参数类型       | 描述              |
|:---------|:-----------|:----------------|
| selectedIndex | Int64 | 当拖拽事件设在父容器的子元素时，selectedIndex表示当前被拖拽子元素是父容器第selectedIndex个子元素，selectedIndex从0开始。<br/>仅在ListItem组件的拖拽事件中生效。|
| insertIndex | Int64 | 当前拖拽元素在List组件中放下时，insertIndex表示被拖拽元素插入该组件的第insertIndex个位置，insertIndex从0开始。<br/>仅在List组件的拖拽事件中生效。|