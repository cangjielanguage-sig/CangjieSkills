### func createConicGradient(Int64, Int64, Int64)

```cangjie
public func createConicGradient(startAngle: Int64, x: Int64, y: Int64): CanvasGradient
```

**功能：** 创建一个圆锥渐变色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|startAngle|Int64|是|-|开始渐变的角度。角度测量从中心右侧水平开始，顺时针移动。<br>单位：弧度。|
|x|Int64|是|-|圆锥渐变的中心x轴坐标。<br>默认单位：vp。|
|y|Int64|是|-|圆锥渐变的中心y轴坐标。<br>默认单位：vp。|

**返回值：**

|类型|说明|
|:----|:----|
|[CanvasGradient](cj-canvas-drawing-canvasgradient.md#class-canvasgradient)|新的CanvasGradient对象，用于在canvas上创建渐变效果。|

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
    @State
    var toDataUrl: String = ""

    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    let grad = this.context.createConicGradient(0, 50, 80)
                    grad.addColorStop(0.0, 0xff0000)
                    grad.addColorStop(0.5, 0xffffff)
                    grad.addColorStop(1.0, 0x00ff00)
                    this.context.fillStyle(grad)
                    this.context.fillRect(0, 30, 100, 100)
                }
            )
            Text(this.toDataUrl)
        }.width(100.percent).height(100.percent)
    }
}
```

![createConicGradient](./figures/canvasrenderingcontext_13.png)

### func createImageData(Float64, Float64)

```cangjie
public func createImageData(sw: Float64, sh: Float64): ImageData
```

**功能：** 创建新的、空白的、指定大小的ImageData 对象，请参考[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sw|Float64|是|-|ImageData的宽度。<br>默认单位：vp。|
|sh|Float64|是|-|ImageData的高度。<br>默认单位：vp。|

**返回值：**

|类型|说明|
|:----|:----|
|[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)|新的ImageData对象。|

### func createImageData(Int64, Int64)

```cangjie
public func createImageData(sw: Int64, sh: Int64): ImageData
```

**功能：** 创建新的、空白的、指定大小的ImageData 对象，请参考[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)，该接口存在内存拷贝行为，高耗时，应避免频繁使用。createImageData示例同[putImageData](#func-putimagedataimagedata-float64-float64)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sw|Int64|是|-|ImageData的宽度。<br>默认单位：vp。|
|sh|Int64|是|-|ImageData的高度。<br>默认单位：vp。|

**返回值：**

|类型|说明|
|:----|:----|
|[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)|新的ImageData对象。|