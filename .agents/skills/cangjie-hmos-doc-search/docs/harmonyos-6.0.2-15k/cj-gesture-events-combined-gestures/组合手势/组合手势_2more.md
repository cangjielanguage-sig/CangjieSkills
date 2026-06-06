# 组合手势

组合手势由多种单一手势组合而成，通过在GestureGroup中使用不同的[GestureMode](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-gesture-groupgesture.md#enum-gesturemode)来声明该组合手势的类型，支持[顺序识别](#顺序识别)、[并行识别](#并行识别)和[互斥识别](#互斥识别)三种类型。

```cangjie
GestureGroup(mode: GestureMode, gesture: Array<GestureType>)
```

- mode：为GestureMode枚举类。用于声明该组合手势的类型。

- gesture：由多个手势组合而成的数组。用于声明组合成该组合手势的各个手势。

## 顺序识别

顺序识别组合手势对应的GestureMode为Sequence。顺序识别组合手势将按照手势的注册顺序识别手势，直到所有的手势识别成功。当顺序识别组合手势中有一个手势识别失败时，后续手势识别均失败。顺序识别手势组仅有最后一个手势可以响应onActionEnd。

以一个由长按手势和拖动手势组合而成的连续手势为例：

在一个Column组件上绑定了translate属性，通过修改该属性可以设置组件的位置移动。然后在该组件上绑定LongPressGesture和PanGesture组合而成的Sequence组合手势。当触发LongPressGesture时，更新显示的数字。当长按后进行拖动时，根据拖动手势的回调函数，实现组件的拖动。

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
    var offsetX: Length = 0.vp
    @State
    var offsetY: Length = 0.vp
    @State
    var count: Int8 = 0
    @State
    var positionX: Length = 0
    @State
    var positionY: Length = 0
    @State
    var borderStyles: BorderStyle = BorderStyle.Solid

    func build() {
        Column() {
            Text(
                'sequence gesture\n' + 'LongPress onAction:' + count.toString() + '\nPanGesture offset:\nX: ' +
                offsetX.value.toString() + '\n' + 'Y: ' + offsetY.value.toString()).fontSize(28)
        }.margin(10).borderWidth(1)
            // 绑定translate属性可以实现组件的位置移动
            .translate(x: offsetX, y: offsetY).height(250).width(300)
            //以下组合手势为顺序识别，当长按手势事件未正常触发时不会触发拖动手势事件
            .gesture(
            // 声明该组合手势的类型为Sequence类型
            GestureGroup(
            GestureMode.Sequence,
            // 该组合手势第一个触发的手势为长按手势，且长按手势可多次响应
            [
                LongPressGesture(repeat: true)
                    // 当长按手势识别成功，增加Text组件上显示的count次数
                    .onAction(
                    {
                        event: GestureEvent =>
                        this.count++
                        Hilog.info(0, "hilog1", "LongPress onAction")
                    }
                ).onActionEnd({event: GestureEvent => Hilog.info(0, "hilog2", "LongPress end")}),
                // 当长按之后进行拖动，PanGesture手势被触发
                PanGesture().onActionStart(
                    {
                        event: GestureEvent =>
                        this.borderStyles = BorderStyle.Dashed
                        Hilog.info(0, "hilog3", "pan start")
                    }
                )
                    // 当该手势被触发时，根据回调获得拖动的距离，修改该组件的位移距离，从而实现组件的移动
                    .onActionUpdate(
                    {
                        event: GestureEvent =>
                        this.offsetX = (this.positionX.value + event.offsetX)
                        this.offsetY = (this.positionY.value + event.offsetY)
                        Hilog.info(0, "hilog4", "pan update")
                    }
                ).onActionEnd(
                    {
                        event: GestureEvent =>
                        this.positionX = this.offsetX
                        this.positionY = this.offsetY
                        this.borderStyles = BorderStyle.Solid
                    }
                )
            ]
        ).onCancel({=> Hilog.info(0, "hilog5", "sequence gesture canceled")}))
    }
}
```

![Sequence](figures/combinedGestureSequence.gif)

> **说明：**
>
> 拖拽事件是一种典型的顺序识别组合手势事件，由长按手势事件和滑动手势事件组合而成。只有先长按达到长按手势事件预设置的时间后，进行滑动，才会触发拖拽事件。如果长按事件未达到，或者长按后未进行滑动，拖拽事件均识别失败。