### func setTransform(Int64, Int64, Int64, Int64, Int64, Int64)

```cangjie
public func setTransform(
    scaleX: Int64,
    skewX: Int64,
    skewY: Int64,
    scaleY: Int64,
    translateX: Int64,
    translateY: Int64
): Unit
```

**功能：** 对应一个变换矩阵，当对一个图形进行变化时，只要设置此变换矩阵相应的参数，对图形的各个定点的坐标分别乘以这个矩阵，就能得到新的定点的坐标。setTransform()方法会重置现有的变换矩阵并创建新的变换矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scaleX|Int64|是|-|指定水平缩放值。|
|skewX|Int64|是|-|指定水平倾斜值。|
|skewY|Int64|是|-|指定垂直倾斜值。|
|scaleY|Int64|是|-|指定垂直缩放值。|
|translateX|Int64|是|-|指定水平移动值。<br>默认单位：vp。|
|translateY|Int64|是|-|指定垂直移动值。<br>默认单位：vp。|

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
    private let context1: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings)
    private let offcontext1: OffscreenCanvasRenderingContext2D = OffscreenCanvasRenderingContext2D(600, 200,
        this.settings)
    private let context2: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings)
    private let offcontext2: OffscreenCanvasRenderingContext2D = OffscreenCanvasRenderingContext2D(600, 200,
        this.settings)
    @State
    var message: String = ""
    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Text("context2")
            Canvas(this.context1).width(230.vp).height(160.vp).backgroundColor(0xffff00).onReady(
                {
                    =>
                    this.offcontext1.fillRect(100, 20, 50, 50)
                    this.offcontext1.setTransform(1.0, -0.5, 0.5, 1.0, 10.0, 10.0)
                    this.offcontext1.fillRect(100, 20, 50, 50)
                    let image = offcontext1.transferToImageBitmap()
                    this.context1.transferFromImageBitmap(image)
                }
            )
            Text("context2")
            Canvas(this.context2).width(230.vp).height(160.vp).backgroundColor(0x0ffff0).onReady(
                {
                    =>
                    this.offcontext2.fillRect(100, 20, 50, 50)
                    let storedTransform = this.offcontext1.getTransform()
                    this.offcontext2.setTransform(storedTransform)
                    this.offcontext2.fillRect(100, 20, 50, 50)
                    let image = this.offcontext2.transferToImageBitmap()
                    this.context2.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_42](figures/offscreenrenderingcontext_42.png)