### func transferToImageBitmap()

```cangjie
public func transferToImageBitmap(): ImageBitmap
```

**功能：** 在离屏画布最近渲染的图像上创建一个ImageBitmap对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

| 类型                                       | 说明              |
| ---------------------------------------- | --------------- |
| [ImageBitmap](./cj-canvas-drawing-imagebitmap.md#class-imagebitmap) | 存储离屏画布上渲染的像素数据。 |

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
                    let imageData = offContext.createImageData(100, 100)
                    offContext.putImageData(imageData, 10, 10)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreencanvasrenderingcontext2d_Transfertoimagebitmap](./figures/offscreencanvasrenderingcontext2d_Transfertoimagebitmap.png)

### func transform(Float64, Float64, Float64, Float64, Float64, Float64)

```cangjie
public func transform(
    scaleX: Float64,
    skewX: Float64,
    skewY: Float64,
    scaleY: Float64,
    translateX: Float64,
    translateY: Float64
): Unit
```

**功能：** transform方法对应一个变换矩阵，当对一个图形进行变化时，只要设置此变换矩阵相应的参数，对图形的各个定点的坐标分别乘以这个矩阵，就能得到新的定点的坐标。矩阵变换效果可叠加。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scaleX|Float64|是|-|指定水平缩放值。|
|skewX|Float64|是|-|指定水平倾斜值。|
|skewY|Float64|是|-|指定垂直倾斜值。|
|scaleY|Float64|是|-|指定垂直缩放值。|
|translateX|Float64|是|-|指定水平移动值。<br>默认单位：vp。|
|translateY|Float64|是|-|指定垂直移动值。<br>默认单位：vp。|