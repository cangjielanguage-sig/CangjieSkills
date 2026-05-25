### func identity()

```cangjie
public func identity(): This
```

**功能：** 创建一个单位矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

| 类型 | 说明 |
|:----|:----|
| This | 创建的单位矩阵对象。 |

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
    private var matrix: Matrix2D = Matrix2D()

    func build() {
        Row {
            Canvas(this.context1).width(240.vp).height(180.vp).backgroundColor(0xffff00).onReady(
                {
                    =>
                    this.context1.fillRect(100, 20, 50, 50)
                    this.matrix = this.matrix.identity()
                    this.context1.setTransform(this.matrix)
                    this.context1.fillRect(100, 100, 50, 50)
                }
            )
        }.height(100.percent).width(100.percent)
    }
}
```

![matrix2D_2](./figures/matrix2D_2.png)

### func invert()

```cangjie
public func invert(): This
```

**功能：** 得到当前矩阵的逆矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|This|逆矩阵结果。|

### func rotate(Float64, Float64, Float64)

```cangjie
public func rotate(degree: Float64, rx!: Float64 = 0.0, ry!: Float64 = 0.0): This
```

**功能：** 以旋转点为中心，对当前矩阵进行右乘旋转运算。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|degree|Float64|是|-|旋转角度。顺时针方向为正角度，可以通过 degree * Math.PI / 180 将角度转换为弧度值。默认单位：弧度。|
|rx|Float64|否|0.0| **命名参数。** 旋转点的水平方向坐标。默认单位：vp。|
|ry|Float64|否|0.0| **命名参数。** 旋转点的垂直方向坐标。默认单位：vp。|

**返回值：**

| 类型 | 说明 |
|:----|:----|
| This | 以旋转点为中心，对当前矩阵进行右乘旋转运算后的矩阵对象。 |

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
                    this.context1.fillRect(60, 80, 50, 50)
                    this.matrix.scaleX = 1.0
                    this.matrix.scaleY = 1.0
                    this.matrix.rotateX = -0.5
                    this.matrix.rotateY = 0.5
                    this.matrix.translateX = 10.0
                    this.matrix.translateY = 10.0
                    this.matrix.rotate(-60.0 * 3.14 / 180.0, rx: 5.0, ry: 5.0)
                    this.context1.setTransform(this.matrix)
                    this.context1.fillRect(60, 80, 50, 50)
                }
            )
        }.height(100.percent).width(100.percent)
    }
}
```

![matrix2D_4](./figures/matrix2D_4.png)