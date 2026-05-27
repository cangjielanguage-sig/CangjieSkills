### func shadowOffsetX(Float64)

```cangjie
public func shadowOffsetX(offset: Float64): Unit
```

**功能：** 设置绘制阴影时和原有对象的水平偏移值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Float64|是|-|设置绘制阴影时和原有对象的水平偏移值。<br>初始值：0.0。 <br>默认单位：vp。|

### func shadowOffsetX(Int64)

```cangjie
public func shadowOffsetX(offset: Int64): Unit
```

**功能：** 设置绘制阴影时和原有对象的水平偏移值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Int64|是|-|设置绘制阴影时和原有对象的水平偏移值。<br>初始值：0。 <br>默认单位：vp。|

### func shadowOffsetY(Float64)

```cangjie
public func shadowOffsetY(offset: Float64): Unit
```

**功能：** 设置绘制阴影时和原有对象的垂直偏移值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Float64|是|-|设置绘制阴影时和原有对象的垂直偏移值。<br>初始值：0.0 <br>默认单位：vp。|

### func shadowOffsetY(Int64)

```cangjie
public func shadowOffsetY(offset: Int64): Unit
```

**功能：** 设置绘制阴影时和原有对象的垂直偏移值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Int64|是|-|设置绘制阴影时和原有对象的垂直偏移值。<br>初始值：0。 <br>默认单位：vp。|

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
                    this.context.shadowBlur(30)
                    this.context.shadowColor(0x0000ff)
                    this.context.shadowOffsetY(20)
                    this.context.shadowOffsetX(20)
                    this.context.fillStyle(0xff0000)
                    this.context.fillRect(20, 20, 100, 80)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![shadow](./figures/canvasrenderingcontext_43.png)

### func stroke()

```cangjie
public func stroke(): Unit
```

**功能：** 进行边框绘制操作。

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
    var message: String = ""
    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    this.context.moveTo(125, 25)
                    this.context.lineTo(125, 105)
                    this.context.lineTo(175, 105)
                    this.context.lineTo(175, 25)
                    this.context.strokeStyle(0xff0000)
                    this.context.stroke()
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![stroke](./figures/canvasrenderingcontext_44.png)