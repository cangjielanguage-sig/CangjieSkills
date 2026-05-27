### Builder方法

Builder方法用于组件内定义方法，可以使得相同代码可以在组件内进行复用。

本示例不仅使用了@Builder方法进行去重，同时对数据进行了移出，可以看到此时代码更加清晰易读，相对于最开始的代码，@Entry组件基本只用于处理页面构建逻辑，而不处理大量与页面设计无关的内容。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import kit.LocalizationKit.*

@Observed
class TodoListData {
    var planList: Array<String> = [
        '7.30 起床',
        '8.30 早餐',
        '11.30 中餐',
        '17.30 晚餐',
        '21.30 夜宵',
        '22.30 洗澡',
        '1.30 起床'
    ]
}

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
class ThingsComponent {
    @Prop
    var isFinished: Bool
    @Prop
    var things: String

    @Builder
    func displayIcon(icon: AppResource) {
        Image(icon).width(28.vp).height(28.vp).onClick({event => this.isFinished = !this.isFinished})
    }

    func build() {
        Row(15) {
            if (this.isFinished) {
                // 此处'app.media.ic_public_todo_filled'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
                this.displayIcon(@r(app.media.ic_public_todo_filled))
            } else {
                // 此处'app.media.ic_public_todo'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
                this.displayIcon(@r(app.media.ic_public_todo))
            }
            Text(this.things).fontSize(24).fontWeight(FontWeight.Bold).decoration(
                decorationType: if (this.isFinished) {
                TextDecorationType.LineThrough
            } else {
                TextDecorationType.None
            }, color: Color.BLACK, decorationStyle: TextDecorationStyle.SOLID).onClick({event => this.things += '啦'})
        }.height(8.percent).width(90.percent).padding(left: 15.vp).opacity(if (this.isFinished) {
            0.3
        } else {
            1.0
        }).border(width: 1).borderColor(Color.WHITE).borderRadius(25).backgroundColor(Color.WHITE)
    }
}

@Entry
@Component
class EntryView {
    @State
    var isFinished = false
    @State
    var data: TodoListData = TodoListData()

    func build() {
        Column() {
            TodoComponent()

            AllChooseComponent(isFinished: this.isFinished)

            List() {
                ForEach(
                    this.data.planList,
                    {
                        item: String, _: Int64 => ListItem() {
                            ThingsComponent(isFinished: this.isFinished, things: item)
                        }.margin(top: 10.vp).width(100.percent)
                    }
                )
            }.margin(left: 10.vp, right: 10.vp)
        }.height(100.percent).width(100.percent).backgroundColor(0x90f1f3f5)
    }
}
```

效果图如下：

![mvvm_builder](./figures/mvvm_builder.gif)