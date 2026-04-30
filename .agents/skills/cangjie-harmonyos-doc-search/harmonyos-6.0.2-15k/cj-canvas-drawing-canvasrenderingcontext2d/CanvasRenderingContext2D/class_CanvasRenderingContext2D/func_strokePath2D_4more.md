### func stroke(Path2D)

```cangjie
public func stroke(path2D: Path2D): Unit
```

**功能：** 进行边框绘制操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path2D|[Path2D](./cj-canvas-drawing-path2d.md#class-path2d)|是|-| 需要绘制的Path2D。|

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
    private var path2Da: Path2D = Path2D()
    @State
    var message: String = ""
    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    this.path2Da.moveTo(25, 25)
                    this.path2Da.lineTo(25, 105)
                    this.path2Da.lineTo(75, 105)
                    this.path2Da.lineTo(75, 25)
                    this.context.strokeStyle(0xff0000)
                    this.context.stroke(this.path2Da)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![stroke2](./figures/canvasrenderingcontext_45.png)

### func strokeRect(Float64, Float64, Float64, Float64)

```cangjie
public func strokeRect(x: Float64, y: Float64, width: Float64, height: Float64): Unit
```

**功能：** 绘制具有边框的矩形，矩形内部不填充。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|指定矩形左上角点的x坐标。<br>默认单位：vp。|
|y|Float64|是|-|指定矩形左上角点的y坐标。<br>默认单位：vp。|
|width|Float64|是|-|指定矩形的宽度。<br>默认单位：vp。|
|height|Float64|是|-|指定矩形的高度。<br>默认单位：vp。|

### func strokeRect(Int64, Int64, Int64, Int64)

```cangjie
public func strokeRect(x: Int64, y: Int64, width: Int64, height: Int64): Unit
```

**功能：** 绘制具有边框的矩形，矩形内部不填充。

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
    private let context: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings)
    @State
    var message: String = ""
    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    this.context.lineWidth(5)
                    this.context.strokeRect(25, 25, 85, 105)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![strokeRect](./figures/canvasrenderingcontext_2.png)

### func strokeStyle(ResourceColor)

```cangjie
public func strokeStyle(color: ResourceColor): Unit
```

**功能：** 设置描边的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|表示设置填充区域的颜色。|