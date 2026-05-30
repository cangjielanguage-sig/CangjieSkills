### func createPattern(ImageBitmap, Repetition)

```cangjie
public func createPattern(image: ImageBitmap, repetition: Repetition): CanvasPattern
```

**功能：** 通过指定图像和重复方式创建图片填充的模板。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|image|[ImageBitmap](./cj-canvas-drawing-imagebitmap.md#class-imagebitmap)|是|-|图源对象，具体参考ImageBitmap对象。|
|repetition|[Repetition](./cj-common-types.md#enum-repetition)|是|-|图像重复的方式。|

**返回值：**

|类型|说明|
|:----|:----|
|[CanvasPattern](./cj-canvas-drawing-canvaspattern.md#class-canvaspattern)|通过指定图像和重复方式创建图片填充的模板对象。|

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
    private let img: ImageBitmap = ImageBitmap("resource://RAWFILE/icon.png")
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
                    let pattern = offContext.createPattern(this.img, repeat)
                    offContext.fillStyle(pattern)
                    offContext.fillRect(0, 0, 200, 200)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_16](figures/offscreenrenderingcontext_16.PNG)