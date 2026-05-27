## 禁止绑定的系统快捷键

以下组合键绑定为快捷键不生效。

- Alt + F4
- Alt + Shift + F4
- Alt + TAB
- Alt + Shift + TAB
- Ctrl + Shift + ESC

## 系统已存在的按键事件

已存在如下系统响应的按键事件，具体规格如下表。

表中的按键事件与自定义按键事件的触发有优先级关系，高优先级的事件会拦截低优先级事件，焦点事件响应优先级详见[按键事件](../../../Dev_Guide/arkui-cj/cj-common-events-device-input-event.md#按键事件)。

|快捷键|获焦组件|用途|事件处理类别|
|:---|:---|:---|:---|
|方向键、Shift + 方向键|输入框组件|移动光标|输入法|
|方向键、Shift + 方向键|通用组件|系统处于走焦状态时，用于方向走焦|系统按键|
|TAB、Shift + TAB|通用组件|触发进入走焦状态/走焦|系统按键|

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
    var message: String = 'disable'
    @State
    var shortCutEnable: Bool = false
    @State
    var keyValue: String = ''

    func build() {
        Row() {
            Column(5) {
                Text('Ctrl+A is ' + this.message)
                Button("Test short cut").onClick(
                    {
                        event =>
                        this.message = "I clicked Button"
                        AppLog.info("I clicked")
                    }
                ).keyboardShortcut(this.keyValue, [ModifierKey.CTRL])
                Button(this.message + 'shortCut').onClick(
                    {
                        event =>
                        this.shortCutEnable = !this.shortCutEnable
                        this.message = if (this.shortCutEnable) {
                            'enable'
                        } else {
                            'disable'
                        }
                        this.keyValue = if (this.shortCutEnable) {
                            'a'
                        } else {
                            ''
                        }
                    }
                )
                Button('multi-shortcut').onClick({
                    event => AppLog.info('Trigger keyboard shortcut success.')
                }).keyboardShortcut('q', [ModifierKey.CTRL]).keyboardShortcut('w', [ModifierKey.CTRL]).keyboardShortcut(
                    '', []) // 不生效，绑定了多个快捷键的组件不能取消快捷键
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

![uni_events_keyboardshortcut](figures/uni_events_keyboardshortcut.png)