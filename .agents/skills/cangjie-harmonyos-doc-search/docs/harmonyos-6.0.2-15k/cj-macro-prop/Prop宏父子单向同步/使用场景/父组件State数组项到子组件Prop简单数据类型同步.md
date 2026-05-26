### 父组件\@State数组项到子组件\@Prop简单数据类型同步

父组件中\@State如果装饰的数组，其数组项也可以初始化\@Prop。以下示例中父组件Index中\@State装饰的数组arr，将其数组项初始化子组件Child中\@Prop装饰的value。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Component
class Child {
    @Prop
    var value: Int64
    func build() {
        Text("${this.value}").fontSize(50.vp).onClick {
            evt => this.value++
        }
    }
}

@Entry
@Component
class EntryView {
    @State
    var arr: Array<Int64> = [1, 2, 3]
    func build() {
        Row {
            Column {
                Child(value: this.arr[0])
                Child(value: this.arr[1])
                Child(value: this.arr[2])
                Divider().height(5)
                ForEach(
                    this.arr,
                    itemGeneratorFunc: {
                        item: Int64, _: Int64 => Child(value: item)
                    },
                    keyGeneratorFunc: {
                        item: Int64, _: Int64 => item.toString()
                    }
                )
                Text('replace entire arr').fontSize(50).onClick {
                    evt => if (this.arr[0] == 1) {
                        this.arr = [3, 4, 5]
                    } else {
                        this.arr = [1, 2, 3]
                    }
                }
            }
        }
    }
}
```

初始渲染创建6个子组件实例，每个\@Prop装饰的变量初始化都在本地拷贝了一份数组项。子组件onclick事件处理程序会更改局部变量值。

如果单击界面上的“1”六下，“2”五下、“3”四下，将所有变量的本地取值都变为“7”。

```text
7
7
7
----
7
7
7
```

单击replace entire arr后，屏幕将显示以下信息。

```text
7
7
7
----
7
4
5
```

- 在子组件Child中做的所有的修改都不会同步回父组件Index组件，所以即使6个组件显示都为7，但在父组件Index中，this.arr保存的值依旧是[1,2,3]。

- 点击replace entire arr，this.arr[0] == 1成立，将this.arr赋值为[3, 4, 5]；

- 因为this.arr[0]已更改，但此情形下修改\@State数组无法触发子组件UI更新，即修改无法同步至\@Prop变量，所以Child({value: this.arr[0]})组件的值仍然是7。

- this.arr的更改触发ForEach更新，this.arr更新的前后都有数值为3的数组项：[3, 4, 5] 和[1, 2, 3]。根据diff算法，数组项“3”将被保留，删除“1”和“2”的数组项，添加为“4”和“5”的数组项。这就意味着，数组项“3”的组件不会重新生成，而是将其移动到第一位。所以“3”对应的组件不会更新，此时“3”对应的组件数值为“7”，ForEach最终的渲染结果是“7”，“4”，“5”。