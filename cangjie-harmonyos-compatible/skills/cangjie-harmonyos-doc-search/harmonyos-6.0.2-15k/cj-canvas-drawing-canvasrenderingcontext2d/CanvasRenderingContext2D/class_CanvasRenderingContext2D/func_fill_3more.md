### func fill()

```cangjie
public func fill(): Unit
```

**功能：** 对封闭路径进行填充。

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
                    this.context.rect(0, 30, 100, 100)
                    this.context.fill()
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![canvas](figures/canvas.png)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

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
|fillRule|[CanvasFillRule](./cj-common-types.md#enum-canvasfillrule)|是|-| 指定要剪切对象的规则。<br/>可选参数为：nonzero, evenodd。<br>初始值：nonzero。|

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
                    this.context.rect(0, 30, 100, 100)
                    this.context.fill()
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![canvas](figures/canvas.png)

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
|path2D|[Path2D](./cj-canvas-drawing-path2d.md#class-path2d)|是|-| Path2D剪切路径。|
|fillRule|[CanvasFillRule](./cj-common-types.md#enum-canvasfillrule)|否|CanvasFillRule.nonzero| **命名参数。**  指定要剪切对象的规则。<br/>可选参数为：nonzero, evenodd。|

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
                    // Fill path
                    this.context.fillStyle(0x00ff00)
                    this.context.fill(region, fillRule: CanvasFillRule.evenodd)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![canvas](./figures/canvasrenderingcontext_11.png)