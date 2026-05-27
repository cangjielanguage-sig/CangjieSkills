### 简单类型和类对象类型的\@Link

以下示例中，点击父组件EntryView中的“Parent View: Set yellowButton”和“Parent View: Set GreenButton”，可以从父组件将变化同步给子组件。

1. 点击子组件GreenButton和YellowButton中的Button，子组件会发生相应变化，将变化同步给父组件。因为\@Link是双向同步，会将变化同步给\@State。

2. 当点击父组件EntryView中的Button时，\@State变化，也会同步给\@Link，子组件也会发生对应的刷新。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Observed
class GreenButtonState {
    @Publish
    var width: Int64 = 0
}

@Component
class GreenButton {
    @Link
    var greenButtonState: GreenButtonState

    func build() {
        Button("Green Button").width(this.greenButtonState.width).height(40).backgroundColor(Color.GREEN).margin(12).
            onClick {
            evt => if (this.greenButtonState.width < 700) {
                // 更新class的属性，变化可以被观察到同步回父组件
                this.greenButtonState.width += 60
            } else {
                // 更新class，变化可以被观察到同步回父组件
                this.greenButtonState = GreenButtonState(width: 180)
            }
        }
    }
}

@Component
class YellowButton {
    @Link
    var yellowButtonState: Int64

    func build() {
        Button("Yellow Button").width(this.yellowButtonState).height(40).backgroundColor(Color.YELLOW).fontColor(
            Color.BLACK).margin(12).onClick {
            evt =>
            // 子组件的简单类型可以同步回父组件
            this.yellowButtonState += 40
        }
    }
}

@Entry
@Component
class EntryView {
    @State
    var greenButtonState: GreenButtonState = GreenButtonState(width: 180)
    @State
    var yellowButtonProp: Int64 = 180
    func build() {
        Column() {
            Flex(FlexOptions(direction: FlexDirection.Column, alignItems: ItemAlign.Center)) {
                // 简单类型从父组件@State向子组件@Link数据同步
                Button("Parent View: Set yellowButton").width(this.yellowButtonProp).height(40).margin(12).onClick {
                    evt => if (this.yellowButtonProp < 700) {
                        this.yellowButtonProp = this.yellowButtonProp + 100
                    } else {
                        this.yellowButtonProp = 100
                    }
                }
                // class类型从父组件@State向子组件@Link数据同步
                Button("Parent View: Set GreenButton").width(this.greenButtonState.width).height(40).margin(12).onClick {
                    evt => if (this.greenButtonState.width < 700) {
                        this.greenButtonState.width = this.greenButtonState.width + 100
                    } else {
                        this.greenButtonState.width = 100
                    }
                }
                // class类型初始化@Link
                GreenButton(greenButtonState: this.greenButtonState)
                // 简单类型初始化@Link
                YellowButton(yellowButtonState: this.yellowButtonProp)
            }
        }
    }
}
```

![Video-link-UsageScenario-one](figures/Video-link-UsageScenario-one.gif)