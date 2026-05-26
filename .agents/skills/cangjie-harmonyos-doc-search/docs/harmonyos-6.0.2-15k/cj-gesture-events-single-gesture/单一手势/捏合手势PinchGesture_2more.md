## 捏合手势（PinchGesture）

```cangjie
PinchGesture(fingers!: Int32 = 2, distance!: Float64 = 5.0)
```

捏合手势用于触发捏合手势事件，有两个可选参数：

- fingers：用于声明触发捏合手势所需要的最少手指数量，最小值为2，最大值为5，默认值为2。

- distance：用于声明触发捏合手势的最小距离，单位为vp，默认值为5。

以在Column组件上绑定三指捏合手势为例，可以通过在捏合手势的函数回调中获取缩放比例，实现对组件的缩小或放大：

<!--run-->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import kit.LocalizationKit.*
import ohos.state_macro_manage.*
import ohos.hilog.*

@Entry
@Component
class EntryView {
    @State
    var scaleValue: Float32 = 1.0;
    @State
    var pinchValue: Float32 = 1.0;
    @State
    var pinchX: Float64 = 0.0;
    @State
    var pinchY: Float64 = 0.0;

    func build() {
        Column() {
            Column() {
                Text('PinchGesture scale:\n' + scaleValue.toString())
                Text('PinchGesture center:\n(' + pinchX.toString() + ',' + pinchY.toString() + ')')
            }.height(200).width(300).border(width: 3).margin(top: 100)
                // 在组件上绑定缩放比例，可以通过修改缩放比例来实现组件的缩小或者放大
                .scale(x: scaleValue, y: scaleValue, z: 1.0).
                gesture(
                // 在组件上绑定三指触发的捏合手势
                PinchGesture(fingers: 3).onActionStart({event: GestureEvent => Hilog.info(0, "Pinch", "Pinch start")})
                    // 当捏合手势触发时，可以通过回调函数获取缩放比例，从而修改组件的缩放比例
                    .
                    onActionUpdate(
                    {
                        event: GestureEvent =>
                        scaleValue = pinchValue * Float32(event.scale)
                        pinchX = event.pinchCenterX
                        pinchY = event.pinchCenterY
                    }
                ).onActionEnd(
                    {
                        event: GestureEvent =>
                        pinchValue = scaleValue
                        Hilog.info(0, "Pinch", "Pinch end")
                    }
                )
            )
        }
    }
}
```

![PinchGesture](figures/singleGesturePinchGesture.png)

## 旋转手势（RotationGesture）

```cangjie
RotationGesture(fingers!: Int32 = 2, angle!: Float64 = 1.0)
```

旋转手势用于触发旋转手势事件，有两个可选参数：

- fingers：用于声明触发旋转手势所需要的最少手指数量，最小值为2，最大值为5，默认值为2。

- angle：用于声明触发旋转手势的最小改变度数，单位为deg，默认值为1。

以在Text组件上绑定旋转手势实现组件的旋转为例，可以通过在旋转手势的回调函数中获取旋转角度，从而实现组件的旋转：

<!--run-->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import kit.LocalizationKit.*
import ohos.state_macro_manage.*
import ohos.hilog.*

@Entry
@Component
class EntryView {
    @State
    var angle: Float32 = 0.0
    @State
    var rotateValue: Float32 = 0.0

    func build() {
        Column() {
            Text('RotationGesture angle:' + angle.toString()).fontSize(28)
                // 在组件上绑定旋转布局，可以通过修改旋转角度来实现组件的旋转
                .rotate(angle).gesture(
                RotationGesture().onActionStart(
                {
                event: GestureEvent => Hilog.info(0, "RotationGesture", "RotationGesture is onActionStart")
            })
                // 当旋转手势生效时，通过旋转手势的回调函数获取旋转角度，从而修改组件的旋转角度
                .onActionUpdate(
                {
                    event: GestureEvent =>
                    angle = rotateValue + Float32(event.angle)
                    Hilog.info(0, "RotationGesture", "RotationGesture is onActionEnd")
                }
            )
                // 当旋转结束抬手时，固定组件在旋转结束时的角度
                .onActionEnd(
                {
                    event: GestureEvent =>
                    this.rotateValue = this.angle
                    Hilog.info(0, "RotationGesture", "RotationGesture is onActionEnd")
                }
            ).onActionCancel({
                => Hilog.info(0, "RotationGesture", "RotationGesture is onActionCancel")
            })).height(200).width(300).padding(20).border(width: 3).margin(100)
        }
    }
}
```

![RotationGesture](figures/singleGestureRotationGesture.png)