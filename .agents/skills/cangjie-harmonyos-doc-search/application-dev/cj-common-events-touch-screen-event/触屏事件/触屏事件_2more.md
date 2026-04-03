# 触屏事件

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

触屏事件指当手指/手写笔在组件上按下、滑动、抬起时触发的回调事件。包括[点击事件](#点击事件)和[触摸事件](#触摸事件)。触屏事件的原理如下图所示：

**图1** 触摸事件原理

![touchEvent](./figures/touchEvent.png)

## 点击事件

点击事件是指通过手指或手写笔做出一次完整的按下和抬起动作。当发生点击事件时，会触发以下回调函数：

```cangjie
func onClick(callback: (ClickEvent)->Unit): This
```

event参数提供点击事件相对于窗口或组件的坐标位置，以及发生点击的事件源。

例如通过按钮的点击事件控制图片的显示和隐藏。

 <!-- run -->

```cangjie
package ohos_app_cangjie_entry
import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*
import ohos.resource_manager.*
import ohos.resource.__GenerateResource__

@Entry
@Component
class EntryView {
    @State var flag = true
    @State var btnMsg: String = 'show'

    func build() {
        Column {
            Button(this.btnMsg)
                .width(80)
                .height(30)
                .margin(30)
                .onClick({ event =>
                    if (this.flag) {
                        this.btnMsg = 'hide'
                    } else {
                        this.btnMsg = 'show'
                    }
                    // 点击Button控制Image的显示和消失
                    this.flag = !this.flag
                })
            if (this.flag) {
                Image(@r(app.media.startIcon))
                    .width(200)
                    .height(200)
            }
        }
        .height(100.percent)
        .width(100.percent)
    }
}
```

**图2** 通过按钮的点击事件控制图片的显示和隐藏

![ClickEventControl.gif](./figures/ClickEventControl.gif)