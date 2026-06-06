### func arcTo(Float64, Float64, Float64, Float64, Float64)

```cangjie
public func arcTo(x1: Float64, y1: Float64, x2: Float64, y2: Float64, radius: Float64): Unit
```

**功能：** 依据给定的控制点和圆弧半径创建圆弧路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x1|Float64|是|-|第一个控制点的x坐标值。<br>默认单位：vp。|
|y1|Float64|是|-|第一个控制点的y坐标值。<br>默认单位：vp。|
|x2|Float64|是|-|第二个控制点的x坐标值。<br>默认单位：vp。|
|y2|Float64|是|-|第二个控制点的y坐标值。<br>默认单位：vp。|
|radius|Float64|是|-|圆弧的圆半径值。<br>默认单位：vp。|

### func arcTo(Int64, Int64, Int64, Int64, Int64)

```cangjie
public func arcTo(x1: Int64, y1: Int64, x2: Int64, y2: Int64, radius: Int64): Unit
```

**功能：** 依据给定的控制点和圆弧半径创建圆弧路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x1|Int64|是|-|第一个控制点的x坐标值。<br>默认单位：vp。|
|y1|Int64|是|-|第一个控制点的y坐标值。<br>默认单位：vp。|
|x2|Int64|是|-|第二个控制点的x坐标值。<br>默认单位：vp。|
|y2|Int64|是|-|第二个控制点的y坐标值。<br>默认单位：vp。|
|radius|Int64|是|-|圆弧的圆半径值。<br>默认单位：vp。|

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
                    // 切线
                    offContext.beginPath()
                    offContext.strokeStyle(0x808080)
                    offContext.lineWidth(1.5)
                    offContext.moveTo(360, 20)
                    offContext.lineTo(360, 170)
                    offContext.lineTo(110, 170)
                    offContext.stroke()

                    // 圆弧
                    offContext.beginPath()
                    offContext.strokeStyle(0x000000)
                    offContext.lineWidth(3)
                    offContext.moveTo(360, 20)
                    offContext.arcTo(360, 170, 110, 170, 150)
                    offContext.stroke()

                    // 起始点
                    offContext.beginPath()
                    offContext.fillStyle(0x00ff00)
                    offContext.arc(360.0, 20.0, 4.0, 0.0, 6.28)
                    offContext.fill()

                    // 控制点
                    offContext.beginPath()
                    offContext.fillStyle(0xff0000)
                    offContext.arc(360.0, 170.0, 4.0, 0.0, 6.28)
                    offContext.arc(110.0, 170.0, 4.0, 0.0, 6.28)
                    offContext.fill()
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_7](figures/offscreenrenderingcontext_7.PNG)

此示例中，`arcTo()`创建的圆弧为黑色，圆弧的两条切线为灰色。控制点为红色，起始点为绿色。

可以想象两条切线：一条切线从起始点到第一个控制点，另一条切线从第一个控制点到第二个控制点。`arcTo()`在这两条切线间创建一个圆弧，并使圆弧与这两条切线都相切。