### 页面的默认焦点

```cangjie
public func defaultFocus(isDefaultFocus: Bool): This
```

设置当前组件是否为当前页面上的默认焦点。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var oneButtonColor: Color = Color.GRAY
    @State
    var twoButtonColor: Color = Color.GRAY
    @State
    var threeButtonColor: Color = Color.GRAY

    func build() {
        Column(20) {
            // 通过外接键盘的上下键可以让焦点在三个按钮间移动，按钮获焦时颜色变化，失焦时变回原背景色
            Button("First Button").width(260).height(70).backgroundColor(oneButtonColor).fontColor(Color.BLACK)
                // 监听第一个组件的获焦事件，获焦后改变颜色
                .onFocus(
                {
                => oneButtonColor = Color.GREEN
            })
                // 监听第一个组件的失焦事件，失焦后改变颜色
                .onBlur({
                => oneButtonColor = Color.GRAY
            })

            Button("Second Button").width(260).height(70).backgroundColor(twoButtonColor).fontColor(Color.BLACK)
                // 监听第二个组件的获焦事件，获焦后改变颜色
                .onFocus(
                {
                => twoButtonColor = Color.GREEN
            })
                // 监听第二个组件的失焦事件，失焦后改变颜色
                .onBlur({
                => twoButtonColor = Color.GRAY
            })

            Button("Third Button").width(260).height(70).backgroundColor(threeButtonColor).fontColor(Color.BLACK)
                // 设置默认焦点
                .
                defaultFocus(true)
                    // 监听第三个组件的获焦事件，获焦后改变颜色
                    .onFocus({
                => threeButtonColor = Color.GREEN
            })
                // 监听第三个组件的失焦事件，失焦后改变颜色
                .onBlur({
                => threeButtonColor = Color.GRAY
            })
        }.width(100.percent).margin(top: 20)
    }
}
```

![defaultFocus.gif](figures/defaultFocus.gif)

上述示例包含以下2步：

- 在第三个Button组件上设置了defaultFocus(true)，进入页面后第三个Button默认获焦，显示为绿色。
- 按下TAB键，触发走焦，第三个Button正处于获焦状态，会出现焦点框。

### 容器的默认焦点

容器的默认焦点受到[获焦优先级](#焦点组与获焦优先级)的影响。

**defaultFocus与FocusPriority的区别：**

[defaultFocus](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-focus.md#func-defaultfocusbool)是用于指定页面首次展示时的默认获焦节点，[FocusPriority](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-focus.md#func-focusscopeprioritystring-focuspriority)是用于指定某个容器首次获焦时其子节点的获焦优先级。上述两个属性在某些场景同时配置时行为未定义，例如下面的场景，页面首次展示无法同时满足defaultFocus获焦和高优先级组件获焦。示例如下：

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Row() {
            Button("Button1").defaultFocus(true)
            Button("Button2").focusScopePriority("RowScope", priority: FocusPriority.PREVIOUS)
        }.focusScopeId("RowScope")
    }
}
```

### 页面/容器整体获焦时的焦点链

#### 整体获焦与非整体获焦

- 整体获焦是页面/容器自身作为焦点链的叶节点获焦，获焦后再把焦点链叶节点转移到子孙组件。例如，页面切换、Navigation组件中的路由切换、焦点组走焦、容器组件主动调用requestFocusById等。

- 非整体获焦是某个组件作为焦点链叶节点获焦，导致其祖先节点跟着获焦。例如TextInput组件主动获取焦点、Tab键在非焦点组场景下走焦等。

#### 整体获焦的焦点链形成

1.页面首次获焦：

- 焦点链叶节点为配置了defaultFocus的节点。
- 未配置defaultFocus时，焦点停留在页面的根容器上。

2.页面非首次获焦：由上次获焦的节点获焦。

3.获焦链上存在配置了获焦优先级的组件和容器：

- 容器内存在优先级大于PREVIOUS的组件，由优先级最高的组件获焦。
- 容器内不存在优先级大于PREVIOUS的组件，由上次获焦的节点获焦。例如，窗口失焦后重新获焦。