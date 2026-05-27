### func rotate(Int64)

```cangjie
public func rotate(angle: Int64): Unit
```

**功能：** 针对当前坐标轴进行顺时针旋转。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|angle|Int64|是|-|设置顺时针旋转的弧度值，可以通过Float64.PI / 180将角度转换为弧度值。<br>单位：弧度。|

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
                    this.context.rotate(45.0 * 3.14 / 180.0)
                    this.context.fillRect(70, 20, 50, 50)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![rotate](./figures/canvasrenderingcontext_39.png)

### func save()

```cangjie
public func save(): Unit
```

**功能：** 将当前状态放入栈中，保存canvas的全部状态，通常在需要保存绘制状态时调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

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
                    this.context.save() // save the default state
                    this.context.fillStyle(0x00ff00)
                    this.context.fillRect(20, 20, 100, 100)
                    this.context.restore() // restore to the default state
                    this.context.fillRect(150, 75, 100, 100)
                }
            )
            Text(this.toDataUrl)
        }.width(100.percent).height(100.percent)
    }
}
```

![save](./figures/canvasrenderingcontext_38.png)