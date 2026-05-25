### func font(FontStyle, FontWeight, Length, String)

```cangjie
public func font(
    style!: FontStyle = FontStyle.Normal,
    weight!: FontWeight = FontWeight.Normal,
    size!: Length = 14.px,
    family!: String = "sans-serif"
): Unit
```

**功能：** 设置文本绘制中的字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 用于指定字体样式。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Normal| **命名参数。** 用于指定字体的粗细。|
|size|[Length](./cj-common-types.md#interface-length)|否|14.px| **命名参数。** 指定字号和行高，单位支持px、vp。|
|family|String|否|"sans-serif"| **命名参数。** 指定字体系列，支持如下几种类型：'sans-serif', 'serif', 'monospace'。|

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
                    offContext.font(size: 30.px, family: "sans-serif")
                    offContext.fillText("Hello px", 20, 60)
                    offContext.font(size: 30.vp, family: "sans-serif")
                    offContext.fillText("Hello vp", 20, 100)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_25](figures/offscreenrenderingcontext_25.PNG)