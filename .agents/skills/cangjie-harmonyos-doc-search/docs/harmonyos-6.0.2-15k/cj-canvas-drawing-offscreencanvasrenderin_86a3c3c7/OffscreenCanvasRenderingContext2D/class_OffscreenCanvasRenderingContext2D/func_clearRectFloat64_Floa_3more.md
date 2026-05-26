### func clearRect(Float64, Float64, Float64, Float64)

```cangjie
public func clearRect(x: Float64, y: Float64, width: Float64, height: Float64): Unit
```

**功能：** 删除指定区域内的绘制内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|指定矩形上的左上角x坐标。<br>默认单位：vp。|
|y|Float64|是|-|指定矩形上的左上角y坐标。<br>默认单位：vp。|
|width|Float64|是|-|指定矩形的宽度。<br>默认单位：vp|
|height|Float64|是|-|指定矩形的高度。<br>默认单位：vp|

### func clearRect(Int64, Int64, Int64, Int64)

```cangjie
public func clearRect(x: Int64, y: Int64, width: Int64, height: Int64): Unit
```

**功能：** 删除指定区域内的绘制内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int64|是|-|指定矩形上的左上角x坐标。<br>默认单位：vp。|
|y|Int64|是|-|指定矩形上的左上角y坐标。<br>默认单位：vp。|
|width|Int64|是|-|指定矩形的宽度。<br>默认单位：vp。|
|height|Int64|是|-|指定矩形的高度。<br>默认单位：vp。|

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
                    offContext.fillRect(30, 30, 200, 200)
                    offContext.clearRect(50, 50, 150, 100)
                    offContext.strokeRect(30, 230, 200, 150)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreenrenderingcontext_9](figures/offscreenrenderingcontext_9.PNG)

### func clip()

```cangjie
public func clip(): Unit
```

**功能：** 设置当前路径为剪切路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19