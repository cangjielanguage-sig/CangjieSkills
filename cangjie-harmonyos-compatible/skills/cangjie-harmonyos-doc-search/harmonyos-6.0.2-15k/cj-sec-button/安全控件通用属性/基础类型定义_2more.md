## 基础类型定义

### enum SecurityComponentLayoutDirection

```cangjie
public enum SecurityComponentLayoutDirection {
    | Horizontal
    | Vertical
}
```

**功能：** 设置安全控件上图标和文字分布的方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### Horizontal

```cangjie
Horizontal
```

**功能：** 安全控件上图标和文字分布的方向为水平排列。

**起始版本：** 20

#### Vertical

```cangjie
Vertical
```

**功能：** 安全控件上图标和文字分布的方向为垂直排列。

**起始版本：** 20

## 示例

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import ohos.base.*
import ohos.state_manage.*
import ohos.state_macro_manage.*
import ohos.component.*

@Entry
@Component
class EntryView {
    func build() {
        Row() {
            Column(5) {
                // 生成一个保存按钮，并设置它的SecurityComponent属性。
                SaveButton().fontSize(35).fontColor(Color.WHITE).iconSize(30).layoutDirection(
                    SecurityComponentLayoutDirection.Horizontal).borderWidth(1).borderStyle(BorderStyle.Dashed).
                    borderColor(Color.BLUE).borderRadius(20).fontWeight(FontWeight.W100).iconColor(Color.WHITE).padding(
                    left: 50,
                    top: 50,
                    bottom: 50,
                    right: 50
                ).textIconSpace(20).backgroundColor(0x3282f6)
                SaveButton().size(width: 200, height: 100)
                SaveButton().size(width: 200, height: 100)
                SaveButton(icon: SaveIconStyle.FullFilled, text: SaveDescription.Download, buttonType: ButtonType.Normal
                ).size(width: 150, height: 80).borderRadius(20.0)
                SaveButton().constraintSize(maxWidth: 60)
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

![SecButton](figures/sec_button.png)