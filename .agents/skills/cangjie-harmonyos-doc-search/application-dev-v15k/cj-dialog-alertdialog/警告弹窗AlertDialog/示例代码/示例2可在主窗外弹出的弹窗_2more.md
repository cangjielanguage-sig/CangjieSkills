### 示例2（可在主窗外弹出的弹窗）

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Column(5.vp) {
            Button("button dialog").onClick(
                {
                => AlertDialog.show(
                    AlertDialogParamWithOptions(
                        "text",
                        title: "title",
                        subtitle: "subtitle",
                        autoCancel: true,
                        cancel: {=> AppLog.info("Closed callbacks")},
                        alignment: DialogAlignment.Center,
                        offset: Offset(0, -20),
                        showInSubWindow: true,
                        buttonDirection: DialogButtonDirection.HORIZONTAL,
                        gridCount: 4,
                        onWillDismiss: {
                            dismissDialogAction: DismissDialogAction => match (dismissDialogAction.reason) {
                                case PRESS_BACK => dismissDialogAction.dismiss()
                                case TOUCH_OUTSIDE => dismissDialogAction.dismiss()
                                case _ => ()
                            }
                        },
                        buttons: [
                            AlertDialogButtonOptions(value: "按钮",
                                action: {=> AppLog.info("Callback when button1 is clicked")}),
                            AlertDialogButtonOptions(value: "按钮",
                                action: {=> AppLog.info("Callback when button1 is clicked")}),
                            AlertDialogButtonOptions(value: "按钮",
                                action: {=> AppLog.info("Callback when button1 is clicked")})
                        ]
                    )
                )
            }).backgroundColor(0x317aff)
        }
    }
}
```

![alertdialog2](figures/alertdialog2.png)

### 示例3（设置弹窗的样式）

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Column(5.vp) {
            Button("button dialog").onClick(
                {
                => AlertDialog.show(
                    AlertDialogParamWithConfirm(
                        "button dialog",
                        title: "AlertDialog 1",
                        autoCancel: true,
                        cancel: {=> AppLog.info("Closed callbacks")},
                        alignment: DialogAlignment.Center,
                        offset: Offset(0, -20),
                        gridCount: 3,
                        width: 300,
                        height: 200,
                        cornerRadius: BorderRadiuses(topLeft: 20, topRight: 20, bottomLeft: 20, bottomRight: 20),
                        borderWidth: 1,
                        borderStyle: EdgeStyle.DASHED,
                        borderColor: Color.BLUE,
                        backgroundColor: Color.WHITE,
                        onWillDismiss: {
                            dismissDialogAction: DismissDialogAction => match (dismissDialogAction.reason) {
                                case PRESS_BACK => dismissDialogAction.dismiss()
                                case TOUCH_OUTSIDE => dismissDialogAction.dismiss()
                                case _ => ()
                            }
                        },
                        confirm: AlertDialogButtonOptions(value: "button",
                            action: {=> AppLog.info("Button-clicking callback")})
                    ),
                    ActionSheetShadowOptions(20.0, color: Color.GREY, offsetX: 50.0, offsetY: 0.0)
                )
            }).backgroundColor(0x317aff)
        }
    }
}
```

![alertdialog3](figures/alertdialog3.png)