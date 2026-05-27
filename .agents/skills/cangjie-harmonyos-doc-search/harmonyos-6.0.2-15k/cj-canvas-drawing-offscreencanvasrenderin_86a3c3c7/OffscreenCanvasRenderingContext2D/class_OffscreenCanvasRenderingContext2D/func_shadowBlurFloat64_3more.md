### func shadowBlur(Float64)

```cangjie
public func shadowBlur(blur: Float64): Unit
```

**功能：** 设置绘制阴影时的模糊级别，值越大越模糊。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|blur|Float64|是|-|设置绘制阴影时的模糊级别，值越大越模糊。<br/>初始值：0.0。<br/>单位：px。<br/>shadowBlur取值不支持负数，负数按异常值处理，异常值按默认值处理。|

### func shadowBlur(Int64)

```cangjie
public func shadowBlur(offset: Int64): Unit
```

**功能：** 设置绘制阴影时的模糊级别，值越大越模糊。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Int64|是|-|设置绘制阴影时的模糊级别，值越大越模糊。<br/>初始值：0。<br/>单位：px。<br/>shadowBlur取值不支持负数，负数按异常值处理，异常值按默认值处理。|

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
                    offContext.shadowColor(0x000000)
                    offContext.fillStyle(0x2787D9)
                    offContext.fillRect(20, 20, 100, 80)
                    let image = this.offCanvas.transferToImageBitmap()
                    this.context.transferFromImageBitmap(image)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![offscreencanvasrenderingcontext2d_shadowblur](./figures/offscreencanvasrenderingcontext2d_shadowblur.jpg)

### func shadowColor(Color)

```cangjie
public func shadowColor(color: Color): Unit
```

**功能：** 设置绘制阴影时的阴影颜色。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[Color](./cj-common-types.md#class-color)|是|-|设置绘制阴影时的阴影颜色。<br>初始值：透明黑色。|