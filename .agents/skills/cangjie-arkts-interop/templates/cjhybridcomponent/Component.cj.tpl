package __PACKAGE_NAME__

import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*

@HybridComponentEntry
@Component
class __COMPONENT_NAME__ {
    @State
    var title: String = "__TITLE__"

    public func build() {
        Column {
            Text(this.title)
                .fontSize(32)
                .fontWeight(FontWeight.Bold)
            Button("__BUTTON_TEXT__")
                .fontSize(24)
                .margin(top: 24.vp)
                .onClick({
                    evt => this.title = "__CLICKED_TITLE__"
                })
        }
        .width(100.percent)
        .height(100.percent)
    }
}
