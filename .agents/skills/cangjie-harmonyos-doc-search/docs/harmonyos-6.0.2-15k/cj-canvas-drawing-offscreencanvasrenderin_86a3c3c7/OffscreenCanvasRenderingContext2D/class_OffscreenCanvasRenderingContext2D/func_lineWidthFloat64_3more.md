### func lineWidth(Float64)

```cangjie
public func lineWidth(width: Float64): Unit
```

**功能：** 设置绘制线条的宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|Float64|是|-|设置绘制线条的宽度。</br>初始值：1.px。</br>默认单位：vp。</br>linewidth取值不支持0和负数，0和负数按异常值处理，异常值按默认值处理。|

### func lineWidth(Int64)

```cangjie
public func lineWidth(width: Int64): Unit
```

**功能：** 设置绘制线条的宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|Int64|是|-|设置绘制线条的宽度。</br>初始值：1.px。</br>默认单位：vp。</br>linewidth取值不支持0和负数，0和负数按异常值处理，异常值按默认值处理。|

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
                    offContext.lineWidth(5)
                    offContext.strokeRect(25, 25, 85, 105)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_2](figures/offscreenrenderingcontext_2.PNG)

### func measureText(String)

```cangjie
public func measureText(text: String): TextMetrics
```

**功能：** 该方法返回一个文本测算的对象，通过该对象可以获取指定文本的宽度值。不同设备上获取的宽度值可能不同。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|需要进行测量的文本。|

**返回值：**

|类型|说明|
|:----|:----|
|[TextMetrics](./cj-canvas-drawing-canvasrenderingcontext2d.md#struct-textmetrics)|文本的尺寸信息。|

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

    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    let offContext = this.offCanvas.getContext(contextType: ContextType.type_2d, options: this.settings)
                    offContext.font(size: 55.px, family: 'sans-serif')
                    offContext.strokeText("Hello World!", 20, 60)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreencanvasrenderingcontext2d_stroketext](./figures/offscreencanvasrenderingcontext2d_stroketext.png)