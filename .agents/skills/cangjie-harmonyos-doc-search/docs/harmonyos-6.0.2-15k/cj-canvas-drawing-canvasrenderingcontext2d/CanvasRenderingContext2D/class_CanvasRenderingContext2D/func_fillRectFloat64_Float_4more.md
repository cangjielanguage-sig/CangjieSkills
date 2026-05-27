### func fillRect(Float64, Float64, Float64, Float64)

```cangjie
public func fillRect(x: Float64, y: Float64, width: Float64, height: Float64): Unit
```

**功能：** 填充一个矩形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|指定矩形左上角点的x坐标。<br>默认单位：vp。|
|y|Float64|是|-|指定矩形左上角点的y坐标。<br>默认单位：vp。|
|width|Float64|是|-|指定矩形的宽度。<br>默认单位：vp。|
|height|Float64|是|-|指定矩形的高度。<br>默认单位：vp。|

### func fillRect(Int64, Int64, Int64, Int64)

```cangjie
public func fillRect(x: Int64, y: Int64, width: Int64, height: Int64): Unit
```

**功能：** 填充一个矩形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int64|是|-|指定矩形左上角点的x坐标。<br>默认单位：vp。|
|y|Int64|是|-|指定矩形左上角点的y坐标。<br>默认单位：vp。|
|width|Int64|是|-|指定矩形的宽度。<br>默认单位：vp。|
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
    private let contextPX: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings, LengthMetricsUnit.PX)
    private let contextVP: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings)
    @State
    var message: String = ""
    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.contextPX).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    this.contextPX.fillRect(10, 10, 100, 100)
                    this.contextPX.clearRect(10, 10, 50, 50)
                }
            )

            Canvas(this.contextVP).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    this.contextVP.fillRect(10, 10, 100, 100)
                    this.contextVP.clearRect(10, 10, 50, 50)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![fillRect](./figures/canvasrenderingcontext_53.png)

### func fillStyle(ResourceColor)

```cangjie
public func fillStyle(color: ResourceColor): Unit
```

**功能：** 指定绘制的填充色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|表示设置填充区域的颜色。|

### func fillStyle(CanvasGradient)

```cangjie
public func fillStyle(gradient: CanvasGradient): Unit
```

**功能：** 指定绘制的填充色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|gradient|[CanvasGradient](cj-canvas-drawing-canvasgradient.md#class-canvasgradient)|是|-|表示渐变对象，使用createLinearGradient方法创建。|