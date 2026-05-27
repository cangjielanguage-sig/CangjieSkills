### 示例3（使用LengthEdgeWidthsType类型值）

borderImage接口中的slice、width、outset属性值使用[LengthEdgeWidthsType](#interface-lengthedgewidthstype)类型。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import kit.LocalizationKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var WidthStartValue: Float64 = 0.0
    @State
    var WidthEndValue: Float64 = 0.0
    @State
    var SliceStartValue: Float64 = 0.0
    @State
    var SliceEndValue: Float64 = 0.0
    @State
    var OutSetStartValue: Float64 = 0.0
    @State
    var OutSetEndValue: Float64 = 0.0
    @State
    var RepeatValue: Array<RepeatMode> = [RepeatMode.REPEAT, RepeatMode.STRETCH, RepeatMode.ROUND, RepeatMode.SPACE]
    @State
    var SelectIndex: Int32 = 0
    @State
    var SelectText: String = 'Repeat'
    @State
    var FillValue: Bool = false

    func build() {
        Row {
            Column(20) {
                Row() {
                    Text('This is borderImage.').textAlign(TextAlign.Center).fontSize(40)
                }.borderImage(
                    BorderImageOption(
                        source: @r(app.media.icon),
                        slice: EdgeWidths(top: 10.px, bottom: 10.px, left: this.SliceStartValue.px,
                            right: this.SliceEndValue.px),
                        width: EdgeWidths(top: 10.px, bottom: 10.px, left: this.WidthStartValue.px,
                            right: this.WidthEndValue.px),
                        outset: EdgeWidths(top: 10.px, bottom: 10.px, left: this.OutSetStartValue.px,
                            right: this.OutSetEndValue.px),
                        repeat: this.RepeatValue[Int64(this.SelectIndex)],
                        fill: this.FillValue
                    )
                )

                Column() {
                    Text('borderImageSliceStart = ${Int64(this.SliceStartValue)}px')
                    Slider(
                        value: this.SliceStartValue,
                        min: 0.0,
                        max: 100.0,
                        style: SliderStyle.OutSet
                    ).showTips(true).onChange({
                        value: Float64, mode: SliderChangeMode => this.SliceStartValue = value
                    })
                }

                Column() {
                    Text('borderImageEndSliceStart = ${Int64(this.SliceEndValue)}px')
                    Slider(
                        value: this.SliceEndValue,
                        min: 0.0,
                        max: 100.0,
                        style: SliderStyle.OutSet
                    ).showTips(true).onChange({
                        value: Float64, mode: SliderChangeMode => this.SliceEndValue = value
                    })
                }

                Column() {
                    Text('borderImageWidthStart = ${Int64(this.WidthStartValue)}px')
                    Slider(
                        value: this.WidthStartValue,
                        min: 0.0,
                        max: 100.0,
                        style: SliderStyle.OutSet
                    ).showTips(true).onChange({
                        value: Float64, mode: SliderChangeMode => this.WidthStartValue = value
                    })
                }

                Column() {
                    Text('borderImageWidthEnd = ${Int64(this.WidthEndValue)}px')
                    Slider(
                        value: this.WidthEndValue,
                        min: 0.0,
                        max: 100.0,
                        style: SliderStyle.OutSet
                    ).showTips(true).onChange({
                        value: Float64, mode: SliderChangeMode => this.WidthEndValue = value
                    })
                }

                Column() {
                    Text('borderImageOutSetStart = ${Int64(this.OutSetStartValue)}px')
                    Slider(
                        value: this.OutSetStartValue,
                        min: 0.0,
                        max: 100.0,
                        style: SliderStyle.OutSet
                    ).showTips(true).onChange({
                        value: Float64, mode: SliderChangeMode => this.OutSetStartValue = value
                    })
                }

                Column() {
                    Text('borderImageOutSetEnd = ${Int64(this.OutSetEndValue)}px')
                    Slider(
                        value: this.OutSetEndValue,
                        min: 0.0,
                        max: 100.0,
                        style: SliderStyle.OutSet
                    ).showTips(true).onChange({
                        value: Float64, mode: SliderChangeMode => this.OutSetEndValue = value
                    })
                }

                Row() {
                    Text('borderImageRepeat: ')
                    Select(
                        [
                            SelectOption("Repeat", icon: ""),
                            SelectOption("Stretch", icon: ""),
                            SelectOption("Round", icon: ""),
                            SelectOption("Space", icon: "")
                        ]
                    ).value(this.SelectText).selected(this.SelectIndex).divider(options: Option.None).onSelect(
                        {
                            index: Int32, text: String =>
                            this.SelectIndex = index
                            this.SelectText = text
                        }
                    )
                }