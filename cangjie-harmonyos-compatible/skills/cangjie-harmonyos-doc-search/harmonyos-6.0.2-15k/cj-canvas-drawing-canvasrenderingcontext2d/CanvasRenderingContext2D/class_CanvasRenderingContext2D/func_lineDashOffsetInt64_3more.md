### func lineDashOffset(Int64)

```cangjie
public func lineDashOffset(offset: Int64): Unit
```

**功能：** 设置画布的虚线偏移量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Int64|是|-|设置画布的虚线偏移量。<br>初始值：0。 <br>默认单位：vp。|

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
                    this.context.arc(100.0, 75.0, 50.0, 0.0, 6.28)
                    this.context.lineDash([10, 20])
                    this.context.lineDashOffset(10.0)
                    this.context.stroke()
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![lineDashOffset](./figures/canvasrenderingcontext_6.png)

### func lineJoin(LineJoinStyle)

```cangjie
public func lineJoin(value: LineJoinStyle): Unit
```

**功能：** 指定线段间相交的交点样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[LineJoinStyle](./cj-common-types.md#enum-linejoinstyle) |是|-|- Round：在线段相连处绘制一个扇形，扇形的圆角半径是线段的宽度。<br>- Bevel：在线段相连处使用三角形为底填充， 每个部分矩形拐角独立。<br>- Miter：在相连部分的外边缘处进行延伸，使其相交于一点，形成一个菱形区域，该属性可以通过设置miterLimit属性展现效果。|

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
                    this.context.beginPath()
                    this.context.lineWidth(8)
                    this.context.lineJoin(LineJoinStyle.Miter)
                    this.context.moveTo(30, 30)
                    this.context.lineTo(120, 60)
                    this.context.lineTo(30, 110)
                    this.context.stroke()
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![lineJoin](./figures/canvasrenderingcontext_5.png)

### func lineTo(Float64, Float64)

```cangjie
public func lineTo(x: Float64, y: Float64): Unit
```

**功能：** 从当前点到指定点进行路径连接。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|指定位置的x坐标。<br>默认单位：vp。|
|y|Float64|是|-|指定位置的y坐标。<br>默认单位：vp。|