## 警告弹窗（AlertDialog）

需要向用户提问或得到用户的许可时，可使用警告弹窗。

- 警告弹窗用来提示重要信息，但会中断当前任务，尽量提供必要的信息和有用的操作。
- 避免仅使用警告弹窗提供信息，用户不喜欢被信息丰富但不可操作的警告打断。

该示例通过配置width、height、transition等接口定义了多个按钮弹窗的样式以及弹出动效。

 <!-- run -->

```cangjie
package ohos_app_cangjie_entry

import ohos.base.*
import ohos.arkui.component.*
import ohos.arkui.ui_context.*
import ohos.arkui.state_management.*
import ohos.arkui.state_macro_manage.*
import kit.PerformanceAnalysisKit.*

@Entry
@Component
class EntryView {
    func build() {
        Column() {
            Button('showAlertDialog')
                .onClick({
                    evt =>
                    let primaryButton = AlertDialogButtonOptions(
                        value: 'cancel',
                        action: {
                            => Hilog.info(0, "cangjie", 'Callback when the first button is clicked')
                        }
                    )
                    let secondaryButton = AlertDialogButtonOptions(
                        enabled: true,
                        defaultFocus: true,
                        style: DialogButtonStyle.Highlight,
                        value: 'ok',
                        action: {
                            => Hilog.info(0, "cangjie", 'Callback when the second button is clicked')
                        }
                    )
                    getUIContext().showAlertDialog(
                        AlertDialogParamWithButtons(
                            message: 'text',
                            title: 'title',
                            autoCancel: true,
                            alignment: DialogAlignment.Center,
                            offset: Offset(0.0, -20.0),
                            gridCount: 3,
                            transition: TransitionEffect.asymmetric(
                                TransitionEffect
                                    .OPACITY
                                    .animation(AnimateParam(duration: 3000, curve: Curve.Sharp))
                                    .combine(TransitionEffect.scale(ScaleOptions(x: 1.5, y: 1.5)))
                                    .animation(AnimateParam(duration: 3000, curve: Curve.Sharp)),
                                TransitionEffect
                                    .OPACITY
                                    .animation(AnimateParam(duration: 100, curve: Curve.Smooth))
                                    .combine(
                                        TransitionEffect
                                            .scale(ScaleOptions(x: 0.5, y: 0.5))
                                            .animation(AnimateParam(duration: 100, curve: Curve.Smooth)))
                            ),
                            primaryButton: primaryButton,
                            secondaryButton: secondaryButton
                        )
                    )
                }).width(100.percent).margin(top: 5)
        }
    }
}
```

![image](figures/UIContextShowAlertDialog.gif)