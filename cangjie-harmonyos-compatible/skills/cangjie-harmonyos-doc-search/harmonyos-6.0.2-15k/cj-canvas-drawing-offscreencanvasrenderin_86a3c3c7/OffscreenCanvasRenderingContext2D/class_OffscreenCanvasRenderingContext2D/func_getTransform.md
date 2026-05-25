### func getTransform()

```cangjie
public func getTransform(): Matrix2D
```

**功能：** 获取当前被应用到上下文的转换矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[Matrix2D](./cj-canvas-drawing-matrix2d.md#class-matrix2d)|矩阵对象。|

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
    private let context1: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings)
    private let offcontext1: OffscreenCanvasRenderingContext2D = OffscreenCanvasRenderingContext2D(600, 200,
        this.settings)
    private let context2: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings)
    private let offcontext2: OffscreenCanvasRenderingContext2D = OffscreenCanvasRenderingContext2D(600, 200,
        this.settings)
    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Text("context1")
            Canvas(this.context1).width(230.vp).height(120.vp).backgroundColor(0xffff00).onReady(
                {
                    =>
                    this.offcontext1.fillRect(50, 50, 50, 50)
                    this.offcontext1.setTransform(1.2, 3.1415926 / 8.0, 3.1415926 / 6.0, 0.5, 30.0, -25.0)
                    this.offcontext1.fillRect(50, 50, 50, 50)
                    let image = this.offcontext1.transferToImageBitmap()
                    this.context1.transferFromImageBitmap(image)
                }
            )
            Text("context2")
            Canvas(this.context2).width(230.vp).height(120.vp).backgroundColor(0x0ffff0).onReady(
                {
                    =>
                    this.offcontext2.fillRect(50, 50, 50, 50)
                    let storedTransform = this.offcontext1.getTransform()
                    this.offcontext2.setTransform(storedTransform)
                    this.offcontext2.fillRect(50, 50, 50, 50)
                    let image = this.offcontext2.transferToImageBitmap()
                    this.context2.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_29](figures/offscreenrenderingcontext_29.png)