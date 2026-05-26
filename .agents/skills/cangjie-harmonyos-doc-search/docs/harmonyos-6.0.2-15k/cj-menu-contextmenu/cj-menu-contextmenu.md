# ContextMenu

在页面范围内关闭通过[bindContextMenu](./cj-universal-attribute-menu.md#func-bindcontextmenu---unit-responsetype)属性绑定的菜单。

## 函数

### static func close()

```cangjie
public static func close(): Unit
```

**功能：** 可以通过该方法在页面范围内关闭通过[bindContextMenu](./cj-universal-attribute-menu.md#func-bindcontextmenu---unit-responsetype)给组件绑定的菜单。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## 示例代码

该示例为ContextMenu.close关闭通过bindContextMenu属性绑定的菜单。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @Builder
    func MenuBuilder() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Button("Test ContextMenu1")
            Divider().strokeWidth(2).margin(5).color(Color.BLACK)
            Button("Test ContextMenu2")
            Divider().strokeWidth(2).margin(5).color(Color.BLACK)
            Button("Test ContextMenu3")
        }.width(200).height(160)
    }

    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Column() {
                Text("Test ContextMenu").fontSize(20).width(100.percent).height(500).backgroundColor(0xAFEEEE).textAlign(
                    TextAlign.Center)
            }.bindContextMenu(builder: this.MenuBuilder, responseType: ResponseType.LongPress).onDragStart(
                {
                evt => ContextMenu.close()
            })
        }.width(100.percent).height(100.percent)
    }
}
```

![contextmenu_close](figures/contextmenu_close.gif)
