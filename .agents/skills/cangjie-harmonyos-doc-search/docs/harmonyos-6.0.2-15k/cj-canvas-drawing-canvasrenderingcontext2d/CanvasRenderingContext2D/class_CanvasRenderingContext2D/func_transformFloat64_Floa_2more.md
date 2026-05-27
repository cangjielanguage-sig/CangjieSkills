### func transform(Float64, Float64, Float64, Float64, Float64, Float64)

```cangjie
public func transform(
    scaleX: Float64,
    skewX: Float64,
    skewY: Float64,
    scaleY: Float64,
    translateX: Float64,
    translateY: Float64
): Unit
```

**功能：** transform方法对应一个变换矩阵。在对一个图形进行变化时，只要设置此变换矩阵相应的参数，对图形的各个定点的坐标分别乘以这个矩阵，就能得到新的定点的坐标。矩阵变换效果可叠加。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scaleX|Float64|是|-|指定水平缩放值。|
|skewX|Float64|是|-|指定水平倾斜值。|
|skewY|Float64|是|-|指定垂直倾斜值。|
|scaleY|Float64|是|-|指定垂直缩放值。|
|translateX|Float64|是|-|指定水平移动值。<br>默认单位：vp。|
|translateY|Float64|是|-|指定垂直移动值。<br>默认单位：vp。|

> **说明：**
>
> 变换后的坐标计算方式（x和y为变换前坐标，x'和y'为变换后坐标）：
>
> x' = scaleX \* x + skewY \* y + translateX
>
> y' = skewX \* x + scaleY \* y + translateY

### func transform(Int64, Int64, Int64, Int64, Int64, Int64)

```cangjie
public func transform(
    scaleX: Int64,
    skewX: Int64,
    skewY: Int64,
    scaleY: Int64,
    translateX: Int64,
    translateY: Int64
): Unit
```

**功能：** transform方法对应一个变换矩阵，想对一个图形进行变化的时候，只要设置此变换矩阵相应的参数，对图形的各个定点的坐标分别乘以这个矩阵，就能得到新的定点的坐标。矩阵变换效果可叠加。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scaleX|Int64|是|-|指定水平缩放值。|
|skewX|Int64|是|-|指定水平倾斜值。|
|skewY|Int64|是|-|指定垂直倾斜值。|
|scaleY|Int64|是|-|指定垂直缩放值。|
|translateX|Int64|是|-|指定水平移动值。<br>默认单位：vp。|
|translateY|Int64|是|-|指定垂直移动值。<br>默认单位：vp。|

> **说明：**
>
> 变换后的坐标计算方式（x和y为变换前坐标，x'和y'为变换后坐标）：
>
> x' = scaleX \* x + skewY \* y + translateX
>
> y' = skewX \* x + scaleY \* y + translateY

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
                    this.context.fillStyle(0x000000)
                    this.context.fillRect(0, 0, 100, 100)
                    this.context.transform(1.0, 0.5, -0.5, 1.0, 10.0, 10.0)
                    this.context.fillStyle(0xff0000)
                    this.context.fillRect(0, 0, 100, 100)
                    this.context.transform(1.0, 0.5, -0.5, 1.0, 10.0, 10.0)
                    this.context.fillStyle(0x0000ff)
                    this.context.fillRect(0, 0, 100, 100)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![transform](./figures/canvasrenderingcontext_49.png)