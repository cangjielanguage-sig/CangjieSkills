### func strokeRect(Int64, Int64, Int64, Int64)

```cangjie
public func strokeRect(x: Int64, y: Int64, width: Int64, height: Int64): Unit
```

**功能：** 绘制具有边框的矩形，矩形内部不填充。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int64|是|-|指定矩形的左上角x坐标。<br>默认单位：vp。|
|y|Int64|是|-|指定矩形的左上角y坐标。<br>默认单位：vp。|
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
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    let offContext = this.offCanvas.getContext(contextType: ContextType.type_2d, options: this.settings)
                    offContext.strokeRect(30, 30, 200, 150)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreencanvasrenderingcontext2d_strokerect](./figures/offscreencanvasrenderingcontext2d_strokerect.png)

### func strokeStyle(Color)

```cangjie
public func strokeStyle(color: Color): Unit
```

**功能：** 设置绘制线条的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[Color](./cj-common-types.md#class-color)|是|-|设置绘制线条的颜色。<br>初始值：黑色。|

### func strokeStyle(UInt32)

```cangjie
public func strokeStyle(color: UInt32): Unit
```

**功能：** 设置绘制线条的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|UInt32|是|-|设置绘制线条的颜色。<br>初始值：0x000000。|

### func strokeStyle(CanvasGradient)

```cangjie
public func strokeStyle(gradient: CanvasGradient): Unit
```

**功能：** 设置绘制线条的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|gradient|[CanvasGradient](cj-canvas-drawing-canvasgradient.md#class-canvasgradient)|是|-|渐变对象，使用[createLinearGradient](#func-createlineargradientfloat64-float64-float64-float64)方法创建。|