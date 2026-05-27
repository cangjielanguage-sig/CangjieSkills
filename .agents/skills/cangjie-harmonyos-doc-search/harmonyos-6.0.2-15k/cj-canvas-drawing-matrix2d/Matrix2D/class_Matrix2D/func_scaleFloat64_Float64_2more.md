### func scale(Float64, Float64)

```cangjie
public func scale(sx!: Float64 = 1.0, sy!: Float64 = 1.0): This
```

**功能：** 对当前矩阵进行右乘缩放运算。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sx|Float64|否|1.0| **命名参数。** 水平缩放比例系数。|
|sy|Float64|否|1.0| **命名参数。** 垂直缩放比例系数。|

**返回值：**

| 类型 | 说明 |
|:----|:----|
| This | 对当前矩阵进行右乘缩放运算后的矩阵对象。 |

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
                    this.context1.fillRect(120, 70, 50, 50)
                    this.matrix.scaleX = 1.0
                    this.matrix.scaleY = 1.0
                    this.matrix.rotateX = -0.5
                    this.matrix.rotateY = 0.5
                    this.matrix.translateX = 10.0
                    this.matrix.translateY = 10.0
                    this.matrix.scale(sx: 0.5, sy: 0.5)
                    this.context1.setTransform(this.matrix)
                    this.context1.fillRect(120, 70, 50, 50)
                }
            )
        }.height(100.percent).width(100.percent)
    }
}
```

![matrix2D_6](./figures/matrix2D_6.png)

### func translate(Float64, Float64)

```cangjie
public func translate(tx!: Float64 = 0.0, ty!: Float64 = 0.0): This
```

**功能：** 对当前矩阵进行左乘平移运算。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|tx|Float64|否|0.0| **命名参数。** 水平方向平移距离。默认单位：vp。|
|ty|Float64|否|0.0| **命名参数。** 垂直方向平移距离。默认单位：vp。|

**返回值：**

| 类型 | 说明 |
|:----|:----|
| This | 对当前矩阵进行左乘平移运算后的矩阵对象。 |

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
                    this.context1.fillRect(40, 20, 50, 50)
                    this.matrix.scaleX = 1.0
                    this.matrix.scaleY = 1.0
                    this.matrix.rotateX = -0.0
                    this.matrix.rotateY = 0.0
                    this.matrix.translateX = 0.0
                    this.matrix.translateY = 0.0
                    this.matrix.translate(tx: 100.0, ty: 100.0)
                    this.context1.setTransform(this.matrix)
                    this.context1.fillRect(40, 20, 50, 50)
                }
            )
        }.height(100.percent).width(100.percent)
    }
}
```

![matrix2D_5](./figures/matrix2D_5.png)