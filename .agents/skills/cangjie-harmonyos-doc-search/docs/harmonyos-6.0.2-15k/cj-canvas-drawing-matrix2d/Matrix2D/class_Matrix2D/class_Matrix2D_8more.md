## class Matrix2D

```cangjie
public class Matrix2D {
    public init(unit!: LengthMetricsUnit = LengthMetricsUnit.DEFAULT)
}
```

**功能：** 矩阵对象类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### prop rotateX

```cangjie
public mut prop rotateX: Float64
```

**功能：** 水平倾斜系数。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### prop rotateY

```cangjie
public mut prop rotateY: Float64
```

**功能：** 垂直倾斜系数。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### prop scaleX

```cangjie
public mut prop scaleX: Float64
```

**功能：** 水平缩放系数。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### prop scaleY

```cangjie
public mut prop scaleY: Float64
```

**功能：** 垂直缩放系数。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### prop translateX

```cangjie
public mut prop translateX: Float64
```

**功能：** 水平平移距离。默认单位：vp。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### prop translateY

```cangjie
public mut prop translateY: Float64
```

**功能：** 垂直平移距离。默认单位：vp。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### init(LengthMetricsUnit)

```cangjie
public init(unit!: LengthMetricsUnit = LengthMetricsUnit.DEFAULT)
```

**功能：** 创建Matrix2D类型的矩阵对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|unit|LengthMetricsUnit|否|LengthMetricsUnit.DEFAULT| **命名参数。** 用来配置Matrix2D对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](./cj-canvas-drawing-canvasrenderingcontext2d.md#class-canvasrenderingcontext2d)。|

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
    private let context1: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings)
    private let matrix: Matrix2D = Matrix2D()

    func build() {
        Row {
            Canvas(this.context1).width(240.vp).height(180.vp).backgroundColor(0xffff00).onReady(
                {
                    =>
                    this.context1.fillRect(100, 20, 50, 50)
                    this.matrix.scaleX = 1.0
                    this.matrix.scaleY = 1.0
                    this.matrix.rotateX = -0.5
                    this.matrix.rotateY = 0.5
                    this.matrix.translateX = 10.0
                    this.matrix.translateY = 10.0
                    this.context1.setTransform(this.matrix)
                    this.context1.fillRect(100, 20, 50, 50)
                }
            )
        }.height(100.percent).width(100.percent)
    }
}
```

![matrix2D_1](./figures/matrix2D_1.png)