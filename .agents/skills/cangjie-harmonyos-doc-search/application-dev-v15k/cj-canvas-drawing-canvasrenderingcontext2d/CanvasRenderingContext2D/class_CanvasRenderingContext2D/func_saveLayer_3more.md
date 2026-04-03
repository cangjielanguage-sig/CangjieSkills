### func saveLayer()

```cangjie
public func saveLayer(): Unit
```

**功能：** 创建一个图层。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

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
                    this.context.fillRect(50, 100, 300, 100)
                    this.context.fillStyle(0x00ffff)
                    this.context.fillRect(50, 150, 300, 100)
                    this.context.globalCompositeOperation(CompositeOperation.DestinationOver)
                    this.context.saveLayer()
                    this.context.globalCompositeOperation(CompositeOperation.SourceOver)
                    this.context.fillStyle(0xff0000)
                    this.context.fillRect(100, 50, 100, 300)
                    this.context.fillStyle(0x00ff00)
                    this.context.fillRect(150, 50, 100, 300)
                    this.context.restoreLayer()
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![saveLayer](./figures/canvasrenderingcontext_40.png)

### func scale(Float64, Float64)

```cangjie
public func scale(x: Float64, y: Float64): Unit
```

**功能：** 设置canvas画布的缩放变换属性，后续的绘制操作将按照缩放比例进行缩放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|设置水平方向的缩放值。<br>默认单位：vp。|
|y|Float64|是|-|设置垂直方向的缩放值。<br>默认单位：vp。|

### func scale(Int64, Int64)

```cangjie
public func scale(x: Int64, y: Int64): Unit
```

**功能：** 设置canvas画布的缩放变换属性，后续的绘制操作将按照缩放比例进行缩放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int64|是|-|设置水平方向的缩放值。|
|y|Int64|是|-|设置垂直方向的缩放值。|

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
                    this.context.lineWidth(3)
                    this.context.strokeRect(30, 30, 50, 50)
                    this.context.scale(2, 2) // Scale to 200%
                    this.context.strokeRect(30, 30, 50, 50)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![scale](./figures/canvasrenderingcontext_41.png)