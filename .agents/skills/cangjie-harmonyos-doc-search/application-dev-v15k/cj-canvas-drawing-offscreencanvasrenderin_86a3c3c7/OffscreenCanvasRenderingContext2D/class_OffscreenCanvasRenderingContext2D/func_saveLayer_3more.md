### func saveLayer()

```cangjie
public func saveLayer(): Unit
```

**功能：** 创建一个图层。

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
                    offContext.fillStyle(0x0000ff)
                    offContext.fillRect(50, 100, 300, 100)
                    offContext.fillStyle(0x00ffff)
                    offContext.fillRect(50, 150, 300, 100)
                    offContext.globalCompositeOperation(CompositeOperation.DestinationOver)
                    offContext.saveLayer()
                    offContext.globalCompositeOperation(CompositeOperation.SourceOver)
                    offContext.fillStyle(0xff0000)
                    offContext.fillRect(100, 50, 100, 300)
                    offContext.fillStyle(0x00ff00)
                    offContext.fillRect(150, 50, 100, 300)
                    offContext.restoreLayer()
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_40](figures/offscreenrenderingcontext_40.PNG)

### func scale(Float64, Float64)

```cangjie
public func scale(x: Float64, y: Float64): Unit
```

**功能：** 设置canvas画布的缩放变换属性，后续的绘制操作将按照缩放比例进行缩放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|水平方向的缩放值。|
|y|Float64|是|-|垂直方向的缩放值。|

### func scale(Int64, Int64)

```cangjie
public func scale(x: Int64, y: Int64): Unit
```

**功能：** 设置canvas画布的缩放变换属性，后续的绘制操作将按照缩放比例进行缩放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int64|是|-|水平方向的缩放值。|
|y|Int64|是|-|垂直方向的缩放值。|

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
                    offContext.lineWidth(3)
                    offContext.strokeRect(30, 30, 50, 50)
                    offContext.scale(2, 2) // Scale to 200%
                    offContext.strokeRect(30, 30, 50, 50)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_41](figures/offscreenrenderingcontext_41.PNG)