### 自定义组件外改变状态变量

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

let storage = LocalStorage()
let temp = storage.setOrCreate("count", 47)

public class Model {
    let storage: LocalStorage = storage

    public func change(propName: String, value: Int64) {
        this.storage.setOrCreate<Int64>(propName, value)
    }
}

let model: Model = Model()

@Entry[storage]
@Component
class EntryView {
    @LocalStorageLink["count"]
    var count: Int64 = 0
    func build() {
        Column() {
            Text("count值: ${this.count}")
            Button("change").onClick({evt => model.change("count", this.count + 1);})
        }
    }
}
```

### 混合UI开发使用ArkTS的LocalStorage

混合UI开发中可以使用仓颉进行部分页面的UI开发，如果希望能共享ArkTS视图中的LocalStorage实例，可以在所属UIAbility中创建LocalStorage实例，并调用windowStage.loadContent。

```ts
// EntryAbility.ets
import UIAbility from '@ohos.app.ability.UIAbility';
import window from '@ohos.window';

export default class EntryAbility extends UIAbility {
    para:Record<string, string> = { 'PropA': '47' };
    storage: LocalStorage = new LocalStorage(this.para);

    onWindowStageCreate(windowStage: window.WindowStage) {
        windowStage.loadContent('pages/Index', this.storage);
    }
}
```

同时在ArkTS侧将LocalStorage的getShared()注册到globalThis。

```ts
import { CJHybridComponentV2 } from "cjhybridview" // 导入CJHybridComponentV2

globalThis.localStorageGetShared = LocalStorage.getShared // 将LocalStorage的getShared()注册到globalThis

// 通过getShared接口获取stage共享得LocalStorage实例
let storage = LocalStorage.getShared()
@Entry(storage)
@Component
struct Index {
  build() {
    Column() {
      CJHybridComponentV2({
        library: "ohos_app",         // 指定加载的so，对应上面的仓颉UI
        component: "MyLocalStorage"  // 指定加载的仓颉class，对应上面仓颉UI中使用@HybridComponentEntry修饰的class
      })
    }
    .height('100%')
    .width('100%')
  }
}
```

在仓颉侧可以使用宏`@LocalStorageProp["propName", "InterOp"]`和`@LocalStorageLink["propName", "InterOp"]`与ArkTS视图LocalStorage实例中的属性建立单向和双向同步关系。

```cangjie
package ohos_app

import kit.HybridUIKit.*
import ohos.state_macro_manage.*

@HybridComponentEntry
@Component
class MyLocalStorage {
    @State
    var text: String = "Text"
    @LocalStorageLink["PropA", "InterOp"]
    var storage: String = "b"
    @LocalStorageProp["PropB", "InterOp"]
    let storage2: String = "b"
    public func build() {
        Column {
            Text(text).onClick({evt => storage = "88"})
            Text("PropA " + storage)
            Text("PropB " + storage2)
        }
    }
}
```