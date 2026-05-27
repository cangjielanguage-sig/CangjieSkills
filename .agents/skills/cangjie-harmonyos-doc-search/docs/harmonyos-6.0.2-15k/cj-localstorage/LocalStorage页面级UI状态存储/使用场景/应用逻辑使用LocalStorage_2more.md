### 应用逻辑使用LocalStorage

```cangjie
let storage = LocalStorage()
let temp = storage.setOrCreate("PropA", 47) // 创建新实例并使用给定对象初始化
let propA = storage.get<Int64>("PropA") // propA == 47
let link1 = storage.link<Int64>("PropA").getOrThrow() // link1.get() == 47
let link2 = storage.link<Int64>("PropA").getOrThrow() // link2.get() == 47

let value1 = link1.set(48) // 双向同步: link1.get() == link2.get() == prop1.get() == 48
let value2 = link1.set(49) // 双向同步: link1.get() == link2.get() == prop.get() == 49
```

### 从UI内部使用LocalStorage

除了应用程序逻辑使用LocalStorage，还可以借助LocalStorage相关的两个宏@LocalStorageProp和@LocalStorageLink，在UI组件内部获取到LocalStorage实例中存储的状态变量。

本示例以@LocalStorageLink为例，展示了：

- 使用构造函数创建LocalStorage实例storage。
- 使用@Entry宏将storage添加到Parent顶层组件中。
- @LocalStorageLink绑定LocalStorage对给定的属性，建立双向数据同步。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

class Data {
    var code: Int64
    init(code: Int64) {
        this.code = code
    }
}
// 创建新实例并使用给定对象初始化
let storage = LocalStorage()
let res1 = storage.setOrCreate("PropA", 47)
let res2 = storage.setOrCreate("PropB", Data(50))

@Component
class Child {
    // @LocalStorageLink变量宏与LocalStorage中的"PropA"属性建立双向绑定
    @LocalStorageLink["PropA"]
    var childLinkNumber: Int64 = 1
    // @LocalStorageLink变量宏与LocalStorage中的"PropB"属性建立双向绑定
    @LocalStorageLink["PropB"]
    var childLinkObject: Data = Data(0)
    func build() {
        Column() {
            Button("Child from LocalStorage ${this.childLinkNumber}") // 更改将同步至LocalStorage中的"PropA"以及Parent.parentLinkNumber
                .onClick({evt => this.childLinkNumber += 1})
            Button("Child from LocalStorage ${this.childLinkObject.code}") // 更改将同步至LocalStorage中的"PropB"以及Parent.childLinkObject
                .onClick(
                {
                    evt =>
                    var temp = this.childLinkObject
                    temp.code += 1
                    this.childLinkObject = temp
                }
            )
        }
    }
}
// 使LocalStorage可从@Component组件访问
@Entry[storage]
@Component
class EntryView {
    // @LocalStorageLink变量宏与LocalStorage中的"PropA"属性建立双向绑定
    @LocalStorageLink["PropA"]
    var parentLinkNumber: Int64 = 1
    // @LocalStorageLink变量宏与LocalStorage中的"PropB"属性建立双向绑定
    @LocalStorageLink["PropB"]
    var parentLinkObject: Data = Data(0)
    func build() {
        Column() {
            Button("Parent from LocalStorage ${this.parentLinkNumber}") // 由于LocalStorage中PropA已经被初始化，因此this.parentLinkNumber的值为47
                .onClick({evt => this.parentLinkNumber += 1})
            Button("Parent from LocalStorage ${this.parentLinkObject.code}") // 由于LocalStorage中PropB已经被初始化，因此this.parentLinkObject.code的值为50
                .onClick(
                {
                    evt =>
                    var temp = this.parentLinkObject
                    temp.code += 1
                    this.parentLinkObject = temp
                }
            )
            // @Component子组件自动获得对Parent LocalStorage实例的访问权限。
            Child()
        }
    }
}
```