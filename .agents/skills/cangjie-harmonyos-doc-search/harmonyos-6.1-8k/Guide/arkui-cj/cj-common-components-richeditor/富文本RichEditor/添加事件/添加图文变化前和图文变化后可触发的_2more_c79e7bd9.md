### 添加图文变化前和图文变化后可触发的回调

通过[onDidChange](../reference/arkui-cj/cj-text-input-richeditor.md#func-ondidchangeondidchangecallback)添加图文变化后可触发的回调。此回调适用于内容保存与同步，例如在用户完成内容编辑后，可使用该回调自动将最新内容保存至本地或同步至服务器。此外，它还适用于内容状态更新与渲染，例如在待办事项列表应用中，用户编辑富文本格式的待办事项描述后，可使用该回调更新待办事项在列表中的显示样式。

 <!-- run -->

```cangjie
package ohos_app_cangjie_entry
import kit.ArkUI.*
import kit.LocalizationKit.*
import ohos.arkui.state_macro_manage.*

@Entry
@Component
class EntryView {
    var controller: RichEditorController = RichEditorController()
    var controller1: RichEditorController = RichEditorController()
    var rangeBefore: TextRange = TextRange(10,13)
    var rangeAfter: TextRange = TextRange(15,18)

    func build() {
        Column() {
            Column() {
                RichEditor(this.controller)
                    .onReady({=>
                        this.controller.addTextSpan(content:"组件内图文变化前，触发回调。\n图文变化后，触发回调。")
                    })
                    .onDidChange({ rangeBefore: TextRange, rangeAfter: TextRange=>
                        this.controller1.addTextSpan(content:"\n图文变化后，触发回调：\nrangeBefore:" + "1234" +
                            "\nrangeAfter：" + "2345")
                        }).width(180)
                Text("查看回调内容：").fontSize(10).fontColor(Color.Gray).width(70)
                RichEditor(this.controller1).width(200).height(500)
            }.width(200).height(200)
        }
    }
}
```

![richeditor-change](figures/richeditor-change.gif)

### 添加输入法输入内容前和完成输入后可触发的回调

在添加输入法输入内容前，可以通过[aboutToImeInput](../reference/arkui-cj/cj-text-input-richeditor.md#func-abouttoimeinputcallbackricheditorinsertvalue-bool)触发回调。在输入法完成输入后，可以通过[onImeInputComplete](../reference/arkui-cj/cj-text-input-richeditor.md#func-onimeinputcompletecallbackricheditortextspanresult-unit)触发回调。

这两种回调机制适用于智能输入辅助。例如：在用户开始输入文本前，利用回调提供词汇联想，在用户完成输入后，利用回调执行自动化纠错或格式转换。

 <!-- run -->

```cangjie
package ohos_app_cangjie_entry
import kit.ArkUI.*
import kit.LocalizationKit.*
import ohos.arkui.state_macro_manage.*

@Entry
@Component
class EntryView {
    var controller: RichEditorController = RichEditorController()
    var controller1: RichEditorController = RichEditorController()

    func build() {
        Column() {
            Column() {
                RichEditor(this.controller)
                    .onReady({=>
                        this.controller.addTextSpan(content:"输入法输入内容前，触发回调。\n输入法完成输入后，触发回调。")
                    })
                    .aboutToImeInput({value:   RichEditorInsertValue=>
                        this.controller1.addTextSpan(content:"输入法输入内容前，触发回调：\n123")
                        return true;
                    })
                    .onImeInputComplete({value: RichEditorTextSpanResult=>
                        this.controller1.addTextSpan(content:"输入法完成输入后，触发回调：\n456")
                    }).width(200).height(200)

                Text("查看回调内容：").fontSize(10).fontColor(Color.Gray).width(200)
                RichEditor(this.controller1).width(200).height(200)
            }.width(200).height(200)
        }
    }
}
```

![shurufa](figures/shurufa.jpg)