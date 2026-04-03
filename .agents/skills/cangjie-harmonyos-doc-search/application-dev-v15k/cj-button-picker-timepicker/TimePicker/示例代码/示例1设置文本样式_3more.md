### 示例1（设置文本样式）

该示例通过配置disappearTextStyle、textStyle和selectedTextStyle实现文本选择器中的文本样式。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.time.*
import ohos.hilog.Hilog

@Entry
@Component
class EntryView {
    @State
    var selectedTime: DateTime = DateTime.of(year: 2022, month: Month.of(7), dayOfMonth: 22, hour: 8)
    var font1: MyFont = MyFont(size: 24, weight: FontWeight.Lighter)
    var font2: MyFont = MyFont(size: 26, weight: FontWeight.Normal)
    var font3: MyFont = MyFont(size: 30, weight: FontWeight.Bolder)
    var disappear: PickerTextStyle = PickerTextStyle(0x000004af, font1)
    var textstyle: PickerTextStyle = PickerTextStyle(Color.BLACK, font2)
    var selected: PickerTextStyle = PickerTextStyle(Color.BLUE, font3)
    func build() {
        Column() {
            TimePicker(selected: this.selectedTime).disappearTextStyle(this.disappear).selectedTextStyle(this.selected).
                textStyle(this.textstyle).onChange(
                {
                value => if (value.hour >= 0) {
                    this.selectedTime = DateTime.of(year: 2022, month: Month.of(7), dayOfMonth: 22, hour: 8,
                        minute: value.hour, second: value.minute)
                    Hilog.info(0, "test", "select current date is: ${value.minute}")
                }
            })
        }
    }
}
```

![picker1](./figures/timepicker1.png)

### 示例2（切换小时制）

该示例通过配置useMilitaryTime实现12小时制、24小时制的切换。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.time.*
import ohos.hilog.Hilog

@Entry
@Component
class EntryView {
    @State
    var isMilitaryTime: Bool = false
    @State
    var selectedTime: DateTime = DateTime.of(year: 2022, month: Month.of(7), dayOfMonth: 22, hour: 8)
    func build() {
        Column() {
            Button("切换12小时制/24小时制").margin(30).onClick {
                evt => if (this.isMilitaryTime) {
                    this.isMilitaryTime = false
                } else {
                    this.isMilitaryTime = true
                }
            }

            TimePicker(selected: this.selectedTime, format: TimePickerFormat.HourMinuteSecond).useMilitaryTime(
                this.isMilitaryTime).onChange(
                {
                value => if (value.hour >= 0) {
                    this.selectedTime = DateTime.of(year: 2022, month: Month.of(7), dayOfMonth: 22, hour: value.hour,
                        minute: value.minute)
                    Hilog.info(0, "test", "select current date is: ${value.minute}")
                }
            })
        }
    }
}
```

![picker2](./figures/timepicker2.gif)

### 示例3（设置时间格式）

该示例使用format和dateTimeOptions设置TimePicker时间格式。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.time.*
import ohos.hilog.Hilog

@Entry
@Component
class EntryView {
    @State
    var isMilitaryTime: Bool = false
    @State
    var selectedTime: DateTime = DateTime.of(year: 2022, month: Month.of(7), dayOfMonth: 22, hour: 8)
    func build() {
        Column() {
            Button("切换12小时制/24小时制").margin(30).onClick {
                evt => if (this.isMilitaryTime) {
                    this.isMilitaryTime = false
                } else {
                    this.isMilitaryTime = true
                }
            }

            TimePicker(selected: this.selectedTime).useMilitaryTime(this.isMilitaryTime).onChange(
                {
                value => if (value.hour >= 0) {
                    this.selectedTime = DateTime.of(year: 2022, month: Month.of(7), dayOfMonth: 22, hour: value.hour,
                        minute: value.minute)
                    Hilog.info(0, "test", "select current date is: ${value.minute}")
                }
            })
        }
    }
}
```

![timepicker3](./figures/timepicker3.gif)