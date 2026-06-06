## 添加文本内容

除了直接在组件内输入内容，也可以通过[addTextSpan](../../API_Reference/source_zh_cn/arkui-cj/cj-text-input-richeditor.md#func-addtextspanstring-richeditortextspanoptions)添加文本内容。

此接口可以实现文本样式多样化，例如需要创建混合样式文本。

如果组件是获焦状态，有光标在闪烁，那么通过addTextSpan添加文本内容后，光标位置会更新，在新添加文本内容的右侧闪烁。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    var controller: RichEditorController = RichEditorController()
    var controller1: RichEditorController = RichEditorController()

    func build() {
        Column() {
            Button("addTextSpan").width(200).height(300).fontSize(13).onClick(
                {
                => this.controller.addTextSpan(value: "新添加一段文字。")
            })
            RichEditor(this.controller).width(200).height(200)
        }.width(100.percent)
    }
}
```

![add](figures/ad.gif)

## 添加图片内容

通过[addImageSpan](../../API_Reference/source_zh_cn/arkui-cj/cj-text-input-richeditor.md#func-addimagespanstring-richeditorimagespanoptions)添加图片内容。

此接口可用于内容丰富与可视化展示，例如在新闻中加入图片，在文档中加入数据可视化图形等。

如果组件是获焦状态，有光标在闪烁，那么通过addImageSpan添加图片内容后，光标位置会更新，在新添加图片内容的右侧闪烁。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import kit.LocalizationKit.*
import ohos.state_macro_manage.*
import ohos.component

@Entry
@Component
class EntryView {
    var controller: RichEditorController = RichEditorController()
    var controller1: RichEditorController = RichEditorController()
    func build() {
        Column() {
            Column() {
                Button("addTextSpan").width(200).height(300).fontSize(13).onClick(
                    {
                    => this.controller.addImageSpan(
                        value: @r(app.media.startIcon),
                        options: RichEditorImageSpanOptions(imageStyle: RichEditorImageSpanStyle(size: (24.vp, 24.vp)))
                    )
                })
                RichEditor(this.controller).onReady(
                    {
                    => this.controller.addTextSpan(value: "对此处文本进行复制粘贴操作可触发对应回调。")
                }).width(200).height(200)
            }.width(200).height(300)
        }
    }
}
```

![tupian](figures/tupian.jpg)