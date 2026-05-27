# PinchGesture

用于触发捏合手势，触发捏合手势的最少手指为2指，最大为5指，最小识别距离为5vp。

## 创建组件

### init(Int32, Float64)

```cangjie
public init(fingers!: Int32 = 2, distance!: Float64 = 5.0)
```

**功能：** 创建一个捏合手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fingers|Int32|否|2| **命名参数。** 触发捏合的最少手指数, 最小为2指，最大为5指。<br/> **说明：** <br/> 触发手势手指可以多于fingers数目，但只有先落下的与fingers相同数目的手指参与手势计算。|
|distance|Float64|否|5.0| **命名参数。** 最小识别距离，单位为vp。 <br/> **说明：** <br/> 当识别距离的值小于等于0时，会被转化为默认值。|

## 组件事件

### func onActionStart((GestureEvent) -> Unit)

```cangjie
public func onActionStart(callback: (GestureEvent) -> Unit): This
```

**功能：** Pinch手势识别成功触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|回调函数，pinch手势识别成功触发。|

### func onActionUpdate((GestureEvent) -> Unit)

```cangjie
public func onActionUpdate(callback: (GestureEvent) -> Unit): This
```

**功能：** Pinch手势移动过程中触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|回调函数，Pinch手势移动过程中触发。|

### func onActionEnd((GestureEvent) -> Unit)

```cangjie
public func onActionEnd(callback: (GestureEvent) -> Unit): This
```

**功能：** Pinch手势识别成功，手指抬起后触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|回调函数，Pinch手势识别成功，手指抬起后触发该事件。|

### func onActionCancel((GestureEvent) -> Unit)

```cangjie
public func onActionCancel(callback: (GestureEvent) -> Unit): This
```

**功能：** Pinch手势识别成功，接收到触摸取消事件触发该事件。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|回调函数，Pinch手势识别成功，接收到触摸取消事件触发该事件|

## 示例代码

该示例通过配置PinchGesture实现了三指捏合手势的识别。

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
    var pinchValue: Float64 = 1.0
    @State
    var pinchX: Float64 = 0.0
    @State
    var pinchY: Float64 = 0.0

    func build() {
        Column() {
            Column() {
                Text('PinchGesture scale:\n' + this.scaleValue.toString())
                Text('PinchGesture center:\n(' + this.pinchX.toString() + ',' + this.pinchY.toString() + ')')
            }.height(200).width(300).padding(20).border(width: 3.vp).scale(x: Float32(this.scaleValue),
                y: Float32(this.scaleValue), z: 1.0).gesture(
                PinchGesture(fingers: 3).onActionUpdate(
                {
                    event: GestureEvent =>
                    this.scaleValue = this.pinchValue * event.scale
                    this.pinchX = event.pinchCenterX
                    this.pinchY = event.pinchCenterY
                }
            ).onActionEnd({
                event: GestureEvent => this.pinchValue = this.scaleValue
            }))
        }
    }
}
```

![pinch](figures/pinch_gesture.gif)
