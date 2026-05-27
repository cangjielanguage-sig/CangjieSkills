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
    @State
    var message: String = ""

    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    this.context.beginPath()
                    this.context.arc(150.0, 700.0, 50.0, 0.0, 6.28)
                    this.context.lineDash([10, 20])
                    let res = this.context.getLineDash()
                    this.context.stroke()

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

![getLineDash](./figures/canvasrenderingcontext_26.png)

### func getPixelMap(Float64, Float64, Float64, Float64)

```cangjie
public func getPixelMap(left: Float64, top: Float64, width: Float64, height: Float64): PixelMap
```

**功能：** 以当前canvas指定区域内的像素创建[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|left|Float64|是|-|需要输出的区域的左上角x坐标。<br>默认单位：vp。|
|top|Float64|是|-|需要输出的区域的左上角y坐标。<br>默认单位：vp。|
|width|Float64|是|-|需要输出的区域的宽度。<br>默认单位：vp。|
|height|Float64|是|-|需要输出的区域的高度。<br>默认单位：vp。|

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)|新的[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)对象。|