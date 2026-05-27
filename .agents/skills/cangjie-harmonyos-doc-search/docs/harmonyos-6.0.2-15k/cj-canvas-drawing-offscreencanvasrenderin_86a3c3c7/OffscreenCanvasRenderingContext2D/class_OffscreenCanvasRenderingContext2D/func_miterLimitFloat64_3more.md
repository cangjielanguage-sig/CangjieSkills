### func miterLimit(Float64)

```cangjie
public func miterLimit(limit: Float64): Unit
```

**功能：** 设置斜接面限制值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|limit|Float64|是|-|指定了线条相交处内角和外角的距离。 <br/>初始值：10.px。<br/>miterLimit取值不支持0和负数，0和负数按异常值处理，异常值按默认值处理。|

### func miterLimit(Int64)

```cangjie
public func miterLimit(limit: Int64): Unit
```

**功能：** 设置斜接面限制值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|limit|Int64|是|-|指定了线条相交处内角和外角的距离。<br/>初始值：10.px。<br/>miterLimit取值不支持0和负数，0和负数按异常值处理，异常值按默认值处理。|

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
                    offContext.lineWidth(8)
                    offContext.lineJoin(LineJoinStyle.Miter)
                    offContext.miterLimit(3)
                    offContext.moveTo(30, 30)
                    offContext.lineTo(60, 35)
                    offContext.lineTo(30, 37)
                    offContext.stroke()
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_35](figures/offscreenrenderingcontext_35.PNG)

### func moveTo(Float64, Float64)

```cangjie
public func moveTo(x: Float64, y: Float64): Unit
```

**功能：** 路径从当前点移动到指定点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|指定位置的x坐标。<br>默认单位：vp。|
|y|Float64|是|-|指定位置的y坐标。<br>默认单位：vp。|