## 备忘录开发实战

本节通过备忘录应用的开发，让开发者了解如何通过ArkUI框架设计自己的应用，本节未设计代码架构直接进行功能开发，即根据需求做即时开发，不考虑后续维护，同时向开发者介绍功能开发所需的装饰器。

### State状态变量

- @State装饰器作为最常用的装饰器，用来定义状态变量，一般作为父组件的数据源，当开发者点击时，通过触发状态变量的更新从而刷新UI，去掉@State则不再支持刷新UI。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.*
import kit.LocalizationKit.*

@Entry
@Component
class EntryView {
    @State
    var isFinished: Bool = false
    func build() {
        Column {
            Row() {
                Text("全部待办").fontSize(30).fontWeight(FontWeight.Bold)
            }.width(100.percent).margin(top: 40.vp, bottom: 10.vp, left: 50.vp)

            // 待办事项
            Row(15) {
                if (this.isFinished) {
                    // 此处'app.media.ic_public_todo_filled'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
                    Image(@r(app.media.ic_public_todo_filled)).width(28).height(28)
                } else {
                    // 此处'app.media.ic_public_todo'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
                    Image(@r(app.media.ic_public_todo)).width(28).height(28)
                }
                Text('学习高数').fontSize(24).fontWeight(FontWeight.Bold).decoration(
                    decorationType: if (this.isFinished) {
                    TextDecorationType.LineThrough
                } else {
                    TextDecorationType.None
                }, color: Color.BLACK, decorationStyle: TextDecorationStyle.SOLID)
            }.width(100.percent).margin(left: 60, top: 15).onClick({event => this.isFinished = !this.isFinished})
        }.height(100.percent).width(100.percent).backgroundColor(0x90f1f3f5)
    }
}
```

![mvvm_state](./figures/mvvm_state.gif)