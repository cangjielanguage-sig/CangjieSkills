### onKeyEvent

```cangjie
public func onKeyEvent(callback: (KeyEvent)->Unit): This
```

当绑定方法的组件处于获焦状态下，外设键盘的按键事件会触发该方法，回调参数为[KeyEvent](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-event-key.md#keyevent)，可由该参数获得当前按键事件的按键行为（[KeyType](../../API_Reference/source_zh_cn/arkui-cj/cj-common-types.md#enum-keytype)）、键码（[keyCode](../../API_Reference/source_zh_cn/apis/InputKit/cj-apis-multimodalInput-keyCode.md#enum-keycode)）、按键英文名称（keyText）、事件来源设备类型（[KeySource](../../API_Reference/source_zh_cn/arkui-cj/cj-common-types.md#enum-keysource)）、事件来源设备id（deviceId）、元键按压状态（metaKey）、时间戳（timestamp）。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var buttonText: String = ''
    @State
    var buttonType: String = ''
    @State
    var columnText: String = ''
    @State
    var columnType: String = ''

    func build() {
        Column() {
            Button('onKeyEvent').defaultFocus(true).width(140).height(70).onKeyEvent(
                {
                    event =>
                    if (event.keyType.getValue() == KeyType.Down.getValue()) {
                        this.buttonType = 'Down'
                    }
                    if (event.keyType.getValue() == KeyType.Up.getValue()) {
                        this.buttonType = 'Up'
                    }
                    this.buttonText = """
                        Button:
                        KeyType: ${this.buttonType}
                        KeyCode: ${event.keyCode.toString()}
                        KeyText: ${event.keyText.toString()}
                    """
                }
            )

            Divider()
            Text(this.buttonText).fontColor(Color.GREEN)

            Divider()
            Text(this.columnText).fontColor(Color.RED)
        }.width(100.percent).height(100.percent).justifyContent(FlexAlign.Center).onKeyEvent(
            {
                event =>
                if (event.keyType.getValue() == KeyType.Down.getValue()) {
                    this.columnType = 'Down'
                }
                if (event.keyType.getValue() == KeyType.Up.getValue()) {
                    this.columnType = 'Up'
                }
                this.columnText = """
                Column:
                KeyType: ${this.columnType}
                KeyCode: ${event.keyCode.toString()}
                KeyText: ${event.keyText.toString()}
            """
            }
        )
    }
}
```

上述示例中给组件Button和其父容器Column绑定onKeyEvent。应用打开页面加载后，组件树上第一个可获焦的非容器组件自动获焦，设置Button为当前页面的默认焦点，由于Button是Column的子节点，Button获焦也同时意味着Column获焦。获焦机制请参见[焦点事件](./cj-common-events-focus-event.md)。

![KeyEvent](./figures/KeyEvent.gif)

打开应用后，依次在键盘上按这些按键：空格、回车、左Ctrl、左Shift、字母A、字母Z。

> **说明：**
>
> - 由于onKeyEvent事件默认是冒泡的，所以Button和Column的onKeyEvent都可以响应。
> - 每个按键都有2次回调，分别对应KeyType.Down和KeyType.Up，表示按键被按下，然后抬起。

如果要阻止冒泡，即仅Button响应键盘事件，Column不响应，在Button的onKeyEvent回调中加入event.stopPropagation()方法即可，如下：

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var buttonText: String = ''
    @State
    var buttonType: String = ''
    @State
    var columnText: String = ''
    @State
    var columnType: String = ''

    func build() {
        Column() {
            Button('onKeyEvent').defaultFocus(true).width(140).height(70).onKeyEvent(
                {
                    event =>
                    // 通过stopPropagation阻止事件冒泡
                    event.stopPropagation()
                    if (event.keyType.getValue() == KeyType.Down.getValue()) {
                        this.buttonType = 'Down'
                    }
                    if (event.keyType.getValue() == KeyType.Up.getValue()) {
                        this.buttonType = 'Up'
                    }
                    this.buttonText = """
                        Button:
                        KeyType: ${this.buttonType}
                        KeyCode: ${event.keyCode.toString()}
                        KeyText: ${event.keyText.toString()}
                    """
                }
            )

            Divider()
            Text(this.buttonText).fontColor(Color.GREEN)