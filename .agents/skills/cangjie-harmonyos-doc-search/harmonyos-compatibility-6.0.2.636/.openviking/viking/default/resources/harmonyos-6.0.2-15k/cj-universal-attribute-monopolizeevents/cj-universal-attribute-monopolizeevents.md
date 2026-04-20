# 事件独占控制

设置组件是否独占事件，事件范围包括组件自带的事件和开发者自定义的点击、触摸、手势事件。<br />
在一个窗口内，设置了独占控制的组件上的事件如果首先响应，则本次交互只允许此组件上设置的事件响应，窗口内其他组件上的事件不会响应。

## func monopolizeEvents(Bool)

```cangjie
public func monopolizeEvents(value: Bool): This
```

**功能：** 设置组件是否独占事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|monopolize|Bool|是|-|组件是否独占事件。<br /> 初始值：false。<br /> true表示组件独占事件，false表示组件不独占事件。<br /> **说明：** <br /> 1、如果第一根手指触发了组件事件独占，在抬起前又按下了一根手指，则第二根手指的交互继续处于组件独占状态，依次类推。<br /> 2、如果开发者通过[parallelGesture](./cj-universal-gesture-bind.md#绑定手势方法)绑定了与子组件同时触发的手势，如[PanGesture](./cj-universal-gesture-pangesture.md#pangesture)，子组件设置了独占控制且首个响应事件，则父组件的手势不会响应。|

## 示例代码

该示例通过配置monopolizeEvents实现组件是否独占事件。

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var message: String = 'set monopolizeEvents false'
    @State
    var messageOut: String = ' '
    @State
    var messageInner: String = ' '
    @State
    var monopolize: Bool = false

    func build() {
        Column() {
            Text(this.message)
            Text(this.messageOut)
            Text(this.messageInner)
            Button('clean').onClick {
                this.messageOut = " "
                this.messageInner = " "
            }
            Button('change monopolizeEvents')
                // 通过button的点击事件来切换内层column的独占控制属性
                .onClick {
                this.monopolize = !this.monopolize
                if (!this.monopolize) {
                    this.message = "set monopolizeEvents false"
                } else {
                    this.message = "set monopolizeEvents true"
                }
            }
            Column {}.width(100.percent).height(40.percent).backgroundColor(Color.BLUE).monopolizeEvents(
                this.monopolize).onTouch(
                {
                event => if (event.eventType.toString() == TouchType.Down.toString()) {
                    this.messageInner = "inner column touch down"
                }
            })
        }.onTouch(
            {
            event => if (event.eventType.toString() == TouchType.Down.toString()) {
                this.messageOut = "inner column touch down"
            }
        })
    }
}
```

![monopolizeEvents](figures/monopolizeEvents.gif)
