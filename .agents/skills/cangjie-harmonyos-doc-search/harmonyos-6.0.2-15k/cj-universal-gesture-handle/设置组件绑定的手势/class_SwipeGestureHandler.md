## class SwipeGestureHandler

```cangjie
public class SwipeGestureHandler <: GestureHandler {}
```

**功能：** 滑动手势处理器对象类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [GestureHandler](#class-gesturehandler)

### init(Int32, SwipeDirection, Float64)

```cangjie
public init(fingers!: Int32 = 1, direction!: SwipeDirection = SwipeDirection.All, speed!: Float64 = 100.0)
```

**功能：** 创建一个滑动手势处理器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fingers|Int32|否|1| **命名参数。** 触发滑动的最少手指数，默认为1，最小为1指，最大为10指。|
|direction|[SwipeDirection](./cj-universal-gesture-swipegesture.md#enum-SwipeDirection)|否|SwipeDirection.All| **命名参数。** 触发滑动手势的滑动方向。|
|speed|Float64|否|100.0| **命名参数。** 识别滑动的最小速度。<br/>**说明：** 当滑动速度的值小于等于0时，会被转化为默认值。|

### func onAction((GestureEvent) -> Unit)

```cangjie
public func onAction(callback: (GestureEvent) -> Unit): This
```

**功能：** Swipe手势识别成功触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|Swipe手势识别成功触发该回调。|