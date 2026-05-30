### 示例1（设置分段渐变色量规图）

该示例通过colors接口，实现了多色量规图效果。

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
        Column() {
            Gauge(value: 50.0, min: 0.0, max: 100.0) {
                Text("50").fontSize(30).textAlign(TextAlign.Center).width(80.percent)
            }.startAngle(220).endAngle(135).colors(this.colorArray).width(80.percent).strokeWidth(18).trackShadow(
                radius: 7.0, offsetX: 7.0, offsetY: 7.0).indicator(icon: "default")
        }.width(100.percent)
    }
}
```

![gauge1](figures/gauge1.png)

### 示例2（设置单色量规图）

该示例通过colors接口，实现了单色量规图效果。

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
            Gauge(value: 50.0, min: 0.0, max: 100.0) {
                Column {
                    Text("50").fontWeight(FontWeight.Medium).width(62.percent).fontColor(0x182431).maxFontSize(60).
                        minFontSize(30).textAlign(TextAlign.Center).margin(35).textOverflow(TextOverflow.Ellipsis).
                        maxLines(1)
                }.width(100.percent).height(100.percent)
            }.startAngle(210).endAngle(150).colors(Color.RED, 1).width(80.percent).height(80.percent).strokeWidth(18).
                trackShadow(radius: 7.0, offsetX: 7.0, offsetY: 7.0).padding(18)
        }.margin(top: 40).width(100.percent).height(100.percent)
    }
}
```

![gauge2](figures/gauge2.png)

### 示例3（设置定制说明区）

该示例通过descriptionBuilder接口，实现了说明区的设置功能。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @Builder
    func descriptionBuilder() {
        Text("说明文本").fontSize(20).textAlign(TextAlign.Center).width(80.percent)
    }
    func build() {
        Column() {
            Gauge(value: 50.0, min: 0.0, max: 100.0) {
                Text("50").fontSize(30).textAlign(TextAlign.Center).width(80.percent)
            }.startAngle(220).endAngle(135).colors(Color.RED, 1).width(80.percent).strokeWidth(18).trackShadow(
                radius: 7.0, offsetX: 7.0, offsetY: 7.0).description(this.descriptionBuilder)
        }.width(100.percent)
    }
}
```

![gauge3](figures/gauge3.png)