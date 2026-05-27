### func bezierCurveTo(Int64, Int64, Int64, Int64, Int64, Int64)

```cangjie
public func bezierCurveTo(cp1x: Int64, cp1y: Int64, cp2x: Int64, cp2y: Int64, x: Int64, y: Int64): Unit
```

**功能：** 创建三次贝赛尔曲线的路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cp1x|Int64|是|-|第一个贝塞尔参数的x坐标值。<br>默认单位：vp。|
|cp1y|Int64|是|-|第一个贝塞尔参数的y坐标值。<br>默认单位：vp。|
|cp2x|Int64|是|-|第二个贝塞尔参数的x坐标值。<br>默认单位：vp。|
|cp2y|Int64|是|-|第二个贝塞尔参数的y坐标值。<br>默认单位：vp。|
|x|Int64|是|-|路径结束时的x坐标值。<br>默认单位：vp。|
|y|Int64|是|-|路径结束时的y坐标值。<br>默认单位：vp。|

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
                    offContext.moveTo(10, 10)
                    offContext.bezierCurveTo(20, 100, 200, 100, 200, 20)
                    offContext.stroke()

                    offContext.beginPath()
                    offContext.moveTo(10, 20)
                    offContext.quadraticCurveTo(100, 100, 200, 20)
                    offContext.stroke()
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_8](figures/offscreenrenderingcontext_8.PNG)