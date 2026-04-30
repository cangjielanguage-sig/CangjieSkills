### 装饰Set类型变量

在下面的示例中，message类型为HashSet\<Int64>，点击Button改变message的值，视图会随之刷新。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.*

@Component
class Child {
    @Consume
    var message: HashSet<Int64>

    @Consume
    var arr: Array<Int64>

    func build() {
        Column {
            ForEach(
                arr,
                {
                    item: Int64, idx: Int64 =>
                    Text("${item}").fontSize(30)
                    Divider()
                }
            )
            Button("Consume init set").onClick {
                =>
                this.message = HashSet<Int64>([0, 1, 2, 3, 4])
                this.arr = this.message.toArray()
            }
            Button("Consume set new one").onClick {
                =>
                this.message.add(5)
                this.arr = this.message.toArray()
            }
            Button("Consume clear").onClick {
                =>
                this.message.clear()
                this.arr = this.message.toArray()
            }
            Button("Consume delete the first one").onClick {
                =>
                this.message.remove(0)
                this.arr = this.message.toArray()
            }
        }
    }
}

@Entry
@Component
class EntryView {
    public override func onPageShow() {
        arr = message.toArray()
    }

    @Provide
    var message: HashSet<Int64> = HashSet([0, 1, 2, 3, 4])

    @Provide
    var arr: Array<Int64> = []

    func build() {
        Row() {
            Column() {
                Button("Provide init Set").onClick {
                    =>
                    this.message = HashSet<Int64>([0, 1, 2, 3, 4, 5])
                    this.arr = this.message.toArray()
                }
                Child()
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

![img5](figures/provide_5_set.gif)