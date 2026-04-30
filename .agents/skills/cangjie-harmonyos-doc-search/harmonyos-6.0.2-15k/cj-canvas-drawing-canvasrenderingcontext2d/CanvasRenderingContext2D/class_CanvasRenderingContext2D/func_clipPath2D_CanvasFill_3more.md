### func clip(Path2D, CanvasFillRule)

```cangjie
public func clip(path2D: Path2D, fillRule!: CanvasFillRule = CanvasFillRule.nonzero): Unit
```

**功能：** 设置当前路径为剪切路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path2D|[Path2D](./cj-canvas-drawing-path2d.md#class-path2d)|是|-|Path2D剪切路径。|
|fillRule|[CanvasFillRule](./cj-common-types.md#enum-canvasfillrule)|否|CanvasFillRule.nonzero| **命名参数。** 指定要剪切对象的规则。<br/>可选参数为：nonzero, evenodd。|

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
    var message: String = ""
    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    let region = Path2D()
                    region.moveTo(30, 90)
                    region.lineTo(110, 20)
                    region.lineTo(240, 130)
                    region.lineTo(60, 130)
                    region.lineTo(190, 20)
                    region.lineTo(270, 90)
                    region.closePath()
                    region.closePath()
                    this.context.clip(region, fillRule: CanvasFillRule.evenodd)
                    this.context.fillStyle(0x00ff00)
                    this.context.fillRect(0.0, 0.0, this.context.width(), this.context.height())
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![clip](./figures/canvasrenderingcontext_11.png)

### func closePath()

```cangjie
public func closePath(): Unit
```

**功能：** 结束当前路径形成一个封闭路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**示例：**

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    var settings: RenderingContextSettings = RenderingContextSettings(antialias: true)
    var context: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings)

    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    this.context.beginPath()
                    this.context.moveTo(30, 30)
                    this.context.lineTo(110, 30)
                    this.context.lineTo(70, 90)
                    this.context.closePath()
                    this.context.stroke()
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![closePath](./figures/canvasrenderingcontext_12.png)

### func createConicGradient(Float64, Float64, Float64)

```cangjie
public func createConicGradient(startAngle: Float64, x: Float64, y: Float64): CanvasGradient
```

**功能：** 创建一个圆锥渐变色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|startAngle|Float64|是|-|开始渐变的角度。角度测量从中心右侧水平开始，顺时针移动。<br>单位：弧度。|
|x|Float64|是|-|圆锥渐变的中心x轴坐标。<br>默认单位：vp。|
|y|Float64|是|-|圆锥渐变的中心y轴坐标。<br>默认单位：vp。|

**返回值：**

|类型|说明|
|:----|:----|
|[CanvasGradient](cj-canvas-drawing-canvasgradient.md#class-canvasgradient)|新的CanvasGradient对象，用于在canvas上创建渐变效果。|