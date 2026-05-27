### func moveTo(Int64, Int64)

```cangjie
public func moveTo(x: Int64, y: Int64): Unit
```

**功能：** 路径从当前点移动到指定点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int64|是|-|指定位置的x坐标。<br>默认单位：vp。|
|y|Int64|是|-|指定位置的y坐标。<br>默认单位：vp。|

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
                    offContext.beginPath()
                    offContext.moveTo(10, 10)
                    offContext.lineTo(280, 160)
                    offContext.stroke()
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreencanvasrenderingcontext2d_moveto](./figures/offscreencanvasrenderingcontext2d_moveto.png)

### func putImageData(ImageData, Float64, Float64)

```cangjie
public func putImageData(imageData: ImageData, dx: Float64, dy: Float64): Unit
```

**功能：** 使用[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)数据填充新的矩形区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|imageData|[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)|是|-|包含像素值的ImageData对象。|
|dx|Float64|是|-|填充区域在x轴方向的偏移量。<br>默认单位：vp。|
|dy|Float64|是|-|填充区域在y轴方向的偏移量。<br>默认单位：vp。|

### func putImageData(ImageData, Int64, Int64)

```cangjie
public func putImageData(imageData: ImageData, dx: Int64, dy: Int64): Unit
```

**功能：** 使用[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)数据填充新的矩形区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|imageData|[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)|是|-|包含像素值的ImageData对象。|
|dx|Int64|是|-|填充区域在x轴方向的偏移量。<br>默认单位：vp。|
|dy|Int64|是|-|填充区域在y轴方向的偏移量。<br>默认单位：vp。|