### func textBaseline(TextBaseline)

```cangjie
public func textBaseline(baseline: TextBaseline): Unit
```

**功能：** 设置文本绘制中的水平对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|baseline|[TextBaseline](./cj-common-types.md#enum-textbaseline)|是|-|设置文本绘制中的水平对齐方式，可选值为：<br>- alphabetic：文本基线是标准的字母基线。<br>- middle：文本基线在文本块的中间。<br>- ideographic：文字基线是表意字基线；如果字符本身超出了alphabetic基线，那么ideograhpic基线位置在字符本身的底部。<br>- bottom：文本基线在文本块的底部。 与ideographic基线的区别在于ideographic基线不需要考虑下行字母。<br>初始值：alphabetic。|

**示例：**

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    private let settings: RenderingContextSettings = RenderingContextSettings(antialias: true)
    private let context: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings)
    @State
    var message: String = ""
    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    this.context.strokeStyle(0x0000ff)
                    this.context.moveTo(0, 120)
                    this.context.lineTo(400, 120)
                    this.context.stroke()
                    this.context.font(size: 20.px, family: "sans-serif")
                    this.context.textBaseline(TextBaseline.Top)
                    this.context.fillText('Top', 10, 120)
                    this.context.textBaseline(TextBaseline.Bottom)
                    this.context.fillText('Bottom', 55, 120)
                    this.context.textBaseline(TextBaseline.Middle)
                    this.context.fillText('Middle', 125, 120)
                    this.context.textBaseline(TextBaseline.Alphabetic)
                    this.context.fillText('Alphabetic', 195, 120)
                    this.context.textBaseline(TextBaseline.Hanging)
                    this.context.fillText('Hanging', 295, 120)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![textBaseline](./figures/canvasrenderingcontext_47.png)