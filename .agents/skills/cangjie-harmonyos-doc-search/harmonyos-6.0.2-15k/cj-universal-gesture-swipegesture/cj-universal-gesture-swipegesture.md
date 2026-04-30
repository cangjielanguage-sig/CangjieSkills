# SwipeGesture

用于触发滑动事件，滑动速度大于100vp/s时可识别成功。

## 创建组件

### init(Int32, SwipeDirection, Float64)

```cangjie
public init(fingers!: Int32 = 1, direction!: SwipeDirection = SwipeDirection.All, speed!: Float64 = 100.0)
```

**功能：** 创建一个滑动手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fingers|Int32|否|1| **命名参数。** 触发滑动的最少手指数，默认为1，最小为1指，最大为10指。|
|direction|[SwipeDirection](#enum-swipedirection)|否|SwipeDirection.All| **命名参数。** 触发滑动手势的滑动方向。|
|speed|Float64|否|100.0| **命名参数。** 识别滑动的最小速度。<br/> **说明：** 当滑动速度的值小于等于0时，会被转化为默认值。|

## 组件事件

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
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|回调函数，Swipe手势识别成功触发。|

## 基础类型定义

### enum SwipeDirection

```cangjie
public enum SwipeDirection {
    | Horizontal
    | Vertical
    | All
    | None
}
```

**功能：** 触发滑动手势的滑动方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### All

```cangjie
All
```

**功能：** 所有方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Horizontal

```cangjie
Horizontal
```

**功能：** 水平方向，手指滑动方向与x轴夹角小于45度时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### None

```cangjie
None
```

**功能：** 任何方向都不可触发拖动手势事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Vertical

```cangjie
Vertical
```

**功能：** 竖直方向，手指滑动方向与y轴夹角小于45度时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## 示例代码

该示例通过配置SwipeGesture实现了滑动手势的识别。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var rotateAngle: Float64 = 0.0
    @State
    var speed: Float64 = 1.0

    func build() {
        Column() {
            Column() {
                Text("SwipeGesture speed\n" + this.speed.toString())
                Text("SwipeGesture angle\n" + this.rotateAngle.toString())
            }.height(200).width(300).padding(20).border(width: 3.vp).margin(80).rotate(Float32(this.rotateAngle)).
                gesture(
                SwipeGesture(direction: SwipeDirection.Vertical).onAction(
                    {
                        event: GestureEvent =>
                        this.speed = event.speed
                        this.rotateAngle = event.angle
                    }
                )
            )
        }
    }
}
```

![swipe](figures/swipe_gesture.gif)
