### \@Prop嵌套场景

在嵌套场景下，每一层都要用\@Observed装饰，且每一层都要被\@Prop接收，这样才能感知到嵌套场景。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

// 以下是嵌套类对象的数据结构。
@Observed
class Son {
    @Publish
    var title: String
}

@Observed
class Father {
    @Publish
    var name: String
    @Publish
    var son: Son
}
// 以下组件层次结构呈现的是@Prop嵌套场景的数据结构。
@Entry
@Component
class EntryView {
    @State
    var person: Father = Father(name: 'Hello', son: Son(title: 'world'));
    func build() {
        Column {
            Flex(
                FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center,
                justifyContent: FlexAlign.SpaceBetween)) {
                Button('change Father name').width(312).height(40).margin(12).onClick({
                    evt => this.person.name = 'Hi'
                })
                Button('change Son title').width(312).height(40).margin(12).onClick(
                    {
                    evt => this.person.son.title = 'ArkUI'
                })
                Text(this.person.name).fontSize(16).margin(12).width(312).height(40).borderRadius(20).textAlign(
                    TextAlign.Center).onClick({
                    evt => this.person.name = 'Bye'
                })
                Text(this.person.son.title).fontSize(16).margin(12).width(312).height(40).borderRadius(20).textAlign(
                    TextAlign.Center).onClick({
                    evt => this.person.son.title = "JS"
                })
                Child(child: this.person.son)
            }
        }
    }
}

@Component
class Child {
    @Prop
    var child: Son
    func build() {
        Column() {
            Text(this.child.title).fontSize(16).margin(12).width(312).height(40).borderRadius(20).textAlign(
                TextAlign.Center).onClick({
                evt => this.child.title = "Bye Bye"
            })
        }
    }
}
```

![Video-prop-UsageScenario-three](figures/Video-prop-UsageScenario-three.gif)