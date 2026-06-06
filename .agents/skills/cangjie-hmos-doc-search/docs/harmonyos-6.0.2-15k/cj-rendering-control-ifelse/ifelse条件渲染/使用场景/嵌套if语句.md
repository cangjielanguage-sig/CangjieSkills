### 嵌套if语句

条件语句的嵌套对父组件的相关规则没有影响。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
internal import ohos.base.*
internal import ohos.component.*

@Entry
@Component
public class EntryView {
    @State
    var toggle: Bool = false;
    @State
    var toggleColor: Bool = false;
    func build() {
        Column(20) {
            Text('Before').fontSize(15)
            if (this.toggle) {
                Text('Top True, positive 1 top').backgroundColor(Color.GREEN).fontSize(20)
                // 内部if语句
                if (this.toggleColor) {
                    Text('Top True, Nested True, positive COLOR  Nested ').backgroundColor(Color.GREEN).fontSize(15)
                } else {
                    Text('Top True, Nested False, Negative COLOR  Nested ').backgroundColor(Color.BLUE).fontSize(15)
                }
            } else {
                Text('Top false, negative top level').fontSize(20).backgroundColor(Color.RED)
                if (this.toggleColor) {
                    Text('positive COLOR  Nested ').backgroundColor(Color.GREEN).fontSize(15)
                } else {
                    Text('Negative COLOR  Nested ').backgroundColor(Color.BLUE).fontSize(15)
                }
            }
            Text('After').fontSize(15)
            Button('Toggle Outer').onClick({
                => this.toggle = !this.toggle
            })
            Button('Toggle Inner').onClick({
                => this.toggleColor = !this.toggleColor
            })
        }.width(100.percent).justifyContent(FlexAlign.Center)
    }
}
```