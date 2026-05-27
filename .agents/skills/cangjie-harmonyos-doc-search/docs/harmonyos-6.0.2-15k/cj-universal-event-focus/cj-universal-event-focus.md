# 焦点事件

焦点事件指页面焦点在可获焦组件间移动时触发的事件，组件可使用焦点事件来处理相关逻辑。

> **说明：**
>
> - 目前仅支持通过外接键盘的tab键、方向键触发。不支持嵌套滚动组件场景按键走焦。
> - 存在默认交互逻辑的组件例如[Button](./cj-button-picker-button.md)、[TextInput](./cj-text-input-textinput.md)等，默认即为可获焦，[Text](./cj-text-input-text.md)、[Image](./cj-image-video-image.md)等组件默认状态为不可获焦，不可获焦状态下，无法触发焦点事件，需要设置focusable属性为true才可触发。
> - 对于有获焦能力的容器组件，例如[Stack](./cj-row-column-stack-stack.md)、[Row](./cj-row-column-stack-row.md)等，若不存在可获焦子组件，该容器组件不可获焦。为其配置onClick或是单指单击的Tap手势，该组件会隐式地成为可获焦组件。
> - 焦点开发及组件获焦能力参考[焦点开发指南](../../../Dev_Guide/arkui-cj/cj-common-events-focus-event.md)。

## func onFocus(() -> Unit)

```cangjie
public func onFocus(callback: ()->Unit): This
```

**功能：** 当前组件获取焦点时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，当前组件获取焦点时触发的回调。|

## func onBlur(() -> Unit)

```cangjie
public func onBlur(callback: ()->Unit): This
```

**功能：** 当前组件失去焦点时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，当前组件失去焦点时触发的回调。|

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
    var oneButtonColor: ResourceColor = Color.PINK
    @State
    var twoButtonColor: ResourceColor = Color.RED
    @State
    var threeButtonColor: ResourceColor = Color.GREEN

    func build() {
        Column(20) {
            // 通过外接键盘的上下键可以让焦点在三个按钮间移动，按钮获焦时颜色变化，失焦时变回原背景色
            Button('First Button').backgroundColor(this.oneButtonColor).width(260).height(70).fontColor(Color.BLACK).
                focusable(true).onFocus({
                => this.oneButtonColor = Color.BLUE
            }).onBlur({
                => this.oneButtonColor = Color.GRAY
            })
            Button('Second Button').backgroundColor(this.twoButtonColor).width(260).height(70).fontColor(Color.BLACK).
                focusable(true).onFocus({
                => this.twoButtonColor = Color.BLUE
            }).onBlur({
                => this.twoButtonColor = Color.GRAY
            })
            Button('Third Button').backgroundColor(this.threeButtonColor).width(260).height(70).fontColor(Color.BLACK).
                focusable(true).onFocus({
                => this.threeButtonColor = Color.BLUE
            }).onBlur({
                => this.threeButtonColor = Color.GRAY
            })
        }.width(100.percent).margin(top: 20)
    }
}
```

![focus_event](figures/focus_event.png)
