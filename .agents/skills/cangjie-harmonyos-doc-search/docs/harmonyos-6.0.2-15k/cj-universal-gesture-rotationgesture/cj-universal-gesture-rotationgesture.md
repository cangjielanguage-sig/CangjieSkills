# RotationGesture

用于触发旋转手势事件，触发旋转手势的最少手指为2指，最大为5指，最小改变度数为1度。

## 创建组件

### init(Int32, Float64)

```cangjie
public init(fingers!: Int32 = 2, angle!: Float64 = 1.0)
```

**功能：** 创建一个旋转手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fingers|Int32|否|2| **命名参数。** 触发旋转的最少手指数, 最小为2指，最大为5指。<br/> **说明：** <br/> 触发手势手指可以多于fingers数目，但只有先落下的两指参与手势计算。|
|angle|Float64|否|1.0| **命名参数。** 触发旋转手势的最小改变度数，单位为deg。 <br/> **说明：** <br/> 当改变度数的值小于等于0或大于360时，会被转化为默认值。|

## 组件事件

### func onActionCancel(() -> Unit)

```cangjie
public func onActionCancel(callback: () -> Unit): This
```

**功能：** Rotation手势识别成功，接收到触摸取消事件触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，Rotation手势识别成功，接收到触摸取消事件触发。|

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
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|回调函数，Rotation手势识别成功，手指抬起后触发。|

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
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|回调函数，Rotation手势识别成功触发。|

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
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|回调函数，Rotation手势移动过程中触发。|

## 示例代码

该示例通过配置RotationGesture实现了双指旋转手势的识别。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var scaleValue: Float64 = 1.0
    @State
    var angle: Float64 = 0.0
    @State
    var rotateValue: Float64 = 0.0

    func build() {
        Column() {
            Column() {
                Text('RotationGesture angle:' + this.angle.toString())
            }.height(200).width(300).padding(20).border(width: 3.vp).margin(80).rotate(Float32(this.angle)).gesture(
                RotationGesture().onActionUpdate({
                event: GestureEvent => this.angle = this.rotateValue + event.angle
            }).onActionEnd({
                event: GestureEvent => this.rotateValue = this.angle
            }))
        }
    }
}
```

![rotation](figures/rotation_gesture.gif)
