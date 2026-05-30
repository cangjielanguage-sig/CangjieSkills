# 图标小符号（SymbolGlyph/SymbolSpan）

SymbolGlyph是图标小符号组件，便于使用精美的图标，如渲染多色图标和使用动效图标。SymbolSpan作为Text组件的子组件，可在文本中穿插显示图标小符号。具体用法请参见[SymbolGlyph](../../API_Reference/source_zh_cn/arkui-cj/cj-text-input-symbolglyph.md)和[SymbolSpan](../../API_Reference/source_zh_cn/arkui-cj/cj-text-input-symbolspan.md)。

## 创建图标

SymbolGlyph通过@r引用Resource资源来创建，目前仅支持系统预置的Symbol资源名。

相关资源请参见系统图标<!-- AddLink -->。

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
    func build() {
        SymbolGlyph(@r(sys.symbol.ohos_folder_badge_plus)).fontSize(96).renderingStrategy(
            SymbolRenderingStrategy.SINGLE).fontColor([Color.BLACK, Color.GREEN, Color.WHITE])
    }
}
```

![tubiao](figures/tubiao.jpg)