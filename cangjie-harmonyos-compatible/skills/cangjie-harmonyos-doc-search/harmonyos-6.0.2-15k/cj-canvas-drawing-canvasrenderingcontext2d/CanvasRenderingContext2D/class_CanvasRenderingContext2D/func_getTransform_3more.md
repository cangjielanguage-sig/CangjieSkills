### func getTransform()

```cangjie
public func getTransform(): Matrix2D
```

**功能：** 获取当前被应用到上下文的转换矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[Matrix2D](./cj-canvas-drawing-matrix2d.md#class-matrix2d)|矩阵对象。|

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
    private let context2: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings)
    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Text("context1")
            Canvas(this.context1).width(230.vp).height(120.vp).backgroundColor(0xffff00).onReady(
                {
                    =>
                    this.context1.fillRect(50, 50, 50, 50)
                    this.context1.setTransform(1.2, 3.1415926 / 8.0, 3.1415926 / 6.0, 0.5, 30.0, -25.0)
                    this.context1.fillRect(50, 50, 50, 50)
                }
            )
            Text("context2")
            Canvas(this.context2).width(230.vp).height(120.vp).backgroundColor(0x0ffff0).onReady(
                {
                    =>
                    this.context2.fillRect(50, 50, 50, 50)
                    let storedTransform = this.context1.getTransform()
                    this.context2.setTransform(storedTransform)
                    this.context2.fillRect(50, 50, 50, 50)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![getTransform](./figures/canvasrenderingcontext_28.png)

### func globalAlpha(Float64)

```cangjie
public func globalAlpha(alpha: Float64): Unit
```

**功能：** 设置透明度，0.0为完全透明，1.0为完全不透明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|alpha|Float64|是|-|设置透明度，0.0为完全透明，1.0为完全不透明。|

### func globalAlpha(Int64)

```cangjie
public func globalAlpha(alpha: Int64): Unit
```

**功能：** 设置透明度，0为完全透明，1为完全不透明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|alpha|Int64|是|-|设置透明度，0为完全透明，1为完全不透明。|

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
                    this.context.fillStyle(0x0000ff)
                    this.context.fillRect(0, 0, 50, 50)
                    this.context.globalAlpha(0.4)
                    this.context.fillStyle(0x0000ff)
                    this.context.fillRect(50, 50, 50, 50)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![globalAlpha](./figures/canvasrenderingcontext_29.png)