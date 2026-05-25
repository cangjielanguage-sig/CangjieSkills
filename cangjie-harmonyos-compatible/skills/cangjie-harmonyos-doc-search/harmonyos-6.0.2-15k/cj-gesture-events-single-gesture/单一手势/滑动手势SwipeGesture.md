## 滑动手势（SwipeGesture）

```cangjie
SwipeGesture(fingers!: Int32 = 1, direction!: SwipeDirection = SwipeDirection.All, speed!: Float64 = 100.0)
```

滑动手势用于触发滑动事件，当滑动速度大于100vp/s时可以识别成功，有三个可选参数：

- fingers：用于声明触发滑动手势所需要的最少手指数量，最小值为1，最大值为10，默认值为1。

- direction：用于声明触发滑动手势的方向，此枚举值支持逻辑与（&）和逻辑或（|）运算。默认值为SwipeDirection.All。

- speed：用于声明触发滑动的最小滑动识别速度，单位为vp/s，默认值为100。

以在Column组件上绑定滑动手势实现组件的旋转为例：

<!--run-->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import kit.LocationKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var rotateAngle: Float32 = 0.0
    @State
    var speed: Float32 = 1.0

    func build() {
        Column() {
            Column() {
                Text("SwipeGesture speed\n" + this.speed.toString())
                Text("SwipeGesture angle\n" + this.rotateAngle.toString())
            }.border(width: 3).width(300).height(200).margin(100)
                // 在Column组件上绑定旋转，通过滑动手势的滑动速度和角度修改旋转的角度
                .rotate(x: 0.0, y: 0.0, z: 1.0, angle: this.rotateAngle,
                centerX: 0, centerY: 0).gesture(
                // 绑定滑动手势且限制仅在竖直方向滑动时触发
                SwipeGesture(direction: SwipeDirection.Vertical)
                    // 当滑动手势触发时，获取滑动的速度和角度，实现对组件的布局参数的修改
                    .onAction(
                    {
                        event: GestureEvent =>
                        this.speed = Float32(event.speed)
                        this.rotateAngle = Float32(event.angle)
                    }
                )
            )
        }
    }
}
```

![SwipeGesture](figures/singleGestureSwipeGesture.gif)

> **说明：**
>
> 当SwipeGesture和PanGesture同时绑定时，若二者是以默认方式或者互斥方式进行绑定时，会发生竞争。SwipeGesture的触发条件为滑动速度达到100vp/s，PanGesture的触发条件为滑动距离达到5vp，先达到触发条件的手势触发。可以通过修改SwipeGesture和PanGesture的参数以达到不同的效果。