# 富文本（RichEditor）

RichEditor是支持图文混排和文本交互式编辑的组件，通常用于响应用户对图文混合内容的输入操作，例如可以输入图文的评论区。具体用法请参见[RichEditor](../../API_Reference/source_zh_cn/arkui-cj/cj-text-input-richeditor.md)。

## 创建RichEditor组件

开发者可以创建[不使用属性字符串](./cj-common-components-richeditor.md#创建不使用属性字符串构建的richeditor组件)构建的RichEditor组件。

### 创建不使用属性字符串构建的RichEditor组件

使用RichEditor(value: [RichEditorOptions](../../API_Reference/source_zh_cn/arkui-cj/cj-text-input-richeditor.md#options))接口创建非属性字符串构建的RichEditor组件，一般用于展示简单的图文信息，例如展示联系人的信息，也可以用于内容要求格式统一的场景，例如一些代码编辑器。

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
                    => this.controller.addTextSpan(value: "创建不使用属性字符串构建的RichEditor组件")
                })
            }.width(200)
        }.height(200)
    }
}
```

![bushiyongshuxing](figures/bushiyongshuxing.jpg)