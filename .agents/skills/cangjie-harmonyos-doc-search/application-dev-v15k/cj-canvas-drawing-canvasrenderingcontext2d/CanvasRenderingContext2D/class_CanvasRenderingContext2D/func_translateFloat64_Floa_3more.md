### func translate(Float64, Float64)

```cangjie
public func translate(x: Float64, y: Float64): Unit
```

**功能：** 移动当前坐标系的原点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|设置水平平移量。<br>默认单位：vp。|
|y|Float64|是|-|设置竖直平移量。<br>默认单位：vp。|

### func translate(Int64, Int64)

```cangjie
public func translate(x: Int64, y: Int64): Unit
```

**功能：** 移动当前坐标系的原点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int64|是|-|设置水平平移量。<br>默认单位：vp。|
|y|Int64|是|-|设置竖直平移量。<br>默认单位：vp。|

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
                    this.context.fillRect(10, 10, 50, 50)
                    this.context.translate(70, 70)
                    this.context.fillRect(10, 10, 50, 50)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![translate](./figures/canvasrenderingcontext_50.png)

### func width()

```cangjie
public func width(): Float64
```

**功能：** 组件宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Float64|组件宽度。<br>默认单位：vp。|

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
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![width](./figures/canvasrenderingcontext_1.png)