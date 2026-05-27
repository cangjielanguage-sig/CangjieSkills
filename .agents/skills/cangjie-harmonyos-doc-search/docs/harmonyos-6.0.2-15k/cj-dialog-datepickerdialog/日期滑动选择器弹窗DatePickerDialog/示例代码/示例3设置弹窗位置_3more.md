### 示例3（设置弹窗位置）

该示例通过alignment、offset设置弹窗的位置。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.time.*

@Entry
@Component
class EntryView {
    @State
    var selectedDate: DateTime = DateTime.of(year: 2010, month: Month.of(1), dayOfMonth: 1)

    func build() {
        Column {
            Button("DatePickerDialog").margin(20).onClick {
                DatePickerDialog.show(
                    options: DatePickerDialogOptions(
                        start: DateTime.of(year: 2000, month: Month.of(1), dayOfMonth: 1),
                        end: DateTime.of(year: 2100, month: Month.of(12), dayOfMonth: 31),
                        selected: this.selectedDate,
                        alignment: DialogAlignment.Center,
                        offset: Offset(20, 0),
                        onDateAccept: {
                            value =>
                            this.selectedDate = value
                            AppLog.info(
                                "DatePickerDialog:onDateAccept(): ${value.year}-${value.monthValue}-${value.dayOfMonth}"
                            )
                        }
                    )
                )
            }
        }.width(100.percent)
    }
}
```

![datepickerdialog3](./figures/datepickerdialog3.png)

### 示例4（设置遮蔽区）

该示例通过maskRect设置遮蔽区。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.time.*

@Entry
@Component
class EntryView {
    @State
    var selectedDate: DateTime = DateTime.of(year: 2010, month: Month.of(1), dayOfMonth: 1)

    func build() {
        Column {
            Button("DatePickerDialog").margin(20).onClick {
                DatePickerDialog.show(
                    options: DatePickerDialogOptions(
                        start: DateTime.of(year: 2000, month: Month.of(1), dayOfMonth: 1),
                        end: DateTime.of(year: 2100, month: Month.of(12), dayOfMonth: 31),
                        selected: this.selectedDate,
                        maskRect: Rectangle(x: 30, y: 60, width: 100.percent, height: 60.percent),
                        onDateAccept: {
                            value =>
                            this.selectedDate = value
                            AppLog.info(
                                "DatePickerDialog:onDateAccept(): ${value.year}-${value.monthValue}-${value.dayOfMonth}"
                            )
                        }
                    )
                )
            }
        }.width(100.percent)
    }
}
```

![datepickerdialog4](./figures/datepickerdialog4.png)

### 示例5（设置弹窗背板）

该示例通过backgroundColor、backgroundBlurStyle、shadow设置弹窗背板。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.time.*

@Entry
@Component
class EntryView {
    @State
    var selectedDate: DateTime = DateTime.of(year: 2010, month: Month.of(1), dayOfMonth: 1)

    func build() {
        Column {
            Button("DatePickerDialog").margin(20).onClick {
                DatePickerDialog.show(
                    options: DatePickerDialogOptions(
                        start: DateTime.of(year: 2000, month: Month.of(1), dayOfMonth: 1),
                        end: DateTime.of(year: 2100, month: Month.of(12), dayOfMonth: 31),
                        selected: this.selectedDate,
                        backgroundColor: 0xFFCCE2FB,
                        backgroundBlurStyle: BlurStyle.NONE,
                        shadow: ShadowOptions(radius: 20.0, shadowType: ShadowType.COLOR, color: 0xFF888C8C),
                        disappearTextStyle: PickerTextStyle(Color.PINK, MyFont(size: 22.fp, weight: FontWeight.Bold)),
                        onDateAccept: {
                            value =>
                            this.selectedDate = value
                            AppLog.info(
                                "DatePickerDialog:onDateAccept(): ${value.year}-${value.monthValue}-${value.dayOfMonth}"
                            )
                        }
                    )
                )
            }
        }.width(100.percent)
    }
}
```

![datepickerdialog5](./figures/datepickerdialog5.png)