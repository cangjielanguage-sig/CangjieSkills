# TapGesture

支持单击、双击和多次点击事件的识别。

## 创建组件

### init(Int32, Int32)

```cangjie
public init(count!: Int32 = 1, fingers!: Int32 = 1)
```

**功能：** 创建一个点击手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|count|Int32|否|1| **命名参数。** 识别的连续点击次数。当设置的值小于1或不设置时，会被转化为默认值。<br/> **说明：** <br/> 1. 当配置多击时，上一次的最后一根手指抬起和下一次的第一根手指按下的超时时间为300毫秒。<br/> 2. 当上次点击的位置与当前点击的位置距离超过60vp时，手势识别失败。|
|fingers|Int32|否|1| **命名参数。** 触发点击的手指数，最小为1指， 最大为10指。当设置小于1的值或不设置时，会被转化为默认值。<br/> **说明：** <br/> 1. 当配置多指时，第一根手指按下后300毫秒内未有足够的手指数按下，手势识别失败；手指抬起时，抬起后剩余的手指数小于阈值时开始计时，如300ms内未全部抬起则手势识别失败。<br/> 2. 实际点击手指数超过配置值，手势识别成功。|

## 组件事件

### func onAction((GestureEvent) -> Unit)

```cangjie
public func onAction(callback: (GestureEvent) -> Unit): This
```

**功能：** Tap手势识别成功触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|回调函数，Tap手势识别成功触发。|

## 示例代码

该示例通过TapGesture实现了双击手势的识别。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var priorityTestValue: String = ""
    @State
    var parallelTestValue: String = ""

    func build() {
        Column() {
            Column() {
                Text('TapGesture:' + this.priorityTestValue).fontSize(28).gesture(
                    TapGesture().onAction({
                        event: GestureEvent => this.priorityTestValue += '\nText'
                    }),
                    GestureMask.Normal
                )
            }.height(200).width(250).padding(20).margin(20).border(width: 3.vp)
                // 设置为priorityGesture时，点击文本会忽略Text组件的TapGesture手势事件，优先识别父组件Column的TapGesture手势事件
                .priorityGesture(
                TapGesture().onAction({
                    event: GestureEvent => this.priorityTestValue += '\nColumn'
                }),
                GestureMask.IgnoreInternal
            )

            Column() {
                Text('TapGesture:' + this.parallelTestValue).fontSize(28).gesture(
                    TapGesture().onAction({
                        event: GestureEvent => this.parallelTestValue += '\nText'
                    }),
                    GestureMask.Normal
                )
            }.height(200).width(250).padding(20).margin(20).border(width: 3.vp)
                // 设置为parallelGesture时，点击文本会同时触发子组件Text与父组件Column的TapGesture手势事件
                .parallelGesture(
                TapGesture().onAction({
                    event: GestureEvent => this.parallelTestValue += '\nColumn'
                }),
                GestureMask.Normal
            )
        }
    }
}
```

![bind_gesture](figures/bind_gesture.gif)
