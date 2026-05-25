### 日期滑动选择器弹窗（DatePickerDialog）

开发者可以根据指定的日期范围，创建日期滑动选择器弹窗，将日期信息清晰地展示在弹出的窗口上。

弹窗中配置lunarSwitch、showTime为true时，展示切换农历的开关以及时间，当checkbox被选中时，显示农历。当按下确定按钮时，弹窗会通过onDateAccept返回目前所选中的日期。如需弹窗再次弹出时显示选中的是上一次确定的日期，就要在回调中重新给selectTime进行赋值。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.time.*
import ohos.hilog.*

@Entry
@Component
class EntryView {
    @State
    var selectedDate: DateTime = DateTime.of(year: 2023, month: Month.of(1), dayOfMonth: 1)
    func build() {
        Column {
            Button("DatePickerDialog").margin(20).onClick {
                Hilog.info(0, "test", "DatePickerDialog.show")
                DatePickerDialog.show(
                    options: DatePickerDialogOptions(
                        start: DateTime.of(year: 2000, month: Month.of(1), dayOfMonth: 1),
                        end: DateTime.of(year: 2100, month: Month.of(12), dayOfMonth: 31),
                        selected: this.selectedDate,
                        showTime: true,
                        lunarSwitch: true,
                        useMilitaryTime: false,
                        disappearTextStyle: PickerTextStyle(Color.PINK, MyFont(size: 22.fp, weight: FontWeight.Bold)),
                        textStyle: PickerTextStyle(0xff00ff00, MyFont(size: 18.fp, weight: FontWeight.Normal)),
                        selectedTextStyle: PickerTextStyle(0xff182431, MyFont(size: 14.fp, weight: FontWeight.Regular)),
                        onDateAccept: {
                            value => Hilog.info(0, "test",
                                "DatePickerDialog:onDateAccept(): ${value.year}-${value.monthValue}-${value.dayOfMonth}"
                            )
                        },
                        onCancel: {=> Hilog.info(0, "test", "DatePickerDialog:onCancel()")},
                        onDateChange: {
                            value => Hilog.info(0, "test",
                                "DatePickerDialog:onDateChange(): ${value.year}-${value.monthValue}-${value.dayOfMonth}"
                            )
                        },
                        onDidAppear: {=> Hilog.info(0, "test", "DatePickerDialog:onDidAppear()")},
                        onDidDisappear: {=> Hilog.info(0, "test", "DatePickerDialog:onDidDisappear()")},
                        onWillAppear: {=> Hilog.info(0, "test", "DatePickerDialog:onWillAppear()")},
                        onWillDisappear: {=> Hilog.info(0, "test", "DatePickerDialog:onWillDisappear()")}
                    )
                )
            }
        }.width(100.percent)
    }
}
```

![datapickerdialog](./figures/datapickerdialog.gif)