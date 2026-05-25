### func stroke(Path2D)

```cangjie
public func stroke(path2D: Path2D): Unit
```

**功能：** 根据指定的路径，进行边框绘制操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path2D|[Path2D](./cj-canvas-drawing-path2d.md#class-path2d)|是|-|需要绘制的Path2D。|

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
    private var path2Da: Path2D = Path2D()
    @State
    var message: String = ""
    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    let offContext = this.offCanvas.getContext(contextType: ContextType.type_2d, options: this.settings)
                    this.path2Da.moveTo(25, 25)
                    this.path2Da.lineTo(25, 105)
                    this.path2Da.lineTo(75, 105)
                    this.path2Da.lineTo(75, 25)
                    offContext.strokeStyle(0xff0000)
                    offContext.stroke(this.path2Da)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_45](figures/offscreenrenderingcontext_45.PNG)

### func strokeRect(Float64, Float64, Float64, Float64)

```cangjie
public func strokeRect(x: Float64, y: Float64, width: Float64, height: Float64): Unit
```

**功能：** 绘制具有边框的矩形，矩形内部不填充。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|指定矩形的左上角x坐标。<br>默认单位：vp。|
|y|Float64|是|-|指定矩形的左上角y坐标。<br>默认单位：vp。|
|width |Float64|是|-|指定矩形的宽度。<br>默认单位：vp。|
|height|Float64|是|-|指定矩形的高度。<br>默认单位：vp。|