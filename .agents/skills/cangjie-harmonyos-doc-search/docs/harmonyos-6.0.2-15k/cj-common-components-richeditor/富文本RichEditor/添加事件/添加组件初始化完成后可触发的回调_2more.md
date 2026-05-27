### 添加组件初始化完成后可触发的回调

通过[onReady](../../API_Reference/source_zh_cn/arkui-cj/cj-text-input-richeditor.md#func-onready---unit)来添加组件初始化完成后可触发的回调。

该回调可在组件初始化后，有效地展示包括图文和表情在内的丰富内容。例如，利用富文本组件展示新闻时，此回调可触发从服务器获取图文数据的操作。随后，将获取到的数据填充至组件中，确保组件在初始化完成后能够迅速在页面上呈现完整的新闻内容。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import kit.LocalizationKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    var controller: RichEditorController = RichEditorController()
    var option: RichEditorTextSpanOptions = RichEditorTextSpanOptions()

    func build() {
        Column() {
            Column() {
                RichEditor(this.controller).onReady(
                    {
                    => this.controller.addTextSpan(value: "onReady回调内容是组件内预置文本")
                })
            }.width(200)
        }.height(200)
    }
}
```

![chushihua](figures/chushihua.jpg)

### 添加组件内容被选中时可触发的回调

通过[onSelect](../../API_Reference/source_zh_cn/arkui-cj/cj-text-input-richeditor.md#func-onselectricheditorselection---unit)来添加组件内容被选中时可触发的回调。

该回调可在文本选择后增强操作体验。例如，在选中文本后，可在回调中触发弹出菜单，以便用户进行文本样式的修改。或者对选中的文本进行内容分析和处理，为用户提供输入建议，从而提升文本编辑的效率和便捷性。

触发回调有两种方式：一是通过鼠标左键选择，即按下左键进行选择，然后在松开左键时触发回调。二是通过手指触摸选择，即用手指进行选择，然后在松开手指时触发回调。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import kit.LocalizationKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    var controller: RichEditorController = RichEditorController()
    var controller1: RichEditorController = RichEditorController()
    var option: RichEditorTextSpanOptions = RichEditorTextSpanOptions()

    func build() {
        Column() {
            Column() {
                RichEditor(this.controller).onReady(
                    {
                    => this.controller.addTextSpan(value: "选中此处文本，触发onselect回调。")
                }).onSelect({
                    value1: RichEditorSelection => this.controller.addTextSpan(value: "1234")
                }).width(200).height(200)
                Text("查看回调内容：").fontSize(10).fontColor(Color.GRAY).width(200)
                RichEditor(this.controller1).width(200).height(200)
            }.width(200)
        }.height(200)
    }
}
```

![callback](figures/callback.gif)