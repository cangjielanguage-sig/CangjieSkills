# LongPressGesture

用于触发长按手势事件，触发长按手势的最少手指数为1，最短长按时间为500毫秒。

## 创建组件

### init(Int32, Bool, Int32)

```cangjie
public init(fingers!: Int32 = 1, repeat!: Bool = false, duration!: Int32 = 500)
```

**功能：** 创建一个长按手势处理器。当组件默认支持可拖拽时，如Text、TextInput、TextArea、HyperLink、Image和RichEditor等组件。长按手势与拖拽会出现冲突，事件优先级如下：

长按触发时间 < 500ms，长按事件优先拖拽事件响应。

长按触发时间 >= 500ms，拖拽事件优先长按事件响应。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fingers|Int32|否|1| **命名参数。** 触发长按的最少手指数，最小为1指， 最大取值为10指。<br/> **说明：** <br/> 手指按下后若发生超过15px的移动，则判定当前长按手势识别失败。|
|repeat|Bool|否|false| **命名参数。** 是否连续触发事件回调|
|duration|Int32|否|500| **命名参数。** 触发长按的最短时间，单位为毫秒（ms）。 <br/> **说明：** <br/> 设置小于等于0时，按照默认值500处理。|

## 组件事件

### func onAction((GestureEvent) -> Unit)

```cangjie
public func onAction(callback: (GestureEvent) -> Unit): This
```

**功能：** LongPress手势识别成功回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|回调函数，LongPress手势识别成功时触发。|

### func onActionCancel(() -> Unit)

```cangjie
public func onActionCancel(callback: () -> Unit): This
```

**功能：** LongPress手势识别成功，接收到触摸取消事件触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，LongPress手势识别成功，接收到触摸取消事件触发。|

### func onActionEnd((GestureEvent) -> Unit)

```cangjie
public func onActionEnd(callback: (GestureEvent) -> Unit): This
```

**功能：** LongPress手势识别成功，最后一根手指抬起后触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|回调函数，LongPress手势识别成功，最后一根手指抬起后触发。|

## 示例代码

该示例通过LongPressGesture实现了长按手势的识别。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var count: Int64 = 0

    func build() {
        Column() {
            Text("LongPress onAction:" + this.count.toString()).fontSize(28).gesture(
                LongPressGesture(repeat: true).onAction({
                event: GestureEvent => if (event.repeat) {
                    this.count++
                }
            }).onActionEnd({
                event: GestureEvent => this.count = 0
            }))
        }.height(200).width(300).padding(20).border(width: 3.vp).margin(30)
    }
}
```

![longpress](figures/longpress_gesture.gif)
