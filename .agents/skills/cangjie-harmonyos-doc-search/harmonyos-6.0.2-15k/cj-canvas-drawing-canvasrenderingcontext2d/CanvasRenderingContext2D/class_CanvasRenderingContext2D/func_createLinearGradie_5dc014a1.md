### func createLinearGradient(Int64, Int64, Int64, Int64)

```cangjie
public func createLinearGradient(x0: Int64, y0: Int64, x1: Int64, y1: Int64): CanvasGradient
```

**功能：** 创建一个线性渐变色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x0|Int64|是|-|起点的x轴坐标。<br>默认单位：vp。|
|y0|Int64|是|-|起点的y轴坐标。<br>默认单位：vp。|
|x1|Int64|是|-|终点的x轴坐标。<br>默认单位：vp。|
|y1|Int64|是|-|终点的y轴坐标。<br>默认单位：vp。|

**返回值：**

|类型|说明|
|:----|:----|
|[CanvasGradient](cj-canvas-drawing-canvasgradient.md#class-canvasgradient)| 渐变对象。使用完毕后需要释放，详见[CanvasGradient](cj-canvas-drawing-canvasgradient.md#class-canvasgradient)。|

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
                    let grad = this.context.createLinearGradient(50, 0, 300, 100)
                    grad.addColorStop(0.0, 0xff0000)
                    grad.addColorStop(0.5, 0xffffff)
                    grad.addColorStop(1.0, 0x00ff00)
                    this.context.fillStyle(grad)
                    this.context.fillRect(0, 0, 400, 400)
                }
            )
            Text(this.toDataUrl)
        }.width(100.percent).height(100.percent)
    }
}
```

![createLinearGradient](./figures/canvasrenderingcontext_15.png)