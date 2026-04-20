## class RotationGestureHandler

```cangjie
public class RotationGestureHandler <: GestureHandler {}
```

**功能：** 旋转手势处理器对象类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [GestureHandler](#class-gesturehandler)

### init(Int32, Float64)

```cangjie
public init(fingers!: Int32 = 2, angle!: Float64 = 1.0)
```

**功能：** 创建一个捏合手势处理器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fingers|Int32|否|2| **命名参数。** 触发旋转的最少手指数, 最小为2指，最大为5指。<br/> **说明：** <br/> 触发手势手指可以多于fingers数目，但只有先落下的两指参与手势计算。|
|angle|Float64|否|1.0| **命名参数。** 触发旋转手势的最小改变度数，单位为deg。 <br/> **说明：** <br/> 当改变度数的值小于等于0或大于360时，会被转化为默认值。|

### func onActionStart((GestureEvent) -> Unit)

```cangjie
public func onActionStart(callback: (GestureEvent) -> Unit): This
```

**功能：** Rotation手势识别成功触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|Rotation手势识别成功触发该回调。|

### func onActionUpdate((GestureEvent) -> Unit)

```cangjie
public func onActionUpdate(callback: (GestureEvent) -> Unit): This
```

**功能：** Rotation手势移动过程中触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|Rotation手势移动过程中触发该回调。|

### func onActionEnd((GestureEvent) -> Unit)

```cangjie
public func onActionEnd(callback: (GestureEvent) -> Unit): This
```

**功能：** Rotation手势识别成功，手指抬起后触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|Rotation手势识别成功，手指抬起后触发该回调。|

### func onActionCancel((GestureEvent) -> Unit)

```cangjie
public func onActionCancel(callback: (GestureEvent) -> Unit): This
```

**功能：** Rotation手势识别成功，接收到触摸取消事件触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|Rotation手势识别成功，接收到触摸取消事件触发该回调。|