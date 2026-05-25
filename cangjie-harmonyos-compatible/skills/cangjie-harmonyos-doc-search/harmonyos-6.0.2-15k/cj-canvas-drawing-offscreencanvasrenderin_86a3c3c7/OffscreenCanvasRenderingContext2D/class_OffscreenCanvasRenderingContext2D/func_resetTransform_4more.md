### func resetTransform()

```cangjie
public func resetTransform(): Unit
```

**功能：** 使用单位矩阵重新设置当前矩阵。

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
                    offContext.setTransform(1.0, -0.5, 0.5, 1.0, 10.0, 10.0)
                    offContext.fillStyle(0x0000ff)
                    offContext.fillRect(0, 0, 100, 100)
                    offContext.resetTransform()
                    offContext.fillStyle(0xff0000)
                    offContext.fillRect(0, 0, 100, 100)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_37](figures/offscreenrenderingcontext_37.PNG)

### func restore()

```cangjie
public func restore(): Unit
```

**功能：** 对保存的绘图上下文进行恢复。

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
    var toDataUrl: String = ""

    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    let offContext = this.offCanvas.getContext(contextType: ContextType.type_2d, options: this.settings)
                    offContext.save() // save the default state
                    offContext.fillStyle(0x00ff00)
                    offContext.fillRect(20, 20, 100, 100)
                    offContext.restore() // restore to the default state
                    offContext.fillRect(150, 75, 100, 100)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
            Text(this.toDataUrl)
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_38](figures/offscreenrenderingcontext_38.PNG)

### func restoreLayer()

```cangjie
public func restoreLayer(): Unit
```

**功能：** 恢复图像变换和裁剪状态至saveLayer前的状态，并将图层绘制在canvas上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### func rotate(Float64)

```cangjie
public func rotate(angle: Float64): Unit
```

**功能：** 针对当前坐标轴进行顺时针旋转。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|angle|Float64|是|-|设置顺时针旋转的弧度值。<br>单位：弧度。|