### 数组类型的\@Link

以下示例中，当用ObservedArrayList\<Int\>修饰items时，可以感知到数组元素的添加，删除和替换。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Component
class Child {
    @Link
    var items: ObservedArrayList<Int>

    func build() {
        Column() {
            Button("Button 1: push").margin(12).size(width: 312, height: 40).onClick {
                => this.items.append(this.items.size + 1)
            }

            Button("Button 2: replace whole item").margin(12).size(width: 312, height: 40).onClick {
                => this.items = ObservedArrayList<Int>([100, 200, 300])
            }
        }
    }
}

@Entry
@Component
class EntryView {
    @State
    var arr: ObservedArrayList<Int> = ObservedArrayList<Int>([1, 2, 3])
    func build() {
        Column() {
            Child(items: arr)
            ForEach(
                this.arr,
                {
                    item: Int, index: Int => Button("${item}").margin(12).size(width: 312, height: 40).backgroundColor(
                        Color.WHITE).fontColor(Color.BLACK)
                }
            )
        }
    }
}
```

![Video-link-UsageScenario-two](figures/Video-link-UsageScenario-two.gif)

### 使用双向同步机制更改本地其他变量

使用[\@Watch](./cj-macro-watch.md)可以在双向同步时，更改本地变量。

下面的示例中，在\@Link的\@Watch里面修改\@State装饰的变量sourceNumber，实现了父子组件间的变量同步。但是\@State装饰的变量memberMessage在本地的修改不会影响到父组件中的变量改变。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Component
class Child {
    @State
    var memberMessage: String = 'Hello World'
    @Link
    @Watch[onSourceChange]
    var sourceNumber: Int64
    func onSourceChange() {
        this.memberMessage = this.sourceNumber.toString()
    }
    func build() {
        Column() {
            Text(this.memberMessage)
            Text("子组件的sourceNumber：" + this.sourceNumber.toString())
            Button("子组件更改memberMessage").onClick {
                => this.memberMessage = "Hello memberMessage"
            }
        }.margin(10)
    }
}

@Entry
@Component
class EntryView {
    @State
    var sourceNumber: Int64 = 0;
    func build() {
        Column() {
            Text("父组件的sourceNumber：" + this.sourceNumber.toString())
            Child(sourceNumber: this.sourceNumber)
            Button("父组件更改sourceNumber").onClick {
                => this.sourceNumber++
            }
        }
    }
}
```

![Video-link-UsageScenario-three](figures/Video-link-UsageScenario-three.gif)