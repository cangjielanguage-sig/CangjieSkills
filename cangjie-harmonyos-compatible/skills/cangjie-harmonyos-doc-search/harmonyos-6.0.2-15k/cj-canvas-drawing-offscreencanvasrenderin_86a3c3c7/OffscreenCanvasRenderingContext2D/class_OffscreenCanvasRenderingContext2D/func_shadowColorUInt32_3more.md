### func shadowColor(UInt32)

```cangjie
public func shadowColor(color: UInt32): Unit
```

**功能：** 设置绘制阴影时的阴影颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|UInt32|是|-|设置绘制阴影时的阴影颜色。<br>初始值：透明黑色。|

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
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xD5D5D5).onReady(
                {
                    =>
                    let offContext = this.offCanvas.getContext(contextType: ContextType.type_2d, options: this.settings)
                    offContext.shadowBlur(30)
                    offContext.shadowColor(0xFFC000)
                    offContext.fillStyle(0x2787D9)
                    offContext.fillRect(30, 30, 100, 80)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreencanvasrenderingcontext2d_shadowcolor](./figures/offscreencanvasrenderingcontext2d_shadowcolor.jpg)

### func shadowOffsetX(Float64)

```cangjie
public func shadowOffsetX(offset: Float64): Unit
```

**功能：** 设置绘制阴影时和原有对象的水平偏移值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Float64|是|-|设置绘制阴影时和原有对象的水平偏移值。<br>初始值：0.0。|

### func shadowOffsetX(Int64)

```cangjie
public func shadowOffsetX(offset: Int64): Unit
```

**功能：** 设置绘制阴影时和原有对象的水平偏移值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Int64|是|-|设置绘制阴影时和原有对象的水平偏移值。<br>初始值：0。|

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
                    offContext.shadowBlur(10)
                    offContext.shadowOffsetX(20)
                    offContext.shadowColor(0x000000)
                    offContext.fillStyle(0xFF0000)
                    offContext.fillRect(20, 20, 100, 80)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreencanvasrenderingcontext2d_shadowoffsetx](./figures/offscreencanvasrenderingcontext2d_shadowoffsetx.png)