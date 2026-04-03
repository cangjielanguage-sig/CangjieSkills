### func lineCap(LineCapStyle)

```cangjie
public func lineCap(value: LineCapStyle): Unit
```

**功能：** 指定线端点的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[LineCapStyle](./cj-common-types.md#enum-linecapstyle) |是|-|- Butt：线端点以方形结束。<br>- Round：线端点以圆形结束。<br>- Square：线端点以方形结束，该样式下会增加一个长度和线段厚度相同，宽度是线段厚度一半的矩形。|

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
                    this.context.lineWidth(8)
                    this.context.beginPath()
                    this.context.lineCap(LineCapStyle.Round)
                    this.context.moveTo(30, 50)
                    this.context.lineTo(220, 50)
                    this.context.stroke()
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![lineCap](./figures/canvasrenderingcontext_4.png)

### func lineDash(Array\<Float64>)

```cangjie
public func lineDash(dashArr: Array<Float64>): Unit
```

**功能：** 设置画布线条为虚线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dashArr|Array\<Float64>|是|-|设置画布线条为虚线。|

### func lineDash(Array\<Int64>)

```cangjie
public func lineDash(dashArr: Array<Int64>): Unit
```

**功能：** 设置画布线条为虚线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dashArr|Array\<Int64>|是|-|设置画布线条为虚线。|

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
                    this.context.arc(100.0, 75.0, 50.0, 0.0, 6.28)
                    this.context.lineDash([10, 20])
                    this.context.stroke()
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![lineDash](./figures/canvasrenderingcontext_34.png)

### func lineDashOffset(Float64)

```cangjie
public func lineDashOffset(offset: Float64): Unit
```

**功能：** 设置画布的虚线偏移量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Float64|是|-|设置画布的虚线偏移量。<br>初始值：0.0 <br>默认单位：vp。|