### 装饰DateTime类型变量

在下面的示例中，@LocalStorageLink装饰的selectedDate类型为DateTime，单击Button改变selectedDate的值，视图会随之刷新。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.time.*

let Storage = LocalStorage()

@Entry[Storage]
@Component
class EntryView {
    @LocalStorageLink["date"]
    var selectedDate: DateTime = DateTime.of(year: 2003, month: Month.of(6), dayOfMonth: 24)
    @State
    var count: Int64 = 0
    func build() {
        Column() {
            Button("set selectedDate to 2025-04-21").margin(10).onClick(
                {evt => this.selectedDate = DateTime.of(year: 2025, month: Month.of(4), dayOfMonth: 21)})
            Button("increase the year by 1").margin(10).onClick(
                {evt => this.selectedDate = this.selectedDate.addYears(1)})
            Button("increase the month by 1").margin(10).onClick(
                {evt => this.selectedDate = this.selectedDate.addMonths(1)})
            Button("increase the day by 1").margin(10).onClick(
                {evt => this.selectedDate = this.selectedDate.addDays(1)})
            DatePicker(
                start: DateTime.of(year: 1970, month: Month.of(1), dayOfMonth: 1),
                end: DateTime.of(year: 2100, month: Month.of(1), dayOfMonth: 1),
                selected: @Binder(this.selectedDate)
            )
        }.width(100.percent)
    }
}
```

### 装饰Map类型变量

在下面的示例中，@LocalStorageLink装饰的message类型为Map\<Int64, string>，单击Button改变message的值，视图会随之刷新。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.Map
import std.collection.HashMap

@Entry
@Component
class EntryView {
    @LocalStorageLink["map"]
    var message: Map<Int64, String> = HashMap<Int64, String>([(0, "a"), (1, "b"), (3, "c")])
    func build() {
        Row() {
            Column() {
                ForEach(
                    this.message.toArray(),
                    itemGeneratorFunc: {
                        item: (Int64, String), _: Int64 =>
                        Text("${item[0]}").fontSize(30)
                        Text("${item[1]}").fontSize(30)
                        Divider()
                    }
                )
                Button("init map").onClick({
                    evt => this.message = HashMap<Int64, String>([(0, "a"), (1, "b"), (3, "c")])
                })
                Button("add new one").onClick(
                    {
                        evt =>
                        var temp = this.message
                        temp.add(4, "d")
                        this.message = temp
                    }
                )
                Button("clear").onClick(
                    {
                        evt =>
                        var temp = this.message
                        temp.clear()
                        this.message = temp
                    }
                )
                Button("replace the first one").onClick(
                    {
                        evt =>
                        var temp = this.message
                        temp.replace(0, "aa")
                        this.message = temp
                    }
                )
                Button("remove the first one").onClick(
                    {
                        evt =>
                        var temp = this.message
                        temp.remove(0)
                        this.message = temp
                    }
                )
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

### 装饰Set类型变量

在下面的示例中，@LocalStorageLink装饰的memberSet类型为Set\<Int64>，单击Button改变memberSet的值，视图会随之刷新。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.HashSet
import std.collection.Set

@Entry
@Component
class EntryView {
    @LocalStorageLink["set"]
    var message: Set<Int64> = HashSet<Int64>([0, 1, 2, 3, 4])
    func build() {
        Row() {
            Column() {
                ForEach(
                    this.message.toArray(),
                    itemGeneratorFunc: {
                        item: Int64, _: Int64 => Text("${item}").fontSize(30)
                    }
                )
                Button("init set").onClick(
                    {
                        evt =>
                        var temp = this.message
                        temp = HashSet<Int64>([0, 1, 2, 3, 4])
                        this.message = temp
                    }
                )
                Button("add new one").onClick(
                    {
                        evt =>
                        var temp = this.message
                        temp.add(5)
                        this.message = temp
                    }
                )
                Button("clear").onClick(
                    {
                        evt =>
                        var temp = this.message
                        temp.clear()
                        this.message = temp
                    }
                )
                Button("remove the first one").onClick(
                    {
                        evt =>
                        var temp = this.message
                        temp.remove(0)
                        this.message = temp
                    }
                )
            }.width(100.percent)
        }.height(100.percent)
    }
}
```