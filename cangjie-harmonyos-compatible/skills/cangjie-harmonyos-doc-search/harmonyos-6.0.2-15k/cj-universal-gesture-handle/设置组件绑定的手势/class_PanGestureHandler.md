## class PanGestureHandler

```cangjie
public class PanGestureHandler <: GestureHandler {}
```

**功能：** 拖动手势处理器对象类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [GestureHandler](#class-gesturehandler)

### init(Int32, Bool, Float64)

```cangjie
public init(fingers!: Int32 = 1, direction!: PanDirection = PanDirection.All, distance!: Float64 = 5.0)
```

**功能：** 创建一个拖动手势处理器。

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fingers|Int32|否|1| **命名参数。** 触发长按的最少手指数，最小为1指，最大取值为10指。<br/>**说明：**<br/>手当设置的值小于1或不设置时，会被转化为默认值。|
|direction|[PanDirection](./cj-universal-gesture-pangesture.md#enum-pandirection)|否|PanDirection.All|用于指定触发拖动的手势方向，此枚举值支持逻辑与(&)和逻辑或(\| **命名参数。** )运算。|
|distance|Float64|否|5.0| **命名参数。** 用于指定触发拖动手势事件的最小拖动距离，单位为vp。<br/>**说明：**<br/>当设定的值小于0时，按默认值5处理。|

### func onActionStart((GestureEvent) -> Unit)

```cangjie
public func onActionStart(callback: (GestureEvent) -> Unit): This
```

**功能：** Pan手势识别成功触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|Pan手势识别成功触发该回调。|

### func onActionUpdate((GestureEvent) -> Unit)

```cangjie
public func onActionUpdate(callback: (GestureEvent) -> Unit): This
```

**功能：** Pan手势移动过程中触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|Pan手势移动过程中回调。|

### func onActionEnd((GestureEvent) -> Unit)

```cangjie
public func onActionEnd(callback: (GestureEvent) -> Unit): This
```

**功能：** Pan手势识别成功，手指抬起后触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|Pan手势识别成功，手指抬起后触发该回调。|

### func onActionCancel((GestureEvent) -> Unit)

```cangjie
public func onActionCancel(callback: (GestureEvent) -> Unit): This
```

**功能：** Pan手势识别成功，接收到触摸取消事件触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|Pan手势识别成功，接收到触摸取消事件触发该回调。|