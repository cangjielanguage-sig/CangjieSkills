### onMouse

```cangjie
public func onMouse(event: ?(MouseEvent) -> Unit): T
```

鼠标事件回调。绑定该API的组件每当鼠标指针在该组件内产生行为（MouseAction）时，触发事件回调，参数为[MouseEvent](../reference/arkui-cj/cj-common-types.md#class-mouseevent)对象，表示触发此次的鼠标事件。该事件支持自定义冒泡设置，默认父子冒泡。常用于开发者自定义的鼠标行为逻辑处理。

开发者可以通过回调中的MouseEvent对象获取触发事件的坐标（screenX/screenY/x/y）、按键（[MouseButton](../reference/arkui-cj/cj-common-types.md#enum-mousebutton)）、行为（[MouseAction](../reference/arkui-cj/cj-common-types.md#enum-mouseaction)）、时间戳（timestamp）、交互组件的区域（[EventTarget](../reference/arkui-cj/cj-common-types.md#class-eventtarget)）、事件来源（[SourceType](../reference/arkui-cj/cj-common-types.md#enum-sourcetype)）等。

> **说明：**
>
> 按键（MouseButton）的值：Left/Right/Middle/Back/Forward 均对应鼠标上的实体按键，当这些按键被按下或松开时触发这些按键的事件。None表示无按键，会出现在鼠标没有按键按下或松开的状态下，移动鼠标所触发的事件中。

 <!-- run -->

```cangjie
package ohos_app_cangjie_entry
import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State var buttonText: String = ''
    @State var columnText: String = ''
    @State var hoverText: String = 'Not Hover'
    @State var color: Color = Color.Gray

    func build() {
        Column(space: 20) {
            Button(this.hoverText)
                .width(200)
                .height(100)
                .backgroundColor(this.color)
                .onHover({isHover =>
                    if (isHover) {
                        this.hoverText = 'Hovered!'
                        this.color = Color.Green
                    } else {
                        this.hoverText = 'Not Hover'
                        this.color = Color.Gray
                    }
                })
                .onMouse({event =>
                this.buttonText = "Button onMouse:\n" +
                    "x,y = (${event.x},${event.y})\n" +
                    "windowXY=(${event.screenX},${event.screenY})"
                })
            Divider()
            Text(this.buttonText).fontColor(Color.Green)
            Divider()
            Text(this.columnText).fontColor(Color.Red)
        }
        .width(100.percent)
        .height(100.percent)
        .justifyContent(FlexAlign.Center)
        .borderWidth(2.px)
        .borderColor(Color.Red)
        .onMouse({event =>
                this.columnText = "Column onMouse:\n" +
                    "x,y = (${event.x},${event.y})\n" +
                    "windowXY=(${event.screenX},${event.screenY})"
        })
    }
}
```

![onMouse1](./figures/onMouse1.gif)