### func fill()

```cangjie
public func fill(): Unit
```

**功能：** 对封闭路径进行填充。

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
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    let offContext = this.offCanvas.getContext(contextType: ContextType.type_2d, options: this.settings)
                    offContext.rect(20, 20, 100, 100) // Create a 100*100 rectangle at (20, 20)
                    offContext.fill()
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_21](figures/offscreenrenderingcontext_21.PNG)

### func fill(CanvasFillRule)

```cangjie
public func fill(fillRule: CanvasFillRule): Unit
```

**功能：** 对封闭路径进行填充。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fillRule|[CanvasFillRule](./cj-common-types.md#enum-canvasfillrule)|是|-|指定要填充对象的规则。<br/>可选参数为：nonzero, evenodd。<br/>初始值：nonzero。|

### func fill(Path2D, CanvasFillRule)

```cangjie
public func fill(path2D: Path2D, fillRule!: CanvasFillRule = CanvasFillRule.nonzero): Unit
```

**功能：** 对封闭路径进行填充。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path2D|[Path2D](./cj-canvas-drawing-path2d.md#class-path2d)|是|-|Path2D填充路径。|
|fillRule|[CanvasFillRule](./cj-common-types.md#enum-canvasfillrule)|否|CanvasFillRule.nonzero| **命名参数。** 指定要填充对象的规则。<br/>可选参数为：nonzero, evenodd。<br/>初始值：nonzero。|

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
                    let region = Path2D()
                    region.moveTo(30, 90)
                    region.lineTo(110, 20)
                    region.lineTo(240, 130)
                    region.lineTo(60, 130)
                    region.lineTo(190, 20)
                    region.lineTo(270, 90)
                    region.closePath()
                    // Fill path
                    offContext.fillStyle(0x00ff00)
                    offContext.fill(region, fillRule: CanvasFillRule.evenodd)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_22](figures/offscreenrenderingcontext_22.PNG)