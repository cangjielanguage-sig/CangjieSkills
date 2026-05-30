## class LongPressGestureHandler

```cangjie
public class LongPressGestureHandler <: GestureHandler {}
```

**功能：** 长按手势处理器配置参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [GestureHandler](#class-gesturehandler)

### init(Int32, Bool, Int32)

```cangjie
public init(fingers!: Int32 = 1, repeat!: Bool = false, duration!: Int32 = 500)
```

**功能：** 创建一个长按手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fingers|Int32|否|1| **命名参数。** 触发长按的最少手指数，最小为1指， 最大取值为10指。<br/> **说明：** <br/> 手指按下后若发生超过15px的移动，则判定当前长按手势识别失败。|
|repeat|Bool|否|false| **命名参数。** 是否连续触发事件回调。|
|duration|Int32|否|500| **命名参数。** 触发长按的最短时间，单位为毫秒（ms）。<br/>**说明：** <br/>设置小于等于0时，按照默认值500处理。|

### func onAction((GestureEvent) -> Unit)

```cangjie
public func onAction(callback: (GestureEvent) -> Unit): This
```

**功能：** LongPress手势识别成功触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|LongPress手势识别成功触发该回调。|

### func onActionEnd((GestureEvent) -> Unit)

```cangjie
public func onActionEnd(callback: (GestureEvent) -> Unit): This
```

**功能：** LongPress手势识别成功，最后一根手指抬起后触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|LongPress手势识别成功，最后一根手指抬起后触发该回调。|

### func onActionCancel((GestureEvent) -> Unit)

```cangjie
public func onActionCancel(callback: (GestureEvent) -> Unit): This
```

**功能：** LongPress手势识别成功，接收到触摸取消事件触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|LongPress手势识别成功，接收到触摸取消事件触发该回调。|