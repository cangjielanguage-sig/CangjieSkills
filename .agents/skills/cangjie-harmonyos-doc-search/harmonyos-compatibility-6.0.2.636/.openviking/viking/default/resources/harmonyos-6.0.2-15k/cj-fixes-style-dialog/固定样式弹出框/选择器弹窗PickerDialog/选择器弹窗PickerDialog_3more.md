## 选择器弹窗（PickerDialog）

选择器弹窗通常用于在用户进行某些操作（如点击按钮）时显示特定的信息或选项。

### 生命周期

弹窗提供了生命周期函数用于通知用户该弹窗的生命周期。
生命周期的触发顺序可看各组件API参考。

| 名称            |类型| 说明                       |
| :----------------- | :------ | :---------------------------- |
| onDidAppear    | () -> Unit  | 弹窗弹出时的事件回调。  |
| onDidDisappear |() -> Unit  | 弹窗消失时的事件回调。  |
| onWillAppear    | () -> Unit | 弹窗显示动效前的事件回调。 |
| onWillDisappear | () -> Unit | 弹窗退出动效前的事件回调。 |

### 日历选择器弹窗（CalendarPickerDialog）

日历选择器弹窗提供日历视图，包含年、月和星期信息，通过[CalendarPickerDialog](../../API_Reference/source_zh_cn/arkui-cj/cj-dialog-calendarpickerdaialog.md#class-calendarpickerdialog)接口实现。开发者可调用show函数，定义并弹出日历选择器弹窗。

通过配置 acceptButtonStyle、cancelButtonStyle可以实现自定义按钮样式。

<!-- run -->

```cangjie
// xxx.cj
package ohos_app_cangjie_entry

import ohos.base.*
import ohos.component.*
import ohos.state_manage.*
import ohos.state_macro_manage.*
import std.collection.*
import std.time.DateTime
import ohos.hilog.Hilog

@Entry
@Component
class EntryView {
    @State
    var selectedDate: DateTime = DateTime.now()
    func build() {
        Row {
            Column {
                Button("Show CalendarPicker Dialog").onClick {
                    Hilog.info(0, "test", "CalendarDialog.show")
                    let acceptButtonStyle = PickerDialogButtonStyle(
                        fontColor: Color.BLUE,
                        fontSize: 16.fp,
                        fontStyle: FontStyle.Normal,
                        fontFamily: "sans-serif",
                        backgroundColor: Color.WHITE,
                        borderRadius: BorderRadiuses(topLeft: 10, topRight: 10, bottomLeft: 10, bottomRight: 10)
                    )

                    let cancelButtonStyle = PickerDialogButtonStyle(
                        fontColor: Color.RED,
                        fontSize: 16.fp,
                        fontStyle: FontStyle.Normal,
                        fontFamily: "sans-serif",
                        backgroundColor: Color.WHITE,
                        borderRadius: BorderRadiuses(topLeft: 10, topRight: 10, bottomLeft: 10, bottomRight: 10)
                    )
                    CalendarPickerDialog.show(
                        options: CalendarDialogOptions(
                            selected: selectedDate,
                            acceptButtonStyle: acceptButtonStyle,
                            cancelButtonStyle: cancelButtonStyle,
                            onAccept: {
                                value => Hilog.info(0, "test",
                                    "calendar onAccept: ${value.year}-${value.monthValue}-${value.dayOfMonth}")
                            },
                            onCancel: {=> Hilog.info(0, "test", "calendar onCancel")},
                            onChange: {
                                value => Hilog.info(0, "test",
                                    "calendar onChange: ${value.year}-${value.monthValue}-${value.dayOfMonth}")
                            },
                            onDidAppear: {=> Hilog.info(0, "test", "calendar onDidAppear")},
                            onDidDisappear: {=> Hilog.info(0, "test", "calendar onDidDisappear")},
                            onWillAppear: {=> Hilog.info(0, "test", "calendar onWillAppear")},
                            onWillDisappear: {=> Hilog.info(0, "test", "calendar onWillDisappear")},
                            shadow: ShadowOptions(radius: 20.0, color: Color.GRAY, offsetX: 50.0, offsetY: 10.0)
                        )
                    )
                }
            }.width(100.percent).padding(top: 5)
        }
    }
}
```

![image](figures/UIContextShowCalendarpickerDialog.gif)