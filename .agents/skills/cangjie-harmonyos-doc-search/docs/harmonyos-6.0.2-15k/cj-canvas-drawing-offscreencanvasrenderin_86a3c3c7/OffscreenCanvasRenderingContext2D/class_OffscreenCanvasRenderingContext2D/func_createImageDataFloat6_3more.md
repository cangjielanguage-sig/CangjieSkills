### func createImageData(Float64, Float64)

```cangjie
public func createImageData(sw: Float64, sh: Float64): ImageData
```

**功能：** 创建新的、空白的、指定大小的ImageData对象，请参考[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sw|Float64|是|-|ImageData的宽度。<br>默认单位：vp。|
|sh|Float64|是|-|ImageData的高度。<br>默认单位：vp。|

**返回值：**

|类型|说明|
|:----|:----|
|[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)|新的ImageData对象。|

### func createImageData(Int64, Int64)

```cangjie
public func createImageData(sw: Int64, sh: Int64): ImageData
```

**功能：** 创建新的、空白的、指定大小的ImageData 对象，请参考[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sw|Int64|是|-|ImageData的宽度。<br>默认单位：vp。|
|sh|Int64|是|-|ImageData的高度。<br>默认单位：vp。|

**返回值：**

|类型|说明|
|:----|:----|
|[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)|新的ImageData对象。|

### func createImageData(ImageData)

```cangjie
public func createImageData(imageData: ImageData): ImageData
```

**功能：** 创建新的、空白的、指定大小的ImageData 对象，请参考[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|imageData|[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)|是|-|现有的ImageData对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)|新的ImageData对象。|

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
                    let imageDataNum = offContext.createImageData(100.0, 100.0)
                    var s = imageDataNum.data
                    for (i in 0..s.size where i % 4 == 0) {
                        s[i + 0] = 255
                        s[i + 1] = 0
                        s[i + 2] = 255
                        s[i + 3] = 255
                    }
                    let data = ImageData(100.0, 100.0, data: s)
                    offContext.putImageData(data, 10, 10)
                    offContext.putImageData(data, 150.0, 10.0, 0.0, 0.0, 50.0, 50.0)
                    let image = offContext.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_14](figures/offscreenrenderingcontext_14.png)