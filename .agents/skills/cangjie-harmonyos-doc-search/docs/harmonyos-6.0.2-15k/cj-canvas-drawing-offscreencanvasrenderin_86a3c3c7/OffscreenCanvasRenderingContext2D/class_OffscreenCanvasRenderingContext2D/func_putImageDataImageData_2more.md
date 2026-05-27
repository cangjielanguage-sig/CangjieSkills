### func putImageData(ImageData, Float64, Float64, Float64, Float64, Float64, Float64)

```cangjie
public func putImageData(
    imageData: ImageData,
    dx: Float64,
    dy: Float64,
    dirtyX: Float64,
    dirtyY: Float64,
    dirtyWidth: Float64,
    dirtyHeight: Float64): Unit
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
|dirtyX|Float64|是|-|源图像数据矩形裁切范围左上角距离源图像左上角的x轴偏移量。<br>默认单位：vp。|
|dirtyY|Float64|是|-|源图像数据矩形裁切范围左上角距离源图像左上角的y轴偏移量。<br>默认单位：vp。|
|dirtyWidth|Float64 |是|-|源图像数据矩形裁切范围的宽度。<br>默认单位：vp。|
|dirtyHeight|Float64|是|-|源图像数据矩形裁切范围的高度。<br>默认单位：vp。|

### func putImageData(ImageData, Int64, Int64, Int64, Int64, Int64, Int64)

```cangjie
public func putImageData(
    imageData: ImageData,
    dx: Int64,
    dy: Int64,
    dirtyX: Int64,
    dirtyY: Int64,
    dirtyWidth: Int64,
    dirtyHeight: Int64): Unit
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
|dirtyX|Int64|是|-|源图像数据矩形裁切范围左上角距离源图像左上角的x轴偏移量。<br>默认单位：vp。|
|dirtyY|Int64|是|-|源图像数据矩形裁切范围左上角距离源图像左上角的y轴偏移量。<br>默认单位：vp。|
|dirtyWidth|Int64 |是|-|源图像数据矩形裁切范围的宽度。<br>默认单位：vp。|
|dirtyHeight|Int64|是|-|源图像数据矩形裁切范围的高度。<br>默认单位：vp。|

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
                    let imageDataNum = offContext.createImageData(40, 40)
                    let imageData = offContext.createImageData(imageDataNum)
                    offContext.putImageData(imageData, 10, 10)
                    offContext.putImageData(imageData, 150, 10, 0, 0, 50, 50)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreencanvasrenderingcontext2d_putimagedata](./figures/offscreencanvasrenderingcontext2d_putimagedata.png)