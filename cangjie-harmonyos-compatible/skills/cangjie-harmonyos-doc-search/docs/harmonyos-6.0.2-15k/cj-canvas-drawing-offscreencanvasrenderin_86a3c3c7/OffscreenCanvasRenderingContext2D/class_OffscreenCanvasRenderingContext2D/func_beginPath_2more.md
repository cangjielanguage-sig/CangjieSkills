### func beginPath()

```cangjie
public func beginPath(): Unit
```

**功能：** 创建一个新的绘制路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

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
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xD5D5D5).onReady(
                {
                    =>
                    let offContext = this.offCanvas.getContext(contextType: ContextType.type_2d, options: this.settings)
                    offContext.beginPath()
                    offContext.lineWidth(6)
                    offContext.strokeStyle(0x0000ff)
                    offContext.moveTo(15, 80)
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

![offscreencanvasrenderingcontext2d_beginpath](./figures/offscreencanvasrenderingcontext2d_beginpath.jpg)

### func bezierCurveTo(Float64, Float64, Float64, Float64, Float64, Float64)

```cangjie
public func bezierCurveTo(cp1x: Float64, cp1y: Float64, cp2x: Float64, cp2y: Float64, x: Float64, y: Float64): Unit
```

**功能：** 创建三次贝赛尔曲线的路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cp1x|Float64|是|-|第一个贝塞尔参数的x坐标值。<br>默认单位：vp。|
|cp1y|Float64|是|-|第一个贝塞尔参数的y坐标值。<br>默认单位：vp。|
|cp2x|Float64|是|-|第二个贝塞尔参数的x坐标值。<br>默认单位：vp。|
|cp2y|Float64|是|-|第二个贝塞尔参数的y坐标值。<br>默认单位：vp。|
|x|Float64|是|-|路径结束时的x坐标值。<br>默认单位：vp。|
|y|Float64|是|-|路径结束时的y坐标值。<br>默认单位：vp。|