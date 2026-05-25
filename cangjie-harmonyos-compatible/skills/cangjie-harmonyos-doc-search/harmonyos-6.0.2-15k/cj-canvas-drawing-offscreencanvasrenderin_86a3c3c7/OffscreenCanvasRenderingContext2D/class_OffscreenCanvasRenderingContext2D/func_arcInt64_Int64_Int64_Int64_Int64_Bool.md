### func arc(Int64, Int64, Int64, Int64, Int64, Bool)

```cangjie
public func arc(x: Int64, y: Int64, radius: Int64, startAngle: Int64, endAngle: Int64, anticlockwise!: Bool = false): Unit
```

**功能：** 绘制弧线路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int64|是|-|弧线圆心的x坐标值。</br>默认单位：vp。|
|y|Int64|是|-|弧线圆心的y坐标值。</br>默认单位：vp。|
|radius|Int64|是|-|弧线的圆半径。<br>默认单位：vp。|
|startAngle|Int64|是|-|弧线的起始弧度。<br>单位：弧度。|
|endAngle|Int64|是|-|弧线的终止弧度。<br>单位：弧度。|
|anticlockwise|Bool|否|false| **命名参数。** 是否逆时针绘制圆弧。<br>true:逆时针方向绘制椭圆。<br>false:顺时针方向绘制椭圆。|

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
                    offContext.arc(100.0, 75.0, 50.0, 0.0, 6.28)
                    offContext.lineDash([10, 20])
                    offContext.lineDashOffset(10.0)
                    offContext.stroke()
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_6](figures/offscreenrenderingcontext_6.PNG)