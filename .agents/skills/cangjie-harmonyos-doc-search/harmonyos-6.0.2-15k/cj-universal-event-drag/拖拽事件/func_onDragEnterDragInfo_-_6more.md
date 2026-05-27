## func onDragEnter((DragInfo) -> Unit)

```cangjie
public func onDragEnter(callback: (DragInfo)->Unit): This
```

**功能：** 拖拽进入组件范围内时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

> **说明：**
>
> 当监听了onDrop事件时，此事件才有效。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([DragInfo](#class-draginfo))->Unit|是|-|拖拽进入组件范围回调函数。|

## func onDragEnter((DragEvent, ?String) -> Unit)

```cangjie
public func onDragEnter(callback: (DragEvent, ?String)->Unit): This
```

**功能：** 拖拽进入组件范围内时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([DragEvent](#class-dragevent),?String)->Unit|是|-| 回调函数。<br/>第一个参数为拖拽事件信息，包括拖拽点坐标。<br/> 第二个参数为拖拽事件额外信息，需要解析为Json格式，参考[extraParams说明](#extraparams说明)。|

## func onDragMove((DragEvent, ?String) -> Unit)

```cangjie
public func onDragMove(callback: (DragEvent, ?String)->Unit): This
```

**功能：** 拖拽在组件范围内移动时，触发回调，当监听了onDrop事件时，此事件才有效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([DragEvent](#class-dragevent), ?String)->Unit|是|-|回调函数，拖拽进入组件范围移动时触发。<br/>第一个参数为拖拽事件信息，包括拖拽点坐标。<br/> 第二个参数为拖拽事件额外信息，需要解析为Json格式，参考[extraParams说明](#extraparams说明)。|

## func onDragMove((DragInfo) -> Unit)

```cangjie
public func onDragMove(callback: (DragInfo)->Unit): This
```

**功能：** 拖拽在组件范围内移动时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

> **说明：**
>
> 当监听了onDrop事件时，此事件才有效。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([DragInfo](#class-draginfo))->Unit|是|-|回调函数，拖拽进入组件范围移动时触发。|

## func onDragLeave((DragEvent, ?String) -> Unit)

```cangjie
public func onDragLeave(callback: (DragEvent, ?String)->Unit): This
```

**功能：** 拖拽离开组件范围内时，触发回调，当监听了onDrop事件时，此事件才有效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([DragEvent](#class-dragevent), ?String)->Unit|是|-|回调函数，拖拽进入组件范围移动时触发。<br/>第一个参数为拖拽事件信息，包括拖拽点坐标。<br/> 第二个参数为拖拽事件额外信息，需要解析为Json格式，参考[extraParams说明](#extraparams说明)。|

## func onDragLeave((DragInfo) -> Unit)

```cangjie
public func onDragLeave(callback: (DragInfo)->Unit): This
```

**功能：** 拖拽离开组件范围内时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

> **说明：**
>
> 当监听了onDrop事件时，此事件才有效。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([DragInfo](#class-draginfo))->Unit|是|-|回调函数，拖拽离开组件范围时触发。<br/>传入参数为拖拽事件信息，包括拖拽点坐标。|