### @Prop、@Link的作用

上述示例中，所有的代码都写在了@Entry组件中，随着需要渲染的组件越来越多，@Entry组件必然需要进行拆分，为此拆分出的子组件就需要使用@Prop和@Link装饰器：

- @Prop是父子间单向传递，子组件会深拷贝父组件数据，可从父组件更新，也可自己更新数据，但不会同步父组件数据。
- @Link是父子间双向传递，父组件改变，会通知所有的@Link，同时@Link的更新也会通知父组件对应变量进行刷新。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.*
import kit.LocalizationKit.*

@Component
class TodoComponent {
    func build() {
        Row() {
            Text('全部待办').fontSize(30).fontWeight(FontWeight.Bold)
        }.width(100.percent).margin(top: 40.vp, bottom: 10.vp, left: 50.vp)
    }
}

@Component
class AllChooseComponent {
    @Link
    var isFinished: Bool

    func build() {
        Row() {
            Button("全选", ButtonOptions(shape: ButtonType.Capsule)).onClick(
                {event => this.isFinished = !this.isFinished}).fontSize(30).fontWeight(FontWeight.Bold).backgroundColor(
                0xf7f6cc74)
        }.width(100.percent).margin(top: 10.vp, left: 60.vp)
    }
}

@Component
class ThingsComponent1 {
    @Prop
    var isFinished: Bool

    func build() {
        Row(15) {
            if (this.isFinished) {
                // 此处'app.media.ic_public_todo_filled'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
                Image(@r(app.media.ic_public_todo_filled)).width(28).height(28)
            } else {
                // 此处'app.media.ic_public_todo'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
                Image(@r(app.media.ic_public_todo)).width(28).height(28)
            }
            Text("学习语文").fontSize(24).fontWeight(FontWeight.Bold).decoration(
                decorationType: if (this.isFinished) {
                TextDecorationType.LineThrough
            } else {
                TextDecorationType.None
            }, color: Color.BLACK, decorationStyle: TextDecorationStyle.SOLID)
        }.width(100.percent).margin(left: 60, top: 15).onClick({event => this.isFinished = !this.isFinished})
    }
}

@Component
class ThingsComponent2 {
    @Prop
    var isFinished: Bool

    func build() {
        Row(15) {
            if (this.isFinished) {
                // 此处'app.media.ic_public_todo_filled'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
                Image(@r(app.media.ic_public_todo_filled)).width(28).height(28)
            } else {
                // 此处'app.media.ic_public_todo'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
                Image(@r(app.media.ic_public_todo)).width(28).height(28)
            }
            Text("学习高数").fontSize(24).fontWeight(FontWeight.Bold).decoration(
                decorationType: if (this.isFinished) {
                TextDecorationType.LineThrough
            } else {
                TextDecorationType.None
            }, color: Color.BLACK, decorationStyle: TextDecorationStyle.SOLID)
        }.width(100.percent).margin(left: 60, top: 15).onClick({event => this.isFinished = !this.isFinished})
    }
}

@Entry
@Component
class EntryView {
    @State
    var isFinished: Bool = false;

    func build() {
        Column() {

            // 全部待办
            TodoComponent()

            // 全选
            AllChooseComponent(isFinished: this.isFinished)

            // 待办事项1
            ThingsComponent1(isFinished: this.isFinished)

            // 待办事项2
            ThingsComponent2(isFinished: this.isFinished)
        }.height(100.percent).width(100.percent).margin(top: 5, bottom: 5).backgroundColor(0x90f1f3f5)
    }
}
```

![mvvm_proplink](./figures/mvvm_proplink.gif)