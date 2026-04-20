### 父组件\@State到子组件\@Prop简单数据类型同步

以下示例是\@State到子组件\@Prop简单数据同步，父组件EntryView的状态变量countDownStartValue初始化子组件CountDownComponent中\@Prop装饰的count，点击“Try again”，count的修改仅保留在CountDownComponent不会同步给父组件EntryView。

EntryView的状态变量countDownStartValue的变化将重置CountDownComponent的count。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Component
class CountDownComponent {
    @Prop
    var count: Int64
    var costOfOneAttempt: Int64 = 1
    func build() {
        Column() {
            if (this.count > 0) {
                Text("You have ${this.count} Nuggets left")
            } else {
                Text('Game over!')
            }
            // @Prop装饰的变量不会同步给父组件
            Button("Try again").margin(10).onClick {
                evt => this.count -= this.costOfOneAttempt
            }
        }
    }
}

@Entry
@Component
class EntryView {
    @State
    var countDownStartValue: Int64 = 10
    func build() {
        Column {
            Text("Grant ${this.countDownStartValue} nuggets to play.")
            // 父组件的数据源的修改会同步给子组件
            Button("+1 - Nuggets in New Game").margin(10).onClick {
                evt => this.countDownStartValue += 1
            }
            // 父组件的修改会同步给子组件
            Button("-1  - Nuggets in New Game").margin(10).onClick {
                evt => this.countDownStartValue -= 1
            }
            CountDownComponent(count: this.countDownStartValue, costOfOneAttempt: 2)
        }
    }
}
```

![Video-Prop-CountDown](figures/Video-Prop-CountDown.gif)

在上面的示例中：

1. CountDownComponent子组件首次创建时其\@Prop装饰的count变量将从父组件\@State装饰的countDownStartValue变量初始化；

2. 按“+1”或“-1”按钮时，父组件的\@State装饰的countDownStartValue值会变化，这将触发父组件重新渲染，在父组件重新渲染过程中会刷新使用countDownStartValue状态变量的UI组件并单向同步更新CountDownComponent子组件中的count值；

3. 更新count状态变量值也会触发CountDownComponent的重新渲染，在重新渲染过程中，评估使用count状态变量的if语句条件（this.count &gt; 0），并执行true分支中的使用count状态变量的UI组件相关描述来更新Text组件的UI显示；

4. 当按下子组件CountDownComponent的“Try again”按钮时，其\@Prop变量count将被更改，但是count值的更改不会影响父组件的countDownStartValue值；

5. 父组件的countDownStartValue值会变化时，父组件的修改将覆盖掉子组件CountDownComponent中count本地的修改。