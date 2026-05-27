### func toDataURL(ImageType, Float64)

```cangjie
public func toDataURL(imageType!: ImageType = ImageType.png, quality!: Float64 = 0.92): String
```

**功能：** 生成一个包含图片展示的URL，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|imageType|[ImageType](./cj-common-types.md#enum-imagetype)|否|ImageType.png| **命名参数。** 用于指定图像格式。|
|quality|Float64|否|0.92| **命名参数。** 在指定图片格式为image/jpeg或image/webp的情况下，可以从0到1的区间内选择图片的质量。如果超出取值范围，将会使用默认值0.92。|

**返回值：**

|类型|说明|
|:----|:----|
|String|图像的URL地址。|

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
    var toDataUrl: String = ""

    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    this.context.fillStyle(0xff0000)
                    this.context.fillRect(0, 0, 100, 100)
                    this.toDataUrl = this.context.toDataURL()
                }
            )
            Text(this.toDataUrl)
        }.width(100.percent).height(100.percent)
    }
}
```

![toDataURL](./figures/canvasrenderingcontext_51.png)

### func transferFromImageBitmap(ImageBitmap)

```cangjie
public func transferFromImageBitmap(image: ImageBitmap): Unit
```

**功能：** 显示给定的ImageBitmap对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|image|[ImageBitmap](./cj-canvas-drawing-imagebitmap.md#class-imagebitmap)|是|-|待显示的ImageBitmap对象。|

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
                => this.context.transferFromImageBitmap(this.img)
            })
        }.width(100.percent).height(100.percent)
    }
}
```

![transferFromImageBitmap](./figures/canvasrenderingcontext_48.png)