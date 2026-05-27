### func textBaseline(TextBaseline)

```cangjie
public func textBaseline(baseline: TextBaseline): Unit
```

**功能：** 设置文本绘制中的水平对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|baseline|[TextBaseline](./cj-common-types.md#enum-textbaseline)|是|-|设置文本绘制中的水平对齐方式。<br/>初始值：Alphabetic。|

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
    private let offCanvas: OffscreenCanvas = OffscreenCanvas(600.0, 600.0)
    @State
    var message: String = ""
    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    let offContext = this.offCanvas.getContext(contextType: ContextType.type_2d, options: this.settings)
                    offContext.strokeStyle(0x0000ff)
                    offContext.moveTo(0, 120)
                    offContext.lineTo(400, 120)
                    offContext.stroke()
                    offContext.font(size: 20.px, family: "sans-serif")
                    offContext.textBaseline(TextBaseline.Top)
                    offContext.fillText('Top', 10, 120)
                    offContext.textBaseline(TextBaseline.Bottom)
                    offContext.fillText('Bottom', 55, 120)
                    offContext.textBaseline(TextBaseline.Middle)
                    offContext.fillText('Middle', 125, 120)
                    offContext.textBaseline(TextBaseline.Alphabetic)
                    offContext.fillText('Alphabetic', 195, 120)
                    offContext.textBaseline(TextBaseline.Hanging)
                    offContext.fillText('Hanging', 295, 120)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_47](figures/offscreenrenderingcontext_47.PNG)