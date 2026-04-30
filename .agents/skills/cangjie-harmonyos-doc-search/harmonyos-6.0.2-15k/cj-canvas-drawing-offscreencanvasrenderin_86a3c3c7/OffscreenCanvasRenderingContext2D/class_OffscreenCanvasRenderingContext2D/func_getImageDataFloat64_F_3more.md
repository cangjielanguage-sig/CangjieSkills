### func getImageData(Float64, Float64, Float64, Float64)

```cangjie
public func getImageData(sx: Float64, sy: Float64, sw: Float64, sh: Float64): ImageData
```

**功能：** 以当前canvas指定区域内的像素创建[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)对象，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sx|Float64|是|-|需要输出的区域的左上角x坐标。<br>默认单位：vp。|
|sy|Float64|是|-|需要输出的区域的左上角y坐标。<br>默认单位：vp。|
|sw|Float64|是|-|需要输出的区域的宽度。<br>默认单位：vp。|
|sh|Float64|是|-|需要输出的区域的高度。<br>默认单位：vp。|

**返回值：**

|类型|说明|
|:----|:----|
|[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)|新的ImageData对象。|

### func getImageData(Int64, Int64, Int64, Int64)

```cangjie
public func getImageData(sx: Int64, sy: Int64, sw: Int64, sh: Int64): ImageData
```

**功能：** 以当前canvas指定区域内的像素创建[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)对象，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sx|Int64|是|-|需要输出的区域的左上角x坐标。<br>默认单位：vp。|
|sy|Int64|是|-|需要输出的区域的左上角y坐标。<br>默认单位：vp。|
|sw|Int64|是|-|需要输出的区域的宽度。<br>默认单位：vp。|
|sh|Int64|是|-|需要输出的区域的高度。<br>默认单位：vp。|

**返回值：**

|类型|说明|
|:----|:----|
|[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)|新的ImageData对象。|

### func getLineDash()

```cangjie
public func getLineDash(): Array<Float64>
```

**功能：** 获得当前画布的虚线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Float64>|返回数组，该数组用来描述线段如何交替和间距长度。<br>默认单位：vp。|

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
                    offContext.beginPath()
                    offContext.arc(100.0, 75.0, 50.0, 0.0, 6.28)
                    offContext.lineDash([10, 20])
                    let res = offContext.getLineDash()
                    offContext.stroke()
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                    for (i in res) {
                        message = message + i.toString()
                    }
                    message = message + res.size.toString()
                }
            )
            Text(message)
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_27](figures/offscreenrenderingcontext_27.PNG)