### func createImageData(ImageData)

```cangjie
public func createImageData(imageData: ImageData): ImageData
```

**功能：** 根据一个现有的ImageData对象重新创建一个宽、高相同的ImageData对象（不会复制图像数据），请参考[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)，该接口存在内存拷贝行为，高耗时，应避免频繁使用。createImageData示例同[putImageData](#func-putimagedataimagedata-float64-float64)。

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
    @State
    var message: String = ""
    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    let imageDataNum = this.context.createImageData(100.0, 100.0)
                    var s = imageDataNum.data
                    for (i in 0..s.size where i % 4 == 0) {
                        s[i + 0] = 255
                        s[i + 1] = 0
                        s[i + 2] = 255
                        s[i + 3] = 255
                    }
                    let data = ImageData(100.0, 100.0, data: s)
                    this.context.putImageData(data, 10, 10)
                    this.context.putImageData(data, 150.0, 10.0, 0.0, 0.0, 50.0, 50.0)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![createImageData](./figures/offscreenrenderingcontext_14.png)

### func createLinearGradient(Float64, Float64, Float64, Float64)

```cangjie
public func createLinearGradient(x0: Float64, y0: Float64, x1: Float64, y1: Float64): CanvasGradient
```

**功能：** 创建一个线性渐变色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x0|Float64|是|-|起点的x轴坐标。<br>默认单位：vp。|
|y0|Float64|是|-|起点的y轴坐标。<br>默认单位：vp。|
|x1|Float64|是|-|终点的x轴坐标。<br>默认单位：vp。|
|y1|Float64|是|-|终点的y轴坐标。<br>默认单位：vp。|

**返回值：**

|类型|说明|
|:----|:----|
|[CanvasGradient](cj-canvas-drawing-canvasgradient.md#class-canvasgradient)| 渐变对象。使用完毕后需要释放，详见[CanvasGradient](cj-canvas-drawing-canvasgradient.md#class-canvasgradient)。|