## 列表选择弹窗（ActionSheet）

列表选择器弹窗适用于呈现多个操作选项，尤其当界面中仅需展示操作列表而无其他内容时。

列表选择器弹窗通过[UIContext](../reference/arkui-cj/cj-apis-uicontext-uicontext.md#class-uicontext)的[showActionSheet](../reference/arkui-cj/cj-apis-uicontext-uicontext.md#func-showactionsheetactionsheetoptions)接口实现。

该示例通过配置width、height、transition等接口定义了弹窗的样式以及弹出动效。

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
            Button('showActionSheet').onClick({ e =>
                let confirm: ActionSheetButtonOptions = ActionSheetButtonOptions(value: "Confirm button", action: {=> Hilog.info(0, "cangjie", "Get Alert Dialog handled")},
                    defaultFocus: true, style: DialogButtonStyle.Default)
                let sheets: Array<SheetInfo> = [
                    SheetInfo(title: "apple", action: {=> Hilog.info(0, "cangjie", "apple")}),
                    SheetInfo(title: "banana", action: {=> Hilog.info(0, "cangjie", "banana")}),
                    SheetInfo(title: "pears", action: {=> Hilog.info(0, "cangjie", "pears")})]
                getUIContext().showActionSheet(
                    ActionSheetOptions(
                        title: 'ActionSheet title',
                        message: 'message',
                        sheets: sheets,
                        autoCancel: false,
                        confirm: confirm,
                        width: 300,
                        height: 300,
                        cornerRadius: BorderRadiuses(topLeft: 20.vp, topRight: 20.vp, bottomLeft: 20.vp,
                            bottomRight: 20.vp),
                        borderWidth: 1.vp,
                        borderStyle: EdgeStyles(),
                        borderColor: Color.Blue,
                        backgroundColor: Color.White,
                        transition: TransitionEffect.asymmetric(
                            TransitionEffect
                                .OPACITY
                                .animation(AnimateParam(duration: 3000, curve: Curve.Sharp))
                                .combine(
                                    TransitionEffect
                                        .scale(ScaleOptions(x: 1.5, y: 1.5))
                                        .animation(AnimateParam(duration: 3000, curve: Curve.Sharp))),
                            TransitionEffect
                                .OPACITY
                                .animation(AnimateParam(duration: 100, curve: Curve.Smooth))
                                .combine(
                                    TransitionEffect
                                        .scale(ScaleOptions(x: 0.5, y: 0.5))
                                        .animation(AnimateParam(duration: 100, curve: Curve.Smooth)))
                        ),
                        alignment: DialogAlignment.Center,
                    )
                )
            })
        }.width(100.percent).margin(top: 5)
    }
}
```

![image](figures/UIContextShowactionSheet.gif)