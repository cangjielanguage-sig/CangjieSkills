### func globalCompositeOperation(CompositeOperation)

```cangjie
public func globalCompositeOperation(operation: CompositeOperation): Unit
```

**功能：** 设置合成操作的方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|operation|[CompositeOperation](./cj-common-types.md#enum-compositeoperation)|是|-|设置合成操作的方式。<br>初始值：SourceOver。|

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
                    offContext.fillStyle(0xff0000)
                    offContext.fillRect(20, 20, 50, 50)
                    offContext.globalCompositeOperation(CompositeOperation.SourceOver)
                    offContext.fillStyle(0x0000ff)
                    offContext.fillRect(50, 50, 50, 50)
                    offContext.fillStyle(0xff0000)
                    offContext.fillRect(120, 20, 50, 50)
                    offContext.globalCompositeOperation(CompositeOperation.DestinationOver)
                    offContext.fillStyle(0x0000ff)
                    offContext.fillRect(150, 50, 50, 50)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_31](figures/offscreenrenderingcontext_31.PNG)