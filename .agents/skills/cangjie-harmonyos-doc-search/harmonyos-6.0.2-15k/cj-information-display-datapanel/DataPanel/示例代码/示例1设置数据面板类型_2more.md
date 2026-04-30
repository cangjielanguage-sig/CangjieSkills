### 示例1（设置数据面板类型）

该示例通过type属性，实现了设置数据面板的类型的功能。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    var valueArr: Array<Float64> = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]
    func build() {
        Column {
            Row() {
                Stack() {
                    DataPanel(values: [30.0], max: 100.0, panelType: DataPanelType.CircleType).width(168).height(168)
                    Column() {
                        Text("30").fontSize(35).fontColor(0x182431)
                        Text("1.0.0").fontSize(9.33).lineHeight(12.83).fontWeight(FontWeight.W500).opacity(0.6)
                    }
                    Text("%").fontSize(9.33).lineHeight(12.83).fontWeight(FontWeight.W500).opacity(0.6).position(
                        x: 104.42, y: 78.17)
                }.margin(right: 44)
                Stack() {
                    DataPanel(values: [50.0, 12.0, 8.0, 5.0], max: 100.0, panelType: DataPanelType.CircleType).width(
                        168).height(168)
                    Column() {
                        Text("75").fontSize(35).fontColor(0x182431)
                        Text("已使用98GB/128GB").fontSize(8.17).lineHeight(11.08).fontWeight(FontWeight.W500).opacity(
                            0.6)
                    }
                    Text("%").fontSize(9.33).lineHeight(12.83).fontWeight(FontWeight.W500).opacity(0.6).position(
                        x: 104.42, y: 78.17)
                }
            }.margin(bottom: 59)
            DataPanel(values: this.valueArr, max: 100.0, panelType: DataPanelType.LineType).width(300).height(10)
        }.width(100.percent).margin(top: 5)
    }
}
```

![dataPanel](figures/dataPanel.png)

### 示例2（设置渐变色和阴影）

该示例通过valueColors和trackShadow接口设置LinearGradient颜色，实现了设置渐变色效果和阴影效果。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    var values1: Array<Float64> = [20.0, 20.0, 20.0, 20.0]
    var color1: LinearGradient = LinearGradient([ColorStop(0x65EEC9A3, 0), ColorStop(0xFFEF629F, 1)])
    var color2: LinearGradient = LinearGradient([ColorStop(0xFF67F9D4, 0), ColorStop(0xFFFF9554, 1)])
    var colorShadow1: LinearGradient = LinearGradient([ColorStop(0x65EEC9A3, 0), ColorStop(0x65EF629F, 1)])
    var colorShadow2: LinearGradient = LinearGradient([ColorStop(0x65e26709, 0), ColorStop(0x65efbd08, 1)])
    var colorShadow3: LinearGradient = LinearGradient([ColorStop(0x6572B513, 0), ColorStop(0x6508efa6, 1)])
    var colorShadow4: LinearGradient = LinearGradient([ColorStop(0x65ed08f5, 0), ColorStop(0x65ef0849, 1)])
    var color3: LinearGradient = LinearGradient(0x00FF00)
    var color4: LinearGradient = LinearGradient(0x20FF0000)
    @State
    var bgColor: UInt32 = 0x08182431
    @State
    var offsetX: Int64 = 15
    @State
    var offsetY: Int64 = 15
    @State
    var radius: Int64 = 5
    @State
    var colorArray: Array<LinearGradient> = [this.color1, this.color2, this.color3, this.color4]
    @State
    var shadowColorArray: Array<LinearGradient> = [this.colorShadow1, this.colorShadow2, this.colorShadow3,
        this.colorShadow4]
    func build() {
        Column {
            Text("LinearGradient").fontSize(9).fontColor(0xCCCCCC).textAlign(TextAlign.Start).width(100.percent).margin(
                top: 20, left: 20)
            DataPanel(values: this.values1, max: 100.0, panelType: DataPanelType.CircleType).width(300).height(300).
                valueColors(this.colorArray).trackShadow(
                DataPanelShadowOptions(
                    radius: this.radius,
                    colors: this.shadowColorArray,
                    offsetX: this.offsetX,
                    offsetY: this.offsetY
                )
            ).strokeWidth(30).trackBackgroundColor(this.bgColor)
        }.width(100.percent).margin(top: 5)
    }
}
```

![LinearGradientDataPanel](figures/LinearGradientDataPanel.png)