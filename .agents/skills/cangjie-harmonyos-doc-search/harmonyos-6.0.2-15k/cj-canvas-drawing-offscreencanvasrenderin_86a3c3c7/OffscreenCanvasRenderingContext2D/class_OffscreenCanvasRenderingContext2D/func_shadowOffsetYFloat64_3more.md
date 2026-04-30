### func shadowOffsetY(Float64)

```cangjie
public func shadowOffsetY(offset: Float64): Unit
```

**功能：** 设置绘制阴影时和原有对象的垂直偏移值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Float64|是|-|设置绘制阴影时和原有对象的垂直偏移值。<br>初始值：0.0。|

### func shadowOffsetY(Int64)

```cangjie
public func shadowOffsetY(offset: Int64): Unit
```

**功能：** 设置绘制阴影时和原有对象的垂直偏移值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Int64|是|-|设置绘制阴影时和原有对象的垂直偏移值。<br>初始值：0。|

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
                    offContext.shadowBlur(30)
                    offContext.shadowColor(0x0000ff)
                    offContext.shadowOffsetY(20)
                    offContext.shadowOffsetX(20)
                    offContext.fillStyle(0xff0000)
                    offContext.fillRect(20, 20, 100, 80)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_43](figures/offscreenrenderingcontext_43.PNG)

### func stroke()

```cangjie
public func stroke(): Unit
```

**功能：** 根据当前的路径，进行边框绘制操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

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
                    offContext.moveTo(125, 25)
                    offContext.lineTo(125, 105)
                    offContext.lineTo(175, 105)
                    offContext.lineTo(175, 25)
                    offContext.strokeStyle(0xff0000)
                    offContext.stroke()
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_44](figures/offscreenrenderingcontext_44.PNG)