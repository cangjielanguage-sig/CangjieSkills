## 主动获焦/失焦

使用focusControl中的方法：

```cangjie
public static func requestFocus(value: ?String): Bool
```

调用此接口可以主动让焦点转移至参数指定的组件上，焦点转移生效时间为下一个帧信号。

 <!-- run -->

```cangjie
package ohos_app_cangjie_entry
import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State var btColor: UInt32 = 0x2787d9
    @State var btColor2: UInt32 = 0x2787d9

    func build() {
        Column(space: 20) {
            Column(space: 5) {
                Button("Button")
                    .width(200)
                    .height(70)
                    .fontColor(Color.White)
                    .focusOnTouch(true)
                    .backgroundColor(0x2787d9)
                    .onFocus({ =>
                        btColor = 0xd5d5d5
                    })
                    .onBlur({ =>
                        btColor = 0x2787d9
                    })
                    .id("testButton")

                Button("Button")
                    .width(200)
                    .height(70)
                    .fontColor(Color.White)
                    .focusOnTouch(true)
                    .backgroundColor(btColor2)
                    .onFocus({ =>
                        btColor2 = 0xd5d5d5
                    })
                    .onBlur({ =>
                        btColor2 = 0x2787d9
                    })
                    .id("testButton2")

                Divider()
                    .vertical(false)
                    .width(80.percent)
                    .backgroundColor(0x707070)
                    .height(10)
                //点击focusControl.requestFocus按钮，第二个Button获焦。
                Button("FocusControl.requestFocus")
                    .width(200)
                    .height(70)
                    .fontColor(Color.White)
                    .onClick({ evt =>
                        FocusControl.requestFocus("testButton2")
                    })
                    .backgroundColor(0xff2787d9)
            }
        }
        .width(100.percent)
        .height(100.percent)
    }
}
```

![focus-2](figures/focus-2.gif)

## 焦点与按键事件

当组件获焦且存在点击事件（`onClick`）或单指单击事件（`TapGesture`）时，回车和空格会触发对应的事件回调。

> **说明：**
>
> - 点击事件（`onClick`）或单指单击事件（`TapGesture`）在回车、空格触发对应事件回调时，默认不冒泡传递，即父组件对应[按键事件](../reference/arkui-cj/cj-universal-event-key.md)不会被同步触发。
> - 按键事件（`onKeyEvent`）默认冒泡传递，即同时会触发父组件的按键事件回调。
> - 组件同时存在点击事件（`onClick`）和按键事件（`onKeyEvent`），在回车、空格触发时，两者都会响应。
> - 获焦组件响应点击事件（`onClick`），与焦点激活态无关。

 <!-- run -->

```cangjie
package ohos_app_cangjie_entry
import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State var count: Int = 0
    @State var name: String = "Button"

    func build() {
        Column {
            Button(name)
                .fontSize(30)
                .onClick({ evt =>
                    count++
                    if (count <= 0) {
                        name = "count is negative number"
                    } else if (count % 2 == 0) {
                        name = "count is even number"
                    } else {
                        name = "count is odd number"
                    }
                })
                .height(60)
        }
        .height(100.percent).width(100.percent).justifyContent(FlexAlign.Center)
    }
}
```

![focus-4](figures/focus-4.gif)