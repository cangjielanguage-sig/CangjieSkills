### 使用if进行条件渲染

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var count: Int64 = 0;
    func build() {
        Column() {
            Text("count=${this.count}")

            if (this.count > 0) {
                Text("count is positive").fontColor(Color.GREEN)
            }

            Button('increase count').onClick({
                => this.count++;
            })

            Button('decrease count').onClick({
                => this.count--;
            })
        }
    }
}
```

if语句的每个分支都包含一个构建函数。此类构建函数必须创建一个或多个子组件。在初始渲染时，if语句会执行构建函数，并将生成的子组件添加到其父组件中。

每当if或else if条件语句中使用的状态变量发生变化时，条件语句都会更新并重新评估新的条件值。如果条件值评估发生了变化，这意味着需要构建另一个条件分支。此时ArkUI框架将：

1.删除所有以前渲染的（早期分支的）组件。

2.执行新分支的构造函数，将生成的子组件添加到其父组件中。

在以上示例中，如果count从0增加到1，那么if语句更新，条件count > 0将重新评估，评估结果将从false更改为true。因此，将执行条件为真分支的构造函数，创建一个Text组件，并将它添加到父组件Column中。如果后续count更改为0，则Text组件将从Column组件中删除。由于没有else分支，因此不会执行新的构造函数。