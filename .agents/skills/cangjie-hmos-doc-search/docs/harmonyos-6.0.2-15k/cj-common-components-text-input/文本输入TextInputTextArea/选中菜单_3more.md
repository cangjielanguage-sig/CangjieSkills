## 选中菜单

输入框中的文字被选中时会弹出包含剪切、复制、翻译的菜单。

TextInput:

```cangjie
TextInput( text: '这是一段文本，用来展示选中菜单')
```

![Text13](figures/Text13.png)

TextArea:

```cangjie
TextArea( text: '这是一段文本，用来展示选中菜单')
```

![Text13](figures/Text13.png)

## 自动填充

输入框可以通过[contentType](../../cj-text-input-textinput/.overview.md)属性设置自动填充类型。

支持的类型请参见[ContentType](../../cj-common-types/.overview.md)。

```cangjie
TextInput( placeholder: '输入你的邮箱...' )
    .width(95.percent)
    .height(40)
    .margin(20)
    .contentType(ContentType.EMAIL_ADDRESS)
```

## 键盘避让

键盘抬起后，具有滚动能力的容器组件在横竖屏切换时，才会生效键盘避让，若希望无滚动能力的容器组件也生效键盘避让，建议在组件外嵌套一层具有滚动能力的容器组件，比如[Scroll](../../cj-scroll-swipe-scroll/.overview.md)、[List](../../cj-scroll-swipe-list/.overview.md)、[Grid](../../cj-scroll-swipe-grid/.overview.md)。

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    var placeHolderArr: Array<String> = ["1", "2", "3", "4", "5", "6", "7"];
    func build() {
        Scroll() {
            Column {
                ForEach(
                    this.placeHolderArr,
                    itemGeneratorFunc: {
                        placeholder: String, _: Int64 => TextInput(placeholder: 'TextInput ' + placeholder).margin(30)
                    }
                )
            }
        }.height(100.percent).width(100.percent)
    }
}
```

![textinputkeyboardavoid](figures/TextInputKeyboardAvoid.gif)