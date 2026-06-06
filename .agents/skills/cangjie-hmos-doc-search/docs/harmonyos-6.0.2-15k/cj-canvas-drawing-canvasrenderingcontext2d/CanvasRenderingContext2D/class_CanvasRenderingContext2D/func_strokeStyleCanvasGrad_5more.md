### func strokeStyle(CanvasGradient)

```cangjie
public func strokeStyle(gradient: CanvasGradient): Unit
```

**功能：** 设置描边的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|gradient|[CanvasGradient](cj-canvas-drawing-canvasgradient.md#class-canvasgradient)|是|-|表示渐变对象，使用createLinearGradient方法创建。|

### func strokeStyle(CanvasPattern)

```cangjie
public func strokeStyle(pattern: CanvasPattern): Unit
```

**功能：** 设置绘制线条的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pattern|[CanvasPattern](./cj-canvas-drawing-canvaspattern.md#class-canvaspattern)|是|-|定图像和重复方式创建图片填充的模板，使用createPattern方法创建。|

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
                    this.context.lineWidth(10)
                    this.context.strokeStyle(0x0000ff)
                    this.context.strokeRect(25, 25, 155, 105)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![strokeStyle](./figures/canvasrenderingcontext_3.png)

### func strokeText(String, Float64, Float64)

```cangjie
public func strokeText(text: String, x: Float64, y: Float64): Unit
```

**功能：** 绘制描边类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|需要绘制的文本内容。|
|x|Float64|是|-|需要绘制的文本的左下角x坐标。<br>默认单位：vp。|
|y|Float64|是|-|需要绘制的文本的左下角y坐标。<br>默认单位：vp。|

### func strokeText(String, Int64, Int64)

```cangjie
public func strokeText(text: String, x: Int64, y: Int64): Unit
```

**功能：** 绘制描边类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|需要绘制的文本内容。|
|x|Int64|是|-|需要绘制的文本的左下角x坐标。<br>默认单位：vp。|
|y|Int64|是|-|需要绘制的文本的左下角y坐标。<br>默认单位：vp。|

### func strokeText(String, Float64, Float64, Float64)

```cangjie
public func strokeText(text: String, x: Float64, y: Float64, maxWidth: Float64): Unit
```

**功能：** 绘制描边类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-| 需要绘制的文本内容。|
|x|Float64|是|-|需要绘制的文本的左下角x坐标。<br>默认单位：vp。|
|y|Float64|是|-|需要绘制的文本的左下角y坐标。<br>默认单位：vp。|
|maxWidth|Float64|是|-|需要绘制的文本的最大宽度。<br>默认单位：vp。|