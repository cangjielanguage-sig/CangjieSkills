## 自定义气泡

开发者可以使用CustomPopupOptions的builder创建自定义气泡，\@Builder中可以放自定义的内容。除此之外，还可以通过popupColor等参数控制气泡样式。

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
    var customPopup: Bool = false
    @State
    var custom: String = "Custom Wait"
    // popup构造器定义弹框内容
    @Builder
    func popupBuilder() {
        Row(2) {
            Image(@r(app.media.startIcon)).width(24).height(24).margin(left: 5)
            Text('This is Custom Popup').fontSize(15)
        }.width(200).height(50).padding(5)
    }
    func build() {
        Column() {
            Button('CustomPopupOptions').position(x: 100, y: 200).onClick({
                => this.customPopup = !this.customPopup
            }).bindPopup(
                show: this.customPopup,
                popup: CustomPopupOptions(
                    builder: bind(popupBuilder, this), // 气泡的内容
                    placement: Placement.Bottom, // 气泡的弹出位置
                    popupColor: Color.PINK, // 气泡的背景色
                    onStateChange: {
                        evt =>
                        custom = "stateChange: ${evt.isVisible}"
                        if (!evt.isVisible) {
                            customPopup = true
                        }
                    }
                )
            )
        }.height(100.percent)
    }
}
```

使用者通过配置placement参数将弹出的气泡放到需要提示的位置。弹窗构造器会触发弹出提示信息，来引导使用者完成操作，也让使用者有更好的UI体验。

![popup3](figures/popup3.jpeg)

## 气泡样式

气泡除了可以通过builder实现自定义气泡，还可以通过接口设置气泡的样式和显示效果。

背景颜色：气泡的背景色默认为透明，但是会有一个默认的模糊效果，手机上为COMPONENT\_ULTRA\_THICK。

蒙层样式：气泡默认有蒙层，且蒙层的颜色为透明。

显示大小：气泡大小有内部的builder大小或者message的长度决定的。

显示位置：气泡默认显示在宿主组件的下方，可以通过Placement接口来配置其显示位置以及对齐方向。

以下示例通过设置popupColor（背景颜色）、mask（蒙层样式）、width（气泡宽度）、placement（显示位置）实现气泡的样式。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var handlePopup: Bool = false
    func build() {
        Column(100) {
            Button('PopupOptions').onClick({
                => this.handlePopup = !this.handlePopup
            }).bindPopup(
                show: this.handlePopup,
                popup: PopupOptions(
                    width: 200,
                    message: 'This is a popup.',
                    popupColor: Color.RED,
                    mask: Color(0x33d9d9d9), // 设置气泡的背景色
                    placement: Placement.Top,
                    backgroundBlurStyle: BlurStyle.NONE
                )
                // 去除背景模糊效果需要关闭气泡的模糊背景
            )
        }.width(100.percent)
    }
}
```

![image](figures/UIpopupStyle.gif)