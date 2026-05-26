### func clearRect(Float64, Float64, Float64, Float64)

```cangjie
public func clearRect(x: Float64, y: Float64, width: Float64, height: Float64): Unit
```

**功能：** 删除指定区域内的绘制内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|指定矩形左上角点的x坐标。<br>默认单位：vp。|
|y|Float64|是|-|指定矩形左上角点的y坐标。<br>默认单位：vp。|
|width|Float64|是|-|指定矩形的宽度。<br>默认单位：vp。|
|height|Float64|是|-|指定矩形的高度。<br>默认单位：vp。|

### func clearRect(Int64, Int64, Int64, Int64)

```cangjie
public func clearRect(x: Int64, y: Int64, width: Int64, height: Int64): Unit
```

**功能：** 删除指定区域内的绘制内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int64|是|-|指定矩形左上角点的x坐标。<br>默认单位：vp。|
|y|Int64|是|-|指定矩形左上角点的y坐标。<br>默认单位：vp。|
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
    var settings: RenderingContextSettings = RenderingContextSettings(antialias: true)
    var context: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings)

    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    this.context.fillStyle(0xD2B48C)
                    this.context.fillRect(20, 20, 200, 200)
                    this.context.clearRect(30, 30, 150, 100)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![clearRect](figures/clearRect.png)

### func clip()

```cangjie
public func clip(): Unit
```

**功能：** 设置当前路径为剪切路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func clip(CanvasFillRule)

```cangjie
public func clip(fillRule: CanvasFillRule): Unit
```

**功能：** 设置当前路径为剪切路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fillRule|[CanvasFillRule](./cj-common-types.md#enum-canvasfillrule)|是|-|指定要剪切对象的规则。<br/>可选参数为：nonzero, evenodd。<br>初始值：nonzero。|

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
                    this.context.rect(0, 0, 100, 200)
                    this.context.stroke()
                    this.context.clip()
                    this.context.fillStyle(0xff0000)
                    this.context.fillRect(0, 0, 200, 200)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

  ![clip](figures/canvasrenderingcontext_10.png)