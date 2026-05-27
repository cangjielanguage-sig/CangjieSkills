### func createPattern(ImageBitmap, Repetition)

```cangjie
public func createPattern(image: ImageBitmap, repetition: Repetition): CanvasPattern
```

**功能：** 通过指定图像和重复方式创建图片填充的模板。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|image|[ImageBitmap](./cj-canvas-drawing-imagebitmap.md#class-imagebitmap)|是|-|图源对象，具体参考ImageBitmap对象。|
|repetition|[Repetition](./cj-common-types.md#enum-repetition)|是|-|设置图像重复的方式：<br>repeat：沿x轴和y轴重复绘制图像；<br>repeat-x：沿x轴重复绘制图像；<br>repeat-y：沿y轴重复绘制图像；<br>no-repeat：不重复绘制图像；<br>clamp：在原始边界外绘制时，超出部分使用边缘的颜色绘制；<br>mirror：沿x轴和y轴重复翻转绘制图像。|

**返回值：**

|类型|说明|
|:----|:----|
|[CanvasPattern](./cj-canvas-drawing-canvaspattern.md#class-canvaspattern)|通过指定图像和重复方式创建图片填充的模板对象。|

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
    private let img: ImageBitmap = ImageBitmap("resource://RAWFILE/icon.png")
    @State
    var message: String = ""
    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    let pattern = this.context.createPattern(this.img, repeat)
                    this.context.fillStyle(pattern)
                    this.context.fillRect(0, 0, 200, 200)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![createPattern](./figures/canvasrenderingcontext_16.png)