## class ActionSheet

```cangjie
public class ActionSheet {}
```

**功能：** 构造一个ActionSheet类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### static func show(ActionSheetOptions, ActionSheetShadowOptions)

```cangjie
public static func show(value: ActionSheetOptions, shadow: ActionSheetShadowOptions): Unit
```

**功能：** 定义列表弹窗并弹出。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ActionSheetOptions](cj-dialog-actionsheet.md#class-actionsheetoptions)|是|-|配置列表选择弹窗的参数。|
|shadow|[ActionSheetShadowOptions](cj-dialog-actionsheet.md#class-actionsheetshadowoptions)|是|-|设置弹窗背板的阴影。|

**示例：**

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Row {
            Column() {
                Button("Click to Show ActionSheet").onClick(
                    {
                        evt =>
                        let sheets: Array<SheetInfo> = [
                            SheetInfo("apple", {=> AppLog.info("apple")}),
                            SheetInfo("banana", {=> AppLog.info("banana")}),
                            SheetInfo("pears", {=> AppLog.info("pears")})
                        ]
                        let confirm: Confirm = Confirm("Confirm button", {=> AppLog.info("Get Alert Dialog handled")},
                            defaultFocus: true, style: DialogButtonStyle.HIGHLIGHT)
                        ActionSheet.show(
                            ActionSheetOptions(
                                "ActionSheet title",
                                "message",
                                sheets,
                                subtitle: "ActionSheet subtitle",
                                autoCancel: true,
                                confirm: confirm,
                                width: 300,
                                height: 350,
                                cornerRadius: BorderRadiuses(topLeft: 20.vp, topRight: 20.vp, bottomLeft: 20.vp,
                                    bottomRight: 20.vp),
                                borderWidth: 1.vp,
                                borderStyle: EdgeStyle.SOLID,
                                borderColor: Color.WHITE,
                                cancel: {=> AppLog.info("actionSheet canceled")},
                                onWillDismiss: {
                                    action =>
                                    match (action.reason) {
                                        case PRESS_BACK => AppLog.info("PRESS_BACK")
                                        case TOUCH_OUTSIDE => AppLog.info("TOUCH_OUTSIDE")
                                        case CLOSE_BUTTON => AppLog.info("CLOSE_BUTTON")
                                        case SLIDE_DOWN => AppLog.info("SLIDE_DOWN")
                                        case _ => throw Exception()
                                    }
                                    action.dismiss()
                                },
                                alignment: DialogAlignment.Bottom,
                                offset: Offset(0, -10)
                            ),
                            ActionSheetShadowOptions(20.0, color: Color.GRAY, offsetX: 50.0, offsetY: 0.0)
                        )
                    }
                )
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

![actionsheet1](./figures/actionsheet1.gif)

### static func show(ActionSheetOptions, ShadowStyle)

```cangjie
public static func show(value: ActionSheetOptions, shadow: ShadowStyle): Unit
```

**功能：** 定义列表弹窗并弹出。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ActionSheetOptions](cj-dialog-actionsheet.md#class-actionsheetoptions)|是|-|配置列表选择弹窗的参数。|
|shadow|[ShadowStyle](./cj-common-types.md#enum-shadowstyle)|是|-|设置弹窗背板的阴影样式。|

### static func show(ActionSheetOptions)

```cangjie
public static func show(value: ActionSheetOptions): Unit
```

**功能：** 定义列表弹窗并弹出。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ActionSheetOptions](cj-dialog-actionsheet.md#class-actionsheetoptions)|是|-|配置列表选择弹窗的参数。|