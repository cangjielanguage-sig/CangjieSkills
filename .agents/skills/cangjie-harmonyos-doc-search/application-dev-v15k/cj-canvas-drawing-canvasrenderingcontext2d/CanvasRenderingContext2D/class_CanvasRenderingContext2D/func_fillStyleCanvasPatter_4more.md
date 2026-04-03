### func fillStyle(CanvasPattern)

```cangjie
public func fillStyle(pattern: CanvasPattern): Unit
```

**功能：** 指定绘制的填充色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pattern|[CanvasPattern](./cj-canvas-drawing-canvaspattern.md#class-canvaspattern)|是|-|通过指定图像和重复方式创建图片填充的模板对象。|

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
                    this.context.fillStyle(0x0000ff)
                    this.context.fillRect(20, 20, 150, 100)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![fillStyle](figures/fillStyle.png)

### func fillText(String, Float64, Float64)

```cangjie
public func fillText(text: String, x: Float64, y: Float64): Unit
```

**功能：** 绘制填充类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|需要绘制的文本内容。|
|x|Float64|是|-|需要绘制的文本的左下角x坐标。<br>默认单位：vp。|
|y|Float64|是|-|需要绘制的文本的左下角y坐标。<br>默认单位：vp。|

### func fillText(String, Int64, Int64)

```cangjie
public func fillText(text: String, x: Int64, y: Int64): Unit
```

**功能：** 绘制填充类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|需要绘制的文本内容。|
|x|Int64|是|-|需要绘制的文本的左下角x坐标。<br>默认单位：vp。|
|y|Int64|是|-|需要绘制的文本的左下角y坐标。<br>默认单位：vp。|

### func fillText(String, Float64, Float64, Float64)

```cangjie
public func fillText(text: String, x: Float64, y: Float64, maxWidth: Float64): Unit
```

**功能：** 绘制填充类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|需要绘制的文本内容。|
|x|Float64|是|-|需要绘制的文本的左下角x坐标。<br>默认单位：vp。|
|y|Float64|是|-|需要绘制的文本的左下角y坐标。<br>默认单位：vp。|
|maxWidth|Float64|是|-|指定文本允许的最大宽度。<br>默认单位：vp。<br>初始值：不限制宽度。|