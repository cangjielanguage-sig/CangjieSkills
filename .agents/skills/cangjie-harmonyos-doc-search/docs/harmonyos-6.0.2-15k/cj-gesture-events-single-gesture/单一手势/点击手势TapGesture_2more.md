## 点击手势（TapGesture）

```cangjie
TapGesture(count!: Int32 = 1, fingers!: Int32 = 1)
```

点击手势支持单次点击和多次点击，有两个可选参数：

- count：声明该点击手势识别的连续点击次数。默认值为1，若设置小于1的非法值会被转化为默认值。如果配置多次点击，上一次抬起和下一次按下的超时时间为300毫秒。

- fingers：用于声明触发点击的手指数量，最小值为1，最大值为10，默认值为1。当配置多指时，若第一根手指按下300毫秒内未有足够的手指数按下则手势识别失败。

以在Text组件上绑定双击手势（count值为2的点击手势）为例：

<!--run-->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var value: String = " "
    func build() {
        Column() {
            Text('Click twice').fontSize(28).gesture(
                // 绑定count为2的TapGesture
                TapGesture(count: 2, fingers: 1).onAction(
                {
                event: GestureEvent => value = "{" + "id:" + event.fingerList[0].id.toString() + ","
                    + "globalX:" + event.fingerList[0].globalX.toString() + ","
                    + "globalY:" + event.fingerList[0].globalY.toString() + ","
                    + "localX:" + event.fingerList[0].localX.toString() + ","
                    + "localY:" + event.fingerList[0].localY.toString() + "}"
            }))
            Text(value)
        }.height(200).width(250).padding(20).border(width: 3).margin(30)
    }
}
```

![TapGesture](figures/singleGestureTapGesture.gif)

## 长按手势（LongPressGesture）

```cangjie
LongPressGesture(fingers!: Int32 = 1, repeat!: Bool = false, duration!: Int32 = 500)
```

长按手势用于触发长按手势事件，有三个可选参数：

- fingers：用于声明触发长按手势所需要的最少手指数量，最小值为1，最大值为10，默认值为1。

- repeat：用于声明是否连续触发事件回调，默认值为false。

- duration：用于声明触发长按所需的最短时间，单位为毫秒，默认值为500。

以在Text组件上绑定可以重复触发的长按手势为例：

<!--run-->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var count: Int8 = 0

    func build() {
        Column() {
            Text('LongPress OnAction:' + count.toString()).fontSize(28).gesture(
                // 绑定可以重复触发的LongPressGesture
                LongPressGesture(repeat: true).onAction({event: GestureEvent => count++}).onActionEnd(
                {
                event: GestureEvent => count = 0
            }))
        }.height(200).width(250).padding(20).border(width: 3).margin(30)
    }
}
```

![LongPressGesture](figures/singleGestureLongPressGesture.gif)