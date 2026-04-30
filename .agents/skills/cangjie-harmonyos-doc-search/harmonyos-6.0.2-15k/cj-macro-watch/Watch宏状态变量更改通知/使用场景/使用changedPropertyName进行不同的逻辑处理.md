### 使用changedPropertyName进行不同的逻辑处理

以下示例说明了如何在@Watch函数中使用changedPropertyName进行不同的逻辑处理。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    @Watch[countUpdated]
    var apple: Int64 = 0
    @State
    @Watch[countUpdated]
    var cabbage: Int64 = 0
    @State
    var propName: String = "test"
    @State
    var fruit: Int64 = 0
    func countUpdated() {
        if (this.propName == "apple") {
            this.fruit = this.apple
        }
    }
    func build() {
        Column() {
            Text("Number of apples: ${this.apple.toString()}").fontSize(30)
            Text("Number of cabbages: ${this.cabbage.toString()}").fontSize(30)
            Text("Total number of fruits: ${this.fruit.toString()}").fontSize(30)
            Button("Add apples").onClick(
                {
                    etv =>
                    this.apple++
                    this.propName = "apple"
                }
            )
            Button("Add cabbages").onClick(
                {
                    etv =>
                    this.cabbage++
                    this.propName = "cabbages"
                }
            )
        }
    }
}
```

处理步骤如下：

1. 单击Button("Add apples")时，apple的值发生变化。
2. 状态管理框架调用@Watch函数countUpdated，发生变化的状态变量名为apple，满足if逻辑条件，fruit的值被改变。
3. 绑定了apple，fruit状态变量的Text重新渲染。
4. 单击Button("Add cabbages")时，cabbage的值发生变化。
5. 状态管理框架调用@Watch函数countUpdated，发生变化的状态变量名为cabbage，不满足if逻辑条件，fruit的值不发生变化。
6. 绑定了cabbage状态变量的Text重新渲染。