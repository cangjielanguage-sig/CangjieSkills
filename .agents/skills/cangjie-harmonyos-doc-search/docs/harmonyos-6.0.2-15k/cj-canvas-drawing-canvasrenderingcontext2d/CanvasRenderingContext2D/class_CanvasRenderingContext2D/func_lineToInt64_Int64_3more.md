### func lineTo(Int64, Int64)

```cangjie
public func lineTo(x: Int64, y: Int64): Unit
```

**功能：** 从当前点到指定点进行路径连接。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int64|是|-|指定位置的x坐标。<br>默认单位：vp。|
|y|Int64|是|-|指定位置的y坐标。<br>默认单位：vp。|

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
                    this.context.lineWidth(8)
                    this.context.lineJoin(LineJoinStyle.Miter)
                    this.context.miterLimit(3)
                    this.context.moveTo(30, 30)
                    this.context.lineTo(60, 35)
                    this.context.lineTo(30, 37)
                    this.context.stroke()
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![lineTo](./figures/canvasrenderingcontext_35.png)

### func lineWidth(Float64)

```cangjie
public func lineWidth(width: Float64): Unit
```

**功能：** 设置绘制线条的宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|Float64|是|-|设置绘制线条的宽度。<br> 初始值：1.px。 <br>默认单位：vp。 <br>linewidth取值不支持0和负数，0和负数按异常值处理，异常值按默认值处理。|

### func lineWidth(Int64)

```cangjie
public func lineWidth(width: Int64): Unit
```

**功能：** 设置绘制线条的宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|Int64|是|-|设置绘制线条的宽度。<br> 初始值：1.px。 <br>默认单位：vp。 <br>linewidth取值不支持0和负数，0和负数按异常值处理，异常值按默认值处理。|

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

![lineWidth](./figures/canvasrenderingcontext_2.png)