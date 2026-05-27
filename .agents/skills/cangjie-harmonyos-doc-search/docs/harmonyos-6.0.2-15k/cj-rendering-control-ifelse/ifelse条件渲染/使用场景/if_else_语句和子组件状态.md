### if ... else ...语句和子组件状态

以下示例包含if ... else ...语句与拥有@State装饰变量的子组件。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
internal import ohos.base.*
internal import ohos.component.*

@Component
public class CounterView {
    @State
    var counter: Int64 = 0;
    var label: String = 'unknown';
    func build() {
        Column(20) {
            Text("${this.label}")
            Button("counter ${this.counter} +1").onClick({
                => this.counter += 1
            })
        }.margin(10).padding(10).border(width: 1)
    }
}

@Entry
@Component
public class EntryView {
    @State
    var toggle: Bool = true;
    func build() {
        Column() {
            if (this.toggle) {
                CounterView(label: "CounterView #positive")
            } else {
                CounterView(label: "CounterView #negative")
            }
            Button("toggle ${this.toggle}").onClick({
                => this.toggle = !this.toggle
            })
        }.width(100.percent).justifyContent(FlexAlign.Center)
    }
}
```

CounterView（label为 'CounterView #positive'）子组件在初次渲染时创建。此子组件携带名为counter的状态变量。当修改CounterView.counter状态变量时，CounterView（label为 'CounterView #positive'）子组件重新渲染并保留状态变量值。当MainView.toggle状态变量的值更改为false时，MainView父组件内的if语句将更新，随后将删除CounterView（label为 'CounterView #positive'）子组件。与此同时，将创建新的CounterView（label为 'CounterView #negative'）实例。而它自己的counter状态变量设置为初始值0。

> **说明：**
>
> CounterView（label为 'CounterView #positive'）和CounterView（label为 'CounterView #negative'）是同一自定义组件的两个不同实例。if分支的更改，不会更新现有子组件，也不会保留状态。

以下示例展示了条件更改时，若需要保留counter值所做的修改。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
internal import ohos.base.*
internal import ohos.component.*

@Component
class CounterView {
    @Link
    var counter: Int64
    var label: String = 'unknown';

    func build() {
        Column(20) {
            Text("${this.label}").fontSize(20)
            Button("counter ${this.counter} +1").onClick({
                => this.counter += 1
            })
        }.margin(10).padding(10).border(width: 1)
    }
}

@Entry
@Component
public class EntryView {
    @State
    var toggle: Bool = true;
    @State
    var counter: Int64 = 0;
    func build() {
        Column() {
            if (this.toggle) {
                CounterView(counter: counter, label: 'CounterView #positive')
            } else {
                CounterView(counter: counter, label: 'CounterView #negative')
            }
            Button("toggle ${this.toggle}").onClick({
                => this.toggle = !this.toggle
            })
        }.width(100.percent).justifyContent(FlexAlign.Center)
    }
}
```

此处，@State counter变量归父组件所有。因此，当CounterView组件实例被删除时，该变量不会被销毁。CounterView组件通过@Link装饰器引用状态。状态必须从子级移动到其父级（或父级的父级），以避免在条件内容或重复内容被销毁时丢失状态。