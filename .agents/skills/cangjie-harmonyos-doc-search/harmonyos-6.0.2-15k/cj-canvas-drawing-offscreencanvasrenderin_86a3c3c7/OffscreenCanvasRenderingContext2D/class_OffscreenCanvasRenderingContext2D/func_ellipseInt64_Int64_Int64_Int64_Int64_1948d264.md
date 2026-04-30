### func ellipse(Int64, Int64, Int64, Int64, Int64, Int64, Int64, Bool)

```cangjie
public func ellipse(
    x: Int64,
    y: Int64,
    radiusX: Int64,
    radiusY: Int64,
    rotation: Int64,
    startAngle: Int64,
    endAngle: Int64,
    anticlockwise!: Bool = false
): Unit
```

**功能：** 在规定的矩形区域绘制一个椭圆。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int64|是|-|椭圆圆心的x轴坐标。<br>默认单位：vp。 |
|y|Int64|是|-|椭圆圆心的y轴坐标。<br>默认单位：vp。 |
|radiusX|Int64|是|-|椭圆x轴的半径长度。<br>默认单位：vp。|
|radiusY|Int64|是|-|椭圆y轴的半径长度。<br>默认单位：vp。|
|rotation|Int64|是|-|椭圆的旋转角度。<br>单位：弧度。|
|startAngle|Int64|是|-|椭圆绘制的起始点角度。<br>单位：弧度。|
|endAngle  |Int64|是|-|椭圆绘制的结束点角度。<br>单位：弧度。|
|anticlockwise|Bool|否|false| **命名参数。**  是否以逆时针方向绘制椭圆。<br>true：逆时针方向绘制椭圆。<br>false：顺时针方向绘制椭圆。|

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
                    offContext.beginPath()
                    offContext.ellipse(200.0, 200.0, 50.0, 100.0, 3.14 * 0.25, 3.14 * 0.5, 3.14 * 2.0,
                        anticlockwise: false)
                    offContext.stroke()
                    offContext.beginPath()
                    offContext.ellipse(200.0, 300.0, 50.0, 100.0, 3.14 * 0.25, 3.14 * 0.5, 3.14 * 2.0,
                        anticlockwise: true)
                    offContext.stroke()
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_20](figures/offscreenrenderingcontext_20.PNG)