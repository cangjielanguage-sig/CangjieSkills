### func imageSmoothingEnabled(Bool)

```cangjie
public func imageSmoothingEnabled(enabled: Bool): Unit
```

**功能：** 用于设置绘制图片时是否进行图像平滑度调整，true为启用，false为不启用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enabled|Bool|是|-|启用图像平滑度调整，true为启用，false为不启用。<br>初始值：true。|

### func imageSmoothingQuality(QualityType)

```cangjie
public func imageSmoothingQuality(quality: QualityType): Unit
```

**功能：** 设置图像平滑度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|quality|[QualityType](./cj-common-types.md#enum-qualitytype)|是|-|imageSmoothingEnabled为true时，用于设置图像平滑度。<br>初始值：Low。|

### func lineCap(LineCapStyle)

```cangjie
public func lineCap(value: LineCapStyle): Unit
```

**功能：** 指定线端点的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[LineCapStyle](./cj-common-types.md#enum-linecapstyle)|是|-|指定线端点的样式。<br/>初始值：Butt。|

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
                    offContext.lineWidth(8)
                    offContext.beginPath()
                    offContext.lineCap(LineCapStyle.Round)
                    offContext.moveTo(30, 50)
                    offContext.lineTo(220, 50)
                    offContext.stroke()
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_4](figures/offscreenrenderingcontext_4.PNG)

### func lineDash(Array\<Float64>)

```cangjie
public func lineDash(dashArr: Array<Float64>): Unit
```

**功能：** 设置画布的虚线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dashArr|Array\<Float64>|是|-|描述线段如何交替和线段间距长度的数组。<br>默认单位：vp。|