### 示例2（为按钮添加渲染控制）

该示例通过if/else控制按钮的显示文本。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var count: UInt32 = 0
    func build() {
        Column() {
            Text('${this.count}').fontSize(30).onClick {
                evt => this.count++
            }
            if (this.count <= 0) {
                Button('count is negative').fontSize(30).height(50)
            } else if (this.count % 2 == 0) {
                Button('count is even').fontSize(30).height(50)
            } else {
                Button('count is odd').fontSize(30).height(50)
            }
        }.height(100.percent).width(100.percent).justifyContent(FlexAlign.Center)
    }
}
```

![Button2](figures/button_2.gif)

### 示例3（设置按钮文本样式）

该示例通过配置labelStyle自定义按钮文本的显示样式。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var txt: String = 'overflowTextOverlengthTextOverflow.Clip'
    func build() {
        Column() {
            Button(this.txt).width(210).height(100).backgroundColor(0x317aff).labelStyle(
                overflow: TextOverflow.Clip,
                maxLines: 1,
                minFontSize: 20.fp,
                maxFontSize: 20.fp,
                font: Fonts(
                    size: 20.fp,
                    weight: FontWeight.Bolder,
                    family: 'cursive',
                    style: FontStyle.Italic
                )
            ).fontSize(40)
        }.height(100.percent).width(100.percent).justifyContent(FlexAlign.Center)
    }
}
```

![Button3](figures/button_3.png)

### 示例4（设置不同尺寸按钮的重要程度）

该示例通过配置controlSize、buttonStyle实现不同尺寸按钮的重要程度。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var txt: String = 'overflowTextOverlengthTextOverflow.Clip'
    func build() {
        Flex(
            FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Start,
            justifyContent: FlexAlign.SpaceBetween)) {
            Text('Normal size button').fontSize(9).fontColor(0xCCCCCC)
            Flex(FlexParams(alignItems: ItemAlign.Center, wrap: FlexWrap.Wrap)) {
                Button('Emphasized').buttonStyle(ButtonStyleMode.EMPHASIZED)
                Button('Normal').buttonStyle(ButtonStyleMode.NORMAL)
                Button('Textual').buttonStyle(ButtonStyleMode.TEXTUAL)
            }

            Text('Small size button').fontSize(9).fontColor(0xCCCCCC)
            Flex(FlexParams(alignItems: ItemAlign.Center, wrap: FlexWrap.Wrap)) {
                Button('Emphasized').controlSize(ControlSize.SMALL).buttonStyle(ButtonStyleMode.EMPHASIZED)
                Button('Normal').controlSize(ControlSize.SMALL).buttonStyle(ButtonStyleMode.NORMAL)
                Button('Textual').controlSize(ControlSize.SMALL).buttonStyle(ButtonStyleMode.TEXTUAL)
            }
        }.height(400).padding(left: 35, right: 35, top: 35)
    }
}
```

![Button4](figures/button_4.png)