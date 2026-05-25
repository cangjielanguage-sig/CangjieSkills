## 拖动手势（PanGesture）

```cangjie
PanGesture(fingers!: Int32 = 1, direction!: PanDirection = PanDirection.All, distance!: Float64 = 5.0)
```

拖动手势用于触发拖动手势事件，滑动达到最小滑动距离（默认值为5vp）时拖动手势识别成功，有三个可选参数：

- fingers：用于声明触发拖动手势所需要的最少手指数量，最小值为1，最大值为10，默认值为1。

- direction：用于声明触发拖动的手势方向，此枚举值支持逻辑与（&）和逻辑或（|）运算。默认值为Pandirection.All。

- distance：用于声明触发拖动的最小拖动识别距离，单位为px，默认值为5。

以在Text组件上绑定拖动手势为例，可以通过在拖动手势的回调函数中修改组件的布局位置信息来实现组件的拖动：

<!--run-->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var offsetX: Length = 0;
    @State
    var offsetY: Length = 0;
    @State
    var positionX: Length = 0;
    @State
    var positionY: Length = 0;

    func build() {
        Column() {
            Text('PanGesture Offset:\nX: ' + offsetX.value.toString() + '\n' + 'Y: ' + offsetY.value.toString()).
                fontSize(28).height(200).width(300).padding(20).border(width: 3)
                    // 在组件上绑定布局位置信息
                    .translate(x: offsetX, y: offsetY, z: 0).
                gesture(
                // 绑定拖动手势
                PanGesture().onActionStart({event: GestureEvent =>})
                    // 当触发拖动手势时，根据回调函数修改组件的布局位置信息
                    .onActionUpdate(
                    {
                        event: GestureEvent =>
                        offsetX = positionX.value + event.offsetX
                        offsetY = positionY.value + event.offsetY
                    }
                ).onActionEnd(
                    {
                        event: GestureEvent =>
                        positionX = offsetX
                        positionY = offsetY
                    }
                )
            )
        }.height(200).width(250)
    }
}
```

![PanGesture](figures/singleGesturePanGesture.gif)

> **说明：**
>
> - 大部分可滑动组件，如List、Grid、Scroll、Tab等组件是通过PanGesture实现滑动，在组件内部的子组件绑定[拖动手势（PanGesture）](#拖动手势pangesture)或者[滑动手势（SwipeGesture）](#滑动手势swipegesture)会导致手势竞争。
>
> - 当在子组件绑定PanGesture时，在子组件区域进行滑动仅触发子组件的PanGesture。如果需要父组件响应，需要通过修改手势绑定方法或者子组件向父组件传递消息进行实现，或者通过修改父子组件的PanGesture参数distance使得拖动更灵敏。当子组件绑定SwipeGesture时，由于PanGesture和SwipeGesture触发条件不同，需要修改PanGesture和SwipeGesture的参数以达到所需效果。
>
> - 不合理的阈值设置会导致滑动不跟手（响应时延慢）的问题。