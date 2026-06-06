### func strokeText(String, Int64, Int64, Int64)

```cangjie
public func strokeText(text: String, x: Int64, y: Int64, maxWidth: Int64): Unit
```

**功能：** 绘制描边类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-| 需要绘制的文本内容。|
|x|Int64|是|-|需要绘制的文本的左下角x坐标。<br>默认单位：vp。|
|y|Int64|是|-|需要绘制的文本的左下角y坐标。<br>默认单位：vp。|
|maxWidth|Int64|是|-|需要绘制的文本的最大宽度。<br>默认单位：vp。|

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
                    this.context.font(size: 50.px, family: "sans-serif")
                    this.context.fillText("Hello World!", 20, 100)
                    let withstr = "width:" + this.context.measureText("Hello World!").width.toString()
                    this.context.fillText(withstr, 20, 200)

                    this.context.font(size: 55.px, family: "sans-serif")
                    this.context.strokeText("Hello World!", 20, 300)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![strokeText](./figures/canvasrenderingcontext_22.png)

### func textAlign(TextAlignStyle)

```cangjie
public func textAlign(align: TextAlignStyle): Unit
```

**功能：** 设置文本绘制中的文本对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|align|[TextAlignStyle](./cj-common-types.md#enum-textalignstyle) |是|-| - Left：文本左对齐。<br>- Right：文本右对齐。<br>- Center：文本居中对齐。<br>- Start：文本对齐界线开始的地方。<br>- End：文本对齐界线结束的地方。<br>ltr布局模式下Start和Left一致，rtl布局模式下Start和Right一致。|

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
                    this.context.strokeStyle(0x0000ff)
                    this.context.moveTo(140, 10)
                    this.context.lineTo(140, 160)
                    this.context.stroke()
                    this.context.font(size: 18.px, family: "sans-serif")
                    this.context.textAlign(TextAlignStyle.Start)
                    this.context.fillText('textAlign=start', 140, 60)
                    this.context.textAlign(TextAlignStyle.End)
                    this.context.fillText('textAlign=end', 140, 80)
                    this.context.textAlign(TextAlignStyle.Left)
                    this.context.fillText('textAlign=left', 140, 100)
                    this.context.textAlign(TextAlignStyle.Center)
                    this.context.fillText('textAlign=center', 140, 120)
                    this.context.textAlign(TextAlignStyle.Right)
                    this.context.fillText('textAlign=right', 140, 140)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![textAlign](./figures/canvasrenderingcontext_46.png)