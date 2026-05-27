## 列表选择弹窗（ActionSheet）

列表选择器弹窗适用于呈现多个操作选项，尤其当界面中仅需展示操作列表而无其他内容时。

列表选择器弹窗通过ActionSheet中的[show](../../API_Reference/source_zh_cn/arkui-cj/cj-dialog-actionsheet.md#static-func-showactionsheetoptions)接口实现。

该示例通过配置width、height、transition等接口定义了弹窗的样式以及弹出动效。

<!-- run -->

```cangjie
// xxx.cj
package ohos_app_cangjie_entry

import ohos.base.*
import ohos.component.*
import ohos.state_manage.*
import ohos.state_macro_manage.*
import std.collection.*

@Entry
@Component
class EntryView {
    func build() {
        Column() {
            Button('showActionSheet').onClick {
                let confirm: Confirm = Confirm("Confirm button", {=> AppLog.info("Get Alert Dialog handled")},
                    defaultFocus: true, style: DialogButtonStyle.DEFAULT)
                let sheets: Array<SheetInfo> = [
                    SheetInfo("apple", {=> AppLog.info("apple")}),
                    SheetInfo("banana", {=> AppLog.info("banana")}),
                    SheetInfo("pears", {=> AppLog.info("pears")})
                ]
                ActionSheet.show(
                    ActionSheetOptions(
                        'ActionSheet title',
                        'message',
                        sheets,
                        autoCancel: false,
                        confirm: confirm,
                        width: 300,
                        height: 300,
                        cornerRadius: BorderRadiuses(topLeft: 20.vp, topRight: 20.vp, bottomLeft: 20.vp,
                            bottomRight: 20.vp),
                        borderWidth: 1.vp,
                        borderStyle: EdgeStyle.SOILD,
                        borderColor: Color.BLUE,
                        backgroundColor: Color.WHITE,
                        transition: TransitionEffect.asymmetric(
                            TransitionEffect.OPACITY.animation(AnimateParam(duration: 3000, curve: Curve.Sharp)).combine(
                                TransitionEffect.scale(ScaleOptions(x: 1.5, y: 1.5)).animation(
                                AnimateParam(duration: 3000, curve: Curve.Sharp))),
                            TransitionEffect.OPACITY.animation(AnimateParam(duration: 100, curve: Curve.Smooth)).combine(
                                TransitionEffect.scale(ScaleOptions(x: 0.5, y: 0.5)).animation(
                                AnimateParam(duration: 100, curve: Curve.Smooth)))
                        ),
                        alignment: DialogAlignment.Center,
                    )
                )
            }
        }.width(100.percent).margin(top: 5)
    }
}
```

![image](figures/UIContextShowactionSheet.gif)