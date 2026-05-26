### 示例7（设置起止角度）

该示例通过startAngle、endAngle接口，实现了量规图起止角度设置的功能。

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
                    Text("50").maxFontSize(60).minFontSize(30).fontWeight(FontWeight.Medium).width(62.percent).height(
                        30.percent).textAlign(TextAlign.Center).margin(top: 35.percent).textOverflow(
                        TextOverflow.Ellipsis).maxLines(1)
                }.width(100.percent).height(100.percent)
            }.startAngle(200).endAngle(100).colors(Color.RED, 1).width(80.percent).height(80.percent).strokeWidth(18).
                trackShadow(radius: 7.0, offsetX: 7.0, offsetY: 7.0).indicator(icon: "null").padding(18)
        }.margin(top: 40).width(100.percent).height(100.percent)
    }
}
```

![gauge7](figures/gauge7.png)

### 示例8（设置隐私隐藏）

该示例通过privacySensitive接口，实现了隐私隐藏效果，效果展示需要卡片框架支持

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
            Gauge(value: 50.0, min: 1.0, max: 100.0) {
                Column {
                    Text("50").maxFontSize(60).minFontSize(30).fontWeight(FontWeight.Medium).width(40.percent).height(
                        30.percent).textAlign(TextAlign.Center).margin(top: 22.2.percent).textOverflow(
                        TextOverflow.Ellipsis).maxLines(1)
                }.width(100.percent).height(100.percent)
            }.startAngle(225).endAngle(135).colors(Color.RED, 1).width(80.percent).height(80.percent).strokeWidth(18).
                trackShadow(radius: 7.0, offsetX: 7.0, offsetY: 7.0).padding(18).privacySensitive(true)
        }.margin(top: 40).width(100.percent).height(100.percent)
    }
}
```

![gauge8](figures/gauge8.gif)