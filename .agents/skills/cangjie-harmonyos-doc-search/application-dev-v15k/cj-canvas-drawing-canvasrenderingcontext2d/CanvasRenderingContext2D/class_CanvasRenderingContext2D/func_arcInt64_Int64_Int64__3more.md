### func arc(Int64, Int64, Int64, Int64, Int64, Bool)

```cangjie
public func arc(x: Int64, y: Int64, radius: Int64, startAngle: Int64, endAngle: Int64, anticlockwise!: Bool = false): Unit
```

**功能：** 绘制弧线路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int64|是|-|弧线圆心的x坐标值。<br>默认单位：vp。|
|y|Int64|是|-|弧线圆心的y坐标值。<br>默认单位：vp。|
|radius|Int64|是|-|弧线的圆半径。<br>默认单位：vp。|
|startAngle|Int64|是|-|弧线的起始弧度。<br>单位：弧度。|
|endAngle|Int64|是|-|弧线的终止弧度。<br>单位：弧度。|
|anticlockwise|Bool|否|false| **命名参数。** 是否逆时针绘制圆弧。<br>是否逆时针绘制圆弧。<br>true:逆时针方向绘制椭圆。<br>false:顺时针方向绘制椭圆。|

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
                    this.context.beginPath()
                    this.context.arc(100.0, 75.0, 50.0, 0.0, 6.283)
                    this.context.stroke()
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![arc](figures/arc.png)

### func arcTo(Float64, Float64, Float64, Float64, Float64)

```cangjie
public func arcTo(x1: Float64, y1: Float64, x2: Float64, y2: Float64, radius: Float64): Unit
```

**功能：** 依据圆弧经过的点和圆弧半径创建圆弧路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x1|Float64|是|-|圆弧经过的第一个点的x坐标值。<br>默认单位：vp。|
|y1|Float64|是|-|圆弧经过的第一个点的y坐标值。<br>默认单位：vp。|
|x2|Float64|是|-|圆弧经过的第二个点的x坐标值。<br>默认单位：vp。|
|y2|Float64|是|-|圆弧经过的第二个点的y坐标值。<br>默认单位：vp。|
|radius|Float64|是|-|圆弧的圆半径值。<br>默认单位：vp。|

### func arcTo(Int64, Int64, Int64, Int64, Int64)

```cangjie
public func arcTo(x1: Int64, y1: Int64, x2: Int64, y2: Int64, radius: Int64): Unit
```

**功能：** 依据圆弧经过的点和圆弧半径创建圆弧路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x1|Int64|是|-|圆弧经过的第一个点的x坐标值。<br>默认单位：vp。|
|y1|Int64|是|-|圆弧经过的第一个点的y坐标值。<br>默认单位：vp。|
|x2|Int64|是|-|圆弧经过的第二个点的x坐标值。<br>默认单位：vp。|
|y2|Int64|是|-|圆弧经过的第二个点的y坐标值。<br>默认单位：vp。|
|radius|Int64|是|-|圆弧的圆半径值。<br>默认单位：vp。|