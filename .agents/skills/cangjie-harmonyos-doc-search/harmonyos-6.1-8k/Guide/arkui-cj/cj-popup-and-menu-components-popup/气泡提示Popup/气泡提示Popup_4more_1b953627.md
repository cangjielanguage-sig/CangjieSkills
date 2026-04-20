# 气泡提示（Popup）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

Popup属性可绑定在组件上显示气泡弹窗提示，设置弹窗内容、交互逻辑和显示状态。主要用于屏幕录制、信息弹出提醒等显示状态。

气泡分为两种类型，一种是系统提供的气泡[PopupOptions](../reference/arkui-cj/cj-common-types.md#class-popupoptions)，一种是开发者可以自定义的气泡[CustomPopupOptions](../reference/arkui-cj/cj-common-types.md#class-custompopupoptions)。其中，PopupOptions通过配置primaryButton和secondaryButton来设置带按钮的气泡，CustomPopupOptions通过配置builder来设置自定义的气泡。

气泡可以通过配置[mask](../reference/arkui-cj/cj-common-types.md#var-mask)来实现模态和非模态窗口，mask为true或者颜色值的时候，气泡为模态窗口，mask为false时，气泡为非模态窗口。

## 文本提示气泡

文本提示气泡常用于只展示带有文本的信息提示，不带有任何交互的场景。Popup属性需绑定组件，当bindPopup属性中参数show为true时会弹出气泡提示。

在Button组件上绑定Popup属性，每次点击Button按钮，handlePopup会切换布尔值，当值为true时，触发bindPopup弹出气泡。

 <!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State var handlePopup: Bool = false
    func build() {
        Column {
            Button('PopupOptions')
                .onClick ({
                    e => this.handlePopup = !this.handlePopup
                })
                .bindPopup(
                    this.handlePopup,
                    PopupOptions(message: 'This is a popup with PopupOptions', placement: Placement.Bottom)
                )
        }.width(100.percent).padding(top: 5)
    }
}
```

![气泡提示（Popup）](figures/popup.gif)

## 添加气泡状态变化的事件

通过onStateChange参数为气泡添加状态变化的事件回调，可以判断当前气泡的显示状态。

 <!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State var handlePopup: Bool = false
    func build() {
        Column {
            Button('PopupOptions')
                .onClick ({
                    e => this.handlePopup = !this.handlePopup
                })
                .bindPopup(
                    this.handlePopup,
                    PopupOptions(
                        message: 'This is a popup with PopupOptions',
                        placement: Placement.Bottom,
                        onStateChange: {
                            e =>
                            if (!e.isVisible) {
                                this.handlePopup = false
                            }
                        }
                    )
                )
        }.width(100.percent).padding(top: 5)
    }
}
```

![PopupOnStateChange](figures/popupOption.gif)

## 带按钮的提示气泡

通过primaryButton、secondaryButton属性为气泡最多设置两个Button按钮，通过此按钮进行简单的交互，开发者可以通过配置action参数来设置想要触发的操作。

 <!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*
import ohos.hilog.*

@Entry
@Component
class EntryView {
    @State var handlePopup: Bool = false
    func build() {
        Column() {
            Button('PopupOptions')
                .margin(top: 200)
                .onClick ({
                    e => this.handlePopup = !this.handlePopup
                })
                .bindPopup(
                    this.handlePopup,
                    PopupOptions(
                        message: 'This is a popup with PopupOptions',
                        placement: Placement.Bottom,
                        primaryButton: PopupButton(
                            value: "Confirm",
                            action: { => Hilog.info(0, 'cangjie', 'Confirm')}
                        ),
                        secondaryButton: PopupButton(
                            value: "Cancel",
                            action: { => Hilog.info(0, 'cangjie', 'Cancel')}
                        )
                    )
                )
        }.width(100.percent).padding(top: 5)
    }
}
```

![popup2](figures/popup2.gif)