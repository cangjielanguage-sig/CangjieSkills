## func onDragStart((DragInfo) -> (() -> Unit))

```cangjie
public func onDragStart(callback: (DragInfo)-> (() -> Unit)): This
```

**功能：** 重载拖拽事件，第一次拖拽此事件绑定的组件时，长按时间 >= 500ms，然后手指移动距离 >= 10vp，触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([DragInfo](#class-draginfo))|是|-|回调函数，拖拽开始时触发。<br/>传入参数为拖拽事件信息，包括拖拽点坐标。<br/>返回参数为拖拽过程中显示的组件信息，使用时结合[@Builder](../../../Dev_Guide/arkui-cj/paradigm/cj-macro-builder.md)和[bind](./cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。|

## func onDragStart((DragInfo) -> Unit)

```cangjie
public func onDragStart(callback: (DragInfo)-> Unit): This
```

**功能：** 重载拖拽事件，第一次拖拽此事件绑定的组件时，长按时间 >= 500ms，然后手指移动距离 >= 10vp，触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([DragInfo](#class-draginfo))->Unit|是|-|回调函数，拖拽开始时触发。<br/>传入参数为拖拽事件信息，包括拖拽点坐标。<br/>返回参数为拖拽过程中显示的组件信息。|

## func onDragStart((DragEvent, ?String) -> DragItemInfo)

```cangjie
public func onDragStart(callback: (DragEvent, ?String)->DragItemInfo): This
```

**功能：** 重载拖拽事件，第一次拖拽此事件绑定的组件时，长按时间 >= 500ms，然后手指移动距离 >= 10vp，触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([DragEvent](#class-dragevent), ?String)->[DragItemInfo](#struct-dragiteminfo)|是|-|回调函数。<br/>第一个参数为拖拽事件信息，包括拖拽点坐标。<br/> 第二个参数为拖拽事件额外信息，需要解析为Json格式，参考[extraParams说明](#extraparams说明)。<br/>返回参数为拖拽过程中显示的组件信息。|

## func onDragStart((DragEvent, ?String) -> (() -> Unit))

```cangjie
public func onDragStart(callback: (DragEvent, ?String)->(()->Unit)): This
```

**功能：** 重载拖拽事件，第一次拖拽此事件绑定的组件时，长按时间 >= 500ms，然后手指移动距离 >= 10vp，触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([DragEvent](#class-dragevent), ?String)->(()->Unit)|是|-|回调函数。<br/>第一个参数为拖拽事件信息，包括拖拽点坐标。<br/> 第二个参数为拖拽事件额外信息，需要解析为Json格式，参考[extraParams说明](#extraparams说明)。|

## func onDragStart((DragEvent, ?String) -> Unit)

```cangjie
public func onDragStart(callback: (DragEvent, ?String)->Unit): This
```

**功能：** 重载拖拽事件，第一次拖拽此事件绑定的组件时，长按时间 >= 500ms，然后手指移动距离 >= 10vp，触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([DragEvent](#class-dragevent), ?String)->Unit|是|-|回调函数。<br/>第一个参数为拖拽事件信息，包括拖拽点坐标。<br/> 第二个参数为拖拽事件额外信息，需要解析为Json格式，参考[extraParams说明](#extraparams说明)。|