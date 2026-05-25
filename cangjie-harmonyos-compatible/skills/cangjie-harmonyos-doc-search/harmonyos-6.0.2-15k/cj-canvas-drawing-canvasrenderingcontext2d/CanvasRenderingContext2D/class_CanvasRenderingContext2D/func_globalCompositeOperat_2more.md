### func globalCompositeOperation(CompositeOperation)

```cangjie
public func globalCompositeOperation(operation: CompositeOperation): Unit
```

**功能：** 设置合成操作的方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|operation|[CompositeOperation](./cj-common-types.md#enum-compositeoperation)|是|-|设置合成操作的方式。|

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
                    this.context.fillStyle(0xff0000)
                    this.context.fillRect(20, 20, 50, 50)
                    this.context.globalCompositeOperation(CompositeOperation.SourceOver)
                    this.context.fillStyle(0x0000ff)
                    this.context.fillRect(50, 50, 50, 50)
                    this.context.fillStyle(0xff0000)
                    this.context.fillRect(120, 20, 50, 50)
                    this.context.globalCompositeOperation(CompositeOperation.DestinationOver)
                    this.context.fillStyle(0x0000ff)
                    this.context.fillRect(150, 50, 50, 50)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![globalCompositeOperation](./figures/canvasrenderingcontext_30.png)

### func height()

```cangjie
public func height(): Float64
```

**功能：** 组件高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Float64|组件高度。|

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
            Canvas(this.context).width(300).height(300).backgroundColor(0xffff00).onReady(
                {
                    =>
                    let h = this.context.height()
                    let w = this.context.width()
                    this.context.fillRect(0, 0, Int64(w / 2.0), Int64(h / 2.0))
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![height](./figures/canvasrenderingcontext_31.png)