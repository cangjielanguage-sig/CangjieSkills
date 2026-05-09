# 富文本（RichEditor）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

RichEditor是支持图文混排和文本交互式编辑的组件，通常用于响应用户对图文混合内容的输入操作，例如可以输入图文的评论区。具体用法请参见[RichEditor](../reference/arkui-cj/cj-text-input-richeditor.md)。

## 创建不使用属性字符串构建的RichEditor组件

创建非属性字符串构建的RichEditor组件，一般用于展示简单的图文信息，例如展示联系人的信息，也可以用于内容要求格式统一的场景，例如一些代码编辑器。

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
    var option: RichEditorTextSpanOptions = RichEditorTextSpanOptions()

    func build() {
        Column() {
            Column() {
                RichEditor(this.controller)
                    .onReady({=>
                        this.controller.addTextSpan(content:"创建不使用属性字符串构建的RichEditor组件")
                    })
            }.width(200)
        }.height(200)
    }
}
```

![bushiyongshuxing](figures/bushiyongshuxing.jpg)

## 设置属性

### 设置自定义选择菜单

通过[bindSelectionMenu](../reference/arkui-cj/cj-text-input-richeditor.md#func-bindselectionmenuricheditorspantype-custombuilder-responsetype-selectionmenuoptions)设置自定义选择菜单。

组件原本具有默认的文本选择菜单，包含复制、剪切和全选的功能。用户可使用该属性设定自定义菜单，例如翻译英文、加粗字体等丰富的菜单功能。

当自定义菜单超长时，建议内部嵌套Scroll组件使用，避免键盘被遮挡。

 <!-- run -->

```cangjie
package ohos_app_cangjie_entry
import kit.ArkUI.*
import kit.LocalizationKit.*
import ohos.arkui.state_macro_manage.*
import ohos.hilog.*
import ohos.arkui.component.CopyOptions as MyCopyOptions
import ohos.resource.*
import std.collection.ArrayList

@Entry
@Component
class EntryView {
    let controller: RichEditorController = RichEditorController()

    @Builder
    func RightClickTextCustomMenu() {
        Menu() {
            MenuItemGroup() {=>
                MenuItem(startIcon: @r(app.media.startIcon), endIcon: @r(app.media.startIcon), content: "剪切", labelInfo: "Ctrl+X" )
                MenuItem(startIcon: @r(app.media.startIcon), endIcon: @r(app.media.startIcon), content: "复制", labelInfo: "Ctrl+C" )
                MenuItem(startIcon: @r(app.media.startIcon), endIcon: @r(app.media.startIcon), content: "粘贴", labelInfo: "Ctrl+V" )
            }
        }.backgroundColor(0XF0F0F0)
    }
    func build() {
        Scroll() {
            Column {
                RichEditor(this.controller)
                .bindSelectionMenu(
                    spanType: RichEditorSpanType.Text,
                    content: bind(this.RightClickTextCustomMenu, this),
                    responseType: ResponseType.LongPress,
                    options: SelectionMenuOptions( onDisappear: {
                            => Hilog.info(0, " ", "自定义选择菜单关闭时  触发该回调")
                        },
                        onAppear: {
                            => Hilog.info(0, " ", "自定义选择菜单弹出时回调")
                        }
                    )
                )
                .onReady({ =>
                    controller.addTextSpan(content: "这是一段文本，用来展示选中菜单")
                })
            }
        }
    }
}
```

![caidan](figures/menu.jpg)