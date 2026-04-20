# PanGesture

滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件

## 创建组件

### init(Int32, PanDirection, Float64)

```cangjie
public init(fingers!: Int32 = 1, direction!: PanDirection = PanDirection.All, distance!: Float64 = 5.0)
```

**功能：** 创建一个滑动手势。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fingers|Int32|否|1| **命名参数。** 触发滑动的最少手指数，最小为1指， 最大取值为10指。<br/> **说明：** <br/> 手当设置的值小于1或不设置时，会被转化为默认值。|
|direction|[PanDirection](#enum-pandirection)|否|PanDirection.All|用于指定触发滑动的手势方向，此枚举值支持逻辑与(&)和逻辑或(\| **命名参数。** )运算。|
|distance|Float64|否|5.0| **命名参数。** 用于指定触发滑动手势事件的最小滑动距离，单位为px。 <br/> **说明：** <br/> 当设定的值小于0时，按默认值5处理。|

### init(PanGestureOptions)

```cangjie
public init(panGestureOptions: PanGestureOptions)
```

**功能：** 创建一个滑动手势。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|panGestureOptions|[PanGestureOptions](#enum-pandirection)|是|-|通过PanGestureOptions对象接口可以动态修改平移手势识别器的属性，从而避免通过状态变量修改属性（状态变量修改会导致UI刷新）。|

## 组件事件

### func onActionCancel(() -> Unit)

```cangjie
public func onActionCancel(callback: () -> Unit): This
```

**功能：** Pan手势识别成功，接收到触摸取消事件触发回调。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，Pan手势识别成功，接收到触摸取消事件触发。|

### func onActionEnd((GestureEvent) -> Unit)

```cangjie
public func onActionEnd(callback: (GestureEvent) -> Unit): This
```

**功能：** Pan手势识别成功，手指抬起后触发回调。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|回调函数，Pan手势识别成功，手指抬起后触发。|

### func onActionStart((GestureEvent) -> Unit)

```cangjie
public func onActionStart(callback: (GestureEvent) -> Unit): This
```

**功能：** Pan手势识别成功回调。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|回调函数，Pan手势识别成功触发。|

### func onActionUpdate((GestureEvent) -> Unit)

```cangjie
public func onActionUpdate(callback: (GestureEvent) -> Unit): This
```

**功能：** Pan手势移动过程中回调。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|回调函数，Pan手势移动过程中触发。|