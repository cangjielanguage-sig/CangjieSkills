### 示例4（设置辅助区）

该示例通过设置子组件，实现了辅助区的设置功能。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    var color1: LinearGradient = LinearGradient([ColorStop(0x65EEC9A3, 0), ColorStop(0xFFEF629F, 1)])
    var color2: LinearGradient = LinearGradient([ColorStop(0xFF67F9D4, 0), ColorStop(0xFFFF9554, 1)])
    var color3: LinearGradient = LinearGradient([ColorStop(0x6572B513, 0), ColorStop(0x6508efa6, 1)])
    var color4: LinearGradient = LinearGradient([ColorStop(0x65ed08f5, 0), ColorStop(0x65ef0849, 1)])
    var colorArray: Array<(LinearGradient, Float32)> = [(this.color1, 1.0), (this.color2, 2.0), (this.color3, 3.0),
        (this.color4, 4.0)]
    func build() {
        Column {
            Gauge(value: 50.0, min: 1.0, max: 100.0) {
                Column {
                    Text("50").maxFontSize(72.0).minFontSize(10.0).fontColor(0x182431).width(80.percent).textAlign(
                        TextAlign.Center).margin(top: 35.percent).textOverflow(TextOverflow.Ellipsis).maxLines(1)
                    Text("辅助文本").maxFontSize(30.0).minFontSize(18.0).fontWeight(FontWeight.Medium).width(62.percent).
                        height(15.9.percent).textAlign(TextAlign.Center)
                }.width(100.percent).height(100.percent)
            }.startAngle(210).endAngle(150).colors(this.colorArray).width(80.percent).height(80.percent).strokeWidth(18).
                trackShadow(radius: 7.0, offsetX: 7.0, offsetY: 7.0).padding(18)
        }.margin(top: 40).width(100.percent).height(100.percent)
    }
}
```

![gauge4](figures/gauge4.png)

### 示例5（设置最大最小值）

该示例通过设置min，max属性，实现了量规图的最大最小值设置的功能。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Column() {
            Gauge(value: 50.0, min: 20.0, max: 50.0) {
                Column {
                    Text("50").maxFontSize(80).minFontSize(60).fontWeight(FontWeight.Medium).width(40.percent).height(
                        30.percent).textAlign(TextAlign.Center).margin(top: 22.2.percent).textOverflow(
                        TextOverflow.Ellipsis).maxLines(1)
                }.width(100.percent).height(100.percent)
            }.startAngle(225).endAngle(135).colors(Color.RED, 1).width(80.percent).height(80.percent).strokeWidth(18).
                trackShadow(radius: 7.0, offsetX: 7.0, offsetY: 7.0).padding(18)
        }.margin(top: 40).width(100.percent).height(100.percent)
    }
}
```

![gauge5](figures/gauge5.png)

### 示例6（设置指针）

该示例通过indicator接口，实现了设置量规图的指针的功能。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Column() {
            Gauge(value: 50.0, min: 20.0, max: 50.0) {
                Column {
                    Text("50").maxFontSize(80).minFontSize(60).fontWeight(FontWeight.Medium).width(40.percent).height(
                        30.percent).textAlign(TextAlign.Center).margin(top: 22.2.percent).textOverflow(
                        TextOverflow.Ellipsis).maxLines(1)
                }.width(100.percent).height(100.percent)
            }.startAngle(225).endAngle(135).colors(Color.RED, 1).width(80.percent).height(80.percent).strokeWidth(18).
                trackShadow(radius: 7.0, offsetX: 7.0, offsetY: 7.0).indicator(icon: "null").padding(18)
        }.margin(top: 40).width(100.percent).height(100.percent)
    }
}
```

![gauge6](figures/gauge6.png)