### func fillRect(Float64, Float64, Float64, Float64)

```cangjie
public func fillRect(x: Float64, y: Float64, width: Float64, height: Float64): Unit
```

**功能：** 填充一个矩形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-| 指定矩形左上角点的x坐标。<br>默认单位：vp。 |
|y|Float64|是|-| 指定矩形左上角点的y坐标。<br>默认单位：vp。 |
|width |Float64|是|-|指定矩形的宽度。<br>默认单位：vp。|
|height|Float64|是|-|指定矩形的高度。<br>默认单位：vp。|

### func fillRect(Int64, Int64, Int64, Int64)

```cangjie
public func fillRect(x: Int64, y: Int64, width: Int64, height: Int64): Unit
```

**功能：** 填充一个矩形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int64|是|-| 指定矩形左上角点的x坐标。<br>默认单位：vp。 |
|y|Int64|是|-| 指定矩形左上角点的y坐标。<br>默认单位：vp。 |
|width |Int64|是|-|指定矩形的宽度。<br>默认单位：vp。|
|height|Int64|是|-|指定矩形的高度。<br>默认单位：vp。|

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
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xD5D5D5).onReady(
                {
                    =>
                    let offContext = this.offCanvas.getContext(contextType: ContextType.type_2d, options: this.settings)
                    offContext.fillRect(30, 30, 100, 100)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreencanvasrenderingcontext2d_fillrect](./figures/offscreencanvasrenderingcontext2d_fillrect.jpg)

### func fillStyle(Color)

```cangjie
public func fillStyle(color: Color): Unit
```

**功能：** 指定绘制的填充色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[Color](./cj-common-types.md#class-color)|是|-|填充区域的颜色。<br>初始值：黑色。|

### func fillStyle(UInt32)

```cangjie
public func fillStyle(color: UInt32): Unit
```

**功能：** 指定绘制的填充色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|UInt32|是|-|填充区域的颜色。<br>初始值：0x000000。|

### func fillStyle(CanvasGradient)

```cangjie
public func fillStyle(gradient: CanvasGradient): Unit
```

**功能：** 指定绘制的填充色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|gradient|[CanvasGradient](cj-canvas-drawing-canvasgradient.md#class-canvasgradient)|是|-|渐变对象，使用[createLinearGradient](#func-createlineargradientfloat64-float64-float64-float64)方法创建。|