### func textAlign(TextAlignStyle)

```cangjie
public func textAlign(align: TextAlignStyle): Unit
```

**功能：** 设置文本绘制中的文本对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|align|[TextAlignStyle](./cj-common-types.md#enum-textalignstyle)|是|-|设置文本绘制中的文本对齐方式。<br/>初始值：Start。|

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
                    offContext.moveTo(140, 10)
                    offContext.lineTo(140, 160)
                    offContext.stroke()
                    offContext.font(size: 18.px, family: "sans-serif")
                    offContext.textAlign(TextAlignStyle.Start)
                    offContext.fillText('textAlign=start', 140, 60)
                    offContext.textAlign(TextAlignStyle.End)
                    offContext.fillText('textAlign=end', 140, 80)
                    offContext.textAlign(TextAlignStyle.Left)
                    offContext.fillText('textAlign=left', 140, 100)
                    offContext.textAlign(TextAlignStyle.Center)
                    offContext.fillText('textAlign=center', 140, 120)
                    offContext.textAlign(TextAlignStyle.Right)
                    offContext.fillText('textAlign=right', 140, 140)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_46](figures/offscreenrenderingcontext_46.PNG)