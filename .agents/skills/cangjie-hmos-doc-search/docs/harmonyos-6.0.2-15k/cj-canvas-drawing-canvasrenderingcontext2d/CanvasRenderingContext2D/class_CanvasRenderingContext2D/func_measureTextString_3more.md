### func measureText(String)

```cangjie
public func measureText(text: String): TextMetrics
```

**功能：** 该方法返回一个文本测算的对象，通过该对象可以获取指定文本的宽度值。不同设备上获取的宽度值可能不同。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|需要进行测量的文本。|

**返回值：**

|类型|说明|
|:----|:----|
|[TextMetrics](#struct-textmetrics)|文本的尺寸信息 |

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
                    this.context.font(size: 85.px, family: "sans-serif")
                    this.context.fillText("Hello World!", 20, 100)
                    this.context.fillText("width: ${this.context.measureText("Hello World!").width}", 20, 200)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![measureText](figures/measureText.png)

### func miterLimit(Float64)

```cangjie
public func miterLimit(limit: Float64): Unit
```

**功能：** 设置斜接面限制值，该值指定了线条相交处内角和外角的距离。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|limit|Float64|是|-|设置斜接面限制值，该值指定了线条相交处内角和外角的距离。<br>初始值：10.px。 <br>默认单位：px。 <br>miterLimit取值不支持0和负数，0和负数按异常值处理，异常值按默认值处理。|

### func miterLimit(Int64)

```cangjie
public func miterLimit(limit: Int64): Unit
```

**功能：** 设置斜接面限制值，该值指定了线条相交处内角和外角的距离。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|limit|Int64|是|-|设置斜接面限制值，该值指定了线条相交处内角和外角的距离。<br>初始值：10.px。 <br>单位：px。 <br>miterLimit取值不支持0和负数，0和负数按异常值处理，异常值按默认值处理。|

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

![miterLimit](./figures/canvasrenderingcontext_35.png)