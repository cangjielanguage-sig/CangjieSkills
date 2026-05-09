## 气泡的动画

气泡通过定义transition控制气泡的进场和出场动画效果。

 <!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State var handlePopup: Bool = false
    @State var customPopup: Bool = false
    @State var popup: Bool = false
    @State var custom: String = "Custom Wait"
    // Popup builder defines popup content
    @Builder
    func popupBuilder() {
        Row() {
            Text('Custom Popup with transitionEffect').fontSize(10)
        }
        .height(50)
        .padding(5)
    }

    func build() {
        Flex(direction: FlexDirection.Column) {
            // 类型设置弹框内容
            Button('PopupOptions')
                .position(x: 100, y: 150)
                .onClick ({
                    e => this.popup = !this.popup
                })
                .bindPopup(
                    this.popup,
                    PopupOptions(
                        message: "This is popup with transitionEffect",
                        placement: Placement.Top,
                        showInSubWindow: false,
                        onStateChange: {
                            e =>
                            custom = "stateChange: ${e.isVisible}"
                            if (!e.isVisible) {
                                this.popup = true
                            }
                        },
                        // 设置弹窗显示动效与退出动效为平移动效
                        transition: TransitionEffect.asymmetric(
                            TransitionEffect
                            .OPACITY
                            .animation(AnimateParam(duration: 1000, curve: Curve.Ease))
                            .combine(
                                TransitionEffect.translate(TranslateOptions(x: 50, y: 50))
                            ),
                            TransitionEffect.IDENTITY
                        )
                    )
                )

            // CustomPopupOptions 类型设置弹框内容
            Button('CustomPopupOptions')
                .position(x: 80, y: 300)
                .onClick ({
                    e => this.customPopup = !this.customPopup
                })
                .bindPopup(
                    this.customPopup,
                    CustomPopupOptions(
                        builder: bind(popupBuilder, this),
                        placement: Placement.Top,
                        showInSubWindow: false,
                        onStateChange: {
                            e =>
                            custom = "stateChange: ${e.isVisible}"
                            if (!e.isVisible) {
                                this.customPopup = true
                            }
                        },
                        // 设置弹窗显示动效与退出动效为缩放动效
                        transition: TransitionEffect
                            .scale(ScaleOptions(x: 1.0, y: 0.0))
                            .animation(AnimateParam(duration: 500, curve: Curve.Ease))
                    )
                )
        }.width(100.percent).padding(top: 5)
    }
}
```

![popup_transition](figures/popup_transition.gif)

## 自定义气泡

开发者可以使用CustomPopupOptions的builder创建自定义气泡，\@Builder中可以放自定义的内容。除此之外，还可以通过popupColor等参数控制气泡样式。

 <!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*
import kit.LocalizationKit.*
import ohos.resource.*

@Entry
@Component
class EntryView {
    @State var customPopup: Bool = false
    @State var custom: String = "Custom Wait"
    // popup构造器定义弹框内容
    @Builder
    func popupBuilder() {
        Row(space: 2) {
            Image(@r(app.media.startIcon))
                .width(24)
                .height(24)
                .margin(left: 5)
            Text('This is Custom Popup').fontSize(15)
        }
        .width(200)
        .height(50)
        .padding(5)
    }
    func build() {
        Column() {
            Button('CustomPopupOptions')
                .position(x: 100, y: 200)
                .onClick ({
                    e => this.customPopup = !this.customPopup
                })
                .bindPopup(
                    this.customPopup,
                    CustomPopupOptions(
                        builder: bind(popupBuilder, this), // 气泡的内容
                        placement: Placement.Bottom, // 气泡的弹出位置
                        popupColor: Color.Red, // 气泡的背景色
                        showInSubWindow: false,
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

![popup3](figures/popup3.gif)