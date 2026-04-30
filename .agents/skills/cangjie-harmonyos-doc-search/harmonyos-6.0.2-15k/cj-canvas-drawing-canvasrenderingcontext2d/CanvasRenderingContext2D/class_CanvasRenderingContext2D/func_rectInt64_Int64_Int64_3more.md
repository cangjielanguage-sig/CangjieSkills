### func rect(Int64, Int64, Int64, Int64)

```cangjie
public func rect(x: Int64, y: Int64, width: Int64, height: Int64): Unit
```

**功能：** 创建矩形路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int64|是|-|指定矩形的左上角x坐标值。<br>默认单位：vp。|
|y|Int64|是|-|指定矩形的左上角y坐标值。<br>默认单位：vp。|
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
    @State
    var message: String = ""
    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    this.context.rect(20, 20, 100, 100) // Create a 100*100 rectangle at (20, 20)
                    this.context.fill()
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![rect](./figures/canvasrenderingcontext_21.png)

### func reset()

```cangjie
public func reset(): Unit
```

**功能：** 将CanvasRenderingContext2D重置为其默认状态，清除后台缓冲区、绘制状态栈、绘制路径和样式。

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
                    this.context.fillRect(20, 20, 150, 100)
                    this.context.reset()
                    this.context.fillRect(20, 150, 150, 100)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![reset](./figures/canvasrenderingcontext_36.png)

### func resetTransform()

```cangjie
public func resetTransform(): Unit
```

**功能：** 使用单位矩阵重新设置当前矩阵。

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
                    this.context.setTransform(1.0, -0.5, 0.5, 1.0, 10.0, 10.0)
                    this.context.fillStyle(0x0000ff)
                    this.context.fillRect(0, 0, 100, 100)
                    this.context.resetTransform()
                    this.context.fillStyle(0xff0000)
                    this.context.fillRect(0, 0, 100, 100)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![resetTransform](./figures/canvasrenderingcontext_37.png)