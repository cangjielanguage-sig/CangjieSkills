### @LocalStorageProp和LocalStorage单向同步的简单场景

下面的示例展示@LocalStorageProp装饰的数据和LocalStorage单向同步的场景：

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

// 创建新实例并使用给定对象初始化
let storage = LocalStorage()
let temp = storage.setOrCreate("PropA", 47)
// 使LocalStorage可从@Component组件访问
@Entry[storage]
@Component
class EntryView {
    // @LocalStorageProp变量宏与LocalStorage中的"PropA"属性建立单向绑定
    @LocalStorageProp["PropA"]
    let storageProp1: Int64 = 1
    func build() {
        Column() {
            Button("Parent from LocalStorage ${this.storageProp1}").onClick(
                {
                evt => storage.set<Int64>("PropA", storageProp1 + 1);
            })
        }
    }
}
```

### @LocalStorageLink和LocalStorage双向同步的简单场景

下面的示例展示了@LocalStorageLink装饰的数据和LocalStorage双向同步的场景：

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

// 构造LocalStorage实例
let storage = LocalStorage()
let temp = storage.setOrCreate("PropA", 47)
// 调用link接口构造"PropA"的双向同步数据，linkToPropA 是全局变量
let linkToPropA = storage.link<Int64>("PropA").getOrThrow()

// 使LocalStorage可从@Component组件访问
@Entry[storage]
@Component
class EntryView {
    // @LocalStorageLink("PropA")在Parent自定义组件中创建"PropA"的双向同步数据，初始值为47，因为在构造LocalStorage已经给“PropA”设置47
    @LocalStorageLink["PropA"]
    var storageLink: Int64 = 1
    func build() {
        Column() {
            Text("incr @LocalStorageLink variable")
                // 单击“incr @LocalStorageLink variable”，this.storageLink加1，改变同步回storage，全局变量linkToPropA也会同步改变
                .onClick({evt => this.storageLink += 1})
            // 并不建议在组件内使用全局变量linkToPropA.get()，因为可能会有生命周期不同引起的错误。
            Text("@LocalStorageLink: ${this.storageLink} - linkToPropA: ${linkToPropA.get()}")
        }
    }
}
```

### 兄弟组件之间同步状态变量

下面的示例展示了通过@LocalStorageLink双向同步兄弟组件之间的状态。

先看Parent自定义组件中发生的变化：

1. 单击“playCount ${this.playCount} dec by 1”，this.playCount减1，修改同步回LocalStorage中，Child组件中的playCountLink绑定的组件会同步刷新。
2. 单击“countStorage ${this.playCount} incr by 1”，调用LocalStorage的set接口，更新LocalStorage中“countStorage”对应的属性，Child组件中的playCountLink绑定的组件会同步刷新。

Child自定义组件中的变化：

playCountLink的刷新会同步回LocalStorage，并且引起兄弟组件和父组件相应的刷新。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

let storage = LocalStorage()
let temp = storage.setOrCreate("countStorage", 1)

@Component
class Child {
    let label: String
    @LocalStorageLink["countStorage"]
    var playCountLink: Int64 = 0
    func build() {
        Row() {
            Text(this.label).width(50).height(60).fontSize(12)
            Text("playCountLink ${this.playCountLink}: inc by 1").onClick({evt => this.playCountLink += 1}).width(200).
                height(60).fontSize(12)
        }.width(300).height(60)
    }
}

@Entry[storage]
@Component
class EntryView {
    @LocalStorageLink["countStorage"]
    var playCount: Int64 = 0
    func build() {
        Column() {
            Row() {
                Text("Parent").width(50).height(60).fontSize(12)
                Text("countStorage ${this.playCount} dec by 1").onClick({evt => this.playCount -= 1}).width(250).height(
                    60).fontSize(12)
            }.width(300).height(60)
            Child(label: "ChildA")
            Child(label: "ChildB")
        }
    }
}
```