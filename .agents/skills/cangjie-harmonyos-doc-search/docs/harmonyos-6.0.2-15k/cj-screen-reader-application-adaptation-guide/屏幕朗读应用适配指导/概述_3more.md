## 概述

屏幕朗读软件（Screen Reader）主要帮助视障人士使用移动智能设备，通过语音输出，获取屏幕或界面中的信息。视障用户无法通过视觉直接感知和理解用户界面。他/她们需要在屏幕上使用手指探索或手势逐步在界面上进行导航，同时通过设备的朗读反馈来理解界面信息和潜在的交互功能。因此，让用户能够快速、准确地感知界面内容并进行正确交互是无障碍开发的关键。视障用户需要先通过手势使某个UI对象获得焦点，同时系统朗读出该对象的内容和功能，然后视障用户双击屏幕点击或选择该对象。

因此，进行开发时应遵循以下原则：

1. 确保视障用户可以通过手势快速、符合使用逻辑顺序地导航至页面内所有有效UI对象。
2. 确保用户在当前获焦的UI对象下接收到适当的语音朗读反馈，朗读内容应简洁清晰地告知用户当前所在UI对象内容、功能、以及可执行的操作。

同时，进行开发时，组件可以设置相应的[无障碍属性](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-accessibility.md)和事件来更好地使用无障碍能力。

## 标注屏幕朗读内容的场景

控件包含显示文本（text）、无障碍文本（accessibilityText）2个属性，其中，显示文本为用户界面上呈现的信息，无障碍文本为无障碍专有的朗读信息，不在界面上显示。屏幕朗读提取信息进行朗读时无障碍文本的优先级大于显示文本，即当无障碍文本不为空时，会朗读无障碍文本，否则朗读显示文本。

所以：

1. 对于文本类控件，尽量使用显示文本来表达信息，使视障用户和视力健全用户可以获取到相同的信息。
2. 对于文本类控件，如果除显示文本外，还额外提供了颜色等视觉效果为视力健全用户提供了更多信息的场景，可采用无障碍文本为视障用户提供更多的信息用于朗读。
3. 对于非文本类控件，可采用无障碍文本为视障用户提供朗读信息。

accessibilityText() 设置无障碍文本。聚焦button时朗读效果为："按钮, Accessibility text"。

```cangjie
import kit.UIKit.*

@Entry
@Component
class EntryView {
    var shortText: String = "Button"
    var longText: String = "Accessibility text"

    func build() {
        Navigation() {
            Column {
                Blank()
                Button(this.shortText).accessibilityText(this.longText).align(Alignment.Center).fontSize(20)
                Blank()
            }.width(100.percent).height(100.percent)
        }
    }
}
```

## 禁用屏幕朗读焦点的场景

装饰性的控件一般为分隔符、占位符和美化图标等，这类图形元素仅仅起到调整页面布局或装饰性效果，并不会向用户传达有效的信息或提供交互功能，删除后不影响指引用户体验。可以设置控件的无障碍是否可见的属性将其设置对无障碍不可见，这样在屏幕朗读模式下控件就不会获取焦点和朗读。

![图1](./figures/graph1.png)

accessibilityGroup(true) 用于多个组件的组合，组合内的默认没有焦点。

.accessibilityLevel("no")用于组件设置不可聚焦，不被无障碍感知。

例如：以下代码同时显示“Broadcast”和“No broadcast”消息，但当ScreenReader处于“打开”状态时，message可被聚焦，但message1将不被聚焦。

```cangjie
import kit.UIKit.*

@Entry
@Component
class EntryView {
    @State
    var message: String = "Broadcast"
    @State
    var message1: String = "No broadcast"

    func build() {
        Navigation() {
            Column {
                Row() {
                    Text(this.message).fontSize(40).fontWeight(FontWeight.Bold).fontColor(Color.BLUE).margin(left: 40)
                }.width(100.percent).height(50.percent)

                Row() {
                    Text(this.message1).fontSize(40).fontWeight(FontWeight.Bold).fontColor(Color.BLUE).margin(left: 40).
                        accessibilityLevel("no") // use for component
                }
                    // .accessibilityGroup(true)
                    //.accessibilityLevel("no-hide-descendants") // use for container
                    // 可以使用这两行代替上面的accessibilityLevel("no")
                    .width(100.percent).height(50.percent)
            }.height(100.percent)
        }
    }
}
```