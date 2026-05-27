## 使用场景

在下面的示例是与后代组件双向同步状态 \@Provide 和 \@Consume 场景。当分别点击EntryView和ToDoItem组件内Button时，count的更改会双向同步在EntryView和ToDoItem中。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Component
class ToDoItem {

    // @Consume装饰的变量通过相同的属性名绑定其祖先组件EntryView内的@Provide装饰的变量
    @Consume
    var count: Int64

    func build() {
        Column {
            Text("count(${this.count})")
            Button("count(${this.count}), count + 1").onClick {
                => this.count += 1
            }
        }.width(100.percent)
    }
}

@Component
class ToDoList {
    func build() {
        Row(5) {
            ToDoItem()
            ToDoItem()
        }
    }
}

@Component
class ToDoDemo {
    func build() {
        Column {
            ToDoList()
        }
    }
}

@Entry
@Component
class EntryView {
    // @Provide装饰的变量index由入口组件EntryView提供其后代组件
    @Provide
    var count: Int64 = 0;

    func build() {
        Column {
            Button("count(${this.count}), count + 1").onClick {
                => this.count += 1
            }
            ToDoDemo()
        }
    }
}
```

![img3](figures/provide_3_binding.gif)

### 装饰Map类型变量

在下面的示例中，message类型为HashMap\<Int64, String>，点击Button改变message的值，视图会随之刷新。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.HashMap

@Component
class Child {
    @Consume
    var message: HashMap<Int64, String> = HashMap<Int64, String>()

    @Consume
    var arr: Array<(Int64, String)>

    func build() {
        Column() {
            ForEach(
                arr,
                {
                    item: (Int64, String), idx: Int64 =>
                    Text("key: ${item[0]} value: ${item[1]}").fontSize(30)
                    Divider()
                },
                keyGeneratorFunc: {
                    item: (Int64, String), idx: Int64 => "${idx}_${item[0]}" + item[1]
                }
            )
            Button("Consume init map").onClick {
                =>
                this.message = HashMap<Int64, String>([(0, "a"), (1, "b"), (3, "c")])
                arr = message.toArray()
            }
            Button("Consume set new one").onClick {
                =>
                this.message.add(4, "d")
                arr = message.toArray()
            }
            Button("Consume clear").onClick {
                =>
                this.message.clear()
                arr = message.toArray()
            }
            Button("Consume replace the first item").onClick {
                =>
                this.message.add(0, "aa")
                arr = message.toArray()
            }
            Button("Consume delete the first item").onClick {
                =>
                this.message.remove(0)
                arr = message.toArray()
            }
        }
    }
}

@Entry
@Component
class EntryView {
    @Provide
    var message: HashMap<Int64, String> = HashMap<Int64, String>([(0, "a"), (1, "b"), (3, "c")])

    @Provide
    var arr: Array<(Int64, String)> = []

    public override func onPageShow() {
        arr = message.toArray()
    }

    func build() {
        Row() {
            Column() {
                Button("Provide init map").onClick {
                    =>
                    this.message = HashMap<Int64, String>([(0, "a"), (1, "b"), (3, "c"), (4, "d")])
                    arr = message.toArray()
                }
                Child()
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

![img4](figures/provide_4_map.gif)