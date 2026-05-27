## 组件事件

### func onBounce(() -> Unit)

```cangjie
public func onBounce(callback: () -> Unit): This
```

**功能：** 完成一次滚动时触该事件，若循环次数不为1，则会多次触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，完成一次滚动时触发。|

### func onFinish(() -> Unit)

```cangjie
public func onFinish(callback: () -> Unit): This
```

**功能：** 滚动全部循环次数完成时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，滚动全部循环次数完成时触发。|

### func onStart(() -> Unit)

```cangjie
public func onStart(callback: () -> Unit): This
```

**功能：** 当滚动的文本内容变化或者开始滚动时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，当滚动的文本内容变化或者开始滚动时触发。|

## 示例代码

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var message: String = "Hello Cangjie"
    @State
    var start: Bool = false
    @State
    var controller: TextClockController = TextClockController()
    @State
    var MyString: String = ""
    @State
    var Mystep: Float64 = 26.0
    func build() {
        Row {
            Column {
                Button("Start").onClick {
                    evt =>
                    this.start = true
                    this.controller.start()
                }.fontSize(40).height(80)
                Button("change step").onClick {
                    this.Mystep = 6.0
                }
                Marquee(start: this.start, src: this.message + this.MyString, step: this.Mystep).width(300).height(80).
                    fontSize(40).fontColor(Color.RED).fontWeight(FontWeight.Medium).marqueeUpdateStrategy(
                    MarqueeUpdateStrategy.PRESERVE_POSITION).margin(bottom: 40).allowScale(false).onStart(
                    {
                    => AppLog.info('Marquee animation complete onStart')
                }).onBounce({
                    => AppLog.info('Marquee animation complete onBounce')
                }).onFinish({
                    => AppLog.info('Marquee animation complete onFinish')
                }).onClick({
                    env => this.Mystep = 16.0
                })
                TextClock(controller: this.controller).onDateChange {
                    value => this.MyString = value.toString()
                }
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

![marquee](figures/marquee.gif)