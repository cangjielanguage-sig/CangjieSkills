### func fillText(String, Int64, Int64, Int64)

```cangjie
public func fillText(text: String, x: Int64, y: Int64, maxWidth: Int64): Unit
```

**功能：** 绘制填充类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|需要绘制的文本内容。|
|x|Int64|是|-|需要绘制的文本内容。|
|y|Int64|是|-|需要绘制的文本内容。|
|maxWidth|Int64|是|-|指定文本允许的最大宽度。<br>默认单位：vp。<br>初始值：不限制宽度。|

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
                    offContext.font(size: 50.px, family: "sans-serif")
                    offContext.fillText("Hello World!", 20, 100)
                    let withstr = "width:" + offContext.measureText("Hello World!").width.toString()
                    offContext.fillText(withstr, 20, 200)

                    offContext.font(size: 55.px, family: "sans-serif")
                    offContext.strokeText("Hello World!", 20, 300)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_23](figures/offscreenrenderingcontext_23.PNG)

### func filter(String)

```cangjie
public func filter(filterStr: String): Unit
```

**功能：** 设置图像的滤镜，可以组合任意数量的滤镜。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|filterStr|String|是|-|用于设置图像的滤镜，可以组合任意数量的滤镜。<br/>支持的滤镜效果如下：<br/>- 'none': 无滤镜效果；<br/>- 'blur'：给图像设置高斯模糊；<br/>- 'brightness'：给图片应用一种线性乘法，使其看起来更亮或更暗；<br/>- 'contrast'：调整图像的对比度；<br/>- 'grayscale'：将图像转换为灰度图像；<br/>- 'hue-rotate'：给图像应用色相旋转；<br/>- 'invert'：反转输入图像；<br/>- 'opacity'：转化图像的透明程度；<br/>- 'saturate'：转换图像饱和度；<br/>- 'sepia'：将图像转换为深褐色；<br/>初始值：'none'。 |