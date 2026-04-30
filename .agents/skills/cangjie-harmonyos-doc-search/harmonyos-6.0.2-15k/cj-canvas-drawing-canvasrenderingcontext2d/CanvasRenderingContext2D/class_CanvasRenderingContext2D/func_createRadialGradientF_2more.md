### func createRadialGradient(Float64, Float64, Float64, Float64, Float64, Float64)

```cangjie
public func createRadialGradient(x0: Float64, y0: Float64, r0: Float64, x1: Float64, y1: Float64, r1: Float64): CanvasGradient
```

**功能：** 创建一个径向渐变色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x0|Float64|是|-|起始圆的x轴坐标。<br>默认单位：vp。|
|y0|Float64|是|-|起始圆的y轴坐标。<br>默认单位：vp。|
|r0|Float64|是|-|起始圆的半径。必须是非负且有限的。<br>默认单位：vp。|
|x1|Float64|是|-|终点圆的x轴坐标。<br>默认单位：vp。|
|y1|Float64|是|-|终点圆的y轴坐标。<br>默认单位：vp。|
|r1|Float64|是|-|终点圆的半径。必须为非负且有限的。<br>默认单位：vp。|

**返回值：**

|类型|说明|
|:----|:----|
|[CanvasGradient](cj-canvas-drawing-canvasgradient.md#class-canvasgradient)|渐变对象。使用完毕后需要释放，详见[CanvasGradient](cj-canvas-drawing-canvasgradient.md#class-canvasgradient)。 |

### func createRadialGradient(Int64, Int64, Int64, Int64, Int64, Int64)

```cangjie
public func createRadialGradient(x0: Int64, y0: Int64, r0: Int64, x1: Int64, y1: Int64, r1: Int64): CanvasGradient
```

**功能：** 创建一个径向渐变色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x0|Int64|是|-|起始圆的x轴坐标。<br>默认单位：vp。|
|y0|Int64|是|-|起始圆的y轴坐标。<br>默认单位：vp。|
|r0|Int64|是|-|起始圆的半径。必须是非负且有限的。<br>默认单位：vp。|
|x1|Int64|是|-|终点圆的x轴坐标。<br>默认单位：vp。|
|y1|Int64|是|-|终点圆的y轴坐标。<br>默认单位：vp。|
|r1|Int64|是|-|终点圆的半径。必须为非负且有限的。<br>默认单位：vp。|

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

    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    let grad = this.context.createRadialGradient(200, 200, 50, 200, 200, 200)
                    grad.addColorStop(0.0, 0xff0000)
                    grad.addColorStop(0.5, 0xffffff)
                    grad.addColorStop(1.0, 0x00ff00)
                    this.context.fillStyle(grad)
                    this.context.fillRect(0, 0, 440, 440)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![createRadialGradient](./figures/canvasrenderingcontext_17.png)