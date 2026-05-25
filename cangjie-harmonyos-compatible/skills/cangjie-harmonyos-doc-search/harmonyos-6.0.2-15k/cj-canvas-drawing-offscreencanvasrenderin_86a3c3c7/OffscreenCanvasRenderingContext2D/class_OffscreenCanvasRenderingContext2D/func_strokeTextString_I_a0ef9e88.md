### func strokeText(String, Int64, Int64, Int64)

```cangjie
public func strokeText(text: String, x: Int64, y: Int64, maxWidth: Int64): Unit
```

**功能：** 绘制描边类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|需要绘制的文本内容。|
|x|Int64|是|-|需要绘制的文本的左下角x坐标。<br>默认单位：vp。|
|y|Int64|是|-|需要绘制的文本的左下角y坐标。<br>默认单位：vp。|
|maxWidth|Int64|是|-|需要绘制的文本的最大宽度。<br>默认单位：vp。|

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

    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    let offContext = this.offCanvas.getContext(contextType: ContextType.type_2d, options: this.settings)
                    offContext.font(size: 55.px, family: 'sans-serif')
                    offContext.strokeText("Hello World!", 20, 60)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreencanvasrenderingcontext2d_stroketext2](./figures/offscreencanvasrenderingcontext2d_stroketext2.png)