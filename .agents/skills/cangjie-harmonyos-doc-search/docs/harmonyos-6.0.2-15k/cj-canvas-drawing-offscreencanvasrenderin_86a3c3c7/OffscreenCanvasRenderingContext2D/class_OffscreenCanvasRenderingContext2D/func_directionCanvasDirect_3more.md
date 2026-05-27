### func direction(CanvasDirection)

```cangjie
public func direction(canvasDirection: CanvasDirection): Unit
```

**功能：** 用于设置绘制文字时使用的文字方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|canvasDirection|[CanvasDirection](./cj-common-types.md#enum-canvasdirection)|是|-|绘制文字时使用的文字方向。<br>初始值：inherit。|

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
                    let ctx = offContext
                    ctx.font(size: 48.px, family: "serif")
                    ctx.textAlign(TextAlignStyle.Start)
                    ctx.fillText("Hi ltr!", 200, 50)

                    ctx.direction(CanvasDirection.rtl)
                    ctx.fillText("Hi rtl!", 200, 100)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_18](figures/offscreenrenderingcontext_18.PNG)

### func drawImage(ImageBitmap, Float64, Float64)

```cangjie
public func drawImage(image: ImageBitmap, dx: Float64, dy: Float64): Unit
```

**功能：** 进行图像绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|image|[ImageBitmap](./cj-canvas-drawing-imagebitmap.md#class-imagebitmap)|是|-|图片资源。|
|dx|Float64|是|-|绘制区域左上角在x轴的位置。<br>默认单位：vp。|
|dy|Float64|是|-|绘制区域左上角在y轴的位置。<br>默认单位：vp。|

### func drawImage(ImageBitmap, Int64, Int64)

```cangjie
public func drawImage(image: ImageBitmap, dx: Int64, dy: Int64): Unit
```

**功能：** 进行图像绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|image|[ImageBitmap](./cj-canvas-drawing-imagebitmap.md#class-imagebitmap)|是|-|图片资源。|
|dx|Int64|是|-|绘制区域左上角在x轴的位置。<br>默认单位：vp。|
|dy|Int64|是|-|绘制区域左上角在y轴的位置。<br>默认单位：vp。|