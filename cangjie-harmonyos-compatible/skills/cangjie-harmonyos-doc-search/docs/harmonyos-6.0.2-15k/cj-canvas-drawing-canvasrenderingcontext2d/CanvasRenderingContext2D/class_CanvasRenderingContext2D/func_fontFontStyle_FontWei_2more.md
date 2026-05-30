### func font(FontStyle, FontWeight, Length, String)

```cangjie
public func font(
    style!: FontStyle = FontStyle.Normal,
    weight!: FontWeight = FontWeight.Normal,
    size!: Length = 14.px,
    family!: String = "sans-serif"
): Unit
```

**功能：** 设置文本绘制中的字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle) |否|FontStyle.Normal| **命名参数。** 用于指定字体样式。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Normal| **命名参数。** 用于指定字体的粗细。|
|size|[Length](./cj-common-types.md#interface-length)|否|14.px| **命名参数。** 指定字号和行高。|
|family|String|否|"sans-serif"| **命名参数。** 指定字体系列。|

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
                    this.context.font(size: 30.px, family: "sans-serif")
                    this.context.fillText("Hello px", 20, 60)
                    this.context.font(size: 30.vp, family: "sans-serif")
                    this.context.fillText("Hello vp", 20, 100)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![font](./figures/canvasrenderingcontext_24.png)

### func getImageData(Float64, Float64, Float64, Float64)

```cangjie
public func getImageData(sx: Float64, sy: Float64, sw: Float64, sh: Float64): ImageData
```

**功能：** 以当前canvas指定区域内的像素创建ImageData对象，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sx|Float64|是|-|需要输出的区域的左上角x坐标。<br> 默认单位：vp。|
|sy|Float64|是|-|需要输出的区域的左上角y坐标。<br> 默认单位：vp。|
|sw|Float64|是|-|需要输出的区域的宽度。<br> 默认单位：vp。|
|sh|Float64|是|-|需要输出的区域的高度。<br> 默认单位：vp。|

**返回值：**

|类型|说明|
|:----|:----|
|[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)|新的ImageData对象。|