## 基础类型定义

### enum SubMenuExpandingMode

```cangjie
public enum SubMenuExpandingMode {
    | SIDE_EXPAND
    | EMBEDDED_EXPAND
    | STACK_EXPAND
}
```

**功能：** Menu子菜单展开样式枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### EMBEDDED_EXPAND

```cangjie
EMBEDDED_EXPAND
```

**功能：** 直接展开样式, 子菜单嵌于主菜单内展开。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### SIDE_EXPAND

```cangjie
SIDE_EXPAND
```

**功能：** 默认展开样式, 子菜单位于同一平面侧边展开。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### STACK_EXPAND

```cangjie
STACK_EXPAND
```

**功能：** 堆叠样式, 子菜单浮于主菜单上方展开。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### func getValue()<sup>deprecated</sup>

```cangjie
public func getValue(): Int32
```

**功能：** 获取展开样式对应的整数格式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## 示例代码

该示例通过配置MenuItem中的builder参数实现多级菜单。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import kit.LocalizationKit.*

@Entry
@Component
class EntryView {
    @State
    var select: Bool = true
    let iconStr: AppResource = @r(app.media.startIcon)
    var iconStr2: AppResource = @r(app.media.right)

    @Builder
    func SubMenu() {
        Menu() {
            MenuItem(startIcon: "", content: "复制", endIcon: "", labelInfo: "Ctrl+C")
            MenuItem(startIcon: "", content: "粘贴", endIcon: "", labelInfo: "Ctrl+V")
        }
    }

    @Builder
    func MyMenu() {
        Menu() {
            MenuItem(startIcon: @r(app.media.startIcon), content: @r(app.string.contentName),
                endIcon: @r(app.media.blank), labelInfo: @r(app.string.emptyName))
            MenuItem(startIcon: @r(app.media.startIcon), content: @r(app.string.contentName),
                endIcon: @r(app.media.blank), labelInfo: @r(app.string.emptyName)).enabled(false)
            MenuItem(
                startIcon: this.iconStr,
                content: @r(app.string.contentName),
                endIcon: this.iconStr,
                labelInfo: @r(app.string.emptyName),
                builder: {=> bind(this.SubMenu, this)()}
            )
            MenuItemGroup(header: "小标题", footer: "") {
                =>
                MenuItem(
                    startIcon: this.iconStr,
                    content: @r(app.string.contentName),
                    endIcon: @r(app.string.emptyName),
                    labelInfo: @r(app.string.emptyName),
                    builder: {=> bind(this.SubMenu, this)()}
                )
                MenuItem(
                    startIcon: @r(app.media.startIcon),
                    content: @r(app.string.contentName),
                    endIcon: @r(app.media.right),
                    labelInfo: @r(app.string.emptyName),
                    builder: {=> bind(this.SubMenu, this)()}
                )
                MenuItem(
                    startIcon: "",
                    content: "菜单选项",
                    endIcon: "",
                    labelInfo: "",
                ).selectIcon(true).selected(select).onChange({
                    selected => iconStr2 = @r(app.media.foreground)
                })
            }
        }
    }

    func build() {
        Row() {
            Column() {
                Text("click to show menu").fontSize(50).fontWeight(FontWeight.Bold)
            }.bindMenu(builder: this.MyMenu).width(50.percent)
        }.height(100.percent)
    }
}
```

![menu](figures/menu.png)