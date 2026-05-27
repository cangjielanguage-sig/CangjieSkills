### 从应用逻辑使用AppStorage和LocalStorage

AppStorage是单例，它的所有API都是静态的，使用方法类似于LocalStorage中对应的非静态方法。

```cangjie
let temp1 = AppStorage.setOrCreate<Int64>("PropA", 47)
let storage = LocalStorage()
let temp2 = storage.setOrCreate("PropA", 17)
let propA = AppStorage.get<Int64>("PropA") // propA in AppStorage == 47, propA in LocalStorage == 17
let link1 = AppStorage.link<Int64>("PropA").getOrThrow() // link1.get() == 47
let link2 = AppStorage.link<Int64>("PropA").getOrThrow() // link2.get() == 47

let value1 = link1.set(48) // 双向同步: link1.get() == link2.get() == prop.get() == 48
let value2 = link1.set(49) // 双向同步: link1.get() == link2.get() == prop.get() == 49

let value3 = storage.get<Int64>("PropA") // == 17
let value4 = storage.set<Int64>("PropA", 101)
let value5 = storage.get<Int64>("PropA") // == 101

let value6 = AppStorage.get<Int64>("PropA") // == 49
let value7 = link1.get() // == 49
let value8 = link2.get() // == 49
```

### 从UI内部使用AppStorage和LocalStorage

@StorageLink变量宏与AppStorage配合使用，正如@LocalStorageLink与LocalStorage配合使用一样。此宏使用AppStorage中的属性创建双向数据同步。

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

let temp1 = AppStorage.setOrCreate("PropA", 47)
let temp2 = AppStorage.setOrCreate("PropB", Data(50))
let storage = LocalStorage()
let res1 = storage.setOrCreate("LinkA", 47)
let res2 = storage.setOrCreate("LinkB", Data(50))

@Entry[storage]
@Component
class EntryView {
    @StorageLink["PropA"]
    var storageLink: Int64 = 1
    @LocalStorageLink["LinkA"]
    var localStorageLink: Int64 = 1
    @StorageLink["PropB"]
    var storageLinkObject: Data = Data(1)
    @LocalStorageLink["LinkB"]
    var localStorageLinkObject: Data = Data(1)

    func build() {
        Column() {
            Text("From AppStorage ${this.storageLink}").onClick({evt => this.storageLink += 1})
            Text("From LocalStorage ${this.localStorageLink}").onClick({evt => this.localStorageLink += 1})
            Text("From AppStorage ${this.storageLinkObject.code}").onClick(
                {
                    evt =>
                    var temp = this.storageLinkObject
                    temp.code += 1
                    this.storageLinkObject = temp
                }
            )
            Text("From LocalStorage ${this.localStorageLinkObject.code}").onClick(
                {
                    evt =>
                    var temp = this.localStorageLinkObject
                    temp.code += 1
                    this.localStorageLinkObject = temp
                }
            )
        }
    }
}
```